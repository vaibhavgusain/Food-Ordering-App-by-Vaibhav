class Food_Ordering_App:

        def __init__(self):
            self.food = {}
            self.food_id = len(self.food)+1
            self.user_details = {}
            self.ordered_item_list = []

    # Admin Fucntionalities

        def add_food_item(self):
            try:
                Name = input("Enter the food name : ")
                Quantity = float(input("Enter the quantity in vlaue :"))
                Price = float(input("Enter the price in numbers : "))
                Discount = float(input("Enter the discount in numbers : "))
                stock = float(input("Enter the available stock in kitchen : "))
                food_items = {"Name":Name,"Quantity":Quantity,"Price":Price,"Discount":Discount,"Stock":stock}
                self.food_id = len(self.food)+1
                self.food[self.food_id] = food_items
                print("****Food Item are added succcessfully*****")
            except Exception as T:
                print("<OPPS something worng>")

        def edit_food_item(self):
            try:
                N = int(input("Enter the food id you want to update : "))
                if x in self.food.keys():
                    print("1.Update Food Name\n2. Update Quantity\n3. Update Price\n4. Update Discount\n5. Update Stock\n")     
                    click = input("Enter : ")
                    if click == 1:
                        self.food[x]["Name"]= input("Update Food name : ")
                        print("**********Name Update********")
                    elif click == 2:
                        self.food[x]["Quantity"]= input("Update Quantity in number only : ")
                        print("**********Quantity Update********")

                    elif click == 3:
                        self.food[x]["Price"]= input("Update Price : ")
                        print("**********Price Update********")


                    elif click == 4:
                        self.food[x]["Discount"]= input("Update Discount in numbers : ")
                        print("**********Discount Update********")
                    elif click == 5:
                        self.food[x]["Stock"]= input("Update Stock in numbers : ")
                        print("**********Stock Update********")

                    else: 
                        print(f"***Click only 1 to 5** you click {click}")

                else:
                    print("<Invalid food id>")        
                        

            except Exception as T:
                print("<OPPS something worng>")   

        def view_food_items(self):
            print("List of food items: \n")
            if len(self.food)!= 0:
                for i in self.food:
                    print(f"Food Id :{i}")
                    for j in self.food[i]:
                        print(j,":",  self.food[i][j])
                    print()
            else :
                print("<Opps No food items in shop> ")


        def delete_food_item(self):
            try:
                print("Deleted items can't be restrored")
                print("Enter the Food Id ")
                click = int(input())
                if click in self.food.keys():
                    del self.food[click]      
                    print("<<Deleted Successfully>>")
                    # print("updated food list",self.food)
                else:
                    print("Incorrect ID ..")
            except Exception as T:
                print("<OPPS something worng>")    


  # User functionalities
        def user_register(self):
            try:
                while True:
                    user_name = input("Enter your Name : ")
                    Mobile_no = int(input("Enter your 10 digit number : "))
                    email = input("Enter your email id :")
                    password = input("Enter your password : ")
                    address = input("Enter your address : ")
                    self.user_details ={"user_name": user_name,"Mobile_no":Mobile_no,"email":email,"password":password,"address":address}
                    print("Registration successful now you can access this app ")

                    print("user Details :")
                    for i in self.user_details:
                        print(i,":",self.user_details[i])
                    break

            except Exception as T:
                print("<OPPS something worng>")   


        def user_login(self):
            try:
                while True:
                    email = input("Enter your Email ID : ")
                    password = input("Enter your password : ")
                    if len(self.user_details) !=0:
                        if email == self.user_details["email"] and password == self.user_details['password']:
                            print("Login Successfully")
                            while True:
                                print("1. Place New Order\n2. Check Order History\n3. Update Your Profile Details\n4. Exit")
                                choose = input("choose : ")
                                if choose == '1':
                                    self.place_order()
                                elif choose == '2':
                                    pass 
                                elif choose == '3':
                                    pass
                                elif choose == '4':
                                    break 
                                else:
                                    print("invalid Number ")    
                        else:
                            print("<Enter a valid Email or Password>")    
                    else:
                        print("There is no Account with this Email Id please registerd first")
                        break
                    break
            except Exception as T:
                print("<OPPS something worng>")


        def place_order(self):
            try:
                if len(self.food)!=0:
                    menu = []
                    for items in self.food:
                        menu.append([self.food[items]['Name'],self.food[items]['Quantity'],self.food[items]['Price']]) 
                    for i in menu:
                        print(i)
                    while True:
                        print("\nEnter 1 to Place the Order\nEnter 2 to Exit ")
                        x = input()
                        if x == '1':
                            print("Enter the food number ")
                            y  = input().split(",")
                            for i in y:
                                z = int(i)
                                if z <=len(menu):
                                    self.ordered_item_list.append(menu[z-1])
                                else:
                                    print(f"Don't match food item {z} ")
                            print("list of food item you select :\n")
                            for j in self.ordered_item_list:
                                print(j)
                        elif x =="2":
                            break
                        else:
                            print("Invalid number") 

                else:
                    print('No food items are available  at this time' )                               

            except Exception as T:
                print('<OPPS something worng>')

        def ordered_history(self):
            print("\nList of Previous ordered : ")
            for i in self.ordered_item_list:
                print(i)

        def update_details(self):
            try:
                while True:
                    print("Select Below Options to Update Your Profile Details\n")
                    print("1. Name\n2. Phone number\n3. Email ID\n4. Password\n5. Address\n6. Exit\n")
                    x=input()
                    if x=="1":
                        self.user_details["User Name"]=input("Enter your updated full name : ")
                        print("\n!! Detail Updated Successfully !!\n")
                    elif x=="2":
                        self.user_details["Phone No."]=int(input("Enter your updated 10 digit phone number : "))
                        print("\n!! Detail Updated Successfully !!\n")      
                    elif x=="3":
                        self.user_details["Email_ID"]=input("Enter your updated email id : ")
                        print("\n!! Detail Updated Successfully !!\n")
                        
                    elif x=="4":
                        self.user_details["Password"]=input("Enter your updated password : ")
                        print("\n!! Detail Updated Successfully !!\n")
                        
                    elif x=="5":
                        self.user_details["Address"]=input("Enter your updated address with area PIN code ")
                        print("\n!! Detail Updated Successfully !!\n")
                        
                    elif x=="6":
                        break
                    else:
                        print("\n!! Invalid Number Entered !!\n")
                              
                    if x in ["1","2","3",'4',"5"]:
                        for i in self.user_details:
                            print(i, ":",self.user_details[i])
                    else:
                        print("Enter correct Input\n")
            except Exception as T:
                print("<opps something went wrong>")


        # Main 

try:
        def Main():
            Object = Food_Ordering_App()
            print("Welcome to Food Ordering app")


            while True:
                print("1. Admin\n2. User\n3. Exit\n")
                x = input('choose any one : ')
                if x == '1':
                    while True:
                        print("1. Add New Food Items\n2. Edit Food Items\n3. View Food Items \n4. Delete Food Items\n5. Exit")
                        y = input()
                        if y == '1':
                            Object.add_food_item()
                        elif y == '2':
                            Object.edit_food_item()
                        elif y == '3':
                            Object.view_food_items()
                        elif y == '4':
                            Object.delete_food_item() 
                        elif y == '5':
                            break
                        else:
                            print("Invalid Number") 

                elif x == '2':
                    while True:
                        print("1. Register\n2. Login\n3. Exit\n")
                        y = input()
                        if  y =='1':
                            Object.user_register()
                        elif y == '2':
                            Object.user_login()
                        elif y == '3':
                            break
                        else:
                            print("Invalid choose at least one ")

                elif x == '3':
                    break
                else:
                    print("Invalid Number")  
except Exception as T:
    print('<Opps something went wrong>')

Main()


                        
                            
