# We create a class called Shoe.

class Shoe:

    # constructor with the following methods, self, country, code, product, cost, quantity.

    def __init__(self, country, code, product, cost, quantity):

        # attributes to set self to country,code,product,cost,quantity.

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    #Method to Return self.cost.

    def get_cost(self):
        return self.cost

    # Method to return with .format the self.country,code,product,cost,quantity.

    def file_updated(self):
        return f'''{self.country},{self.code},{self.product},{self.cost},{self.quantity}'''

    # Method to return self.quantity.

    def get_quantity(self):
        return self.quantity

    #To string method Then return in our parameters country,code,product,cost,quantity.

    def __str__(self):
        return (f'''\nCountry:{self.country}
Shoe Code: {self.code}
Shoe Name: {self.product}
Shoe Cost: {self.cost}
Quantity: {self.quantity}\n''')

# Below creates shoe list

shoe_list = []

# Function called read_shoes_data as inventory.txt.

def read_shoes_data():

    try:

        with open('inventory.txt', 'r') as shoe_list_inventory:
            shoe_list_inside_file = shoe_list_inventory.readlines()
        
        # Calculate using len paramater (shoe_inside_file).
        
        for line in range(1, len(shoe_list_inside_file)):

                #create the country, code, product, cost and quntity, stripping and splitting into list
                country, code, product, cost, quantity = shoe_list_inside_file[line].strip('\n').split(',')

                # We create an object named shoes. 
                # We call the shoe class.
                # And pass in country,code,product,cost as a float and quantity as an integer
                # Then we append shoes to our global list shoe_list.

                shoes = Shoe(country,code,product,float(cost),int(quantity))
                shoe_list.append(shoes)
    
    except FileNotFoundError:
        print('inventory file not found. Please check file name correctly')
      

read_shoes_data()
   
# Method to capture_shoes and append to list

def capture_shoes(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity):
    shoes_captured = Shoe(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity)
    shoe_list.append(shoes_captured)

#Method to update list

def update():

    #create a variabe obj_data to take in shoe_list

    obj_data = f'Country,Code,Product,Cost,Quantity'

    # For loop to iterate shoe_list
    
    for shoe in shoe_list:
        obj_data += '\n' + shoe.file_updated()

    # opens text file and writes to it

    with open('inventory.txt', 'w') as shoe_list_inventory:
        shoe_list_inventory.write(obj_data)  

# Function view_all to print out entire shoe_list


def view_all():
    print(*shoe_list)

# Function for restock

def re_stock():

    #create a shoe_list qty(qunatity) and shoe_index counter

    qty = shoe_list[0].quantity
    shoe_index = 0

    # For loop to enumerate and iterate list

    for i, s in enumerate(shoe_list):
        if s.get_quantity() < qty:
          qty = s.quantity
          shoe_index = i

    # Return shoe index

    return shoe_index
  

    
# Function and method for searching shoe via SKU code

def search_shoe(s_code):
   
   # For loop to find code in list, if found returns shoe, if not error message displayed

    for shoe_code in shoe_list:
        if shoe_code.code == s_code:
            return shoe_code 
    
    return f'The shoe code {s_code} is not found\n'
    

# Method value_per_item

def value_per_item():

    # For loop to iterate through Shoe_list, value determined by cost times qunitty


    for s in shoe_list:
        value = s.cost * s.quantity
        print(f'{s}Value: {value}\n')


# Method for highest_qty shoe index intitalised to zero and variable max quantity, if highest quantity shoe is for sale

def highest_qty():
    shoe_index = 0
    max_quantity = shoe_list[shoe_index].get_quantity()

    for s, shoe in enumerate(shoe_list):
        if shoe.get_quantity() > max_quantity:
            max_quantity = shoe.get_quantity()
            shoe_index = s

    # Print sale and list the shoe which has the highest quantity

    print(f'This shoe is on sale, buy now to avoid dissapointment {shoe_list[shoe_index]}\n')


# Logic below

user_choice = ''' '''

# Using a while loop

while user_choice != 'end stock taking':
    user_choice = input('''\nWelcome to the inventory management system, please select below.
    capture = Will add new data about a shoe to management system
    view = list all shoes in the inventory
    restock = will find the shoe with lowest quantity and you can restock
    find shoe = Search for a shoe with an SKU code. Please type SKU8585 for example
    value = calculate the total value for each item
    sale = shoe with highest quantity, which is on sale \n''').lower()

    # If user choice equals capture, variables below taken into account and shoe added to inventory.txt

    if user_choice == 'capture':

        shoe_country = input('Please enter the country of the shoes ')
        shoe_code = input('Please enter the shoe code ')
        shoe_name = input('Please enter product name ')
        shoe_cost = float(input('Please enter the cost of the shoe ')) 
        shoe_quantity = int(input('Please enter the quantity of the shoes '))
        capture_shoes(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity )

    # if user enters view, view_all list printed

    elif user_choice == 'view':
        view_all()

    # elif user enters restock append to shoe_index variable

    elif user_choice == 'restock':
        shoe_index = re_stock()

    # We print the shoe with the lowest quantiy and ask if wants to restock

        print(f' This shoe has the lowest quantity {shoe_list[shoe_index]} ')
        restock_choice = input('''Please advise if you want to restock
Please choose:
Yes - to enable restock
No -  to exit restock \n''')
        

    #If yes, ask user to enter quantity number to resotk

        if restock_choice == 'yes':
            shoe_list[shoe_index].quantity = int(input('Please enter new quantity number: \n'))
    
    # If 'no quantity wil remain the same.
        if restock_choice == 'no':
            print('Quantity will remain the same\n')

        # use methods update() and re_stock()

        update()
        re_stock()
       
        
    # if the 'find shoe' is entered.
    # We create a variable called s_code which is our parameter.
    # Then we print(the shearch_shoe method and pass (s_code)).

    elif user_choice == 'find shoe':
        s_code = input('Please enter the shoe code you looking for: ')
        
        print(f'{search_shoe(s_code)}')
        
    # if the user enters 'value'
    # We call the value function. 

    elif user_choice == 'value':
        value_per_item()
    
    # We the user enters 'sale'.
    # Then we call the highest_qty() function.

    elif user_choice == 'sale':
        highest_qty()

    # if user enters 'end stock taking'
    # then we exist the programme.

    elif user_choice == 'end stock taking':
        print('Thank you')
    
    # if user enters any incorrect string.
    # The else statement will be executed.

    else:
        print('Please select correctly what you would like to do.')