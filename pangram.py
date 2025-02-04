import string

data = input('Enter the data here : ')
vowels = {
    'a' : 0,
    'e' : 0,
    'i' : 0,
    'o' : 0,
    'u' : 0,
}
for i in data:
    if i in vowels:
        vowels[i] += 1
print(vowels)

v = ['a','e','i','o','u']
vd = {}
for i in data:
    if i in v:
        if i in vd:
            vd[i] += 1
        else:
            vd[i] = 1    
    
print(vd)
alph = list(string.ascii_lowercase)
#print(alph)

ad = {}
for i in alph:
    ad[i] = 0
#print(ad)
for i in data:
    if i in ad:
        ad[i] += 1

panag = False
for i in ad:
    if ad[i] >= 1:
        panag = True
    else:
        panag = False

print(ad,panag)
char = {}
'''
for i in data:
    if i isalpha():
        if i in char:
            char[i] += 1
        else:
            char[i] = 1
print(char)
'''
