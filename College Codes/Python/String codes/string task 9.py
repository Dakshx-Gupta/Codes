l1 = ['Withania Somnifera', 'Curcuma Longa', 'Ocimum Sanctum', 
      'Azadirachta Indica', 'Tinospora Cordifolia', 'Phyllanthus Niruri', 
      'Aloe Vera', 'Glycyrrhiza Glabra', 'Centella Asiatica', 'Bacopa Monnieri']

first_words = []

for name in l1:
    first, sep, rest = name.partition(' ')
    first_words.append(first)

print("First Words List:")
print(first_words)

# Join them with commas using join()
joined = ', '.join(first_words)

print("\nJoined with commas:")
print(joined)
