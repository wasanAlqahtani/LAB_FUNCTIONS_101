#Lab loop bonus (wasan alqahtani)

#Create a function that takes 1 parameter of type int , then return the pattern in string
def invert_traingle (num:int)->str:
    ''' this function takes an integer number and then return string in descending order like invert triangle'''
    #create string varaible to store the pattern of each round 
    pattern:str = ""
    #create neastedloop 
    for firstnumber in range(num,0, -1):
        for secondnum in range (firstnumber, 0 ,-1):
            #add the number in the pattern
            pattern += str(secondnum) + " "
            #to add new line
        pattern+= "\n"
    #return the pattern
    return pattern

#then print the documentation.
print(invert_traingle.__doc__)

#call the function 
print(invert_traingle(5))