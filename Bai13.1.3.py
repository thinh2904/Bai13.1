import os
list1=[]
list2=[]
for (a,b,c) in os.walk('D:\\'):
	if c!=[]:
		list1.append(c)
	if b!=[]:
		list2.append(b)
print(list1)	
print(list2)