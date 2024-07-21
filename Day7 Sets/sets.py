set1 = {1, 2, 5, "Hellow", "Noob", 3}

print(set1)
print(type(set1))

#Set is unordered every time it shows different value
'''{1, 2, 3, 'Hellow', 5, 'Noob'}
   <class 'set'>'''

#store's duplicate values once
set1.add(input("enter: "))
print(set1) 

#Set are mutable but inside elements immutable  
'''enter: 10
   {1, 2, 3, 5, 'Hellow', 'Noob', '10'}'''
