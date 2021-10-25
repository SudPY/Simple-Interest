p = float(input("Enter the Principle : "))
t = float(input("Enter the Time Period : "))
r = float(input("Enter the Rate of Interest : "))

def simple_interest(p, t, r):
    si = (p * t * r)/100
    print("The Principle is ", p)
    print("The Time Period is ", t)
    print("The Rate of Interest is ", r)
    print("The Simple Interest is ", si)

    return si

simple_interest(p, t, r)
