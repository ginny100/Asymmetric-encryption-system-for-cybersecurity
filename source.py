import random

'''Test if p is prime with Fermat\'s little theorem\n'''
def Fermat(p = 137):
    t = True
    #running this 30 times
    for i in range(31):
        x = random.randint(2, p)
        if pow(x, p-1, p) != 1:
            t = False
            break
    if not t:
        return
    else:
        #print(p, 'is prime.')
        return "prime"

''' The gcd function implements Euclid's
    GCD algorithm to find the greatest common
    divisor of two positive integers a and b'''
def gcd(a=1, b=1):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

''' The extended_gcd function implements the
    extension of Euclid's GCD algorithm  to find integers x and y
    such that d = ax + by = gcd(a, b) '''
def extended_gcd(a = 1, b = 1):
    if b == 0:  # We cannot devide anymore, just return (1,0,a)
        return (1, 0, a)
    (x, y, d) = extended_gcd(b, a%b)
    return y, x - a//b*y, d


def general(e, n, S, prmessage):
    pm = 0
    while True:
        #userd stands for user decision
        while True:
            userd = input("Type encrypt or authenticate: ")
            if S != 0 or userd == "encrypt":
                break
            else:
                print("There is no signature to authenticate")
                #stoppage = input("If you want to do someting else type y \nIf you want to terminate the conversation type t \nOtherwise type n to go to the next person: ")
        if userd == "encrypt":
            message = input("Message: ")
            message = int(message)
            #pm = public message
            pm = pow(message, e, n)
            print("Your encrypted message is " + str(pm))
        elif userd == "authenticate":
            print("The original message is " + str(prmessage))
            print("The signature is " + str(S))
            check = pow(S, e, n)
            print("The decrypted signature is " + str(check))
            if check == prmessage:
                print("The message is authentic!")
            else:
                print("The message is NOT authentic")
        stoppage = ""
        if S != 0:
            stoppage = input("If you want to encrypt a message or reauthenticate type y \nIf you want to terminate the conversation type t \nOtherwise type n to go to the next person: ")
            if stoppage != "y":
                return pm, stoppage
        else:
            return pm, stoppage

def owner(publicmessage, Signature):
    while True:
        #userd stands for user decision
        prmessage = 0
        while True:
            userd = input("Type decrypt or sign: ")
            if publicmessage != 0 or userd == "sign":
                break
            else:
                print("There is no message to decrypt")
        if userd == "sign":
            prmessage = input("Message: ")
            prmessage = int(prmessage)
            Signature = pow(prmessage, d, n)
            print("This is your Signature: " + str(Signature))
        elif userd == "decrypt":
            decryptedmessage = pow(publicmessage, d, n)
            print("This is your decrypted message " + str(decryptedmessage))
        stoppage = ""
        if publicmessage != 0:
            stoppage = input("If you want to write a new signature or decrypt again type y \nIf you want to terminate the conversation type t \nOtherwise type n to go to the next person: ")
            if stoppage != "y":
                return Signature, prmessage, stoppage
        else:
            return Signature, prmessage, stoppage

# def signature(e, Fofn):

#     d, g, r = extended_gcd(e, Fofn)
publicmessage = 0 
S = 0
prmessage = 0

while True: 
    while True:
        p = random.randint(10000, 100000)
        if Fermat(p) == "prime":
            break
    while True:
        q = random.randint(10000, 100000)
        if Fermat(q) == "prime":
            break
    if p != q:
        break
n = p*q
Fofn = (p-1)*(q-1)
#print(p, q, n, Fofn)
for i in range(2, Fofn): 
    e = random.randint(2, Fofn)      
    if gcd(e, Fofn) == 1: 
        break
#print(e)
d, g, r = extended_gcd(e, Fofn)
#print(d, g, r)
print("Bob")
Bob = input("Enter if you are a general user or keys owner: ")
if Bob == "general user":
    #given public key and digital signature from owner
    publicmessage, stoppage = general(e, n, S, prmessage)
elif Bob == "keys owner":
    #given both public and private key
    S, prmessage, stoppage = owner(publicmessage, S)
print("\n\nAlice")
Alice = input("Enter if you are a general user or keys owner: ")
if Alice == "general user":
    #given public key and digital signature from owner
    publicmessage, stoppage = general(e, n, S, prmessage)
elif Alice == "keys owner":
    #given both public and private key
    S, prmessage, stoppage = owner(publicmessage, S)
while True:
    print("\n\nBob " + Bob)
    #Bob = input("Enter if you are a general user or keys owner: ")
    if Bob == "general user":
        #given public key and digital signature from owner
        publicmessage, stoppage = general(e, n, S, prmessage)
    elif Bob == "keys owner":
        #given both public and private key
        S, prmessage, stoppage = owner(publicmessage, S)
    if stoppage == "t":
        break
    print("\n\nAlice " + Alice)
    #Alice = input("Enter if you are a general user or keys owner: ")
    if Alice == "general user":
        #given public key and digital signature from owner
        publicmessage, stoppage = general(e, n, S, prmessage)
    elif Alice == "keys owner":
        #given both public and private key
        S, prmessage, stoppage = owner(publicmessage, S)
    if stoppage == "t":
        break
# message = 298483438
# encryptedmessage = pow(message, d, n)
# print(encryptedmessage)
# decryptedmessage = pow(encryptedmessage, e, n)
# print(decryptedmessage)
