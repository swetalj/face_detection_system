import math
import random
import pickle as pickle


def find_prime_number(number):
    if number<=2 or number%2==0:
        return False
    for i in range(3,math.floor(math.sqrt(number)),2):
        if number % i == 0:
            return False
    return True


def mod_inverse(input_a,input_b):
    mod = input_b
    y = 0
    x = 1
    if input_b == 1:
        return 0
    while input_a > 1:
        k = input_a // input_b
        temp=input_b
        input_b=input_a%input_b
        input_a=temp
        temp=y
        y=x-k*y
        x=temp
    if x<0:
        x=x+mod
        return x
def gcd(x,y):
    while y!=0:
        x,y=y,x%y
    return x

x=pow(20,12)
y=pow(99,8)

def generate_prime_number(start=x,end=y):
    number=random.randint(x,y)
    while(not find_prime_number(number)):
        number=random.randint(x,y)
    return number

def generate_rsa_key():
    prime_number_a=generate_prime_number()
    prime_number_b=generate_prime_number()
    num = prime_number_a*prime_number_b
    phi=(prime_number_a-1)*(prime_number_b-1)
    e=random.randrange(1,phi)
    while gcd(e,phi)!=1:
        e=random.randrange(1,phi)
    d=mod_inverse(e,phi)
    return ((d,num),(e,num))


if __name__=="__main__":
    path1="../files/privatetext"
    path2="../files/publictext"
    private_key,public_key = generate_rsa_key()
    with open(path1,'wb') as wpk:
        pickle.dump(private_key,wpk)
    with open(path2,'wb') as wpub_key:
        pickle.dump(public_key,wpub_key)
    print("This is the privatetext",private_key)
    print("This is the public_key",public_key)
