# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def datetonumber(cls, date):
        return [int(i) for i in date.split('-')]

    @staticmethod
    def validation(date):
        errors = []
        try:
            day, month, year = Date.datetonumber(date)[0], Date.datetonumber(date)[1], Date.datetonumber(date)[2]
        except ValueError:
            print(f'{date}: Дата должна состоять только из цифр!')
        except IndexError:
            print(f'{date}: Дата должна состоять из 3 чисел!')
        else:
            if day > 31 or day < 1:
                errors.append("День должен быть от 1 до 31")
            if month > 12 or month < 1:
                errors.append("Месяц должен быть от 1 до 12")
            if day > 30 and month in (4, 6, 9, 11):
                errors.append("В этом месяце 30 дней")
            if day > 28 and month == 2 and year % 4 != 0:
                errors.append("В этом году в феврале 28 дней")
            if day > 29 and month == 2:
                errors.append("В феврале не может быть больше 29 дней")
            if errors:
                print(f'{date}:', ' и '.join(errors))
            else:
                print(f'{date}: Дата корректна')

Date.validation('13-2020')
Date.validation('13-hello-2020')
Date.validation('32-13-2020')
Date.validation('29-02-2021')
Date.validation('30-02-2020')
Date.validation('31-04-2020')
Date.validation('01-12-2020')
