from colorama import Fore
import time
def affiche(l,n,state):
       if(state!=7):
              print(Fore.BLACK+"|",end="")
              for i in range(len(l)) :
                     if(i!=n):
                            print(Fore.BLACK+l[i]+Fore.BLACK+"|" , end="")
                     else:
                            print(Fore.RED+l[i]+Fore.BLACK+"|" , end="")

              print("  ")
       else:
              s=0
              print(Fore.BLACK+"|",end="")
              for i in range(len(l)) :
                     if(l[i]!="1"):
                            print(Fore.BLACK+l[i]+Fore.BLACK+"|" , end="")
                     else:
                            print(Fore.RED+l[i]+Fore.BLACK+"|" , end="")
                            s+=1
                            

              print("  ")
              print("resultat = " , s)
              
       
              
       
n=int(input("donner le nombre 1 "))
m=int(input("donner le nombre 1 "))
l=[]
for i in range(n*m+5*max(m,n) ):
       l.append("B")
for i in range(2,n+2):
       l[i]="1"
l[n+2]="0"
for i in range(n+3,n+3+m):
       l[i]="1"
l[n+m+3]="0"
i=2
state=0

while state!=7 :
       time.sleep(1) 
      
       affiche(l,i,state)     
       if(state==0):
              if(l[i]=="1" ) :
                     l[i]="B"
                     i+=1
                     state=1
              elif(l[i]=="0"):
                       l[i]="B"
                       i+=1
                       state=6
       elif(state==1):
              if(l[i]=="1"):
                     l[i]="1"
                     i=i+1
              elif(l[i]=="0"):
                     l[i]="0"
                     i+=1
                     state=2
       elif(state==2):
              if(l[i]=="1"):
                     l[i]="X"
                     i+=1
                     state=3
              elif(l[i]=="0"):
                     i-=1
                     state=5
       elif(state==3):
              if(l[i]=="1" or l[i]=="0"):
                     i+=1
              elif(l[i]=="B"):
                     l[i]="1"
                     i-=1
                     state=4
       elif(state==4):
              if(l[i]=="1" or l[i]=="0"):
                     i-=1
              elif(l[i]=="X"):
                     i+=1
                     state=2
       elif(state==5):
              if(l[i]=="X"):
                     l[i]="1"
                     i-=1
              elif(l[i]=="1" or l[i]=="0"):
                     i-=1
              else:
                     i+=1
                     state=0
       elif(state==6):
              if(l[i]=="1"):
                     l[i]="B"
                     i+=1
              elif(l[i]=="0"):
                     l[i]="B"
                     i+=1
                     state=7
              
time.sleep(1) 
                     
affiche(l,-1,state)             
              
              
       
