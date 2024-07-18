import read
import write
import operation

#Giving option to the users to buy or sell the laptop
def user_option():
    '''This function helps for whole working of the system'''
    laptops = read.laptop_textfile_read()
    loop = True
    print("\t \t \t \t \t Silver Fox Electronics Shop\n")
    print("---------------------------------------------------------------------------------------------\n")
    print("\t \t \t \t \t Kamal Pokhari, | 9818181818\n")
    print("---------------------------------------------------------------------------------------------\n")
    print("\n")
    while loop==True:
        print("---------------------------------------------------------------------------------------------")
        print("\t\t\t\t\tPlease select the option below")
        print("---------------------------------------------------------------------------------------------")
        print("\n")
        print("Press 1 to sell items to the customers")
        print("Press 2 to buy items from the manufacturers")
        print("Press 3 to exit the system")
        print("\n")
        print("---------------------------------------------------------------------------------------------")
        try:
            system_input = int(input("Enter the option to continue:"))
            print("\n")

            if system_input == 1:
                # sell laptop to the customer
                read.laptop_table()
                user_laptop_id = operation.id_byuser(laptops)
                user_quantity = operation.quantity_byuser(laptops, user_laptop_id)
                write.update_aftersell(laptops, user_laptop_id, user_quantity)
                operation.user_purchased_items(laptops, user_laptop_id, user_quantity)
                while loop == True:
                    continue_buying = input("Do you want to continue buying laptops? (yes/no): ")
                    if continue_buying.lower() == "yes":
                        read.laptop_table()
                        user_laptop_id = operation.id_byuser(laptops)
                        user_quantity = operation.quantity_byuser(laptops, user_laptop_id)
                        write.update_aftersell(laptops, user_laptop_id, user_quantity)
                        operation.user_purchased_items(laptops, user_laptop_id, user_quantity)
                    elif continue_buying.lower() == "no":
                        loop = False
                        write.update_customerbill()
                        break
                    else:
                        print("Invalid Option! Please select 'yes' or 'no' only.")
            elif system_input == 2:
                # purchase laptop from the manufacturer
                read.laptop_table()
                user_laptop_id = operation.id_byuser(laptops)
                buy_quantity = operation.manufacture_quantity(laptops, user_laptop_id)
                write.update_manufacture_stock(laptops, user_laptop_id, buy_quantity)
                operation.manufacture_purchased_items(laptops, user_laptop_id, buy_quantity)
                while loop == True:
                    continue_buying = input("Do you want to buy more laptops? (yes/no): ")
                    if continue_buying.lower() == "yes":
                        read.laptop_table()
                        user_laptop_id = operation.id_byuser(laptops)
                        buy_quantity = operation.manufacture_quantity(laptops, user_laptop_id)
                        write.update_manufacture_stock(laptops, user_laptop_id, buy_quantity)
                        operation.manufacture_purchased_items(laptops, user_laptop_id, buy_quantity)
                    elif continue_buying.lower() == "no":
                        loop = False
                        write.update_manufactureinvoice()
                        break
                    else:
                        print("Invalid Option! Please select 'yes' or 'no' only.")
            elif system_input == 3:
                # exit from the system
                print("System exit")
                print("\n")
                loop = False
            else:
                print("Error 404! Invalid Option Selected")
        except ValueError:
            print("Invalid Option! Please select a valid option (1, 2, or 3) only.")

user_option()   #Calling function to give option to user
