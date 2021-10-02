print("##########1##########")
print()
#lista [3 ,.... ,10]
x=[x for x in range(3,11)]
#lista [0,.... ,3]
y=[y for y in range(3)]

z=list(zip(x,y))
print(z)                                        #[(3, 0), (4, 1), (5, 2)]

print (any(([],(0),0)))                         #False

#długość krótszej z xi y
size=len(list(zip(x,y)))

#suma elementów o zgodnych indeksach
#dla size elementów od końca z listy x
#i size elementów od początku z listy y
d=[k for k in map(lambda x,y:x+y, x[len(x)-size::1], y)]
print(d)                                        #8, 10, 12]

nums = list (range (2, 30))
for i in range (2, 8):
    nums=list((filter(lambda x: x%i or x==i, nums)))
print (nums)                                      #[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
