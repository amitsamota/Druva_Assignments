s='khtkh'

if s==s[::-1]:
    print('palindrome')

print(s[:len(s)//2])
print(s[len(s)//2:])
if s[:len(s)//2] == s[len(s)//2:]:
    
    print('symmetrical')
    