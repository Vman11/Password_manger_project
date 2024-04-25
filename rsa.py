# -*- coding: utf-8 -*- 
# Exploring RSA 

# RSA Encrypt and Decrypt from PEM file 
 
from Crypto.Cipher import PKCS1_OAEP 
from Crypto.PublicKey import RSA 
from Crypto.PublicKey import RSA 
 
#Generate a public/ private key pair using 4096 bits key length (512 bytes) 
new_key = RSA.generate(4096, e=65537) 
 
#The private key in PEM format 
private_key = new_key.exportKey("PEM") 
 
#The public key in PEM Format 
public_key = new_key.publickey().exportKey("PEM") 
 
print (private_key) 
fd = open("private_key.pem", "wb") 
fd.write(private_key) 
fd.close() 
 
print (public_key) 
fd = open("public_key.pem", "wb") 
fd.write(public_key) 
fd.close() 





message =b'Sandwich' 
 
key = RSA.importKey(open('public_key.pem').read()) 
cipher = PKCS1_OAEP.new(key) 
ciphertext = cipher.encrypt(message) 
print (ciphertext) 
key = RSA.importKey(open('private_key.pem').read()) 
cipher = PKCS1_OAEP.new(key) 
plaintext = cipher.decrypt(ciphertext) 
print (plaintext) 