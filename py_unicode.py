s = u'Café'
print(type(s.encode('utf-8'))) # <class 'bytes'>

s = bytes('Café', encoding='utf-8')
print(s.decode('utf-8'))

# get unicode code point
s = u'Café'
for _c in s: print('U+%04x' % ord(_c))

# unicode normalization
u1 = 'Café'
u2 = 'Cafe\u0301'

print(u1, u2) # 'Café', 'Café'

print(len(u1), len(u2)) # 4, 5

print(u1 == u2) # False

print(u1.encode('utf-8')) 
print(u2.encode('utf-8'))

from unicodedata import normalize
s1 = normalize('NFC', u1) # get NFC format
s2 = normalize('NFC', u2)
print(s1 == s2) # True

print(s1.encode('utf-8'), s2.encode('utf-8')) 

s1 = normalize('NFD', u1) # get NFD format
s2 = normalize('NFD', u2)

print(s1 == s2) # True

print(s1.encode('utf-8'), s2.encode('utf-8'))
