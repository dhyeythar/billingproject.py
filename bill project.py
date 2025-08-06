while True:
    print("Welcome to the Billing App!")
    t_billAm = float(input("Enter your total amount: "))
    n_ofPeople = int(input("Enter total number of people: "))
    tip_per = int(input("Enter tip percentage (0/5/10/15/20): "))
    tipAm = (t_billAm*tip_per)/100
    print("Amount of tip: ", tipAm)
    t_BillWithTip = t_billAm + tipAm
    print("Total Bill (with Tip): ", t_BillWithTip)
    splitAm = t_BillWithTip / n_ofPeople
    print("Share for each person: ", splitAm)

    res = input("Would you like to calculate your next bill? (y/n): ")
    if res == "y":
        continue
    elif res == "n":
        break
    else:
        print("Output is invalid!!")
        break