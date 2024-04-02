# input the integers (A,B,C)
#.split() the integers into 3 
# cast string to integers 
# check for A-B-C 

# input the order 
# create a string for output 
# use a for loop to iterate the order
        # ifletter is A, add A integer +" "  to string
        # ifletter is B, add B integer +" "  to string
        # ifletter is C, add C integer +" "  to string
        # print the correct order to the 

 integers = input("A, B, C,")
 A, B, C = integers.split()
 A = int(A)
 B = int(B)
 C = int(C)
 if A > B:
    A, B = B, A 
 if B > C:
    B, C = C, B
 if a > b: 
 
A, B = B, A 