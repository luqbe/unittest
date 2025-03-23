#using list comprehension
list=[1,2,3,24,5,10,7,8,78]
list_comp=[x for x in list[::2] if x%2==0]
print(list_comp)