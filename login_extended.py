import zarejestrowac

while True:

    def option_selection():

        option = input("option gir: ")

        if option == "1":
            zarejestrowac.register(zarejestrowac.users)
        elif option == "2":
            for key in zarejestrowac.users:
                print(key)
        elif option == "3":
            login = input('Podaj swoj login: ')
            password = input('Podaj swoj haslo: ')
            if login in zarejestrowac.users and password in zarejestrowac.users.values():
                print("correct")
                print(zarejestrowac.users)
                zarejestrowac.users.update({login: input("pass: ")})
                print(zarejestrowac.users)

            else:
                print("wrong id pass")
        elif option == "4":
            login = input('Podaj swoj login: ')
            password = input('Podaj swoj haslo: ')
            if login in zarejestrowac.users and password in zarejestrowac.users.values():
                print(zarejestrowac.users)
                zarejestrowac.users.pop(login)
                print(zarejestrowac.users)
            else:
                print("wrong id pass")
        elif option == "5":
            quit()
        else:
            print("geçerli gir")


    option_selection()