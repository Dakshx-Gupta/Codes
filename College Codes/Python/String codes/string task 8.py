l1 = ['Withania Somnifera', 'Curcuma Longa', 'Ocimum Sanctum', 
      'Azadirachta Indica', 'Tinospora Cordifolia', 'Phyllanthus Niruri', 
      'Aloe Vera', 'Glycyrrhiza Glabra', 'Centella Asiatica', 'Bacopa Monnieri']

cleaned_names = []

for name in l1:
    first, sep, rest = name.partition(' ')
    print(f"Original  : {name}")
    print(f"Partition : ('{first}', '{sep}', '{rest}')")
    print(f"First Word: {first}  |  Rest: {rest}")
    cleaned_names.append(name)
    
# Combine all names into ONE multi-line string
multiline_string = '\n'.join(cleaned_names)

print("\nMulti-line String:")
print(multiline_string)

# Split using splitlines()
split_result = multiline_string.splitlines()

print("\nAfter splitlines():")
for line in split_result:
    print(f"  → {line}")
