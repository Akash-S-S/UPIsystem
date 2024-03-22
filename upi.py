# ─── MODULES ─p───────────────────────────────────────────────────────────────────
import math
import json
import random
from datetime import datetime
from os.path import exists

# ─── FILE ──────────────────────────────────────────────────────────────────
FILE_PATH = "bank.json"

# ─── FILE OPERATIONS ───────────────────────────────────────────────────────────────────
def get_data():
    # Reads the bank information from the data file.
    # assume none existent file as empty file
    if not exists(FILE_PATH):
        return {}
    f = open(FILE_PATH, "r")
    data = f.read()
    # convert string json to dictionary(object of python)
    return json.loads(data)

def set_data(data):
    # Writes the bank information into the data file
    f = open(FILE_PATH, "w")
    json_data = json.dumps(data)
    f.write(json_data)

def list_to_linked_list(arr):
    n = None
    for i in range(len(arr) - 1, -1, -1):
        node = LinkedList(arr[i], n)
        n = node
    return n

def get_users_as_list():
    # gets user data and converts dictionary to list and appends account_number as key to Linked List
    result = []
    users = get_data()
    for user_account_number in users:
        user_data = users[user_account_number]
        user_data["account_number"] = user_account_number
        result.insert_end(user_data)
    results_as_ll = list_to_linked_list(result)
    return results_as_ll

# ─── LINKED LIST ────────────────────────────────────────────────────────────────


    def index(self, index):
        # Similar to A[i], this works as A.index(i)
        if index == 0:
            return self.data
        else:
            if self.ref == None:
                return None
            else:
                return self.ref.index(index - 1)

    def set_index(self, index, data):
        # Similar to A[i] = value, this is A.set_index(i, value)
        if index == 0:
            self.data = data
        else:
            self.ref.set_index(index - 1, data)

    def size(self):
        # Similar to len(A), this is A.size()
        if self.ref == None:
            return 1
        else:
            return 1 + self.ref.size()

    def insert_end(self, data):
        # Appends a new node to the end of nodes
        if self.ref == None:
            self.ref = LinkedList(data, None)
        else:
            self.ref.insert_end(data)

# ─── ACCOUNT NUMBER ─────────────────────────────────────────────────────────────
def generate_account_number():
    # Generates a new unique account number
    #The bank prefix number is 1717 2424,the 8 other digits are then generated randomly
    prefix = "17172424"
    result = ""
    for _ in range(0, 8):
        random_number = random.randint(1, 9)
        result += str(random_number)

    return prefix + result

# ─── TRANSACTION ────────────────────────────────────────────────────────────────
def perform_transaction_via_AccNo(sender_number, receiver_number, amount):
    users = get_data()

    if sender_number not in users:
        print("Did not found the account with number: " + sender_number)
        return

    if receiver_number not in users:
        print("Did not found the account with number: " + receiver_number)
        return

    if users[sender_number]["balance"] < amount:
        print("your account balance is not enough")
        return

    users[sender_number]["balance"] -= amount
    users[receiver_number]["balance"] += amount

    set_data(users)

    print("Transferred ", amount, "/- from account",users[sender_number]["full_name"],"to",users[receiver_number]["full_name"])

# ─── update information ──────────────────────────────────────────────────────────
def update_information(account_number):
    users = get_data()
    print_horizontal_line()
    print("► 1 ∙ Full Name ")
    print_horizontal_line()
    print("► 2 ∙ Gender ")
    print_horizontal_line()
    print("► 3 ∙ City ")
    print_horizontal_line()
    print("► 4 ∙ Phone Number ")
    print_horizontal_line()
    command = int(input("What to change? "))
    print_horizontal_line()
    if command == 1:
        new_name = input("New Full Name: ")
        users[account_number]["full_name"] = new_name
    if command == 2:
        new_gender = input("New Gender: ")
        users[account_number]["gender"] = new_gender
    if command == 3:
        new_city = input("New City: ")
        users[account_number]["city"] = new_city
    if command == 4:
        new_phone_number = input("New Phone Number: ")
        users[account_number]["phone_number"] = new_phone_number

    set_data(users)
    display_account_information_by_given_account_number(account_number)

# ─── CREATE A NEW USER ──────────────────────────────────────────────────────────
def create_new_user(full_name, balance, gender, city, phone_number):
    # Creates a new user with the given information
    users = get_data()
    date = datetime.today().strftime('%Y-%m-%d')
    account_number = generate_account_number()
    users[account_number] = {
        "full_name": full_name,
        "gender": gender,
        "balance": balance,
        "account_creation_date": date,
        "city": city,
        "phone_number": phone_number
    }
    set_data(users)
    display_account_information_by_given_account_number(account_number)

# ─── CHECK BALANCE ────────────────────────────────────────────────────────
def check_balance(accno):
  users = get_data()
  if accno not in users:
      print("Did not found the account with number: " + accno)
      return
  else:
    user = users[accno]
    print("Balance:", user["balance"])

# ─── DELETE AN ACCOUNT ──────────────────────────────────────────────────────────
def delete_account(account_number):
    # Deletes an account if exists, otherwise displays an error
    users = get_data()
    if account_number not in users:
        print("Did not found the account with number: " + account_number)
        return
    del users[account_number]
    set_data(users)
    print("Account number", account_number, "removed.")

def print_horizontal_line():
    print("─────────────────────────────────────────────")

# ─── DISPLAY USER OBJECT ────────────────────────────────────────────────────────
def display_account_information_by_given_account_number(account_number):
    users = get_data()
    user = users[account_number]
    display_user_object(user, account_number)

def display_user_object(user_object, account_number):
    print_horizontal_line()
    print("Full name:      ", user_object["full_name"])
    print("Account number: ", account_number)
    print("Created at:     ", user_object["account_creation_date"])
    print("Balance:        ", user_object["balance"])
    print("Gender:         ", user_object["gender"])
    print("City:           ", user_object["city"])
    print("Phone:          ", user_object["phone_number"])

# ─── DISPLAY MENU ───────────────────────────────────────────────────────────────
def display_menu():
    print()
    print("  ┌────────────────┐  ╭───────────────────────╮           ")
    print("  │                │  │ ▶︎ 1 • Create Account  │           ")
    print("  │                │  ├───────────────────────┴───────╮     ")
    print("  │                │  │ ▶︎ 2 • Pay Via Account Number  │     ")
    print("  │                │  ├───────────────────────────┬───╯     ")
    print("  │  R u P a y     │  │ ▶︎ 3 • Update Account Info │      ")
    print("  │                │  ├──────────────────────┬────╯           ")
    print("  │                │  │ ▶︎ 4 • Check Balance  │            ")
    print("  │                │  ├──────────────────────┴────╮       ")
    print("  │                │  │ ▶︎ 5 • Delete Account      │       ")
    print("  │                │  ├────────────────────┬──────╯      ")
    print("  │                │  │ ▶︎ 6 • Exit System  │              ")
    print("  └────────────────┘  ╰────────────────────╯              ")

    user_choice = int(input("\n Enter your command: "))

    if user_choice == 1:
        print("── Creating a new user ──────────────────────")
        user_name = input("Full Name: ")
        balance = float(input("Balance: "))
        gender = input("Gender: ")
        city = input("City of Residence: ")
        phone_number = input("Phone Number: ")
        create_new_user(user_name, balance, gender, city, phone_number)

    if user_choice == 2:
        print("── Requesting Transaction ───────────────────")
        sender = input("Sender's Account Number:    ")
        receiver = input("Recipient's Account Number: ")
        amount = float(input("Transaction Amount: "))
        perform_transaction_via_AccNo(sender, receiver, amount)

    if user_choice == 3:
        print("── Changing Account Information ─────────────")
        account_number = input("Account Number To Change: ")
        update_information(account_number)

    if user_choice == 4:
        print("── Check Balance ───────────────────────────")
        accno = input("Enter Account Number: ")
        check_balance(accno)

    if user_choice == 5:
        print("── Deleting an Account ──────────────────────")
        account_number = input("Account number to delete: ")
        delete_account(account_number)

    if user_choice == 6:
        quit()

    if user_choice > 6 or user_choice < 1:
      print("Invalid Command!,Please enter valid Command")

    print()
    print_horizontal_line()
    input("PRESS ENTER TO CONTINUE ")
    print()

while True:
    display_menu()
