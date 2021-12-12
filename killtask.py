#Made by Copecofee - Ethical Hacker

import os

os.system("clear")

id = os.getuid()
if id != 0:
 exit("PLEASE RUN THE SCRIPT AS SUDO")
else:
 pass


install = str(print("What Do you want to install: "))

print("kali-2021.3 iso      [1]")
print("Kali Weekly iso      [2]")
print("balenaEtcher         [3]")
print("Visual Studio Code   [4]")
print("metasploitable-linux [5]")
print("Kali Linux ova       [6]")
print("Windows 7  ova       [7]")
print("Windows 10 ova       [8]")
print("NGROK                [9]")
print("ALL OPTIONS         [100]")
choose = int(input("  ====CHOOSE====> "))

#-------------------------------------------------------------------------------------------------------

option1 = "https://cdimage.kali.org/kali-2021.3/kali-linux-2021.3a-live-amd64.iso"
option2 = "https://cdimage.kali.org/kali-images/kali-weekly/kali-linux-2021-W48-live-amd64.iso"
option3 = "https://github.com/balena-io/etcher/releases/download/v1.7.1/balena-etcher-electron-1.7.1-linux-x64.zip?d_id=929341b7-22bf-47c8-81d2-22ab8ec22b59R"
option4 = "https://az764295.vo.msecnd.net/stable/ccbaa2d27e38e5afa3e5c21c1c7bef4657064247/code_1.62.3-1637137107_amd64.deb"
option5 = "https://sourceforge.net/projects/metasploitable/files/latest/download"
option6 = "https://kali.download/virtual-images/kali-2021.3/kali-linux-2021.3-virtualbox-amd64.ova"
option7 = "https://az792536.vo.msecnd.net/vms/VMBuild_20150916/VirtualBox/IE8/IE8.Win7.VirtualBox.zip"
option8 = "https://az792536.vo.msecnd.net/vms/VMBuild_20190311/VirtualBox/MSEdge/MSEdge.Win10.VirtualBox.zip"
option9 = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.tgz"

list = [option1, option2, option3, option4, option5, option6, option7, option8, option9]

#--------------------------------------------------------------------------------------------------------

#kali-2021.3 iso (1)

if choose == 1:
 try:
  os.system("clear")
  os.system("wget {}".format(option1))
 except:
   print("Something Went Wrong")

#Kali Weekly iso (2)

elif choose == 2:
 try:
  os.system("clear")
  os.system("wget {}".format(option2))
 except:
   print("Something Went Wrong")


#balenaEtcher (3)

elif choose == 3:
 try: 
  os.system("clear")
  os.system("wget {}".format(option3))
  os.system("clear")
  change3 = str(input("Wanna install right now? yes/no  "))
  if change3 == 'yes' or change3 == 'y' or change3 == 'Yes':
   print(os.system("mv balena-etcher-electron-1.7.1-linux-x64.zip\?d_id=929341b7-22bf-47c8-81d2-22ab8ec22b59R balena-etcher-electron-1.7.1-linux-x64.zip\?d_id=929341b7-22bf-47c8-81d2-22ab8ec22b59R.zip"))
   print(os.system("unzip balena-etcher-electron-1.7.1-linux-x64.zip\?d_id=929341b7-22bf-47c8-81d2-22ab8ec22b59R.zip"))
   print(os.system("rm -rf balena-etcher-electron-1.7.1-linux-x64.zip\?d_id=929341b7-22bf-47c8-81d2-22ab8ec22b59R.zip"))
  else:
   print("Write ====> dpkg -i code_1.62.3-1637137107_amd64.deb")
 except:
   print("Something Went Wrong")


#Visual Studio Code (4)

elif choose == 4:
 try: 
  os.system("clear")
  os.system("wget {}".format(option4))
  change4 = str(input("Wanna install the deb? yes/no  "))
  if change4 == 'yes' or change4 == 'y' or change4 == 'Yes':
   print(os.system("dpkg -i code_1.62.3-1637137107_amd64.deb && rm -rf code_1.62.3-1637137107_amd64.deb"))
  else:
    print("Write ====> dpkg -i code_1.62.3-1637137107_amd64.deb && rm -rf code_1.62.3-1637137107_amd64.deb")
 except:
   print(os.system("clear && echo 'Something Went Wrong' "))


#metasploitable-linux (5)

elif choose == 5:
 try:
  os.system("clear")
  os.system("wget {}".format(option5))
  change5 = str(input("Wanna install the zip? yes/no "))
  if change5 == 'yes' or change5 == 'y' or change5 == 'Yes':
   print(os.system("mv download download.zip && unzip download.zip "))
  else:
   print("Write ====> mv download download.zip && unzip download.zip")
 except:
  print("Something Went Wrong")


#Kali Linux ova (6)

elif choose == 6:
 try: 
  os.system("clear")
  os.system("wget {}".format(option6))
 except:
   print("Something Went Wrong")

#Windows 7 ova (7)

elif choose == 7:
 try: 
  os.system("clear")
  os.system("wget {}".format(option7))
  change7 = str(input("Extract the file? yes/no  "))
  if change7 == 'yes' or change7 == 'y' or change7 == 'Yes':
   print(os.system("unzip IE8.Win7.VirtualBox.zip && rm -rf IE8.Win7.VirtualBox.zip"))
  else:
   print("Write ====> unzip IE8.Win7.VirtualBox.zip && rm -rf IE8.Win7.VirtualBox.zip")
 except:
   print("Something Went Wrong")
   
#Windows 10 ova (8)

elif choose == 8:
 try:
  os.system("clear")
  os.system("wget {}".format(option8))
  change8 = str(print("Extract the file? yes/no  "))
  if change8 == 'yes' or change8 == 'y' or change8 == 'Yes':
   print(os.system("unzip MSEdge.Win10.VirtualBox.zip && rm -rf MSEdge.Win10.VirtualBox.zip"))
  else:
   print("Write ====> unzip MSEdge.Win10.VirtualBox.zip && rm -rf MSEdge.Win10.VirtualBox.zip")
 except:
   print("Something Went Wrong")

#NGROK (9)

elif choose == 9:
 os.system("clear")
 os.system("wget {}".format(option9))
 change9 = str(input("Extract the file? yes/no  "))
 if change9 == 'yes' or change9 == 'y' or change9 == 'Yes':
  print(os.system("tar -xf ngrok-stable-linux-amd64.tgz && rm -rf ngrok-stable-linux-amd64.tgz"))

#ALL OPTION (100)

elif choose == 100:
 for options in list:
  os.system("mkdir here && cd here")
  print(os.system("clear"))
  print(os.system("wget {}".format(options)))

#CHOSING NOT FOUND
 
else:
 print("There's no option {}".format(choose))
 
