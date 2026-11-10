l1 = ['Withania Somnifera', 'Curcuma Longa', 'Ocimum Sanctum', 
      'Azadirachta Indica', 'Tinospora Cordifolia', 'Phyllanthus Niruri', 
      'Aloe Vera', 'Glycyrrhiza Glabra', 'Centella Asiatica', 'Bacopa Monnieri']

for i in range(0, len(l1)):
    a = l1[i]
    b = a[0]
    if b.isupper():
        print("This word starts with capital: ", a)
print()
for i in range(0, len(l1)):
    a = l1[i]
    res = all(a.isalpha() or a.isspace() for a in a)
    print("Does the string contain only alphabets and spaces:", res)
print()
for i in range(0, len(l1)):
    a = l1[i]
    if len(a.split()) > 1:
        print("This string contains multiple words: ", a)
