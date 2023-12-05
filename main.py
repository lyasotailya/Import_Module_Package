from application.salary import calculate_salary
from application.db.people import get_employees
import datetime
import emoji


def today_date():
    date = datetime.date.today()
    return date


def heart():
    red_heart = emoji.emojize("Python :red_heart:")
    return red_heart


if __name__ == '__main__':
    print(calculate_salary())
    print(get_employees())
    print(today_date())
    print(heart())
