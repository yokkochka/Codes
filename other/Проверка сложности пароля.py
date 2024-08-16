def validator():
    user_pass = input("Введите пароль")
    has_digit = False
    for i in range(len(user_pass)):
        if user_pass[i].isdigit():
            has_digit = True
            break
        
    if len(user_pass) >= 8 and has_digit:
        return 'Ваш пароль безопасен'
    elif len(user_pass) < 8:
        return 'Ваш пароль слишком короткий'
    else:
        return 'В вашем пароле нет цифр'


response = validator()
print(response)