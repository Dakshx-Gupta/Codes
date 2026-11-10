plants = [" withania SOMNIFERA ", "Curcuma_longa123", "Ocimum@Sanctum", " azadirachta indica ", "Tinospora-Cordifolia",
          "phyllanthus niruri ", " Aloe VERA ", "glycyrrhiza glabra##", "Centella@Asiatica", " Bacopa Monnieri "]
l2 = []
l3 = []
l4 = []
for i in range(0, len(plants)):
    a = plants[i].title()
    l2.append(a.strip())

# print(l2)
for i in range(0, len(l2)):
    # print(l2[i])
    b = l2[i]
    for i in range(0, len(b)):
        if b[i].isdigit() or b[i] == "#" or b[i] == "_" or b[i] == "@" or b[i] == "-":
            c = b[i]
            # print(b)
            b = b.replace(c, " ")
    l3.append(b)
# print(l3)
for i in range(0, len(l3)):
    e = l3[i]
    l4.append(e.strip())
print(l4)
for i in range(0, len(l4)):
    f = l4[i]
    f = f.swapcase()
    print(f)
