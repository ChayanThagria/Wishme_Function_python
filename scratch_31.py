import datetime

def wishme():
    hour =  int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        print("Good Morning sir")


    elif hour >=12 and hour < 16:
        print("Good Afternoon Sir")


    elif hour >= 16 and hour < 22:
        print("Good Evening Sir")


    else:
        print("Good Night Sir")


