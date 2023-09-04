
import random 

r = int(input("number of letters you need in your password  "))
n = int(input("how many number you need   "))
s = int(input("how many symbols you need   "))

symbol = ['!', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']


print(" Welcome to Password Generator ")

word = []
for i in range (1, r + 1):
     word += random.choice(letters)
#print(word)   

num = ""
for i in range (1, n + 1):
     word += random.choice(number)
#print(num)   

sym = ""
for i in range (1, s + 1):
     word += random.choice(symbol)

# print(sym)   
random.shuffle(word)

print("your password is  : ")

#print((word))

password = ""
for i in word :
     password += i

print(password)     