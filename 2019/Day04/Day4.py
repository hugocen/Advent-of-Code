def check_double(password, il=None):
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            if i+2 < len(password):
                if password[i+1] != password[i+2]:
                    return True
                else:
                    left = password[i+3:].replace(password[i], '')
                    if len(left) > 1:
                        return check_double(left)
                    else:
                        return False
            else:
                return True

def check(password):
    password = str(password)
    if check_double(password):
        for j in range(len(password)-1):
            if int(password[j]) > int(password[j+1]):
                return False
        return True
    else:
        return False
    
num = 0
for password in range(234208,(765869+1)):    
    if check(password):
        num += 1
print(num)
