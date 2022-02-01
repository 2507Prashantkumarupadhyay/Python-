yy=eval(input("Enter the year : "))

if yy%100!=0 or yy%400==0 and yy%4==0:
    print(f"{yy} is a Leap year...")
else:
    print(f"{yy} is not Leap year...")
