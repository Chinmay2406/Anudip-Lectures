#file = open()
#data.write("hello world")
#content = file.read()
#print(content)
#file.close()
#data.close()


#file = open("c.txt","r")
#line1 = file.readline()
#print(line1)

#with open("c.txt","r") as file: # r for read 
   # print("reading line by line")
    #for line in file:
     #   print(line.strip()) 



#with open("c.txt","w") as file:
 #   file.write("first line. \n") 
  #  file.write("second line")

#with open("c.txt","a") as file:
 #   file.write("\n third line") #append

#with open("c.txt","r") as file:
 #   print(file.read())

with open("c.txt", "w") as file:
    file.write("hello everyone\n")  
    file.write("we are learning file\n")  
    file.write("using java\n")  
    file.write("i like programming in java\n")
with open("c.txt", "r") as file:
    data = file.read()
new_data = data.replace("java","Python")

with open("c.txt","w") as file:
    data = file.write(new_data) 

word = "programming"
with open("c.txt","r") as file:
    data = file.read()
    if data.find(word) != -1:
        print("found")
    else:
        print("Not Found")