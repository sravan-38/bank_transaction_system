import datetime
customer_name=[]
customer_pin=[]
customer_address=[]
pan_num=[]
aadhar_num=[]
min_balance=10000
name = []
while True:
    print('''
            WELCOME TO BHARAT BANK     
            1:OPEN A NEW ACCOUNT      
            2:DEPOSIT         
            3:WITHDRAW          
            4:BALANCE ENQUIRY         
            5:CLOSE BANK ACCOUNT     
            6:MODIFY YOUR ACCOUNT     
            7:SEE ACCOUNT HOLDERS LIST
            8:EXIT                   ''')
    options=int(input("choose from above options:"))
    if options==1:
        name=input("enter your name:")
        customer_name.append(name)
        address=input("enter your address:")
        customer_address.append(address)
        pnum=input("enter pan number:")
        pan_num.append(pnum)
        adnum=int(input("enter aadhar number:"))
        aadhar_num.append(adnum)
        pin=int(input("enter pin:"))
        customer_pin.append(pin)
        print("YOUR DETAILS ARE...")
        print("\nNAME=",name,
            "\nAADHAR NUMBER=",adnum,
            "\nPAN NUMBER=",pnum,
            "\nADDRESS=",address)
        print('''please confirm the details----
                    1:CONTINUE
                    2:NEED CHANGES''')
        option=int(input("choose from above....:"))
        if option==1:
            print("CONGRATS... ", name,"YOUR ACCOUNT HAS CREATED SUCCESSFULLY")

        elif option==2:
            
            print('''what do you want to change
            1:NAME
            2:ADDRESS
            3:AADHAR NUMBER
            4:PAN NUMBER
            5:EXIT
            ''')
            option_s=int(input("choose from above..:"))
            if option_s==1:
                name=input("enter your name:")
                customer_name.append(name)
                print("your name has successfully updated")
                print("AFTER MODIFYING YOUR DETAILS ARE..")
                print("\nNAME=",name,
                      "\nAADHAR NUMBER=",adnum,
                      "\nPAN NUMBER=",pnum,
                      "\nADDRESS=",address)
            elif option_s==2:
                address=input("enter your address:")
                customer_address.append(address)
                print("your address has successfully updated")
                print("AFTER MODIFYING YOUR DETAILS ARE..")
                print("\nNAME=",name,
                      "\nAADHAR NUMBER=",adnum,
                      "\nPAN NUMBER=",pnum,
                      "\nADDRESS=",address)
            elif option_s==3:
                adnum=int(input("enter aadhar number:"))
                aadhar_num.append(adnum)
                print("your addhar number has successfully updated")
                print("AFTER MODIFYING YOUR DETAILS ARE..")
                print("\nNAME=",name,
                      "\nAADHAR NUMBER=",adnum,
                      "\nPAN NUMBER=",pnum,
                      "\nADDRESS=",address)
            elif option_s==4:
                pnum=input("enter pan number:")
                pan_num.append(pnum)
                print("your pan number has successfully updated")
                print("AFTER MODIFYING YOUR DETAILS ARE..")
                print("\nNAME=",name,
                      "\nAADHAR NUMBER=",adnum,
                      "\nPAN NUMBER=",pnum,
                      "\nADDRESS=",address)
            elif option_s==5:
                print("exited..")
            else:
                print("check the options...")
    elif options==2:
        damount=int(input("enter deposit amount:"))
        min_balance=min_balance+damount
        print("DEPOSIT SUCESSFUL...")
        tim=datetime.datetime.now()
        print(tim.strftime("%c"))
        print(name," your current balance is=",min_balance)
    elif options==3:
        wamount=int(input("enter withdrawal amount:"))
        if wamount<min_balance:
            min_balance=min_balance-wamount
            print("WITHDRAWAL SUCCESS....")
            tim=datetime.datetime.now()
            print(tim.strftime("%c"))
            print(name," your current balance is=",min_balance)
        else:
            print("INSUFFICIENT BALANCE....")
    elif options==4:
        tim=datetime.datetime.now()
        print(tim.strftime("%c"))
        print("YOUR BALANCE IS:",min_balance)
    elif options==5:
        print("WHY YOU ARE CLOSING YOUR ACCOUNT:")
        print("\n1:NO SERVICE FROM BANK\n2:I CHANGED MY MIND\n3:MY PERSONAL")
        cacc=int(input("choose your choice:"))
        if cacc==1:
            print("SORRY FOR INCONVIENCE SIR/MADAM WE WILL TRY OUT BEST TO GIVE BEST BANKING EXPERINCE")
            cacc1=int(input("press 1 to close account\npress 2 to exit"))
            if cacc1==1:
                customer_name.remove(name)
                customer_address.remove(address)
                aadhar_num.remove(adnum)
                pan_num.remove(pnum)
                print(name," YOUR ACCOUNT HAS BEEN CLOSED SUCCESSFULLY THANK YOU")
            elif cacc1==2:
                print("THANK YOU WITH US",name)
                exit()
            else:
                exit()
        elif cacc==2:
            print("SORRY FOR INCONVIENCE SIR/MADAM WE WILL TRY OUT BEST TO GIVE BEST BANKING EXPERINCE")
            cacc1=int(input("press 1 to close account\npress 2 to exit"))
            if cacc1==1:
                customer_name.remove(name)
                customer_address.remove(address)
                aadhar_num.remove(adnum)
                pan_num.remove(pnum)
                
                print(name," YOUR ACCOUNT HAS BEEN CLOSED SUCCESSFULLY THANK YOU")
            elif cacc1==2:
                print("THANK YOU WITH US",name)
                exit()
            else:
                exit()
        elif cacc==3:
            print("SORRY FOR INCONVIENCE SIR/MADAM WE WILL TRY OUT BEST TO GIVE BEST BANKING EXPERINCE")
            cacc1=int(input("press 1 to close account\npress 2 to exit"))
            if cacc1==1:
                customer_name.remove(name)
                customer_address.remove(address)
                aadhar_num.remove(adnum)
                pan_num.remove(pnum)
                print(name," YOUR ACCOUNT HAS BEEN CLOSED SUCCESSFULLY THANK YOU")
            elif cacc1==2:
                print("THANK YOU WITH US",name)
                exit()
            else:
                exit()
        else:
            exit()
    elif options==6:
        print('''what do you want to change
            1:NAME
            2:ADDRESS
            3:AADHAR NUMBER
            4:PAN NUMBER
            5:EXIT
            ''')
        option_s=int(input("choose from above..:"))
        if option_s==1:
                
                name=input("enter your name:")
                customer_name.append(name)
                print("your name has successfully updated")
                print("AFTER MODIFYING YOUR DETAILS ARE..")
                print("\nNAME=",name,
                       "\nAADHAR NUMBER=",adnum,
                       "\nPAN NUMBER=",pnum,
                       "\nADDRESS=",address)
        elif option_s==2:
                address=input("enter your address:")
                customer_address.append(address)
                print("your address has successfully updated")
                print("AFTER MODIFYING YOUR DETAILS ARE..")
                print("\nNAME=",name,
                      "\nAADHAR NUMBER=",adnum,
                      "\nPAN NUMBER=",pnum,
                      "\nADDRESS=",address)
        elif option_s==3:
                adnum=int(input("enter aadhar number:"))
                aadhar_num.append(adnum)
                print("your addhar number has successfully updated")
                print("AFTER MODIFYING YOUR DETAILS ARE..")
                print("\nNAME=",name,
                      "\nAADHAR NUMBER=",adnum,
                      "\nPAN NUMBER=",pnum,
                      "\nADDRESS=",address)
        elif option_s==4:
                pnum=input("enter pan number:")
                pan_num.append(pnum)
                print("your pan number has successfully updated")
                print("AFTER MODIFYING YOUR DETAILS ARE..")
                print("\nNAME=",name,
                      "\nAADHAR NUMBER=",adnum,
                      "\nPAN NUMBER=",pnum,
                      "\nADDRESS=",address)
        elif option_s==5:
                print("exited")
        
        else:
                print("check the options...")
    elif options==7:
         print("THE ACCOUNT HOLDERS ARE:")
         tim=datetime.datetime.now()
         print(tim.strftime("%c"))
         print("\nNAMES:",customer_name,"\nBALANCES ARE:",min_balance,"\naddress",customer_address)
         

    elif options==8:
        print("THANK YOU FOR CHOOSING NARI BANK VISIT AGAIN")
        break
    else:
        exit()