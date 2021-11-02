close = 'N'
print('Give me any date (1753-9999) and I will tell you the corresponding day of the week')
while close == 'N':
    def split(x):
        return [char for char in x]
    date=(input("DD MM YYYY ").split())
    year=date[2]
    month=date[1]
    day=int(date[0])
    century=split(year)
    century=int((str(century[0])+str(century[1])))
    c_loop=century-16
    remainder=c_loop%4
    if remainder == 0:
        answer = 2
    elif remainder == 1:
        answer = 0
    elif remainder == 2:
        answer = 5
    elif remainder == 3:
        answer = 3
    years=split(year)
    years=int((str(years[2])+str(years[3])))
    r=int(years%12)
    leaps=(int(years-r))/12
    answer = answer + leaps + r
    rr=int(r-(r%4))
    answer = answer + (rr/4)
    if month == '01':
        if r%4 == 0:
            answer = answer - 4 + day
        else:
            answer = answer - 3 + day
    elif month == '02':
        if r%4 == 0:
            answer = answer - 29 + day
        else:
            answer = answer - 28 + day
    elif month == '03':
        answer = answer - 14 + day
    elif month == '04':
        answer = answer - 4 + day
    elif month == '05':
        answer = answer - 9 + day
    elif month == '06':
        answer = answer - 6 + day
    elif month == '07':
        answer = answer - 11 + day
    elif month == '08':
        answer = answer - 8 + day
    elif month == '09':
        answer = answer - 5 + day
    elif month == '10':
        answer = answer - 10 + day
    elif month == '11':
        answer = answer - 7 + day
    elif month == '12':
        answer = answer - 12 + day
    if answer%7 == 0:
        print('Sunday')
    elif answer%7 == 1:
        print('Monday')
    elif answer%7 == 2:
        print('Tuesday')
    elif answer%7 == 3:
        print('Wednesday')
    elif answer%7 == 4:
        print('Thursday')
    elif answer%7 == 5:
        print('Friday')
    elif answer%7 == 6:
        print('Saturday')
    close=input('Exit? Y/N ')
