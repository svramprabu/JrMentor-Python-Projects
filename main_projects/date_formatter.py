def main():
    date = date_check()
    print(date)

def date_check():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]
    while True:
        try:
            date = input('Enter Date: ')
            # 9/8/1636 or 
            if '/' in date:
                m,d,y = list(map(int,date.split('/'))) #map(fn,seq) int
                # print(m,d,y)
                if m > 12:
                    print('Wrong date by no of months')
                    continue
                if d > 31:
                    print('Wrong date by no of days')
                    continue
                return f"{y}-{m:02}-{d:02}"
            # September 8, 1636
            elif ',' in date:
                m,d,y = date.split()
                print(m,d,y)
                d = int(d[:-1]) #8, -> 8
                if d > 31:
                    print('Wrong date by no of days')
                    continue
                if m not in months:
                    continue
                m = months.index(m)+1
                return f"{y}-{m:02}-{d:02}"
        except ValueError:
            continue
if __name__=='__main__':
    main()