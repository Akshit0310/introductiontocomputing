

def start():
    a = int(input("Enter the date:"))
    b = int(input("Enter the month:"))
    c = int(input("Enter the year:"))
    if(b<=0 or b>12 or a<=0):
        print("Invalid date")
        print("Taking you back to options")
        start()

    elif(b==1 or b==3 or b==5 or b==7 or b==8 or b==10):
        if(a>31):
            print("Invalid date")
            print("Taking you back to options")
            start()

        elif(a<31):
            a+=1
            print("Next date is %d/%d/%d"%(a,b,c))
            
        elif(a==31):
            a=1
            b+=1
            print("Next date is %d/%d/%d" % (a, b, c))

    elif(b==1 and a==31):
        b+=1
        a=1
        print("Next date is %d/%d/%d"%(a,b,c))

    elif(b==2 and a<28):
        a+=1
        print("Next date is %d/%d/%d"%(a,b,c))

    elif(c%100==0 and b==2):
        if(c%400==0 and a==29):
            print("Invalid date(Leap year does not exist in years divided by 400)")
            print("Taking you back to options")
            start()

        elif(c%400!=0 and a==29):
            a=1
            b+=1
            print("Next date is %d/%d/%d"%(a,b,c))

    elif(c%100!=0 and c%4==0 and b==2 and a==29):
        a=1
        b+=1
        print("Next date is %d/%d/%d"%(a,b,c))

    elif(b==4 or b==6 or b==9 or b==11):
        if(a>30):
            print("Invalid date")
            print("Taking you back to options")
            start()

        elif(a<30):
            a+=1
            print("Next date is %d/%d/%d"%(a,b,c))

        elif(a==30):
            a=1
            b+=1
            print("Next date is %d/%d/%d"%(a,b,c))

    elif(b==12):
        if(a>31):
            print("Invalid date")
            print("Taking you back to options")
            start()

        elif(a<31):
            a+=1
            print("Next date is %d/%d/%d"%(a,b,c))

        elif(a==31):
            a=1
            b=1
            c+=1
            print("Next date is %d/%d/%d"%(a,b,c))

    else:
        print("Invalid date")
        print("Taking you back to options")
        start()
start()

