while True:
    print("Available operators: ""\n"
        "1.addition""\n"
        "2.subtractio""\n"
        "3.multiplication""\n"
        "4.division""\n"
        )
    "\n"
    ch=int(input("enter a choice: "))
    if ch!= "1" or "2" or "3" or "4":
        print("wrong choice try again")
        continue
        
    "\n"
    n1=int(input("ENTER A NUMBER: "))
    n2=int(input("ENTER A NUMBER: "))
    "\n"
    
    if ch==1:
        print("your answer is: ", n1+n2, "--------------------------")
    elif ch==2:
        print("your answer is: ", n1-n2, "--------------------------")
    elif ch==3:
        print("your answer is: ", n1*n2, "--------------------------")  
    elif ch==4:
        print("your answer is: ", n1/n2, "--------------------------") 
