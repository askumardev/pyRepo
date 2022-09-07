# fo = open("foo.txt", "wb")
# print ("Name of the file: ", fo.name)
# print ("Closed or not : ", fo.closed)
# print ("Opening mode : ", fo.mode)
# fo.close()

fo = open("foo.txt", "r+")
str = fo.read(10)
print ("Read String is : ", str)

# Close opened file
fo.close()

# foo = open("foo.txt", "w")
# foo.write( "Python is a great language.\nYeah its great!!\n")

# # Close opend file
# foo.close()

#python3 pyConcepts/files/file_read.py