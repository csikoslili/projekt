host=int(input("add meg a hosztok számát:"))
alap=input("add meg a hálózatot:")
a=0
while a==0:
    for i in range(1,32):
        if int(2**i/host) == 1:
            print(i)
            a=1
        

