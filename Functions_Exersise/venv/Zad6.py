def lenght_validator(password):
    if 6 <= len(password) <= 10:
        return True
    else:
        return False


def conatains_valid_chars(password):
    for each in password:
        if 48 <= ord(each) <= 57 or 65 <= ord(each) <= 122:
            pass
        else:
            return False
    return True


def digit_validator(password):
    counter = 0
    for each in password:
        if 48 <= ord(each) <= 57:
            counter += 1
    if counter>=2:
        return True
    else:
        return False

password = input()

list = [
    [lenght_validator(password),"Password must be between 6 and 10 characters"],
    [conatains_valid_chars(password), "Password must consist only of letters and digits"],
    [digit_validator(password), "Password must have at least 2 digits"]
    ]

is_correct = True
for func, error in list:
    if not func:
        print(error)
        is_correct=False

if is_correct:
    print("Password is valid")