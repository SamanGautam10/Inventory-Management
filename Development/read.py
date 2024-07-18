#Function to read the text file for the laptops
def laptop_textfile_read():
    '''Reading the laptop.txt file and appending them in a list'''
    laptop_id = 1
    laptops = {}
    try:
        file = open("laptop.txt","r")   #Reads the .txt file
        for lines in file:
            lines = lines.replace("\n","")
            laptop = lines.split(",")
            laptops.update({laptop_id: laptop})
            laptop_id = laptop_id + 1
        file.close()
    except:
        print("File not found")
    return laptops

#Function to display laptop in a arranged table
def laptop_table():
    '''This function prints the laptops from laptop.txt in a table'''
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("S.N. \t Laptop Name \t\tCompany Name \t Price \t      Quantity \t\t Processor \t\tGraphics Card\n")
    print("-------------------------------------------------------------------------------------------------------------------------")
    try:
        file = open("laptop.txt","r")
        serial_Number = 1
        for line in file:
            lines = line.replace(",","\t\t")
            print(serial_Number,"\t",lines)
            serial_Number = serial_Number + 1
            print("----------------------------------------------------------------------------------------------------------------------------")
        file.close()
    except:
        print("File not found")

