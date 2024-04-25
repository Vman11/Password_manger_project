import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
def decode(password,path):
    print('decoding...')
    password = password.encode()

    mysalt = b'G\xef\xaa\xe5\xb6\xc7bu\xf2\xcb\r\xe8\xbd\x97s}'

    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256,
        length = 32,
        salt=mysalt,
        iterations = 100000,
        backend = default_backend()
    )

    key =base64.urlsafe_b64encode(kdf.derive(password))

    cipher = Fernet(key)


    directory = path
    
        # iterate over files in
    # that directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            with open(f,'rb') as g:
                e_file = g.read()
                try:
                    encrypted_file = cipher.decrypt(e_file)
                except:
                        return -1
                os.remove(f)

            
            with open(directory+"/" +filename,'wb') as ef:
                ef.write(encrypted_file)
    return 0