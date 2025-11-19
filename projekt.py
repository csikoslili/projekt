
host=int(input("add meg a hosztok számát:"))
host+=2
alap=input("add meg a hálózatot:")
a=0
while a==0:
    for i in range(1,32):
        if int(2**i/host) == 1:
            a=i
        
x=32-a
print(x)

elso=0
masodik=0
harmadik=0
negyedik=0

if x>=8:
    elso=255
    x=x-8
else:
    elso=256-(2**(8-x))

if x>=8:
    masodik=255
    x=x-8
    print(x)
else:
    if elso==255:
        masodik=256-(2**(8-x))

if x>=8:
    harmadik=255
    x=x-8
else:
    if masodik==255:
        harmadik=256-(2**(8-x))

if x>=8:
    negyedik=255
    x=x-8
else:
    if harmadik==255:
        negyedik=256-(2**(8-x))



print("alhálózati maszk: {}.{}.{}.{}".format(elso,masodik,harmadik,negyedik))
<<<<<<< HEAD

=======
print(2**(8-x))
#asd
>>>>>>> f465c9c326a11b7d4179d11bed9ca5549f21b74c
