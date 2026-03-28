print('____REVERSE STRINGS____')

i='Hello world'
print(i[::-1])

i='Hello world'
res=''
for ind in i:
    res=ind+res
print(res)

i='Hello world'
res=''
for ind in range(len(i)):
    res=i[ind]+res
print(res)

i='Hello world'
res=''
for ind in range(len(i)-1,-1,-1):
    res+=i[ind]
print(res)

i='Hello world'
res=''
ind=len(i)-1
while ind!=-1:
    res+=i[ind]
    ind-=1
print(res)

print('_____STRINGS POLINDROM OR NOT_____')

s='malayalam'
if s==s[::-1]:
    print('polindrom')
else:
    print('Not polindrom')
for ind in range(len(s)):
    if s[ind]!=s[-ind-1]:
        print('Not polindrom')
        break
else:
    print('polindrom')

s='malayalam'
ind=0
while ind!=0:
    if s[ind]!=s[-ind-1]:
        print('Not polindrom')
        break
    ind+=1
else:
    print('polindrom')
    
print('_____VOWELS IN STRING_____')

string='Iam a Good Boy'
vow='aeioiuAEIOU'
res=''
for ch in string:
    if ch in vow:
        res+=ch
print(res)

string='Iam a Good Boy'
res=''
for ch in string:
    if ('A'<=ch<='Z'):
        res+=ch
print(res)

string='Iam a Good Boy'
res=''
for ch in string:
    if ('a'<=ch<='z'):
        res+=ch
print(res)

string='Iam a Good Boy'
vow='aeioiuAEIOU'
res=''
for ch in string:
    if ch in vow and ('a'<=ch<='z'):
        res+=ch
print(res)

string='Iam a Good Boy'
vow='aeioiuAEIOU'
res=''
for ch in string:
    if ch in vow and ('A'<=ch<='Z'):
        res+=ch
print(res)

string='Iam a Good Boy'
res=''
for ch in string:
    if ('a'<=ch<='z'):
        res+=chr(ord(ch)-32)
    else:
        res+=ch
print(res)

string='Iam a Good Boy'
res=''
for ch in string:
    if ('A'<=ch<='Z'):
        res+=chr(ord(ch)+32)
    else:
        res+=ch
print(res)

string='Iam a Good Boy'
res=''
for ch in string:
    if('A'<=ch<='Z'):
        res+=chr(ord(ch)+32)
    elif('a'<=ch<='z'):
        res+=chr(ord(ch)-32)
    else:
        res+=ch
print(res)

print('____SUBSTRINGS_____')

m='mama'
for si in range(len(m)):
    for ei in range(si+1,len(m)+1):
        print(m[si:ei])
        
print('********')
m='mama'
for si in range(len(m)):
    for ei in range(si+1,len(m)+1):
        res=''
        for val in range(si,ei):
            res+=m[val]
        print(res)
        
print('********')
m='mama'
for si in range(len(m)):
    for ei in range(si+1,len(m)+1):
        res=m[si:ei]
        if res==res[::-1]:
            print(res)
print('********')
s='aaabbcccd'
count=1
res=''
for ind in range(len(s)-1):
    if s[ind]==s[ind+1]:
        count+=1
    else:
        res+=str(count)+s[ind]
res+=str(count)+s[ind+1]
print(res)

m='3a2b3c1d'
res=''
for ind in range(0,len(m),2):
    res+=int(m[ind])*m[ind+1]
print(res)

print('____REMOVE STRINGS____')

s='engineering'
res=''
for ch in s:
    if ch not in res:
        res+=ch
print(res)

s='degree'
res=''
ind=0
while ind!=len(s):
    if s[ind]not in res:
        res+=s[ind]
    ind+=1
print(res)

s='engineering'
res=''
for ch in s:
    if ch not in res:
        res+=ch
for ch in res:
    print(f'{ch}={s.count(ch)}')

print('____BUILT IN METHODS IN STRINGS____')

s='Hello world'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())
print(s.split())
print(s.split('l'))
print(s.replace('e','a'))
print(s.index('l'))
print(s.find('o'))
print(s.rindex('d'))
print(s.startswith('He'))
print(s.endswith('ld'))
print(s.count('l'))
print(s.strip('l'))
print(sorted(s))
