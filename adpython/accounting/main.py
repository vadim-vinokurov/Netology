from accounting.application.db import people
from accounting.application import salary
import datetime






if __name__ == '__main__':
    print(people.get_employees(1))
    print(salary.calculate_salary(1))
    print(f'Today is: {datetime.date.today()}')
