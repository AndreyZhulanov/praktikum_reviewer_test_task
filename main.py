import datetime as dt

"""
В нескольких местах кода используется вычисление текущей даты
предлагаю использовать глобальную переменную
today = dt.datetime.now().date()
"""

today = dt.datetime.now().date()


class Record:
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        """
        Удаление лишних переносов строк и обратное условие if
        повысит читабельность кода.
        self.date = (
            dt.datetime.strptime(date, '%d.%m.%Y').date()
            if date else today)
        """
        self.date = (
            dt.datetime.now().date() if
            not
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        """
        Наименование Record было использовано для класса Record
        лучше назвать переменную иначе, например "record".
        """
        for Record in self.records:
            """
            Используйте глобальную переменную today
            """
            if Record.date == dt.datetime.now().date():
                """
                Используйте сокращенный оператор "+=".
                """
                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        week_stats = 0
        """
        Используйте глобальную переменную today
        """
        today = dt.datetime.now().date()
        for record in self.records:
            """
            Конструкция 7 > (today - record.date).days >= 0 
            позволит упросить условие.
            """
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        """
        Используйте значимое наименование переменную вместо "x"
        """
        x = self.limit - self.get_today_stats()
        if x > 0:
            """
            Используйте круглые скобки для многострочных операторов.
            """
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        else:
            """
            else не обязателен. И круглые скобки после return тоже не нужны.
            """
            return('Хватит есть!')


class CashCalculator(Calculator):
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.

    def get_today_cash_remained(self, currency,
                    USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        """
        currency_type = currency - лишняя строка,
        т.к. далее переменной будет присвоено новое значение
        """
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            """
            cash_remained == 1.00 ошибочная строка,
            т.к. cash_remained здесь изменять не нужно
            """
            cash_remained == 1.00
            currency_type = 'руб'
        """
        Лучше разделить условные блоки для читаемости.
        """
        if cash_remained > 0:
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}')
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)
        """
        Если заранее округлить cash_remained, то
        условный блок с выводом сообщения можно упростить:
        text = 'Денег нет, держись'
        if cash_remained > 0:
            text = f'На сегодня осталось {cash_remained} {currency_type}'
        if cash_remained < 0:
            cash_remained *= -1
            text += f': твой долг - {cash_remained} {currency_type}'
        return text
        """

    """
    Избыточное определение. Метод и так будет унаследован от родителя
    """
    def get_week_stats(self):
        super().get_week_stats()
