import requests
import re
import subprocess
from subprocess import Popen, PIPE
import os

def subdomain():
    p = Popen(['/usr/bin/which', "assetfinder"], stdout=PIPE, stderr=PIPE)
    p.communicate()
    if(p.returncode == 1):
        os.system("wget https://github.com/tomnomnom/assetfinder/releases/download/v0.1.0/assetfinder-linux-amd64-0.1.0.tgz")
        os.system("tar zxvf assetfinder-linux-amd64-0.1.0.tgz;chmod +x assetfinder;sudo cp assetfinder /usr/bin/;rm assetfinder-linux-amd64-0.1.0.tgz;rm assetfinder")
        subdomain()
    else:
        x = input("Enter the Website to find Subdomains : ")
        print("[+]Finding all the possible subdomains....")
        os.system("assetfinder --subs-only " + x + " | httprobe > " + x + ".txt")
        list_sub = []
        new_list=[]
        file1 = open(x + '.txt','r')
        count = 0
        while True:
            count +=1
            line = file1.readline()

            if not line:
                break
            list_sub.append(line)
        print("Total no. of Subdomains Found for "+x+" - "+str(len(list_sub)))
        for i in range(len(list_sub)):
            z = str(list_sub[i])
            z = re.sub("\\n$","",z)
            new_list.append(z)

        for m in new_list:
            try:
                response = requests.get(m)
                if response.status_code == 200:
                    print(m,":",response.status_code,response.reason)
            except:
                continue   
        file1.close() 
        os.system("rm "+x+".txt")
subdomain()    