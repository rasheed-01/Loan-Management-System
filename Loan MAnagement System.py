#Program : Loan Management system of Malaysia Bank
print("Welcome To Malaysia Bank")
print()

#MAIN MENU
def main_menu():
    back=True
    while back:
        print("Types Of Users: \n1.Admin \n2.New Customer\n3.Registered Customer\n4.Exit")
        user=int(input("Enter User Type Here:"))
        if user==1:
            admin()
        elif user==2:
            new_customer()
        elif user==3:
            registered_customer()
        elif user==4:
            quit()
        else:
            print("Inavlid Entry")
#admin Validation
def Authorize_staff() :
    username=input("Enter Username: ")
    password=input("Enter Passoword: ")
    with open("Validate.txt", "r") as f:
            for line in f:
              loginInfo = line.strip().split(",")
              if username==loginInfo[0] and password == loginInfo[1]:
                  return True
            return False
#Admin Validation             
def admin():
    correct=True
    while correct:
        if Authorize_staff():
            print()
            print("Access Granted!")
            print("Welcome Admin")
            print()
            admin_functions()
            break
        else:
            print("Access Denied")
            print("Please Try Again")
            print()
                
#Admin Options
def admin_functions():
    options1= True
    while options1:
       
        print("""  Admin Options:
       1.View the new customer’s registration request
       2.Give approval to new customer to access system with their Username and Password
       3.Provide unique LoanID, instalment Date and instalment Amount per month to registered customer
       4.View all the transactions of a specific customer
       5.View all the transactions of specific Loan type (EL/CL/HL/PL)
       6.View all the transactions of all the customers
       7.View all the transactionss of all types of Loans
       8.View All Approved Customer registeration requests
       9.View all Rejected Customer registeration requests
       10.Exit""")
        admin_func=int(input("Kindly Select an option:"))
        if admin_func==1:
            admin_func_1()
            
        elif admin_func==2:
            admin_func_2()

        elif admin_func==3:
            admin_func_3()

        elif admin_func==4:
            admin_func_4()

        elif admin_func==5:
            admin_func_5()

        elif admin_func==6:
            admin_func_6()                   

        elif admin_func==7:
            admin_func_7()

        elif admin_func==8:
            admin_func_8()
   
        elif admin_func==9:
           admin_func_9()
                                  
        elif admin_func==10:
            main_menu()

        else:
            print("Invalid Entry")
            print("Please Try Again")
            
        exit=input("Enter any key to go back to Admin Options:")
        print()

#New Requests
def admin_func_1():
    with open("Customers.txt", "r") as nfile:
        record=False
        for line in nfile:
            nfile_read=line.split("\t")
            if "Pending Approval"==nfile_read[14]:
                print(line)
                record=True
    if record==True:
        pass
    else:
        print("No new registeration requests pending for approval")

#Approval 
def admin_func_2():
    with open("Customers.txt", "r") as nfile:
                for line in nfile:
                    if "Pending Approval" in line:
                        print(line)
    approval=input("Enter Your Choice \n1. Approve all Together \n2.Reject all Together \n3.Approve or Reject one by one:")
    if approval=="1":
        fin = open("Customers.txt", "r")
        data1 = fin.read()
        data = data1.replace('Pending Approval', 'Approved')
        fin.close()
        fin = open("Customers.txt", "w")
        fin.write(data)
        fin.close()
        print("All Pending Requests are Approved Successfully")

    elif approval=="2":
        fin = open("Customers.txt", "r")
        data1 = fin.read()
        data = data1.replace('Pending Approval', 'Rejected')
        fin.close()
        fin = open("Customers.txt", "w")
        fin.write(data)
        fin.close()
        print("All Pending Requests are Rejected Successfully")

    elif approval=="3":
        with open("Customers.txt",'r') as f:
            for tine in f:
                if len(tine)>0:
                    tist=tine.split()
                    if tist[15]=="Pending":
                        print(tine)
                        tam=input("Enter 1 for APPROVE or 2 for REJECT")
                        with open("Customers.txt","r") as testfile, open("Customers.txt",'r') as testfile2 :
                            coolnewread=testfile2.readlines()
                            k=0
                            for j in coolnewread:
                                j2=j.split()
                                if "Pending"==j2[15]:
                                    for line in testfile:
                                        if tam=="1":
                                            testlist=line.split()
                                            thebiglist=line.replace("Pending Approval","Approved")
                                            thebiglist2=thebiglist
                                            if j2[2]==testlist[2]:
                                                coolnewread[k]=thebiglist2
                                            else:
                                                pass
                                        else:
                                            testlist=line.split()
                                            thebiglist=line.replace("Pending Approval","Rejected")
                                            thebiglist2=thebiglist
                                            if j2[2]==testlist[2]:
                                                coolnewread[k]=thebiglist2
                                            else:
                                                pass

                                else:
                                    pass
                                k=k+1
                            coolnewread2="".join(coolnewread)
                            testfile3=open("Customers.txt",'w')
                            testfile3.write(coolnewread2)
                            testfile3.close()   
            else:
                print("No more Approvals Pending")
                print()
                admin_functions()
    else:
        print("Invalid Entry")
#Loan ID Generator
def admin_func_3():
    with open("Customers.txt") as f:   
        with open("Loan Info.txt", "a") as f1:
            for line in f:
                loginInfo = line.strip().split("\t")
                if "Approved"==loginInfo[14] and "Loan ID Unassigned"==loginInfo[15] : 
                    loan_info=loginInfo
                    import random
                    loan_Id=random.randint(1000, 10000)
                    
                    name=loan_info[0]
                    loan_amt =loan_info[11]
                    loan_type=loan_info[10]
                    loan_month=loan_info[12]
                    username=loan_info[2]
                    password=loan_info[3]
                    years=int(loan_info[13])
                    months=years*12
                    
                    f1.write(name+"\t"+str(loan_Id)+"\t"+username+"\t"+password+"\t"+loan_type+"\t"+str(loan_amt)+"\t"+str(loan_month)+"\t"+str(months)+"\n")
                    fin = open("Customers.txt", "r")
                    data1 = fin.read()
                    data = data1.replace('Loan ID Unassigned', 'Loan ID Assigned')
                    fin.close()
                    fin = open("Customers.txt", "w")
                    fin.write(data)
                    fin.close()
            print("Loan Ids Assigned Successfully")
#Specific Trasanction Viewer
def admin_func_4():
    record=False
    loan_id=input("Enter Customers Unique Loan ID: ")
    with open ('transactions.txt','r') as file:
        for line in file:
            file_read=line.split("\t")
            if loan_id ==file_read[1]:
                liner=line.rstrip()
                print(liner)
                record=True

    if record==True:
        pass
    else:
        print("No Such Record Exists")
                
def admin_transac_view(loan):
    with open ('transactions.txt','r') as file:
        record=False
        for line in file:
            loan_Info=line.split("\t")
            if loan== loan_Info[2]:
                print(line)
                record=True
        if record==True:
            pass
        else:
            print("No Transactions Exists under the Selected Type of Loan")
            
#View transaction details of different types of loans        
def admin_func_5():
    options2= True
    while options2:
        print('''   View Transactions for different Types of Loans:
                  1.Education Loan
                  2.Home Loan
                  3.Personal Loan
                  4.Car Loan
                  5.Exit''')
                            
        loan_type=int(input("Enter Type Of Loan You Want"))
        with open ('transactions.txt','r') as file:
            if loan_type==1:
                loan="Education Loan"
                admin_transac_view(loan)
                
            elif loan_type==2:
                loan="Home Loan"
                admin_transac_view(loan)
            elif loan_type==3:
                loan="Personal Loan"
                admin_transac_view(loan)
                       
            elif loan_type==4:
                loan="Car Loan"
                admin_transac_view(loan)
                
            elif loan_type==5:
                admin_functions()
            else:
                print("Invalid Entry \nPlease Try Again")

            exit=input("Enter any key to go back:")
            print()
#View all types of loans Transactions
def admin_func_6():
    with open ('transactions.txt','r') as file:
        for line in file:
            liner=line.rstrip()
            print(liner)

#View All transactions
def admin_func_7():
    with open ('transactions.txt','r') as file:
        for line in file:
            liner=line.rstrip()
            print(liner)

#View Approved Customer Requests
def admin_func_8():
    with open("Customers.txt", "r") as nfile:
        record=False
        for line in nfile:
            nfile_read=line.split("\t")
            if "Approved"== nfile_read[14]:
                print(line)
                record=True

    if record==True:
        pass
    else:
        print("No Approved Customer Registeration Requests Available")

#View Rejected Customer Requests
def admin_func_9():
    with open("Customers.txt", "r") as nfile:
        record=False
        for line in nfile:
            nfile_read=line.split("\t")
            if "Rejected" ==nfile_read[14]:
                print(line)
                record=True
    if record==True:
        pass
    else:
        print("No Rejected Customer Registeration Requests Available")
    
#New Customer Options
def new_customer():
    options3= True
    while options3:
        print('''   New Customer Options:
                1. Check Loan details
                2. Use Loan Calculator
                3. Register
                4. Exit''')
        newc_func=int(input("Kindly Select an option: "))
        
        if newc_func==1:
            loan_details()

        elif newc_func==2:
            loan_calcs()

        elif newc_func==3:
            register()

        elif newc_func==4:
            main_menu()

        else :
            print("Invalid Entry \nPlease Try Again")
        exit=input("Enter any key to go back to New Customer Options")
        print()
        

#Loan Details
def loan_details():
    options4= True
    while options4:
        print('''Loan Detail Options:
                    1.Education Loan
                    2.Home Loan
                    3.Personal Loan
                    4.Car Loan
                    5.Exit''')
        loan_detail=int(input("Select an option to view more details: "))
            
        if loan_detail==1 :
            with open("Education Loan.txt", "r") as edul:
                edul_read=edul.read()
                print(edul_read)

        elif loan_detail==2 :
            with open("Home Loan.txt", "r") as homel:
                homel_read=homel.read()
                print(homel_read)

        elif loan_detail==3 :
            with open("Personal Loan.txt", "r") as pl:
                pl_read=pl.read()
                print(pl_read)

        elif loan_detail==4:
            with open("Car Loan.txt", "r") as cl:
                cl_read=cl.read()
                print(cl_read)

        elif loan_detail==5:
            new_customer()

        else:
            print ("Invalid Entry") 
        exit=input("Enter any key to go back to Loan detail Options")
        print()

#Loan Calculator Options
def loan_calcs():
    options5=True
    while options5:
        print ('''   Loan Calculator Options:
                  1.Education Loan
                  2.Home Loan
                  3.Personal Loan
                  4.Car Loan
                  5.Exit ''')
        loan_calc=int(input("Select the type of loan to calculate "))
        if loan_calc == 1:
            loan_calc_el()

        elif loan_calc==2:
            loan_calc_hl()

        elif loan_calc==3:
            loan_calc_pl()

        elif loan_calc==4:
            loan_calc_cl()

        elif loan_calc==5:
            new_customer()

        else:
            print ("Invalid Entry")
        print()
        exit=input("Enter any key to go back Loan Calculator Options")
        print()
 
        
#Education Loan Calculator
def loan_calc_el():
    wrongloan=True
    while wrongloan:
        loan_amt=float(input("Enter the loan amount (Max = RM200,000) :RM "))
        if (loan_amt > 200000):
            print("Sorry! We don't provide loan for more than RM200,000")
        else:
            break
    wrongyear=True
    while wrongyear:
         loan_years=int(input("How many years will you take to repay the loan? (Max=15yrs)"))
         if loan_years >15:
              print("Sorry! We don't provide loan for more than 15 years")
         else :
             break
        
             
    print("No of years:",loan_years,"yrs")

    if (0<loan_years<10):
        rate=7.6
        print ("Interest rate=",rate,"% p.a")
        period_rate=rate/12/100
        num_payments=loan_years*12
        payment_amt= period_rate * loan_amt/(1-(1+period_rate) **-num_payments)
        total_cost= num_payments * payment_amt - loan_amt
        total_loanamt=total_cost+loan_amt
        print("The Payment Amount is RM"+format(payment_amt,",.2f"),"per month")
        print("The Total Cost of Borrowing is RM"+format(total_cost,",.2f"))
        print("The Total Loan Amount with Interest is  RM"+format(total_loanamt,",.2f"))                                  
    elif (10<=loan_years<=15):
        rate=8.1
        print ("Interest rate=",rate,"% p.a")
        period_rate=rate/12/100
        num_payments=loan_years*12
        payment_amt= period_rate * loan_amt/(1-(1+period_rate) **-num_payments)
        total_cost= num_payments * payment_amt - loan_amt
        total_loanamt=total_cost+loan_amt
        print("The Payment Amount is RM"+format(payment_amt,",.2f"),"per month")
        print("The Total Cost of Borrowing is RM"+format(total_cost,",.2f"))
        print("The Total Loan Amount with Interest is : RM"+format(total_loanamt,",.2f"))
    

#Home Loan Calculator
def loan_calc_hl():
    income=int(input("Enter Your Annual Income:RM"))
    max_amt=income/0.2
    print("Maximum Amount that can be borrowed from the bank according to income = RM",max_amt)
    loan_amt=float(input("Enter the loan amount:RM "))
    loan_years=int(input("How many years will you take to repay the loan?(Max 40 years)"))
    print("No of years:",loan_years,"yrs")
    if loan_amt <=max_amt and loan_years <=40:
        rate=5
        print ("Interest rate=",rate,"% p.a")
        period_rate=rate/12/100
        num_payments=loan_years*12
        payment_amt= period_rate * loan_amt/(1-(1+period_rate) **-num_payments)
        total_cost= num_payments * payment_amt - loan_amt
        total_loanamt=total_cost+loan_amt
        print("The Payment Amount is RM"+format(payment_amt,",.2f"),"per month")
        print("The Total Cost of Borrowing is RM"+format(total_cost,",.2f"))
        print("The Total Loan Amount with interest is : RM"+format(total_loanamt,",.2f"))

    else:
        print("Sorry,the required loan amount is more than your maximum loan amount")
        print("OR")
        print("We dont provide loan for a tenure more than 40 years")
    
#Personal Loan Calculator
def loan_calc_pl():
    wrongloan=True
    while wrongloan:
        loan_amt=float(input("Enter the loan amount (Max = RM100,000) :RM "))
        if (loan_amt >= 100000):
            print("Sorry! We don't provide loan for more than RM100,000")
        else:
            break
    wrongyears=True
    while wrongyears:
        loan_years=int(input("How many years will you take to repay the loan?( Maximum=6years)" ))
        print("No of years:",loan_years,"yrs")
        if (loan_years>=6):
            print("Sorry! We don't provide loan for a tenure more than 6 years")
        else:
            break        
    if (loan_amt<20000 ):
        rate=8
        print ("Interest rate=",rate,"% p.a")
        period_rate=rate/12/100
        num_payments=loan_years*12
        payment_amt= period_rate * loan_amt/(1-(1+period_rate) **-num_payments)
        total_cost= num_payments * payment_amt - loan_amt
        total_loanamt=total_cost+loan_amt
        print("The Payment Amount is RM"+format(payment_amt,",.2f"),"per month")
        print("The Total Cost of Borrowing is RM"+format(total_cost,",.2f"))
        print("The Total Loan Amount with interest is : RM"+format(total_loanamt,",.2f"))                                       

    elif (20001<=loan_amt<50000):
        rate=7
        print ("Interest rate=",rate,"% p.a")
        period_rate=rate/12/100
        num_payments=loan_years*12
        payment_amt= period_rate * loan_amt/(1-(1+period_rate) **-num_payments)
        total_cost= num_payments * payment_amt - loan_amt
        total_loanamt=total_cost+loan_amt
        print("The Payment Amount is RM"+format(payment_amt,",.2f"),"per month")
        print("The Total Cost of Borrowing is RM"+format(total_cost,",.2f"))
        print("The Total Loan Amount with interest is : RM"+format(total_loanamt,",.2f")) 

    elif (50001<=loan_amt<=100000):
         rate=6.5
         print ("Interest rate=",rate,"% p.a")
         period_rate=rate/12/100
         num_payments=loan_years*12
         payment_amt= period_rate * loan_amt/(1-(1+period_rate) **-num_payments)
         total_cost= num_payments * payment_amt - loan_amt
         total_loanamt=total_cost+loan_amt
         print("The Payment Amount is RM"+format(payment_amt,",.2f"),"per month")
         print("The Total Cost of Borrowing is RM"+format(total_cost,",.2f"))   
         print("The Total Loan Amount with interest is : RM"+format(total_loanamt,",.2f"))   
        
#Car Loan Calculator  
def loan_calc_cl():
    wrongloan=True
    while wrongloan:
        loan_amt=float(input("Enter the amount of the car :RM "))
        if loan_amt>100001:
            print("Sorry we dont provide loan more than RM 100000")
        else:
            break
    wrongyears=True
    while wrongyears:
        loan_years=int(input("Tenure(Max 10 years):"))
        if loan_years>=10:
            print("Sorry! we dont provide loan for a tenure more than 10 years")
        else:
            break
    print("No of years:",loan_years,"yrs")
    rate=10
    print ("Interest rate=",rate,"% p.a")
    period_rate=rate/12/100
    num_payments=loan_years*12
    payment_amt= period_rate * loan_amt/(1-(1+period_rate) **-num_payments)
    total_cost= num_payments * payment_amt - loan_amt
    total_loanamt=total_cost+loan_amt
    print("The Payment Amount is RM"+format(payment_amt,",.2f"),"per month")
    print("The Total Cost of Borrowing is RM"+format(total_cost,",.2f"))
    print("The Total Loan Amount with interest is : RM"+format(total_loanamt,",.2f"))

#Register / Sign up portal
def register():
    newc_name=input("Enter Your Name Here: ")
    newc_age=int(input("Enter your age: "))
    newc_address=input("Enter Your Residential Address Here: ")
    newc_email=input("Enter Your Email ID Here: ")
    newc_contact=int(input("Enter Your Phone number Here:"))
    wronggender= True
    while wronggender:
        newc_gender= int(input("Enter Your Choice (1.Male 2.Female 3.Other) :"))
        if newc_gender==1:
            gender="Male"
            break
        elif newc_gender==2:
            gender="Female"
            break
        elif newc_gender==3:
            gender="Other"
            break
        else:
            print("Invalid Entry")
            print("Please try again")
            
        
    newc_dob=input("Enter Your Date Of Birth Here :")
    newc_income=float(input("Enter your annual income:RM"))

    wrong_type=True
    while wrong_type:
        print ('''          Types of Loans:
        1.Education Loan (MAX loan amt = RM 200,000;MAX tenure = 15yrs)
        2.Home Loan      (MAX loan amt = Depends on your salary;MAX tenure = 40yrs)
        3.Personal Loan  (MAX loan amt = RM 100,000 ; MAX tenure = 6 years 
        4.Car Loan       (MAX loan amt = RM 100,000: MAX tenure= 10 years''')


        newc_loantype=int(input("Select the type Of loan according to your requirements? "))


        if newc_loantype==1:
            loan="Education Loan"
            wrongloan=True
            while wrongloan:
                loan_amt=float(input("Enter the loan amount (Max = RM200,000) :RM "))
                if (loan_amt > 200000):
                    print("Sorry! We don't provide loan for more than RM200,000")
                else:
                    break
            wrongyear=True
            while wrongyear:
                loan_years=int(input("How many years will you take to repay the loan? (Max=15yrs):"))
                print("No of years:",loan_years,"yrs")

                if (0<loan_years<10):
                    rate=7.6
                    print ("Interest rate=",rate,"% p.a")
                    period_rate=rate/12/100
                    num_payments=loan_years*12
                    payment_amt= period_rate * loan_amt/(1-(1+period_rate) **-num_payments)
                    total_cost= num_payments * payment_amt - loan_amt
                    total_loanamt=total_cost+loan_amt
                    newc_loanamt=format(total_loanamt,".2f")
                    newc_loanmonth=format(payment_amt,".2f")
                    break
                elif (10<=loan_years<15):
                    rate=8.1
                    print ("Interest rate=",rate,"% p.a")
                    period_rate=rate/12/100
                    num_payments=loan_years*12
                    payment_amt= period_rate * loan_amt/(1-(1+period_rate) **-num_payments)
                    total_cost= num_payments * payment_amt - loan_amt
                    total_loanamt=total_cost+loan_amt
                    newc_loanamt=format(total_loanamt,".2f")
                    newc_loanmonth=format(payment_amt,".2f")
                    break
                else :
                    print("Sorry! We don't provide loan for more than 15 years")
                
            break


        elif newc_loantype==2:
            loan="Home Loan"
            max_amt=newc_income/0.2
            print("Maximum Amount that can be borrowed from the bank according to income = RM",max_amt)
            wrongamt=True
            while wrongamt:
                loan_amt=float(input("Enter the loan amount:RM "))
                loan_years=int(input("How many years will you take to repay the loan?(Max 40 years)"))
                print("No of years:",loan_years,"yrs")
                if loan_amt <=max_amt and loan_years <=40:
                    rate=5
                    print ("Interest rate=",rate,"% p.a")
                    period_rate=rate/12/100
                    num_payments=loan_years*12
                    payment_amt= period_rate * loan_amt/(1-(1+period_rate) **-num_payments)
                    total_cost= num_payments * payment_amt - loan_amt
                    total_loanamt=total_cost+loan_amt
                    newc_loanamt=format(total_loanamt,".2f")
                    newc_loanmonth=format(payment_amt,".2f")
                    break

                else:
                    print("Sorry,the required loan amount is more than your maximum loan amount")
                    print("OR")
                    print("We dont provide loan for a tenure more than 40 years")
                        
            break


        elif newc_loantype==3:
            loan="Personal Loan"
            wrong=True
            while wrong:
                loan_amt=float(input("Enter the loan amount (Max = RM100,000) :RM "))
                if (loan_amt > 100000):
                    print("Sorry! We don't provide loan for more than RM100,000")
                else:
                    break
            wrongyears=True
            while wrong:
                loan_years=int(input("How many years will you take to repay the loan?( Maximum=6years)" ))
                print("No of years:",loan_years,"yrs")
                if (loan_years<=6):
                    break
                else:
                    print("Sorry! We don't provide loan for a tenure more than 6 years")        
            if (loan_amt<20000 and 2<=loan_years<6):
                rate=8
                print ("Interest rate=",rate,"% p.a")
                period_rate=rate/12/100
                num_payments=loan_years*12
                payment_amt= period_rate * loan_amt/(1-(1+period_rate) **-num_payments)
                total_cost= num_payments * payment_amt - loan_amt
                total_loanamt=total_cost+loan_amt
                newc_loanamt=format(total_loanamt,".2f")
                newc_loanmonth=format(payment_amt,".2f")                                       

            elif (20001<=loan_amt<50000 and 2<=loan_years<6):
                rate=7
                print ("Interest rate=",rate,"% p.a")
                period_rate=rate/12/100
                num_payments=loan_years*12
                payment_amt= period_rate * loan_amt/(1-(1+period_rate) **-num_payments)
                total_cost= num_payments * payment_amt - loan_amt
                total_loanamt=total_cost+loan_amt
                newc_loanamt=format(total_loanamt,".2f")
                newc_loanmonth=format(payment_amt,".2f") 

            elif (50001<=loan_amt<100000 and 2<=loan_years<6):
                 rate=6.5
                 print ("Interest rate=",rate,"% p.a")
                 period_rate=rate/12/100
                 num_payments=loan_years*12
                 payment_amt= period_rate * loan_amt/(1-(1+period_rate) **-num_payments)
                 total_cost= num_payments * payment_amt - loan_amt
                 total_loanamt=total_cost+loan_amt
                 newc_loanamt=format(total_loanamt,".2f")
                 newc_loanmonth=format(payment_amt,".2f") 
            break


        elif newc_loantype==4:
            loan="Car Loan"
            wrongamt=True
            while wrongamt:
                loan_amt=float(input("Enter the loan amount you require (Max = RM100,000) :RM "))
                if (loan_amt > 100000):
                    print("Sorry! We don't provide loan for more than RM100,000")
                else:
                    break
            wrongyear=True
            while wrongyear:
                loan_years=int(input("Tenure(Max 10 years):"))
                print("No of years:",loan_years,"yrs")
                if 0<loan_years<=10:
                    rate=10
                    print ("Interest rate=",rate,"% p.a")
                    period_rate=rate/12/100
                    num_payments=loan_years*12
                    payment_amt= period_rate * loan_amt/(1-(1+period_rate) **-num_payments)
                    total_cost= num_payments * payment_amt - loan_amt
                    total_loanamt=total_cost+loan_amt
                    newc_loanamt=format(total_loanamt,".2f")
                    newc_loanmonth=format(payment_amt,".2f") 
                    break
                else:
                    print("Sorry! We dont provide car loan for a tenure more than 10 years")
            break


        else:
            print("Invalid Entry")
            print ("Please try again")

    userwrong=True
    while userwrong:
        username=input("Enter Your Username: ")
        with open("Customers.txt", "r") as f:
                record=False
                for line in f:
                    loginInfo = line.split("\t")
                    if username==loginInfo[2]:     
                        record=True
        if record==True:
                print("Username Exists")
                print("Please Try Again")
                
        else:
             username1=username
             break
                
            
                    
    wrongpass=True
    while wrongpass:
        newc_passw=input("Create a unique password: ")
        newc_rewrite=input("Rewrite Password :")
        if (newc_rewrite==newc_passw):
             print ("Password matches")
             password1=newc_passw
             break
        else:
             print("Password doesn't match")
             print("Please Try Again")
    
    print()
    print("Review Your Information before submitting")
    print()
    print("Name:",newc_name)
    print("Age:",newc_age,"years")
    print("Address:",newc_address)
    print("Email:",newc_email)
    print("Contact Number:",newc_contact)
    print("Gender:",gender)
    print("Date Of Birth",newc_dob)
    print("Your Annual Income:RM",newc_income)
    print("Loan Type:",loan)
    print("Loan Amount with Interest:RM",newc_loanamt)
    print("Monthly Instalment:RM",newc_loanmonth,"per month")
    print("Loan Tenure:",loan_years,"years")
    print("Username:",username1)
    print("Password",password1)
    print()
    confirm =input("Do you want to submit your details for approval? (yes/no)")
    if confirm =="yes":
        file=open("Customers.txt",'a')
        file.write(newc_name+"\t"+str(newc_age)+"\t"+username1+"\t"+password1+"\t"+newc_address+"\t"+newc_email+"\t"+str(newc_contact)+"\t"+gender+"\t"+newc_dob+"\t"+str(newc_income)+"\t"+loan+"\t"+str(newc_loanamt)+"\t"+str(newc_loanmonth)+"\t"+str(loan_years)+"\t"+"Pending Approval"+"\t"+"Loan ID Unassigned"+"\n")
        file.close()
        print("Thank You For Registering With Malaysia Bank")
        print("Pending Approval from Admin")
        print("Check the status of your Loan Registeration Request under Registered Customer from the main menu")
        print()
        
#Registered Customer
def registered_customer():
    username=input("Enter Your Username: ")
    password=input("Enter Your Password: ")
    reg_status(username,password)

#Registered Customer Options                
def registered_c_func(username,password):
    print("Welcome Back ",username)
    print()
    options5 =True
    while options5:
        print('''   Registered Customer Options:
                1. Check your Loan Details with LOAN Instalment date and LOAN ID
                2. Pay Loan Instalment
                3. View all my Transactions
                4. Check Your Loan Status
                5. Exit''')
        reg_func=int(input("Kindly Select an option:"))

        if (reg_func==1):
            loan_details_reg(username,password)

        elif (reg_func==2):
            loan_pay()

        elif (reg_func==3):
            view_transactions()

        elif (reg_func==4):
            loan_status(username,password)

        elif (reg_func==5):
            main_menu()
        else:
            print("Invalid Entry")
            print("Please Try Again")
        print()
        exit=input("Enter Any Key to go back to options")
        print()
#Customer Details
def loan_details_reg(username,password):
    with open("Customers.txt") as file:
            for line in file:
                loginInfo1= line.rstrip()
                loginInfo = line.rstrip().split("\t")
                if username==loginInfo[2] and "Approved"==loginInfo[14]:
                    
                    print(loginInfo1)
                    break
    with open("Loan Info.txt") as file:
        for line in file:
            loanInfo=line.rstrip().split("\t")
            if username==loanInfo[2]:
                print("Name:",loanInfo[0])
                print("Loan Type:",loanInfo[4])
                print("Your Unique loan ID is :",loanInfo[1])
                print("Please Refrain from disclosing your Loan ID ")
                break
             
#View Transactions
def view_transactions():
     with open("transactions.txt") as file:
         record=False
         loan_id=input("Enter your Unique Loan ID: ")
         for line in file:
             file_read=line.split("\t")
             if file_read[1]==loan_id:
                 print(line)
                 record=True
     if record==True:
        pass
     else:
         print("No such record exists")
         
#Loan Status ,Whenever customer proceeds with a transaction the values get updated
def loan_status(username,password):
    with open("Loan Info.txt",'r') as file:
        for line in file:
            liner=line.split("\t")
            if username==liner[2]:
                amt=float(liner[5])
                print("Name:",liner[0])
                print("Loan Type:",liner[4])
                print("Your Total Loan Amount with Interest:RM",format(amt,",.2f"))
                print("Total Number of Months Remaining to Pay:",liner[7],"months")
#Loan Payment System
def loan_pay():
    wrong1=True
    while wrong1:
        loan_id=input("Enter your Unique Loan ID: ")
        with open("Loan Info.txt") as f:
            with open("transactions.txt", "a") as f1:
                for line in f:
                    loginInfo=line.rstrip().split("\t")
                    if loan_id ==loginInfo[1]:
                        loan_inst=float(loginInfo[5])
                        loan_month=float(loginInfo[6])
                        months=int(loginInfo[7])
                        print("Your Total Instalment with Interest:RM",loan_inst)
                        print("Your Monthly Installment:RM",loan_month)
                        loan_type=loginInfo[4]
                        wrong2=True
                        while wrong2:
                            payment=float(input("Enter the exact monthly instalment amount:RM"))
                            if payment==loan_month:
                                break
                            else:
                                print("Amount does not matches the monthy instalment amount")
                        name=input("Enter your name (as in the Card):")
                        credit_card=input("Enter your Card Number:")
                        sec_code=input("Enter your 4 digit security code:")
                        expiry_date=input("Enter the expiry date of your card:")
                        import datetime
                        now = datetime.datetime.now()
                        date_time=(now.strftime("%d-%m-%Y %H:%M:%S"))

                        print()
                        print("Review Your Information Before making the transaction")
                        print()
                        print("Name:",name)
                        print("Loan ID:",loan_id)
                        print("Loan Type:",loan_type)
                        print("Transaction Amount:RM",payment)
                        print("Card Number:",credit_card)
                        confirm =input("Do you want to submit your details for approval? (yes/no)")
                        if confirm =="yes":
                            f1.write(name+"\t"+loan_id+"\t"+loan_type+"\t"+"Transaction Amount:RM"+str(payment)+"\t"+date_time+"\n")
                            new_amt=loan_inst-loan_month
                            new_month=months-1
                            loan_inst1=str(loan_inst)
                            loan_month2=str(months)
                            n_amt=str(new_amt)
                            n_m=str(new_month)

                            fin=open("Loan Info.txt",'r')
                            data1=fin.read()
                            data=data1.replace(loan_inst1,n_amt)
                            data2=data.replace(loan_month2,n_m)
                            fin.close()

                            
                            fin=open("Loan Info.txt","w")
                            fin.write(data2)
                            fin.close()

                            print()
                            print("Transaction Successful")

                        break
                else:
                    print("Invalid Loan ID")
                break
#Status of the Approval Requests           
def reg_status(username,password):
    with open("Customers.txt") as f:
        for line in f:
            loginInfo = line.strip().split("\t")
            if (username==loginInfo[2] and password == loginInfo[3] and "Pending Approval"==loginInfo[14]):
                print()
                print("Pending Approval from the Admin")
                print("Please Check Back Later")
                print()
                exit=input("Enter any key to go back options ")
                print()
                break

            elif (username==loginInfo[2] and password == loginInfo[3] and "Approved"==loginInfo[14]) :
                print()
                registered_c_func(username,password)
                break

            elif (username==loginInfo[2] and password == loginInfo[3] and "Rejected"==loginInfo[14]) :
                print()
                print("Sorry,Your Loan Registeration Request has been Rejected ")
                print("Please Try Again with Legitimate Information")
                print()
                exit=input("Enter any key to go back options ")
                print()
                break
    
            
        else:
            print("No Record Found")
            print("Please Try Again")
            print()
            

            
main_menu()
