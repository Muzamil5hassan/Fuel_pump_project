print("The petrol pump program")
a=int(input("Enter the quantity of petrol ->"))
ap=eval(input("Enter the price of petrol ->"))
b=int(input("Enter the quantity of diseal ->"))
bp=eval(input("Enter the price of diseal ->"))
while True:
    s1=int(input('''
        select the option...
        1-> Sell the petrol
        2-> Sell the diseal
        3-> Check the total amount of petrol and diseal in fuel tank
        4->Exit/stop
        select the option-> '''))
    if s1==1:
        print("\n\t***SELL***\n")
        a1=int(input("\n\nEnter the purchasing amount of petrol :"))
        a2=a1/ap
        a=a-a2
        print("Liter ->",a2,"\n\n")
    elif s1==2:
        print("\n\t***SELL***\n")
        b1=int(input("\n\nEnter the purchasing amount of petrol :"))
        b2=b1/bp
        b=b-b2
        print("Liter ->",b2,"\n\n")
    elif s1==3:
        print("\n\t***CHECKING THE FUEL QUATITIES***\n")
        print(f"The remaining pertol is ->{a}\nThe remaining diseal is ->{b}")
    else:
        print("\n\t***THANK YOU***\n\n")
        break
