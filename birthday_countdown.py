import datetime


def print_header():
    print('-------------------------------------')
    print('              birthday            ')
    print('--------------------------------------')


def get_user_birthday():
    print("enter your birthday")
    year = int(input("year : [yyyy] "))
    month = int(input("month :[mm] "))
    day = int(input("Day : [dd] "))

    birthday = datetime.date(year, month, day)
    return birthday


def compute_days_between(date1, date2):
    this_year = datetime.date(date2.year, date1.month, date1.day)

    difference = this_year - date2
    return difference.days


def print_birthday_information(diff_day):
    if diff_day < 0:
        print("you have a birthday {} days ago".format(-diff_day))
    elif diff_day > 0:
        print("you have a birthday in {} days".format(diff_day))
    else:
        print("happy birthday!")


def main():
    print_header()
    birth = get_user_birthday()
    new = datetime.date.today()
    number_of_days = compute_days_between(birth, new)
    print_birthday_information(number_of_days)


main()
