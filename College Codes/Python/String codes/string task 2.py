l1 = ['Withania Somnifera', 'Curcuma Longa', 'Ocimum Sanctum', 
      'Azadirachta Indica', 'Tinospora Cordifolia', 'Phyllanthus Niruri', 
      'Aloe Vera', 'Glycyrrhiza Glabra', 'Centella Asiatica', 'Bacopa Monnieri']
l2 = []
l3 = []
l4 = []
for i in range(0, len(l1)):
    f = l1[i]
    f = f.upper()
    g = f.lower()
    l2.append(f)
    l3.append(g)

for i in range(0, len(l1)):
    h = l1[i]
    h = h.swapcase()
    l4.append(h)
    
print(l2)
print(l3)
print(l4)
