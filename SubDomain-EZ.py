import requests
import re

list_sub = []
new=[]
file1 = open('/home/j1t3sh/Documents/Project/subdomain/paytm.txt','r')
count = 0
while True:
    count +=1
    line = file1.readline()

    if not line:
        break
    list_sub.append(line)
    #print(list_sub)
for i in range(len(list_sub)):
    z = str(list_sub[i])
    z = re.sub("\\n$","",z)
    new.append(z)
#print(new)
    #print(list_sub[i])
    #print(count,":",line)

for m in new:
    try:
        response = requests.get(m)
        print(m,":",response.status_code)
    except:
        continue   
file1.close() 