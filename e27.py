n=int(input("Donner un nombre : "))
while n<=0 :
    n=int(input("Donner un nombre : "))
s=0
for i in range(1,n+1):
    if n % i ==0 :
        print(i)
    
