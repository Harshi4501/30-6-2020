fh=open("2.txt","a")
x=input("Enter string to be appended:")
fh.write(x)
fh.close()
fh=open("2.txt","r")
print(fh.read())