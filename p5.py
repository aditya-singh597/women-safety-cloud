a={"a":2,"d":4,"c":3,"b":1}
b=sorted(a.items())
print(b)
print(sorted(a.items(), key=lambda x:x[1],reverse=False))