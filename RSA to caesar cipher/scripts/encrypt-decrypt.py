import math
import pickle as pickle



def encrypt_msg(public_key,msg):
    e,num=public_key
    encrypted_msg = []
    for i in msg:
        temp=ord(i)
        encrypted_msg.append(pow(temp,e,num))
    return encrypted_msg

if __name__=="__main__":
    path1="../files/publictext"
    path2="../files/plaintext"
    path3="../files/encrypted_msg"

    with open(path1,'rb') as rpk:
        with open(path2,'r') as pt:
            cipher_text=encrypt_msg(pickle.load(rpk),pt.read())

            print("This is the cipher text:",cipher_text)

            with open(path3,'wb') as wpk:
                pickle.dump(cipher_text,wpk)




def decrypt_msg(public_key,encrypted_msg):
    e,num=public_key
    decrypted_msg = []
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()_-=+{[]}\|:;'<,>.?/"
    for i in encrypted_msg:
        if  i in alphabet:
            position=alphabet.find(i)
            new_position= (position-e)%68
            new_character=alphabet[new_position]
            new_message+=new_character
    return decrypted_msg


if __name__=="__main__":
    path1="../files/publictext"
    path2="../files/encrypted_msg"

    with open(path1,'rb') as rpk:
         with open(path2,'rb') as rencrypt_data:
            plaintext=decrypt_msg(pickle.load(rpk),pickle.load(rencrypt_data))
            print("This is the decrypted text:",plaintext)