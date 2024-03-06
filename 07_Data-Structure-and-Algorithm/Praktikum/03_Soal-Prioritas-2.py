
#NO 1 Soal Prioritas 2

def collect_chars(word, rooms):
    word = word.replace(" ", "")
    word_length = len(word)
    word_count = rooms // word_length
    available_rooms = rooms % word_length
    new_word = word * word_count + word[:available_rooms]
    return new_word


print(collect_chars("alta", 10))
print(collect_chars("sepulsa", 20))
print(collect_chars("sepulsa mantap", 20))