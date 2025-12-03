import random
import string
def generate_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+=-"
    password = ''.join(random.choice(chars) for i in range(length))
    return password
length = int(input("طول پسورد؟"))
print("پسورد تصادفی شما:",generate_password(length))