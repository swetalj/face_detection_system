import math
import pickle as pickle


def decrypt_msg(private_key,encrypted_msg):
    d,num=private_key

    plain_text=''
    for i in encrypted_msg:
        temp=pow(i,d,num)
        plain_text = plain_text + str(chr(temp))
    return plain_text

if __name__=="__main__":
    path1="../files/privatetext"
    path2="../files/encrypted_msg"

    with open(path1,'rb') as rpk:
         with open(path2,'rb') as rencrypt_data:
            plaintext=decrypt_msg(pickle.load(rpk),pickle.load(rencrypt_data))
            print("This is the decrypted text:",plaintext)


