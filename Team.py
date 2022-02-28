value = int(input())
y = 0
z = 0
for x in range(0,value):
    val1 = input()
    z = int(val1.count("1"))
    if z>= 2:
        y+=1;
print(y)