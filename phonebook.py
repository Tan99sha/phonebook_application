import sys

def display_menu():
    print("Phone Book Application")
    print("~~$$~~$$~~$$~~$$~~$$~~")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete Contact")
    print("4. Display all contacts")
    print("5. Exit")

def add():
    name = input("Enter The Contact Name: ")
    number = input("Enter the Contact number: ")
    contact = name + ":" + number + "\n"
    
    file=open("contacts.txt", "a") 
    file.write(contact)
    file.close()
    
    print("Contact added successfully!")

def search():
    search_term = input("Enter the name or number to search: ")
    
    file=open("contacts.txt","r")
    contacts = file.readlines()
    file.close()
    
    results = []
    for contact in contacts:
        if search_term.lower() in contact.lower():
            results.append(contact)
    
    if results:
        print("Search Result:")
        for result in results:
            print(result)
    else:
        print("No contacts found matching the search term.")

def delete():
    serach_term=input("Enter the name or number of the contact")
    file=open("contacts.txt","r")
    contacts=file.readlines()
    file.close()

    result=[]
    for contact in contacts:
        if serach_term.lower()not in contact.lower():
            result.append(contact)
    
    file=open("contacts.txt","w")
    contacts=file.writelines(result)
    file.close()
    
    print("Contact deleted successfully")

def display():
    file=open("contacts.txt","r")
    contacts=file.readlines()
    file.close
    
    if contacts:
        print("All Contacts:")
        for contact in contacts:
            print(contact.strip())
    else:
        print("No contacts found.")

def exit():
    sys.exit()

def phone():
    display_menu()
    
    while True:
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add()
        elif choice == "2":
            search()
        elif choice == "3":
            delete()
        elif choice == "4":
            display()
        elif choice == "5":
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    phone()