
# Soal Ekplorasi

import uuid

def add_item(list):
    id = str(uuid.uuid4())
    name = input("enter expense name: ")
    while True:
        try:
            amount = int(input("enter amount: "))
            break
        except ValueError:
            print("enter the amount in number format")
    list.append({"id": id, "name": name, "amount": amount})
    print("data added !")


def view_item(list):
    total_amount = 0
    print("all expenses")
    for item in list:
        print("==")
        print(f"id: {item["id"]}\nname: {item["name"]}\namount: {item["amount"]}")
        total_amount += item['amount']
        print("==")
    print(f"==TOTAL:{total_amount}==")


def update_item(list):
    id = input("enter expense id: ")
    item_found = False
    for item in list:
        if item["id"] == id:
            item_found = True
            new_name = input("enter expense name: ")
            while True:
                try:
                    new_amount = int(input("enter amount: "))
                    break
                except ValueError:
                    print("enter the amount in number format")
            item["name"] = new_name
            item["amount"] = new_amount
            print("data updated !")
            break

    if not item_found:
        print("data not found !")


def delete_item(list):
    id = input("enter expense id: ")
    item_found = False
    for item in list:
        if item["id"] == id:
            item_found = True
            list.remove(item)
            print(f"data deleted !")
            break

    if not item_found:
        print("data not found !")


def main():
    list_item = []

    while True:
        print("\n== Menu: ==")
        print("1. create new expense data")
        print("2. view expenses")
        print("3. update expense")
        print("4. delete expense")
        print("5. exit")
        print("===========")

        choice = input("enter your choice: ")

        if choice == '1':
            add_item(list_item)
        elif choice == '2':
            view_item(list_item)
        elif choice == '3':
            update_item(list_item)
        elif choice == '4':
            delete_item(list_item)
        elif choice == '5':
            print("bye...")
            break
        else:
            print("invalid choice")

main()
