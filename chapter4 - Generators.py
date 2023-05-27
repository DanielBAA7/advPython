def gen_secs():
    for sec in range(60):
        yield sec


def gen_minutes():
    for minute in range(60):
        yield minute


def gen_hours():
    for hour in range(24):
        yield hour


def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)


def gen_years(start=2023):
    while True:
        yield start
        start += 1


def gen_months():
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    if month == 2 and leap_year:
        yield from range(1, 30)
    else:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        yield from range(1, days_in_month[month - 1] + 1)


def gen_date():
    for year in gen_years():
        for month in gen_months():
            leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            for day in gen_days(month, leap_year):
                for time in gen_time():
                    yield "%02d/%02d/%04d %s" % (day, month, year, time)


def main():
    count = 0
    for date in gen_date():
        count += 1
        if count % 1000000 == 0:
            print(date)

#     result
# 12/01/2023 13:46:39
# 24/01/2023 03:33:19
# 04/02/2023 17:19:59
# 16/02/2023 07:06:39
# 27/02/2023 20:53:19
# 11/03/2023 10:39:59
# ...


if __name__ == "__main__":
    main()
