s = input("")
if 'a' in s:
    print("Index of the vowel:", s.index('a'))
    s = s.replace('a', 'b')
if 'e' in s:
    print("Index of the vowel:", s.index('e'))
    s = s.replace('e', 'f')
if 'i' in s:
    print("Index of the vowel:", s.index('i'))
    s = s.replace('i', 'j')
if 'o' in s:
    print("Index of the vowel:", s.index('o'))
    s = s.replace('o', 'p')
if 'u' in s:
    print("Index of the vowel:", s.index('u'))
    s = s.replace('u', 'v')
print("After replacing vowels")
print(s)
