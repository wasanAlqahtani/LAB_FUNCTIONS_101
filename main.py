#Lab Functions (Wasan Alqahtani)


#Create a function that takes 1 parameter of type int , then it prints out the result
def invert_traingle (num:int):
    ''' this function takes an integer number and then print the number in descending order like invert triangle'''
    #create nested loop
    for firstnumber in range(num,0, -1):
        for secondnum in range (firstnumber, 0 ,-1):
           #print the number 
           print(secondnum, end=" ")
           #print new line
        print(" ")

#then print the documentation.
print(invert_traingle.__doc__)

#call the function
invert_traingle(5)