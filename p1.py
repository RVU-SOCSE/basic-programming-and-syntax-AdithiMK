# Name: ADITHI MAHENDRAN
#USN:1RUA25BCA0005
a=int(input("enter a number:"))
b=int(input("enter 2nd number:"))
cal=int(input("1.addition\n2.sub\n3.multiplication\n4.division\nchoose an option:"))
match cal:
    case 1 :
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case _:
        print("invalid option")
    
        
