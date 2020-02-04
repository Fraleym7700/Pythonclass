def main():
    print("Program calculates comission....")
    choice = 0
    while choice!=2:
        menu()
        choice = int(input("Enter your choice"))
        
        if choice == 1:
            sales, rate = get_input()
            ##can do both
            comm = calc_comm(rate, sales)
            print("comission is $",comm, sep="")
            print("comission is $",calc_comm(rate, sales), sep="")
        elif choice == 2:
            print("Bye...")
        else:
            print("Error.... Invalid entry!(Enter 1 or 2)")


def menu():
    """Function displays menu of options"""
    print("----MENU---------")
    print("1)Calculate Comission")
    print("2) Exit")
    print("---------------------")
   
        
def get_input():
    """fucntion collect sales and commison rate"""
    sales = float(input("Enter sales generated: "))
    comm_rate = float(input("Enter commission rate(0.10,0.15): "))
    
    return sales, comm_rate

def calc_comm(rate,sales):
    """Function calculates comission"""
    comm = rate * sales
    return comm
main()