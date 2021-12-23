def Enquiry(lis1):
    if not lis1:
        return 1
    else:
        return 0
          
# Driver Code
lis1 = [2,4,5]
if Enquiry(lis1):
    print ("The list is Empty",Enquiry(lis1))
else:
    print ("The list is not empty",Enquiry(lis1))