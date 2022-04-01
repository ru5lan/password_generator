from random import choices

def generator(length):
    keys = 'abcdefghigklmnopqrstuvwxyz1234567890ABCDEFGHIGKLMNOPQRSTUVWXYZ'
    password = ''.join(choices(keys, k = length))
    return password

length = int(input("Enter length of password:"))
result = generator(length)
print(f"Your password:{result}")

