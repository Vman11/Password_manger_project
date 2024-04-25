import image_hash
import cv2
import os
import hashlib


image_hash.create_directory("Original_Image")
image_hash.create_directory("Secure_Images")
image_hash.create_directory("New_Images")

user_input = input("N: New Password\nC: Check Passwords\n")
print("You entered:", user_input)

if(user_input == "N"):
    print("New Password")
    user_input = input("What is the name of the file? Please Place in New_Files\n")
    if(image_hash.check_file_existence("New_Images", user_input)):
        print("Image Found Generating...")
        changed_image = image_hash.random_change_image("New_Images\\"+str(user_input))
        print(changed_image)
        user_input = input("What is file for?\n")
        if(image_hash.check_file_existence("Secure_Images",str(user_input)+".png")):
           user_input = input("ALERT A FILE ALREADY EXISTS ARE YOU SURE?? [Y/N]\n")
           if( user_input == 'Y' or user_input =='y'):
               cv2.imwrite('Secure_Images\\'+str(user_input)+".png", changed_image)
               print("Image Saved!")
           else:
               print("discarded")
        else:
            cv2.imwrite('Secure_Images\\'+str(user_input)+".png", changed_image)
            print("Image Saved!")
            
        
        
        
    else:
        print("No Image Found..")
    
    
elif(user_input == "C"):
    print("Checking... ")
    for file_name in os.listdir("Secure_Images/"):
        with open("D:\\Password Manager Project\\Secure_Images\\"+str(file_name),"rb") as f:
            bytes = f.read() # read entire file as bytes
            readable_hash = hashlib.sha256(bytes).hexdigest()
            print(str(file_name) + ": " +str(readable_hash))
    
else:
    print("error")
    