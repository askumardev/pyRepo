foo = open("foo.txt", "w")
foo.write( "Python is a great language.\nYes...\n")

# Close opend file
foo.close()

foo = open("foo.txt", "a")
foo.write( "adding new text")

# Close opend file
foo.close()

# python3 adv/files/file_write.py