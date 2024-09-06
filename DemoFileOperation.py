import os

'''f=open('MyData.txt', 'r')

#print(f.read())
print(f.readline())#poiner is at the first line of the  file
print(f.readline())#poiner is at the second line of the  file

f1=open('abc.txt', 'w')
f1.write("Something")
f1.write(" another thing")

#appending in that file
f2= open('abc.txt', 'a')
f2.write("\nAnother Line")

#copying the content of one file to another file
f3=open('abc.txt', 'r')
 
for data in f:
    print(data)
    f4=open('abc.txt', 'a')
    f4.write(data)'''

    # Renaming a file
os.rename('abc.txt', 'new_file.txt')

    # Deleting a file
os.remove('MyData.txt')