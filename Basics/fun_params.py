def greet(str):
	print(str)

def printinfo( arg1, *vartuple ):
	"This prints a variable passed arguments"
	print ("Output is: ")
	print (arg1)

	for var in vartuple:
		print ("in loop", +var)
	return

greet("Hello")

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )

# python3 Basics/fun_params.py