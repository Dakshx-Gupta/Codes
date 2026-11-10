l1 = ['Withania Somnifera', 'Curcuma Longa', 'Ocimum Sanctum', 
      'Azadirachta Indica', 'Tinospora Cordifolia', 'Phyllanthus Niruri', 
      'Aloe Vera', 'Glycyrrhiza Glabra', 'Centella Asiatica', 'Bacopa Monnieri']

for i in range(0, len(l1)):
    a = l1[i]
    print("Number of times character 'a' appears in the word", a, "is:", a.count("a"))
    print("Position of first 'i' is: ", a.find('i'))
    print("Position of last 'a' is: ", a.rfind('a'))
