matric = float(input("Matric marks : "))
inter = float(input("Intermediate marks : "))
test = float(input("Entry test (out of 100): "))
interview = float(input("Interview score (out of 100): "))

if matric <= 60:
    print("Rejected: Matric below 60%")
elif inter <= 65:
    print("Rejected: Intermediate below 65%")
elif test <= 50:
    print("Rejected: Entry test below 50")
else:
    merit = (matric * 0.20) + (inter * 0.30) + (test * 0.40) + (interview * 0.10)
    print("Merit:", merit)

    if merit >= 85:
        print("Scholarship + Admission")
    elif merit >= 70:
        print("Admission Confirmed")
    elif merit >= 60:
        print("Waiting List")
    else:
        print("Rejected")
