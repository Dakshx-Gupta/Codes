e = int(input("Enter the num of elements: "))
nums = []
for i in range(0, e):
    x = int(input('Enter the values: '))
    nums.append(x)
v = int(input('Which num you want to remove from the list: '))
for n in range(0, len(nums)):
    for j in nums:
        if j == v:
            nums.remove(j)
print()
print("List: ", nums)
print("Number of items in the list: ", len(nums))
