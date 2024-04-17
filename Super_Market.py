while True:
    Name1=input("Enter Your Full Name := ")
    total=0

    while True:
         Quantity=int(input("Enter The Quantity Did You Purchase : "))
         Amount=int(input("Enter The Amount of The Product : "))
         total+=Quantity*Amount
    
         repet=input("Do you Want to continue (Yes/No) : ")
         if repet=="no" or repet=="Not" or repet=="No":
               break
      
    print("-"*50)
      
    print("****Bill Printing****")
    Name=print("Your name: ",Name1)
    Total_Amount=print("Your Total Amount Payable is : ",total)
    print("-"*50)
    
    Repet1=input("CONTINUE OR NOT (Yes/No)")
    if Repet1=="no" or repet== "Not" or repet== "No":
     break 
 
