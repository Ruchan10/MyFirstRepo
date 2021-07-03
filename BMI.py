m=float(input("Enter mass in KG:"))
h=float(input("Enter height in metres:"))
def fun(m,h):
    BMI = m/h**2
    print(f'Your BMI is {BMI}')
fun()