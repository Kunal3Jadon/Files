#1..WAP to read a file and no of characters in upper
with open('kunal.txt','r') as f:
    c=0
    for i in f.read():
        if i.isupper():
            c+=1
    print(c)
#2..WAP to check word is in file or not
with open('kunal.txt','r') as f:
    s=input()
    for i in f:
        l=i.split()
        if s in l:
            print("word in file")
            break
    else:
        print("word not found")
#3..WAP to count no of words in file
with open('kunal.txt','r') as f:
    c=0
    for i in f:
        l=i.split()
        c+=len(l)
    print("no of words in file",c)
#4..WAP to count no of characters in file
with open('kunal.txt','r') as f:
    c=0
    for i in f.read():
        c+=1
    print("no of characters",c)
#5..WAP to count no of lines in a file
with open('kunal.txt','r') as f:
    c=0
    for i in f:
        c+=1
    print("no of lines",c)
#6..WAP to copy odd no of lines to another file
f1=open('kunal.txt','r')
f2=open('kunal2.txt','a')
c=1
for i in f1:
    if c%2!=0:
       f2.write(i)
    c+=1
f1.close()
f2.close()
#7..WAP to copy odd no of words to another file
f1=open('kunal.txt','r')
f2=open('kunal2.txt','a')
for i in f1:
    l=i.split()
    for j in range(len(l)):
        if j%2==0:
            f2.write(l[j])
f1.close()
f2.close()
#8..WAP to count no of space,\n in file
with open('kunal.txt','r')as f:
    c=0
    c1=0
    for i in f.read():
        if i==' ':
            c+=1
        elif i=='\n':
            c1+=1
    print('no of characters',c)
    print('no of \n',c1)
#9..WAP to count no of vowels in file
l=['A','E','I','O','U','a','e','i','o','u']
with open('kunal.txt','r') as f:
    c=0
    for i in f.read():
        if i in l:
            c+=1
    print('no of vowels',c)
#10..WAP to append values in file until value is '@'
with open('kunal.txt','a') as f:
    while(1):
        s=input()
        if s!='@':
            f.write(s)
        else:
            break


