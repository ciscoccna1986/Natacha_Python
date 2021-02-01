username = input("Введите user: ")
password = input("Введите Pass: ")

if len(password) < 8:
    print("пароль короткий")
elif username in password:
    print("Pass содержит user and pass")
else:
    print("Пароль установлен для пользователя {}".format(username))
