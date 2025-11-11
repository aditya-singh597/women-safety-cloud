my_list=[1,2,3,4,5,2]
for i in my_list:
    if my_list.count(i)>1:
        my_list.remove(i)
print(my_list)        