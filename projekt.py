
host=int(input("add meg a hosztok számát:"))
host+=2
egy=0
ketto=0
harom=0
negy=0

alap=input("add meg a hálózatot:")

darabolt=alap.split(".")
egy=int(darabolt[0])
ketto=int(darabolt[1])
harom=int(darabolt[2])
negy=int(darabolt[3])

a=0
while a==0:
    for i in range(1,32):
        if int(2**i/host) == 1:
            a=i
        
x=32-a
y=x

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


if 2**a <= (2**8)-1:
    negy+=2**a

elif 2**a <= (2**16)-1:
    negy=0
    harom+=int(2**a/2**8)

elif 2**a <= (2**24)-1:
    negy=0
    harom=0
    ketto+=int(2**a/2**16)

else:
    negy=0
    harom=0
    ketto=0
    egy+=int(2**a/2**32)


print()
print()
print("hálózat: {}/{}".format(alap,y))
print("alhálózati maszk: {}.{}.{}.{}".format(elso,masodik,harmadik,negyedik))
print()
print("következő hálózat: {}.{}.{}.{}/{}".format(egy,ketto,harom,negy,y))