from prettytable import PrettyTable
import json
from termcolor import colored
import datetime
import datetime


def main():
    ascii_art = """
███╗   ███╗██╗   ██╗███╗   ███╗██████╗  █████╗ ██╗    ███╗   ███╗██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗██╗███████╗███████╗
████╗ ████║██║   ██║████╗ ████║██╔══██╗██╔══██╗██║    ████╗ ████║██║   ██║████╗  ██║██╔════╝██║  ██║██║██╔════╝██╔════╝
██╔████╔██║██║   ██║██╔████╔██║██████╔╝███████║██║    ██╔████╔██║██║   ██║██╔██╗ ██║██║     ███████║██║█████╗  ███████╗
██║╚██╔╝██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══██║██║    ██║╚██╔╝██║██║   ██║██║╚██╗██║██║     ██╔══██║██║██╔══╝  ╚════██║
██║ ╚═╝ ██║╚██████╔╝██║ ╚═╝ ██║██████╔╝██║  ██║██║    ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║╚██████╗██║  ██║██║███████╗███████║
╚═╝     ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
                                                                                                                       
                                                                    
    """
    print(ascii_art)


main()

 
menu_options = [
    "Menu List",
    "Add A Snack",
    "Delete A Snack",
    "Update Availability of a Snack",
    "Update the Price of a Snack",
    "Record a Sale",
    "Bulk update of Snack by Category",
    "Bulk Removal of Snack by Category",
    "Sell Record"
]


styles = [
    {"color": "green", "attrs": ["bold"]},
    {"color": "cyan", "attrs": ["bold"]},
    {"color": "red", "attrs": ["bold"]},
    {"color": "yellow", "attrs": ["bold"]},
    {"color": "magenta", "attrs": ["bold"]},
    {"color": "blue", "attrs": ["bold"]},
    {"color": "white", "attrs": ["bold"]},
    {"color": "red", "attrs": ["bold"]},
    {"color": "cyan", "attrs": ["bold"]}
]

add_all = ""

for i, option in enumerate(menu_options):
    style = styles[i]
    formatted_option = colored(f"{i + 1}.   {option}", **style)
    add_all =  add_all + formatted_option + "\n"
  


current_date = datetime.date.today().strftime("%Y-%m-%d")
current_time = datetime.datetime.now().time().strftime("%H:%M:%S")



# with open("Sellrecord.json", "w") as json_file:
#     json.dump([{"name":"shuhdanshu"}], json_file)



with open("snacks.json", "r") as json_file:
    existing_snacks = json.load(json_file)

with open("Sellrecord.json", "r") as json_file:
    sell_data = json.load(json_file)


table = PrettyTable(["ID", "Name", "Price", "Availability"])
saletable= PrettyTable(["ID", "Name", "Total Sell", "Date of Sell","Time of Sell"])

for item in existing_snacks:
    table.add_row([item["id"], item["name"], item["price"], item["availability"]])
    
for item in sell_data:
    saletable.add_row([item["id"], item["name"], item["total sale"], item["date"], item["time"]])


admin = "admin"
canteen_staff = "staff"
cashier = "cashier"

role = input("Enter Your role(admin, cashier, staff): ")

if role == "admin":
    password = input("Enter password:")
    if password == "1234":
        while True:
            print(add_all)
            user_input = input("Select Your Option: ")

            if user_input == "2":
                while True:
                    snack_id = input("Enter Snack ID: ")
                    if snack_id.isdigit():
                        snack_id = int(snack_id)
                        id_present = any(int(item["id"]) == snack_id for item in existing_snacks)
                        if id_present:
                            print(f"ID {snack_id} is already present in the list.")
                        else:
                            break
                    else:
                        print("Invalid input. Please enter a valid snack ID (numeric).")

                snack_name = input("Enter Snack Name: ")

                while True:
                    snack_price = input("Enter Snack Price: ")
                    if snack_price.isdigit():
                        snack_price = int(snack_price)
                        break
                    else:
                        print("Invalid input. Please enter a valid number for the snack price.")

                snack_availability = input("Enter Snack Availability: ")

                new_snack = {
                    "id": snack_id,
                    "name": snack_name,
                    "price": snack_price,
                    "availability": snack_availability
                }

                existing_snacks.append(new_snack)

                with open("snacks.json", "w") as json_file:
                    json.dump(existing_snacks, json_file)

                table.add_row([new_snack["id"], new_snack["name"], int(new_snack["price"]), new_snack["availability"]])
                print("\n" + str(table))

            if user_input == "3":
                delete_id = input("Enter ID of Snack to Delete: ")
                for item in existing_snacks:
                    if item["id"] == delete_id:
                        existing_snacks.remove(item)
                        break

                with open("snacks.json", "w") as json_file:
                    json.dump(existing_snacks, json_file)
                    table = PrettyTable(["ID", "Name", "Price", "Availability"])
                    for item in existing_snacks:
                        table.add_row([item["id"], item["name"], item["price"], item["availability"]])
                    print("\n" + str(table))

            if user_input == "4":
                print("")
                print(table)
                availability_update = input("Enter id of Snack to update Availability: ")
                for item in existing_snacks:
                    if item["id"] == int(availability_update):
                        decide_avail =input("Is the Snack available(yes/no)")
                        item["availability"] = decide_avail
                        break

                with open("snacks.json", "w") as json_file:
                    json.dump(existing_snacks, json_file)
                    table = PrettyTable(["ID", "Name", "Price", "Availability"])
                    for item in existing_snacks:
                        table.add_row([item["id"], item["name"], item["price"], item["availability"]])
                    print("\n" + str(table))

            if user_input == "5":
                price_update_by_name = input("Enter name of Snack to update its Price: ")
                for item in existing_snacks:
                    if item["name"] == price_update_by_name:
                        updated_price = input(f"Enter the updated price for {item['name']}: ")
                        item["price"] = updated_price
                        print("")
                        print("Price Updated Successfully")
                        break

                with open("snacks.json", "w") as json_file:
                    json.dump(existing_snacks, json_file)
                    table = PrettyTable(["ID", "Name", "Price", "Availability"])
                    for item in existing_snacks:
                        table.add_row([item["id"], item["name"], item["price"], item["availability"]])
                    print("\n" + str(table))
                    
            if user_input == "6":
                print("")
                print(table)
                snack_sold_id=  input("Enter the snack ID sold: ")
                snack_qty = input("Enter quantity: ")
                snack_total =0
                snack_sold_name=""
                for item in existing_snacks:
                  
                    if int(snack_sold_id) == item["id"]:
                        snack_sold_name = item["name"]
                        snack_total = int(item["price"]) * int(snack_qty)
                        sell_data.append({"id":int(snack_sold_id), "name":item["name"], "total sale": snack_total, "date":current_date , "time": current_time})
                        break
                
                with open("sellrecord.json", "w") as json_file:
                    json.dump(sell_data, json_file)

                saletable.add_row([int(snack_sold_id), snack_sold_name, snack_total , current_date, current_time ])
                print("\n" + str(saletable))
              
            if user_input == "9":
                print(saletable)
            
            if user_input == "1":
                print("\n" + str(table) + "\n")
                print("")
                decision = input("Do you want to close the Canteen (yes/no): ")
                if decision.lower() == "yes":
                    break
    else:
        print("Wrong Password!!")
        
if role == "cashier":
    password = input("Enter password:")
    if password == "1234":
        while True:
            print("")
            print(add_all)
            user_input = input("Select Your Option: ")
            
            if user_input == "6":
                print("")
                print(table)
                snack_sold_id = input("Enter the snack ID sold: ")
                snack_qty = input("Enter quantity: ")
                snack_total = 0
                snack_sold_name = ""
                for item in existing_snacks:
                    if int(snack_sold_id) == item["id"]:
                        snack_sold_name = item["name"]
                        snack_total = int(item["price"]) * int(snack_qty)
                        sell_data.append({"id": int(snack_sold_id), "name": item["name"], "total sale": snack_total, "date": current_date, "time": current_time})
                        break

                with open("sellrecord.json", "w") as json_file:
                    json.dump(sell_data, json_file)

                saletable.add_row([int(snack_sold_id), snack_sold_name, snack_total, current_date, current_time])
                print("\n" + str(saletable))

            elif user_input == "9":
                print(saletable)

            else:
                print("You are not authorized!!")
                
            print("")
            decision = input("Do you want to close the Canteen (yes/no): ")
            if decision.lower() == "yes":
                break
    else:
        print("Wrong Password!!")

if role == "staff":
    password = input("Enter password:")
    if password == "1234":
        while True:
            print("")
            print(add_all)
            user_input = input("Select Your Option: ")
            
            if user_input == "1":
                print("\n" + str(table) + "\n")
      
            
            if user_input == "4":
                print("")
                print(table)
                availability_update = input("Enter id of Snack to update Availability: ")
                for item in existing_snacks:
                    if item["id"] == int(availability_update):
                        decide_avail =input("Is the Snack available(yes/no)")
                        item["availability"] = decide_avail
                        break

                with open("snacks.json", "w") as json_file:
                    json.dump(existing_snacks, json_file)
                    table = PrettyTable(["ID", "Name", "Price", "Availability"])
                    for item in existing_snacks:
                        table.add_row([item["id"], item["name"], item["price"], item["availability"]])
                    print("\n" + str(table))
            
            else:
                print("You are not authorized!!")
            
            print("")
            decision = input("Do you want to close the Canteen (yes/no): ")
            if decision.lower() == "yes":
                break  
    else:
        print("Wrong Password!!")       
                       
else:
    print("Wrong Choice!!")
            
                    
                    
    




            



