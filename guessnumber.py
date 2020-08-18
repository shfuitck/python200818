import random
num=random.randint(1,20)
i=1
while i<6:
    ans=int(input("please tipethe number:"))
    if ans==num:
        print("you are right at ", i ,"time")
        break
    else:
        if num<ans:
          print("to big")
        else:
          print("to small")  
    i=i+1    

