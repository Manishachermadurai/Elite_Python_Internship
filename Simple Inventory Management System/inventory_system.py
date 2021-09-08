#importing library for printing time
import datetime
import json

#Starting
print("Welcome to Speed Shopping!!!")
#creating a system for soap sales
print("Welcome to Soap section")


#acessing the before_record file for the product details
fd=open("before_record.json","r")
t=fd.read()
products_details=json.loads(t)
fd.close()

#brand names and id of soaps
print("Thanks for coming..!")
print()
print("*****Soap Brand Names we have*****")
print()
for i in products_details.keys():
    print(products_details[i]["Name"])

#List to store the items purchased
cart={}
list_of_items=[]
sales={}
list_of_sales=[]
#asking
def menu():
    print()
    print("A-Add an item")
    print("P-Purchase")
    print("C-Checkout")
    print("S-Show all parts purchased")
    print("Q-Quit")
    print("H-help to See all commands again")
    print()

while True:
    menu()
    c= input("What would you like to do? ") 
    if(c=="q" or c=="Q"):#quit
        break
    if(c=="h" or c=="H"):#help
        menu()
    if(c=="P" or c=="p"):#purchase
        print("Are you interested to place your orders?(Y/N)")
        yes_or_no=str(input())
        if(yes_or_no=="Y" or yes_or_no=="y"):
            for i in products_details.keys():
                print(i,products_details[i]["Name"])
            print()
            print("Which brand would you like to buy?\nKindly enter the product id mentioned above:")
            prod_id=str(input())
            print("How many {} soaps you want to buy?/n".format(products_details[prod_id]["Name"]))
            quan=int(input())
            if(int(products_details[prod_id]["Stock"])>=quan):
                print("Your order went successful!!!")   
                amount=quan*int(products_details[prod_id]["Price"])
                products_details[prod_id]["Stock"]=str(int(products_details[prod_id]["Stock"])-quan)
                if prod_id not in list_of_items:
                    list_of_items.append(prod_id)
                    cart[prod_id]={}
                    cart[prod_id]["Name"]=products_details[prod_id]["Name"] 
                    cart[prod_id]["Quantity"]=quan
                    cart[prod_id]["Amount"]=amount
                else:
                    cart[prod_id]["Quantity"]+=quan
                    cart[prod_id]["Amount"]+=amount    
            else:
                print("Out of stock.Sorry we only have {} pieces left!!!".format(products_details[prod_id]["Stock"]))
        else:
            print("Thanks for coming!!!")

    if(c=="a" or c=="A"):#adding or updating products list
        print("Adding or Updating Product to Products List")
        print("Enter Product id:")
        new_prod_id=str(input())
        if(new_prod_id in products_details.keys()):
            print("The product already exists")
            print("Would you like to update the number of stocks?(Y/N)")
            a=str(input())
            if(a=="Y" or a=="y"):
                print("The stock of {} already exist is {} pieces".format(new_prod_id,products_details[new_prod_id]["Stock"]))
                print("Would you like to increase or decrease the number of items?")
                print("I-Increase the number of stock")
                print("D-Decrease the number of stock")
                b=str(input())
                if(b=='i' or b=="I"):
                    print("How many number of pieces you have to add?")
                    d=int(input())
                    products_details[new_prod_id]["Stock"]=str(int(products_details[new_prod_id]["Stock"])+d)
                elif(b=='d' or b=="D"):
                    print("How many number of pieces you have to decrease?")
                    d=int(input())
                    products_details[new_prod_id]["Stock"]=str(int(products_details[new_prod_id]["Stock"])-d)
                else:
                    print("Enter correct option.")
            else:
                print("Thanks for coming")
        else:
            print("The product you have entered is new product")
            print('Kindly enter the details ')
            products_details[new_prod_id]={}
            print("Enter the name of product:")
            products_details[new_prod_id]["Name"]=str(input())
            print("How much quantity? Example:1 piece")
            products_details[new_prod_id]["Quantity"]=str(input())
            print("Enter the price of the product:")
            products_details[new_prod_id]["Price"]=str(input())
            print("Enter the number of stocks left:")
            products_details[new_prod_id]["Stock"]=str(input())
            print("Added Successfully")
            print("The new product added was id:{} \t Name:{} \t Quantity:{} \t Price:{} \t Stock left:{}".format(new_prod_id,products_details[new_prod_id]["Name"],products_details[new_prod_id]["Quantity"],products_details[new_prod_id]["Price"],products_details[new_prod_id]["Stock"]))
        js_new=json.dumps(products_details)
        fd=open("after_record.json","w")
        fd.write(js_new)
        fd.close()
   
    if(c=="s" or c=="S"):#showing the products in your cart
        if(cart!={}):
            print()
            print("You have bought {} products".format(len(cart)))
            print("********************************************")
            print("Name \t Quantity \t Price")
            print("**********************************************")
            for i in cart:
                print(cart[i]["Name"],"\t",cart[i]["Quantity"],"\t ","$",cart[i]["Amount"])
        else:
            print()
            print("Sorry,Your cart is empty")
    

    if(c=="c" or c=="C"):#checkout
        print("Would you really like to checkout?(Y/N)")
        yes_or_no=str(input())
        if(yes_or_no=="Y" or yes_or_no=="y"):
            if(cart!={}):
                print("Enter your bill no:")
                bill_no=int(input())
                print("Enter your Name:")
                name=str(input())
                e=datetime.datetime.now()
                date=e.strftime("%d-%m-%y")
                time=e.strftime("%H:%M:%S")
                print()
                print("Welcome to Speed Shopping")
                print("*************************************")
                print("Bill No:\t",bill_no)
                print("Customer Name:\t",name)
                print("Date:\t",date)
                print("Time:\t",time)
                print("*************************************")
                total_amount=0
                for i in cart:
                    total_amount+=int(cart[i]["Amount"])
                print()
                print("Product Id \t Product Name \t Product Quantity \t Product Price")
                for i in cart:
                    print(i,"\t \t",cart[i]["Name"],"\t \t",cart[i]["Quantity"],"\t \t \t",cart[i]["Amount"])
                print("______________________________________________________________________")
                print("Total Price: \t \t \t \t \t {}".format(total_amount))
                print()
                print()
                print("***********************************************************************")
                print("\t \t Thank You for visiting us!!!")
                print("***********************************************************************")
                #updating sales
                if bill_no not in list_of_sales:
                    list_of_sales.append(bill_no)
                    sales[bill_no]={}
                    sales[bill_no]=cart
                    print("Thank you for coming!!!")
                    print("Please enter \"Q\" to quit!!!" )
                    cart={}
                    #updating sales file
                    js_sales=json.dumps(sales)
                    fc=open("sales.json","w")
                    fc.write(js_sales)
                    fc.close() 
                else:
                    print("The bill number you have entered already exists.Please enter correct number")
                    print("Please checkout by giving correct credentials")
                    menu()
                               
                # After checking out only the new record json 
                # file will be created
                js_new=json.dumps(products_details)
                fd=open("after_record.json","w")
                fd.write(js_new)
                fd.close()              
            else:
                print("Sorry,Your cart is empty.Please buy something first to checkout")
        elif(yes_or_no=="N" or yes_or_no=="n"):
            menu()
        else:
            print("Please enter correct option")

#After checking out only the after_record file will be updated
#after buying the product and completing billing process the after_record file is updated

#If we quit the process ends and begin with the before_record file
# so we can use this for one day and at the end of the day we can quit
# but for the next day we have to update the before_record file  

                














