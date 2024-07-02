#Greet 
print("Welcome To Love Cafe")
print("-"*30)

#Define the menu of the restaurant

Menu={'Burger':59,
      'Pizza':149,
      'Cold Coffee':49,
      'Kullad Pizza':199,
      'Pav Bhaji':179,
      'Dosa':99,
      'Paneer Tikka':139,
      'Adrak Tea':39,
      'Pasta':49,
      'Meggi':49,
      'Coca Cola':49,
      'Healthy Salad':99,
    
}
print(" ITEM            PRICE")
print("-"*30)
print(" Burger  :      Rs-59\n Pizza  :      Rs-149\n Cold Coffee :  Rs-49\n Kullad Pizza: Rs-199\n Pav Bhaji  :  Rs-179\n Dosa  :        Rs-99\n Paneer Tikka: Rs-139\n Adrak Tea :    Rs-39\n Pasta  :       Rs-49\n Meggi  :       Rs-49\n Coca Cola  :   Rs-49\n Healthy Salad: Rs-99")

order_total=0

item1=input("Enter the name of your item you want to order := ")
if item1 in Menu:
    order_total+= Menu[item1]
    print(f"Your item {item1} has been added to your order")
    
else:
    print(f"Ordered item {item1} are not available yet ")
    
another_order=input("Do you want to add another item? (yes/no): ")
if another_order == "Yes" or "yes":
    item2=input("What do you want to order:=")
    if item2 in Menu:
        order_total+= Menu[item2]
        print(f"Your item {item2} has been added to order ")
        
    else:
        print(f"Your item {item2} are not avaliable yet")
        
print("-"*10,"Bill Printing","-"*10)
print(input("Enter Your Name: "))
print(f"The Total Amount of {item1} and {item2} to pay  :{order_total}")
print(" -"*5,"Thank You for visting us "," -"*5)