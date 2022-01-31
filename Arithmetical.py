a=int(input("Enter the value : "))
b=int(input("Enter the value : "))
print("Press 1 for add \nPress 2 for substraction \nPress 3 for division \nPress 4 for modulas ")
ch=int(input("Enter your choice : "))

if (ch==1):
    {
        print(f"{a}+{b}",(a+b))
    }
elif(ch == 2):
    {
        print(f"{a}-{b}", (a - b))
    }
elif(ch == 3):
    {
        print(f"{a}+{b}", (a / b))
    }
elif(ch==4):
    {
        print(f"{a}%{b}",(a%b))
    }
            