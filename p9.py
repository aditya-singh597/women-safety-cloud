from timeit import default_timer as timer
mylist=['a']*1000000

start=timer()
string=''
for x in mylist:
    string+=x
stop=timer()
print(stop-start)

start=timer()
string=''.join(mylist)
stop=timer()
print(stop-start)

