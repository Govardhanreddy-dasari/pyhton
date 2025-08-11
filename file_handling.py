'''
open
read or write
close
'''
x=open("demo.txt",mode="r")
print(x.read())
x.close()
'''y=open("demo.txt","r")
print(y.read())
y.close()'''
'''x=open("demo.txt","w")
x.write("hello world")
x.close()'''
'''m=open("demo.txt","a")
m.write("\nhello world")
m.close()'''
'''r=open("demo.txt","w+")
r.write("hello world")
r.seek(0)  
print(r.read())
r.close()'''
'''s=open("demo.txt",mode="r+")
print(s.read())
s.write("r+ mode")
s.close()'''
'''s=open("demo.txt",mode="w+")
s.write(" w+ mode")
s.seek(0)
print(s.read())
s.close()'''