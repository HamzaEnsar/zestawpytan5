users = {"Admin": "1234567", "hamzaensar": "hamzaensarpassword", "hamzademirhan": "hamzademirhanpassword"}


def register(dic):
    login1 = input('podaj swoj login: ')
    password = input('Podaj swoj haslo: ')
    repeat_haslo = input('Podaj haslo ponownie: ')

    try:

        assert len(login1) >= 5, 'Podany login musi miec przynajmniej 5 znaki'

        if not password == repeat_haslo:
            raise ValueError("Hasla sa nie zgodne")
        if not len(password) >= 6:
            raise ValueError('Haslo musi byc przynajmniej 6 zankow')

        add = {login1: password}

        dic.update(add)

        print(dic)

        return dic, login1, password


    except AssertionError:
        print('Napotkano asserstion error. Zly login')

    except ValueError:
        print('Napotkano value error.Zly haslo')

#register(users)
