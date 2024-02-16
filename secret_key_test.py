import random
import string

login_secretkey = ''.join(
    (random.choice(string.ascii_letters + string.digits)) for x in range(32))
print("login_secretkey=", login_secretkey)
