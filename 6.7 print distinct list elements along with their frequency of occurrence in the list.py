li =[1,2,1,1,3,2,5,6,3,'a','a']
freq = {}
for items in li:
    freq[items] = li.count(items)
print(freq)