from operation import customer_billgenerate, update_invoice

#Function to update the laptop.txt file after user sells laptop to customer
def update_aftersell(laptops, user_laptop_id, user_quantity):
    '''This function updates the stock in laptop.txt file after selling laptop to customer'''
    laptops[user_laptop_id][3] = int(laptops[user_laptop_id][3]) - user_quantity #Decreasing the quantity in dictionary

    #Updating laptop.txt file to update the quantity
    file = open("laptop.txt","w")
    for line in laptops.values():
        file.write(str(line[0])+","+ str(line[1])+","+ str(line[2])+","+ str(line[3])+","+ str(line[4]) +","+ str(line[5])+"\n")
    file.close()

#This function is used to update quantity
def update_manufacture_stock(laptops,user_laptop_id,buy_quantity):
    '''This function is used to increase the stock in laptop.txt file after laptops are purchased from manufacture'''

    stock_available = int(laptops[user_laptop_id][3])       #stock that is available in laptop.txt file
    laptops[user_laptop_id][3] = stock_available + buy_quantity

    #Writes in the text file
    file = open("laptop.txt","w")
    for line in laptops.values():
        file.write(str(line[0])+","+ str(line[1])+","+ str(line[2])+","+ str(line[3])+","+ str(line[4]) +","+ str(line[5])+"\n")
    file.close()

#Function used to write bill in .txt file
def update_customerbill():
    '''This function writes the bill in the text file'''
    generate_bill = customer_billgenerate()

    try:
        file = open("customerbill.txt","w")
        file.write(generate_bill)
        print("\n")
        print("Bill printed successfully!!!")
        file.close()
    
    except:
        print("Error generating bill!!!")

#Function used to write invoice in .txt file
def update_manufactureinvoice():
    '''This function writes the invoice in the text file'''
    generate_invoice = update_invoice()

    try:
        file = open("invoice.txt","w")
        file.write(generate_invoice)
        print("\n")
        print("Invoice printed successfully")
        file.close()
    except:
        print("Error generating invoice")