import pymysql
import pandas as pd

class DatabaseManager:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database
            )
            print("Connected to MySQL database")
        except pymysql.Error as e:
            print(f"Error: {e}")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection to MySQL database closed")

    def create_tables(self):
        try:
            with self.connection.cursor() as cursor:
                # Create sentiments table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS sentiments (
                        sentiment_id INT PRIMARY KEY,
                        sentiment_label VARCHAR(50) DEFAULT 'Undefined'
                    )
                """)
                
                # Insert default sentiment data
                cursor.executemany("""
                    INSERT INTO sentiments (sentiment_id, sentiment_label) 
                    VALUES (%s, %s)
                """, [(1, 'Good'), (2, 'Bad'), (3, 'Neutral')])
                
                
                # Create tweets table
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tweets (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        text TEXT,
                        sentiment_id INT,
                        FOREIGN KEY (sentiment_id) REFERENCES sentiments(sentiment_id)
                    )
                """)
                
            self.connection.commit()
            print("Tables created successfully")
        except pymysql.Error as e:
            print(f"Error creating tables: {e}")
            self.connection.rollback()

    def insert_from_csv(self, filename, table_name):
        try:
            df = pd.read_csv(filename)
            with self.connection.cursor() as cursor:
                for index, row in df.iterrows():
                    # Insert data into database
                    if table_name == 'tweets':
                        cursor.execute("""
                            INSERT INTO tweets (text, sentiment_id) 
                            VALUES (%s, %s)
                        """, (row['tweets'], row['sentiment']))
            
            self.connection.commit()
            print(f"Data inserted into {table_name} table successfully")
        except (pymysql.Error, pd.errors.EmptyDataError, pd.errors.ParserError) as e:
            print(f"Error inserting data into {table_name} table: {e}")
            self.connection.rollback()


# Inisiasi objek DatabaseManager
db_manager = DatabaseManager(host='localhost', 
                             username='root', 
                             password='hikmal', 
                             database='sentiment_chatgpt')

# Membuat koneksi ke database
db_manager.connect()

# Membuat tabel-tabel
db_manager.create_tables()

# Memasukkan data dari CSV ke dalam database
db_manager.insert_from_csv('sentiment_chatgpt/sentiment_good.csv', 'tweets')
db_manager.insert_from_csv('sentiment_chatgpt/sentiment_bad.csv', 'tweets')
db_manager.insert_from_csv('sentiment_chatgpt/sentiment_neutral.csv', 'tweets')

# Menutup koneksi ke database
db_manager.close_connection()
