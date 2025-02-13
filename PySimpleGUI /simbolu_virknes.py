virkne3 = "Te ir simbolu virkne"
print(virkne3.split(" "))
print(*virkne3.split(" "))

for i in range(10, 21, 2):
	print(i)

n = int(input() )
for i in range(n):
	print("Sveiks!", end=" ") 

teksts = input()
vardi=teksts.split()  
# tiek sadalīts pa vārdiem, iegūstot vārdu sarakstu.
for vards in vardi :
	print(len(vards) )




