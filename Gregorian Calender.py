import math

def isleapyear(x):
    if x%4==0 and x%100!=0:
        return True
    elif x%400==0:
        return True
    else:
        return False

date=input("Enter the date in dd/mm/yyyy format: ")
ref="01/01/1988"
yr=int(date[6:])
yrgap=yr-1988
leapyrs=0
if yr>=1988:
    for i in range(1988,yr):
        if isleapyear(i):
            leapyrs+=1
else:
    for i in range(1987,yr-1,-1):
        if isleapyear(i):
            leapyrs+=1
if yr>=1988:
    yrdays=yrgap*365+leapyrs
else:
    yrdays=yrgap*365-leapyrs

mnthdays=0
for i in range(1,int(date[3:5])):
    if i==1:
        mnthdays+=30
    elif i==2:
        if isleapyear(yr):
            mnthdays+=29
        else:
            mnthdays+=28
    elif i==3:
        mnthdays+=31
    elif i==4:
        mnthdays+=30
    elif i==5:
        mnthdays+=31
    elif i==6:
        mnthdays+=30
    elif i==7:
        mnthdays+=31
    elif i==8:
        mnthdays+=31
    elif i==9:
        mnthdays+=30
    elif i==10:
        mnthdays+=31
    elif i==11:
        mnthdays+=30

datedays=int(date[:2]) if int(date[3:5])!=1 else int(date[:2])-1
days=yrdays+mnthdays+datedays
if yr>=1988:
    rem=days%7
else:
    rem=days%-7
week=["Friday","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday"]
print(week[rem])



