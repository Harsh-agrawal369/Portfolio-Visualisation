print("Hello User!!")
User_new = input("Are you a new user?(Yes/No): ")

#lst user 1) personal Information

#import lgn_lst as lg

def user_check(Username):
    lst_login=open("New_file_login.txt",'r')
    info= lst_login.read()
    info= info.split()

    if Username in info:
        lst_login.close()
        return True
        
    else:
        lst_login.close()
        return False
    
            
def pass_check(Username,password):
    lst_login= open("New_file_login.txt",'r')
    info= lst_login.read()
    info= info.split()
   
    if Username in info:
        index= info.index(Username)+1
        usr_pass = info[index]
        if usr_pass == password:
    
            return True
                        
        else:
            return False
                        
                        
def sign_up():
        Username= str(input("\nEnter a Unique Username: "))
        
        while user_check(Username)==True:
            print("Username alraedy Exists!")
            Username= str(input("\nEnter a Unique Username: "))
        
        password= input("\nEnter a password: ")
        lst_login=open("New_file_login.txt",'r')
        info= lst_login.read()
        lst_login.close()
        lst_login=open("New_file_login.txt",'w')
        info= info + " " + Username + " " + password
        lst_login.write(info)
        lst_login.close()
        lst_login=open("New_file_login.txt",'r')
        #print(lst_login.read())
        lst_login.close()
        return Username
        
def login():
    Username= str(input("\nEnter Your username: "))
    if user_check(Username)==True:
        password= input("\nEnter your Password: ")
        if pass_check(Username,password)==True:
            print("\nAccess Granted")
                
                
        elif pass_check(Username,password)==False:
            print("\nAccess Denied")
               
    elif user_check(Username)==False:
        print("\nUser does not Exist!")
        
    return Username
            

import pickle as ps
import os
os.system("cls")

def menu():
    print('''\nPress 1 for cash in house Details(if any)
press 2 for Money in Bank Accounts(if any)
Press 3 for stocks details(if any)
Press 4 for Crypto details(if any)
Press 5 for Real estate deatils(if any)
Press 6 for precious metal details(if any)
Press 7 for financial bond detais(if any)
press 8 for other miscellaneous assests(if any)
press 0 to terminate!''')


def data_entry():
    print("\nHello user! \nAfter completing your personal details let's head to list some assests.")
    menu()
    
    asset_option= int(input("\nEnter the option you first want to enter details: "))
    lst=[]
    lst_title=[]

    while 0<asset_option<=9 and asset_option!=0:
        
        if asset_option==1:
            lst_title.append("Cash_in_House")
            cash_in_house= int(input("\nEnter the total amount you have in house as cash: "))
        
            cash= []
            cash.append("Cash In House: ")
            cash.append(cash_in_house)
            lst.append(cash)
            
        
    
        elif asset_option==2:
            k=1
            Bank_details=[]
            Bank_details.append(asset_option)
            lst_title.append("Bank_details")
            while k!=0:
                Account_details=[]
                Bank_Name= str(input("\nEnter the name of the bank: "))
                Account_holder_name= str(input("Enter the account holder's name: "))
                Account_type= str(input("Enter the type of account(Current/Savings): "))
                Amount= int(input("Enter the Amount in the account: "))
                Account_details.append(Bank_Name)
                Account_details.append(Account_holder_name)
                Account_details.append(Account_type)
                Account_details.append(Amount)
                Bank_details.append(Account_details)
                k= int(input("\nEnter 0 to stop adding more Bank accounts: "))  
        
            lst.append(Bank_details)
       
        elif asset_option==3:
            k=1
            lst_title.append("Stocks details")
            stock_list= []
            stock_list.append(asset_option)
            while k !=0:
                lst_stock=[]
                Stock_name= input("\nEnter the stock name: ")
                units= int(input("Enter the number of units you have: "))
                price_unit= int(input("Enter the price of 1 unit: "))
                Total_value= units*price_unit    
                lst_stock.append(Stock_name)
                lst_stock.append(units)
                lst_stock.append(price_unit)       
                lst_stock.append(Total_value)   
                stock_list.append(lst_stock) 
                k= int(input("\nEnter 0 to stop adding more stocks: "))   
            
            lst.append(stock_list)
        
        elif asset_option==4:
            lst_title.append("Crypto Details")
            k=1
            Crypto_list= []
            Crypto_list.append(asset_option)
            while k !=0:
                lst_crypto=[]
                Crypto_name= input("\nEnter the Crypto Currency name: ")
                units= int(input("Enter the number of units you have: "))
                price_unit= int(input("Enter the price of 1 unit: "))
                Total_value= units*price_unit    
                lst_crypto.append(Crypto_name)
                lst_crypto.append(units)
                lst_crypto.append(price_unit)       
                lst_crypto.append(Total_value)   
                Crypto_list.append(lst_crypto) 
                k= int(input("\nEnter 0 to stop adding more Crypto's: "))   
            
            lst.append(Crypto_list)
        
        elif asset_option==5:
            lst_title.append("Real Estate")
            k=1
            Real_estate_list= []
            Real_estate_list.append(asset_option)
            while k !=0:
                lst_Property=[]
                property_type= input("\nEnter the Property Type: ")
                Carpet_Area= int(input("Enter the Carpet Area Of the Property(In sq ft): "))
                location= input("Enter the Location of Property(Locatily,City): ")
                Price= int(input("Enter the price of the Property: "))   
                lst_Property.append(property_type)
                lst_Property.append(Carpet_Area)
                lst_Property.append(location)       
                lst_Property.append(Price)   
                Real_estate_list.append(lst_Property) 
                k= int(input("\nEnter 0 to stop adding more Real Estate Properties: "))   
            
            lst.append(Real_estate_list)
 
        
        elif asset_option==6:
            lst_title.append("Metal Details")
            lst_metals=[]
            lst_metals.append(asset_option)
            k=1
            while k!=0:
                Metals=[]
                Metal_Name= input("\nEnter the name of the metal: ")
                Price_per_kg= int(input("Enter the price of metal(per grams): "))
                Quantity= int(input("Enter the quantity you have in grams: "))
                Total_value= Price_per_kg*Quantity
                Metals.append(Metal_Name)
                Metals.append(Quantity)
                Metals.append(Price_per_kg)
                Metals.append(Total_value)
                lst_metals.append(Metals)
                k= int(input("\nEnter 0 to stop adding more Metals details: "))
        
            lst.append(lst_metals)
        
        elif asset_option==7:
            lst_title.append("Financial Bonds")
            lst_financial_bonds=[]
            lst_financial_bonds.append(asset_option)
            k=1
            while k!=0:
                financial_bond=[]
                Name_of_Company= input("\nEnter the name of company: ")
                Name_of_scheme= input("Enter the name of the Scheme: ")
                Tenure= int(input("Enter the Tenure of the scheme in years: "))
                Amount_Invested= int(input("Enter the Amount Invested: "))
                #We are here considering the invested amount not the maturity amount because it is a safe amount 
                #to consider and we are calculating the current Portfolio so we don't have maturity Amount Now.
                financial_bond.append(Name_of_Company)
                financial_bond.append(Name_of_scheme)
                financial_bond.append(Tenure)
                financial_bond.append(Amount_Invested)
                lst_financial_bonds.append(financial_bond)
                k= int(input("\nEnter 0 to stop adding more financial bond details: "))
            
            lst.append(financial_bond)
        
        
        elif asset_option==8:
            lst_title.append("Misellaneous")
            lst_misellaneous=[]
            lst_misellaneous.append(asset_option)
            k=1
            while k!=0:
                Misellaneous=[]
                Name_Type = input("\nEnter the name\Type of the item: ")
                Quantity= input("Enter the units: ")
                Total_value= int(input("Enter the total value of the item: "))
                Misellaneous.append(Name_Type)
                Misellaneous.append(Quantity)
                Misellaneous.append(Total_value)
                lst_misellaneous.append(Misellaneous)
                k= int(input("\nEnter 0 to stop adding more Items details: "))
        
            lst.append(lst_misellaneous)
            
        elif asset_option==9:
            menu()
        
        
        asset_option= int(input("\nEnter the option to enter details \nPress 9 to print menu: "))
        
    
    return lst    


         
import portfolio_view as prt 
        
if User_new=="Yes":
    Username=sign_up()
    ps.dump(data_entry(), open(Username + "_mini", "wb"))
    k= Username + "_mini"
    
    prft_ask= input("Due You Want to Print Your Portfolio(Yes/NO): ")
    if prft_ask=="Yes":
        prt.portfolio(k)
    
elif User_new == "No":
    Username= login()
    k= Username + "_mini"
    
    prft_ask= input("\nDue You Want to Print Your Portfolio(Yes/NO): ")
    if prft_ask=="Yes":
        prt.portfolio(k)
    
    
else:
    print("Type Error!!")
    