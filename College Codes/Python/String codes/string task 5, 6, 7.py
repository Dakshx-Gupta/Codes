l1 = ['Withania Somnifera', 'Curcuma Longa', 'Ocimum Sanctum', 
      'Azadirachta Indica', 'Tinospora Cordifolia', 'Phyllanthus Niruri', 
      'Aloe Vera', 'Glycyrrhiza Glabra', 'Centella Asiatica', 'Bacopa Monnieri']

translation_table = str.maketrans('aeiouAEIOU', '1234512345')
encoded_barcodes = []

for i in range(0, len(l1)):
    a = l1[i].upper()
    a = a.replace(" ", "-")
    a = "PLANT-" + a
    
    #string task 7 starts
    encoded = a.encode()
    translated = a.translate(translation_table)

    encoded_barcodes.append({
        'original'   : a,
        'encoded'    : encoded,
        'translated' : translated
    })

# Display results
for item in encoded_barcodes:
    print(f"Original   : {item['original']}")
    print(f"Encoded    : {item['encoded']}")
    print(f"Translated : {item['translated']}")
    print("-" * 45)

#string task 6
#     print("Center Aligned")
#     print(a.center(40,"*"))
#     print()
#     print("Left Aligned")
#     print(a.ljust(40, "*"))
#     print()
#     print("Right Aligned")
#     print(a.rjust(40, "*"))
