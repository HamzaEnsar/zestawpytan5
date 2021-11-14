import zarejestrowac

while True:

    def option_selection():
        print('1-Register')
        print('2-View the users')
        print('3-Change my password')
        print('4-Delete my account')
        print('5-Exit')
        option = input("Wybierz opcja: ")

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
                zarejestrowac.users.update({login: input("Podaj nowy password:  ")})
                print(zarejestrowac.users)

            else:
                print("Zly id ")
        elif option == "4":
            login = input('Podaj swoj login: ')
            password = input('Podaj swoj haslo: ')
            if login in zarejestrowac.users and password in zarejestrowac.users.values():
                print(zarejestrowac.users)
                zarejestrowac.users.pop(login)
                print(zarejestrowac.users)
            else:
                print("wrong id or pass")
        elif option == "5":
            quit()
        else:
            print("Nie ma taki opcji")


    option_selection()
