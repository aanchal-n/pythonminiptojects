import random as rand
import datetime 
d=datetime.date.today().strftime("%d")
p=rand.randrange(1,d+1)
la2=[]
lb2=[]
ladj=[]
for i in range(1,p-2):
  lb2.append(i)
for i in range(p+3,26):
  la2.append(i)
for i in range(p-2,p+3):
  ladj.append(i)
n=int(input("Enter passcode:"))
flag=1
c=0
cor=0
while flag<=5:
  if n==p:
    print("Welcome!!!")
    cor+=1
    break
  else:
    if n in lb2:
      print("invalid passcode")
    elif n in la2:
      print("INVALID PASSCODE")
    elif n in ladj:
      print("InVaLiD PaSsCoDe")
      c+=1
  if c==0 and flag==4:
    break
  if flag<5:
    n=int(input("enter passcode"))
  flag+=1
if (flag==4 or flag==5) and cor!=1:
  print("Login FAILED!!!")
