#write in file using with() function
with open('sample_doc.txt','w') as file:
    file.write(" Hi! My name is Zara and i am 16 yr old.")
    file.close()
#split file
with open('sample_doc.txt','r') as file:
    data=file.readlines()
    for line in data:
        word = line.split()
        print(word)
file.close()