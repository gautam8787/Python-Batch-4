# what is file handling ???

# file ???  to store the data permanently

a = 10 

# why ? 
# permanent data storage 
# data sharing is possible 
# reports generate 
# can also store these files into database 
# Log storage 

# file operations
# Open
# read 
# write 
# close 
 
# File Mode 
# r --> read mode   ---> read tha data which is inside a file  
# w --> write mode  ---> write any data inside a file  
# a --> append mode ---> with existing data if you want to add new data 
# x ---> create ---> new file creation 
# r+ , w+ ,a+
# rb , wb 

# types of files 
# Text files  --> txt files
# csv files  --> comma separated values  
# Json files  --> Json 
# Binary files ---> images , videos , mp3 , zip files 

'''
# open("filename" , "mode of operation")

try :
    f = open("demo.txt" ,"x")
    f.close()
except Exception as e:
    print(e)


d = open("demo.txt" , "r")
data =  d.read() # reads all the lines in the file 
print(data)
d.close()


d = open("demo.txt" , "w")    # write mode will override the old data 
d.write(" Tinnavaa raa ")
d.close()


d = open("memo.txt" , "w")    # write mode will override the old data and if file not exists then create a new file 
d.write(" data is changed")
d.close()


d = open("memo.txt" , "a")    # write mode will override the old data and if file not exists then create a new file 
d.write("\nnew data is added from the end the file.")
d.close()


with open("memo.txt" , "r") as f:
    print(f.tell())

    print(f.seek(17))
    print(f.read())       # read all the lines 

    print(f.tell())

    print(f.readline())   # reads only one line

    print(f.tell())

    print(f.readlines())  # returns all lines as a list  
    print(f.tell())

"""
data is changed

new data is added from the end the file.
new data is added from the end the file.
new data is added from the end the file.
new data is added from the end the file.


[]
PS C:

"""
with open("memo.txt" , "r") as f:
    for i in range(6):
        print(f.tell())
        print(f.readline())

    print(f.tell())



# write Multiple lines 

with open("demo.txt", "w") as f:
    f.write("this is python training\n")
    f.write("no one is singing song\nwhy this kolavari di\n")
    f.write("why this kolavari di")



# using loop 

with open("demo.txt", "r") as f:
    for i in f:
        print(i)

        

# input 

with open("demo.txt","a") as f:
    name = input("enter your name : ")
    f.write(" " + name + " ")



# copy data from one file to another file ??

a = open("demo.txt" , "r")
b = open("memo.txt" , "w")

data = a.read()
b.write(data)

a.close()
b.close()



a = open("demo.txt" , "a")


print(a.name)
print(a.closed)
print(a.flush)
a.write("\ndata is appended after flushing")

a.close()


a = open("demo.txt" , "r")
print(a.read().split())
a.close()


# CSV files : comma separated values 

# name , age , job , salary 
# sairam , 29 , trainer , 50000 

# csv methods 

# writer()
# writerow()
# writerows()
# reader()
# Dictwriter()
# Dictreader()


import csv

with open("data.csv","w" ,newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name " , "age " , "salary"])
    writer.writerow(["Rocky " , 29 , 50000])


import csv

data =[["sairam",26,40000],["sumit",22,30000],["chiru", 60,1000000]]

with open("data.csv","a") as f:
    writer = csv.writer(f)
    writer.writerows(data)

'''
import csv

with open("data.csv","r") as f:
    reader = csv.reader(f)
   
    for row in reader:
        print(row)
        
        