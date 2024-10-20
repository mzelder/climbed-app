import calendar 
from django.utils import timezone

#TODO current day need to be fixed
def get_month_informations(current_month, current_year):
    if current_month > 12:
        current_month = 1
        current_year += 1
    if current_month < 1:
        current_month = 12
        current_year -= 1

    now = timezone.localtime(timezone.now())
    current_month_string = calendar.month_name[current_month]
    current_day = now.day
    days_in_month = calendar.monthrange(current_year, current_month)[1]
    days_list = [day for day in range(1, days_in_month+1)]
    return {
        "current_year": current_year,
        "current_month_number": current_month,
        "current_month_string": current_month_string,
        "current_day": current_day,
        "days_list": days_list
    }