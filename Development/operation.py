import datetime

#Function used to take id laptop from user
def id_byuser(laptops):
    '''This function takes laptop ID from customer which they want to buy'''
    loop = True
    while loop == True:
        try:
            user_laptop_id = int(input("Enter the ID of laptop:"))

            # Validating the ID given by user
            if user_laptop_id <= 0 or user_laptop_id > len(laptops):
                print("Invalid ID! Please re-enter the ID of laptop you want to sell.")
                continue
            else:
                return user_laptop_id

        except ValueError:
            print("Invalid Input!! Please enter a valid input to continue")

#Function to get quantity to sell laptops to the customer
def quantity_byuser(laptops,user_laptop_id):
    '''This function asks user for the quantity of laptop they want to buy'''
    loop = True
    #Loop initiates after validating the laptop ID given by user
    while loop == True:
        try:
            user_quantity = int(input("Enter the quantity of laptop:"))
            stock_available = int(laptops[user_laptop_id][3])       #storing the value of stock available in stock_available variable    

            if stock_available == 0:
                print("Sorry!! This laptop is out of stock!!!")
                choice = input("Enter Y to buy other laptop or enter any word to exit the system!!!")
                if choice.lower() == 'y':
                    return 0
                else:
                    print("Thank you for visiting")
                    exit()

            #Checking the stock available
            while user_quantity <= 0 :
                print("Quantity cannot be less than 1!!!")
                print("\n")
                user_quantity = int(input("Please re-enter the quantity of laptop you want to buy:"))

            while user_quantity > stock_available:
                print("Sorry!! That much stock is not available!!!")
                print("\n")
                user_quantity = int(input("Please re-enter the quantity of laptop you want to buy:"))

            return user_quantity
        
        except ValueError:
            print("Invalid input! Please enter a valid input") 

purchased_items = []
#Function used to get items purchased by user
def user_purchased_items(laptops,user_laptop_id,user_quantity):
    '''This function is to keep items purchased by user to do further iteration'''

    if user_quantity > 0:
        #Appending required elements in list for bill generation
        nameoflaptop = laptops[user_laptop_id][0]
        purchased_quantity = user_quantity
        unit_price = laptops[user_laptop_id][2].replace("$","")
        total_price = int(unit_price) * purchased_quantity

        purchased_items.append([nameoflaptop,purchased_quantity,unit_price,total_price])

    return purchased_items

#FUnction to get quantity of laptop to be purchased from manufacture
def manufacture_quantity(laptops,user_laptop_id):
    '''This function is used to get quantity to be purchased from manufacture'''
    loop = True
    while loop == True:
        try:
            buy_quantity = int(input("Enter the quantity you want to purchase from manufacture: "))
            if buy_quantity <= 0:
                print("Quantity cannot be less than 1!!")
                print("\n")
            else:
                return buy_quantity
        except ValueError:
            print("Invalid input!! Please enter a valid quantity to continue.")

manufacture_items = []
#Function used to get items purchased from manufacture
def manufacture_purchased_items(laptops,user_laptop_id,buy_quantity):
    '''This function is to keep items purchased from manufacture for furthur iteration'''

    #Appending required items in the list
    nameoflaptop = laptops[user_laptop_id][0]
    purchased_quantity = buy_quantity
    unit_price = laptops[user_laptop_id][2].replace("$","")
    total_price = int(unit_price) * purchased_quantity

    manufacture_items.append([nameoflaptop,purchased_quantity,unit_price,total_price])

    return manufacture_items

#Function to generate bills when customer buys laptop from shop
def customer_billgenerate():
    '''This function generated bills after customer purchases items from the shop'''
    print("\n")
    while True:
        nameofcustomer = input("Enter name of customer: ")
        if nameofcustomer.replace(" ", "").isalpha():       #checks if user gave any integer
            break
        else:
            print("How can a name have anything else from alphabets?")

    while True:
        numberofcustomer =  input("Enter number of customer: ")
        if numberofcustomer.isnumeric() and len(numberofcustomer) == 10:
            break
        else:
            print("Please enter a valid number.")
    
    while True:
        addressofcustomer = input("Enter the address of customer: ")
        #checking if user gave combination of alphabets and numeric value of only numerical value
        if (addressofcustomer.replace(" ","").isalnum() or addressofcustomer.isprintable()) and not addressofcustomer.isdigit(): 
            break
        else:
            print("Please enter valid address!!!!")

    #Asking user if they want their order to be delivered
    shipping = input("Do you want your items to be delivered to your location?(y/n): ")
    loop = True
    while loop == True:
        if shipping.lower() == "y":
            shipping_cost = 69
            break

        elif shipping.lower() == "n":
            shipping_cost = 0
            loop = False

        else:
            print("Please select y or n!")
            shipping = input("Do you want your items to be delivered to your location?(y/n): ")

    #Formatting date and time for the bill
    now = datetime.datetime.now()
    formatted_day = now.strftime("%Y-%m-%d")
    formatted_time = now.strftime("%H:%M:%S")

    bill = ""
    #Bill details
    bill += "\n"
    bill += "\t \t \t \t \t Silver Fox Electronics Shop\n"
    bill += "---------------------------------------------------------------------------------------------\n"
    bill += "\t \t \t \t \t Kamal Pokhari, | 9818181818\n"
    bill += "---------------------------------------------------------------------------------------------\n"
    bill += "\n"
    bill += "Date: {}\n".format(formatted_day)
    bill += "Time: {}\n".format(formatted_time)
    bill += "Name of Customer: {}\n".format(nameofcustomer)
    bill += "Address: {}\n".format(addressofcustomer)
    bill += "Phone No.: {}\n".format(numberofcustomer)
    bill += "\n"
    bill += "|==================================================|\n"
    bill += "| S.N. \t  Laptop Name \t  Qty \t  Rate \t   Amount  |\n"
    bill += "|==================================================|\n"

    serial_number = 1
    total_price = 0

    #Getting the elements from list of purchased item and formatting them
    for i in purchased_items:
        bill += f"|   {serial_number:<3}  {i[0]:<17}{i[1]:<6}{i[2]:<11}{i[3]:<8}|\n"
        bill += "|--------------------------------------------------|\n"
        serial_number += 1

        total = i[3]        #Unit price taken from the list
        total_price += total

    price_withoutshipping = total_price
    total_price = total_price + shipping_cost
    bill += " Without Shipping Cost: ${}\n".format(price_withoutshipping)
    bill += " Shipping Cost: ${}\n".format(shipping_cost)
    bill += " Grand Total: ${}\n".format(total_price)
    bill += " Thank you for purchasing\n"

    print(bill)
    return bill

#Function to generate an invoice
def update_invoice():
    '''This function generates invoice when laptops are purchased from manufatures'''
    
    #Date and time for invoice
    now = datetime.datetime.now()
    formatted_day = now.strftime("%Y-%m-%d")
    formatted_time = now.strftime("%H:%M:%S")

    invoice = ""

    serial_number = 1
    total_price = 0

    #Invoice details
    invoice += "\n"
    invoice += "\t \t \t \t \t Silver Fox Electronics Shop\n"
    invoice += "---------------------------------------------------------------------------------------------\n"
    invoice += "\t \t \t \t \t Kamal Pokhari, | 9818181818\n"
    invoice += "---------------------------------------------------------------------------------------------\n"
    invoice += "\n"
    invoice += "Date: {}\n".format(formatted_day)
    invoice += "Time: {}\n".format(formatted_time)
    invoice += "\n"
    invoice += "|==================================================|\n"
    invoice += "| S.N. \t  Laptop Name \t  Qty \t  Rate \t   Amount  |\n"
    invoice += "|==================================================|\n"

    #Formatting the items of list to form a table
    for i in manufacture_items:
        invoice += f"|   {serial_number:<3}  {i[0]:<17}{i[1]:<6}{i[2]:<11}{i[3]:<8}|\n"
        invoice += "|--------------------------------------------------|\n"
        serial_number += 1

        total = i[3]        #Unit price taken from the list
        total_price += total
    
    #Vat calculation
    vat = 0.13
    total_withoutvat = total_price
    vat_amount = total_withoutvat * vat
    total_withvat = total_withoutvat + vat_amount

    invoice += " Total without Vat: ${}\n".format(total_withoutvat)
    invoice += " Vat Amount : ${}\n".format(vat_amount)
    invoice += " Gross Total: ${}\n".format(total_withvat)

    print(invoice)
    return invoice