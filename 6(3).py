fh=open("2.txt","r")
l1=fh.readlines()
m=len(l1)
n=int(input("ener n:"))
print(l1[(m-n):])