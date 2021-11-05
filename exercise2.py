inpt=input("Please enter an e-mail:")

def check_mail(mail):
    a=0
    b=0
    for c in mail:
        if c == "@":
            a += 1
        elif c == ".":
            b += 1

    if a >= 1 and b >= 1:
       return True
    else:
        return False

print(check_mail(inpt))
