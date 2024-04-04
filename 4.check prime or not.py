num=int(input("enter a number:"))
if num==1:
  print("its a prime")
elif num>2:
  for i in range(2,num):
    if num%i==0:
      print("its not a prime")
      break
    else:
      print("its a prime") 
      break
else:
  print("not a prime")      
  
