from matplotlib.patches import Wedge
import numpy as np
import pandas as pd
import pickle 
import matplotlib.pyplot as plt

def portfolio(p):
    #Approaching Pickle Function(Opening Saved File)
    k= pickle.load(open(p,"rb"))
    
    print('''Hello User!!
Here's Your Portfolio''')
    print("\nCash in house: ",k[0])
    
    #Databases for pie chart
    Names_Graph=[]
    Amounts=[]
    Names_Graph.append("Cash In House")
    Amounts.append(int(k[0][1]))
    
    for i in k:
        
        if i[0]==2:
            Names_Graph.append("Money_in_Bank")
            #Defining Dictionaries
            dict_Bank = {
                "Bank_name" : [],
                "Account_Holder's_Name": [],
                "Account_type": [],
                "Amount(Rupee)" : []
                
            }
            sum_f=0
            for j in range(1,len(i)):
                dict_Bank["Bank_name"].append(i[j][0])
                dict_Bank["Account_Holder's_Name"].append(i[j][1])
                dict_Bank["Account_type"].append(i[j][2])
                dict_Bank["Amount(Rupee)"].append(int(i[j][3]))
                sum_f= sum_f + int(i[j][3])
                        
            print("\nBank Account Details\n")    
            print(pd.DataFrame(dict_Bank))
            
            Amounts.append(sum_f)
            
            
        if i[0]==4:
            Names_Graph.append("Crypto Currency ")
            dict_Crypto = {
                "Crypto_name" : [],
                "Units": [],
                "Price_per_unit": [],
                "Value(Indian Rupee)" : []
            }
            sum_f=0
            for j in range(1,len(i)):
                dict_Crypto["Crypto_name"].append(i[j][0])
                dict_Crypto["Units"].append(i[j][1])
                dict_Crypto["Price_per_unit"].append(i[j][2])
                dict_Crypto["Value(Indian Rupee)"].append(i[j][3])
                sum_f= sum_f +int(i[j][3])
                
            print("\nCrypto Currency details\n")    
            print(pd.DataFrame(dict_Crypto))
            Amounts.append(sum_f)
            
        if i[0]==3:
            Names_Graph.append("Stock Market Investments")
            dict_Stocks = {
                "Stock_name" : [],
                "Units": [],
                "Price_per_unit": [],
                "Value(Indian Rupee)" : []
            }
            sum_f=0
            for j in range(1,len(i)):
                dict_Stocks["Stock_name"].append(i[j][0])
                dict_Stocks["Units"].append(i[j][1])
                dict_Stocks["Price_per_unit"].append(i[j][2])
                dict_Stocks["Value(Indian Rupee)"].append(i[j][3])
                sum_f= sum_f + int(i[j][3])
            print("\nStocks Details\n")   
            print(pd.DataFrame(dict_Stocks))
            Amounts.append(sum_f)
            
            
        if i[0]==5:
            Names_Graph.append("Real estate Investments")
            dict_Real_Estate = {
                "Property_Type" : [],
                "Area(in Sq Ft.)": [],
                "Location": [],
                "Value(Indian Rupee)" : []
            }
            sum_f=0
            for j in range(1,len(i)):
                dict_Real_Estate["Property_Type"].append(i[j][0])
                dict_Real_Estate["Area(in Sq Ft.)"].append(i[j][1])
                dict_Real_Estate["Location"].append(i[j][2])
                dict_Real_Estate["Value(Indian Rupee)"].append(i[j][3])
                sum_f= sum_f + int(i[j][3])
            print("\nReal Estate Properties\n")   
            print(pd.DataFrame(dict_Real_Estate))
            Amounts.append(sum_f)
            
        if i[0]==6:
            Names_Graph.append("Precious Metals")
            dict_Metals = {
                "Metal_Name" : [],
                "Value": []
            }
            sum_f=0
            for j in range(1,len(i)):
                dict_Metals["Metal_Name"].append(i[j][0])
                dict_Metals["Value"].append(i[j][1])
                sum_f = sum_f + int(i[j][1])
                
            print("\nPrecious Metals Details\n")   
            print(pd.DataFrame(dict_Metals))
            Amounts.append(sum_f)
            
        if i[0]==7:
            Names_Graph.append("Financial Bonds")
            dict_Financial_Bonds = {
                "Company" : [],
                "Scheme_Name": [],
                "Tenure": [],
                "Amount_Invested(Indian Rupee)" : []
            }
            sum_f=0
            for j in range(1,len(i)):
                dict_Financial_Bonds["Company"].append(i[j][0])
                dict_Financial_Bonds["Scheme_Name"].append(i[j][1])
                dict_Financial_Bonds["Tenure"].append(i[j][2])
                dict_Financial_Bonds["Amount_Invested(Indian Rupee)"].append(i[j][3])
                sum_f =sum_f + int(i[j][3])
            print("\nFinancial Bonds details\n")   
            print(pd.DataFrame(dict_Financial_Bonds))
            Amounts.append(sum_f)
            
        if i[0]==8:
            Names_Graph.append("Misellenous Assests")
            dict_Misellaneous = {
                "Type/Name" : [],
                "Units": [],
                "Total_VAlue(Indian Rupee)": []
            }
            sum_f = 0
            for j in range(1,len(i)):
                dict_Misellaneous["Type/Name"].append(i[j][0])
                dict_Misellaneous["Units"].append(i[j][1])
                dict_Misellaneous["Total_VAlue(Indian Rupee)"].append(i[j][2])
                sum_f = sum_f + int(i[j][2])
                
            print("\nMisellaneous Assests\nS")   
            print(pd.DataFrame(dict_Misellaneous))
            Amounts.append(sum_f)
            
    #Plotting Pie Chart For Better Vsualization
    
    #Creating Explode
    Explode_data= (0.1, 0.2, 0.05, 0.25, 0.75, 0.35, 0.225, 0.01)
    
    #Creating Colors list
    Color= ("orange", "blue", "red", "green", "yellow", "brown", "Purple", "beige")
    
    #Wedge Propeties
    wp = {'linewidth' : 1 , 'edgecolor' : "cyan"}
    
    def func(pct, allvalues):
        absolute = int(pct/100.* np.sum(allvalues))
        return "{:.1f}%\n({:d} g)".format(pct, absolute) 
    
    #Creating Plot
    fig, ax = plt.subplots(figsize = (10,7))
    wedges, texts, autotexts = ax.pie(Amounts,
                                      autopct= lambda pct: func(pct, Amounts),
                                      explode= Explode_data,
                                      labels= Names_Graph,
                                      shadow= True,
                                      colors= Color,
                                      startangle= 90,
                                      wedgeprops= wp,
                                      textprops= dict(color = "magenta")
                                      )
    
    #Plotting
    ax.set_title("Portfolio Pie Chart")
    
    #show plot
    plt.show()
    
    
            
            
        

  
            

                
       
