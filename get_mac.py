

# Python 3 code to print MAC
# in formatted way.
 
import uuid
from hashlib import sha256
# joins elements of getnode() after each 2 digits.
 
print ("The MAC address in formatted way is : ", end="")
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))

test=hex(uuid.getnode())


print(sha256(test.encode('utf-8')).hexdigest())