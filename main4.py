with open('Codingal.txt') as fp:
    data1 = fp.read()

with open('sample.txt') as fp:
    data2 = fp.read()

#merging two files
data1 += "\n"
data1+= data2
print("Merging two files....")
with open ('MergedFile.txt',"w") as fp:
    fp.write(data1)