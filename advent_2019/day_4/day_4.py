
import re

def check_password(pw: int) -> bool:
    #Confirm 6 digits
    if len(str(pw)) != 6:
        return False

    #Confirm valid range
    if pw < 178416 or pw > 676461:
        return False

    #Confirm [exactly] 2 digits repeat
    rx = r'(\d)(?<!\1\1)\1(?!\1)'
    if re.search(rx, str(pw)) == None:
        return False

    #Confirm all numbers increase and there's a group of exactly two
    last_i = str(pw)[0]
    for i in str(pw)[1:]:
        if i < last_i:
            return False

        last_i = i

    #Passed all checks
    return True

def count_valid_passwords(pw_range: str) -> int:
    begin = int(pw_range.split("-")[0])
    end = int(pw_range.split("-")[1])

    valid_passwords = 0
    for pw in range(begin, end + 1):
        if check_password(pw):
            valid_passwords += 1
    
    return valid_passwords

print(count_valid_passwords("178416-676461"))

def check_password_orig(pw: int) -> bool:
    #Confirm 6 digits
    if len(str(pw)) != 6:
        return False

    #Confirm valid range
    if pw < 178416 or pw > 676461:
        return False

    #Confirm 2 digits repeat
    rx = r"(\d)\1"
    if re.search(rx, str(pw)) == None:
        return False

    #Confirm all numbers increase
    last_i = str(pw)[0]
    for i in str(pw)[1:]:
        if i < last_i:
            return False
        last_i = i

    #Passed all checks
    return True