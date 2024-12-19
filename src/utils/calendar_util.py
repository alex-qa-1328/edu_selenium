import calendar

def day_of_week(year, month, day):
    current_day = calendar.weekday(year, month, day)
    days = list(calendar.day_name)
    return days[current_day]
