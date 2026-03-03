import turtle

ob=turtle.Turtle(); 
ob.speed(10000) 
ob.hideturtle() 
turtle.bgcolor("black") 
ob.pencolor("green") 
old=['f','l'] 
new=['f','l'] 
steps=[] 
k=0 
iterations=int(input("Iterations : ")) 
size=int(input("Size of lines : ")) 
while(k<iterations): 
 for i in range(0,len(old)-1): 
  if old[i]=='r': 
   old[i]='l' 
  elif old[i]=='l': 
   old[i]='r' 
  for i in range(0,len(old)//2): 
   t=old[i] 
   old[i]=old[len(old)-i-2] 
   old[len(old)-i-2]=t 
  for i in old: 
   new.append(i) 
  for i in old[:]: 
   old.remove(i) 
  for i in new: 
   old.append(i) 
  for i in steps[:]: 
   steps.remove(i) 
  for i in range(0,len(new)): 
   steps.append(new[i]) 
   k+=1 
  for i in steps: 
   if i=='f': 
    ob.forward(size) 
   elif i=='r': 
    ob.right(90) 
   elif i=='l': 
    ob.left(90) 
import turtle 
turtle.speed(10000) 
turtle.hideturtle() 
wn=turtle.Screen() 
wn.bgcolor("black") 
turtle.pencolor("green") 
 
def dragoncurve(l,n): 
  for i in range(1): 
    def x(n): 
            if n==0: 
                    return 
            x(n-1) 
            turtle.right(90) 
            y(n-1) 
            turtle.forward(l) 
    def y(n): 
            if n==0: 
                    return 
            turtle.forward(l) 
            x(n-1) 
            turtle.left(90) 
            y(n-1) 
    turtle.fd(l) 
    x(n) 
dragoncurve(5,15)
