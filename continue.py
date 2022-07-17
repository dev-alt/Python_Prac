while True:
    print("Whoa are you?")
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe, what is the apssword? (it is a fish)')
    password = input()
    if password == 'swordfish':
        break
    print('access granted')