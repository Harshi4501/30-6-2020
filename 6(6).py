fh=open("2.txt","a")
fi=open("1.txt","r")
for i in fi:
    fh.write(i)
fh.close()
fh=open("2.txt","r")
print(fh.read())