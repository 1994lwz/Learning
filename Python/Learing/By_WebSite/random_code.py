import random
import string

code = ''.join(random.sample((string.digits + string.ascii_lowercase + string.ascii_uppercase), 8))
print(code)
