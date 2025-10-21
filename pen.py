run = True
user = input("\n Enter your name: ")
print("Hello " + user +"\n")
while run:
    x = input("\n Do you want to add a contact: ")
    print()
    if x == "yes":
        a = input("contact's name: ")
        b = input("contact's email adress: ")
        c = input("contact's phone number: ")
        print()
        adress_book = { "Name:" : a,
                        "Number:" : c,
                        "Email Adress:" : b,
                    }
        for x,y in adress_book.items():
            print(x,y)
    elif x == "no":
        break