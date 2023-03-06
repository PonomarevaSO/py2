from typing import Union
import doctest


class Cellphone:
    def __init__(self, charge_level: int, memory_level: Union[int, float]):
        """
        Создание и подгoтовка в работе объекта "Телефон"

        :param charge_level: Заряд телефона, %
        :param memory_level: Объем памяти телефона, Гб

        Примеры:
        >>> cell_phone = Cellphone(99, 512)
        """
        if not charge_level > 0:
            raise ValueError("Заряд телефона должен быть положительным")
        if not isinstance(charge_level, int):
            raise TypeError("Заряд телефона должен быть целым числом, выраженным в %")
        self.charge_level = charge_level

        if not memory_level > 0:
            raise ValueError("Объем памяти должен быть положительным")
        if not isinstance(memory_level, int):
            raise TypeError("Объем памяти должен быть  числом, выраженным в Гб")
        self.memory_level = memory_level

    def charge_change(self, traffic_costs: int):
        """
        Метод вычисляет итоговое значение заряда телефона после активности в приложениях

        :param
        traffic_costs: Активность в приложении за фиксированное время, %
        :return: Итоговое значение заряда телефона

        Примеры:
        >>> cell_phone = Cellphone(99, 512)
        >>> cell_phone.charge_change(12)
        87
        """

        if not traffic_costs > 0:
            raise ValueError("Активность в приложении не может быть отрицательной")
        if not isinstance(traffic_costs, int):
            raise TypeError("Активность в приложении должна быть целым числом")
        self.charge_level -= traffic_costs
        return self.charge_level

    def memory_change(self, app_weigh: Union[int, float]):
        """
        Метод вычисляет оставшееся количество памяти после установки приложения

        :param app_weigh: Вес приложения в Гб
        :return: Оставшееся количество памяти в Гб

        Примеры:
        >>> cell_phone = Cellphone(99, 512)
        >>> cell_phone.memory_change(12)
        500
        """
        if not app_weigh > 0:
            raise ValueError("Вес приложения не может быть отрицательным")
        if not isinstance(app_weigh, (int, float)):
            raise TypeError("Вес приложения должен быть числом, выраженным в ГБ")
        self.memory_level -= app_weigh
        return self.memory_level


class CoursePaper:
    def __init__(self, volume: int, day_before_the_pass: int):
        """
        Инициализация объекта "Курсовая работа":

        :param volume: Объем курсовой работы, количество страниц
        :param day_before_the_pass: Количество дней до сдачи, сутки

        Примеры:
        >>> course_paper = CoursePaper(120,12)
        """
        if not volume > 0:
            raise ValueError("Объем курсовой работы должен быть положительным")
        if not isinstance(volume, int):
            raise TypeError("Объем курсовой работы должен быть целым числом, выраженным в страницах")
        self.volume = volume

        if not day_before_the_pass > 0:
            raise ValueError("Количество дней до сдачи не может быть отрицательным ")
        if not isinstance(day_before_the_pass, int):
            raise TypeError("Количество дней до сдачи должно быть целым числом, выраженным в сутках")
        self.day_before_the_pass = day_before_the_pass

    def percentage_of_completed_work(self, done_volume: int):
        """
        Метод определяет процент выполнения курсовой работы

        :param done_volume: Объем выполненной работы, кол-во стр
        :return: Процент выполнения, %

        Примеры:
        >>> course_paper = CoursePaper(120,12)
        >>> course_paper.percentage_of_completed_work(12)
        10
        """
        if not done_volume > 0:
            raise ValueError("Объем выполненной работы не может быть отрицательным")
        if not isinstance(done_volume, int):
            raise TypeError("Объем выполненной работы должен быть целым числом, выраженным в страницах")
        return int(done_volume/self.volume*100)

    def deadline(self, days_of_work) -> bool:
        """
        Метод определяет, успеваете ли Вы сдать курсовую работу до дедлайна

        :param days_of_work: Запланированное количество дней для завершения работы, сутки
        :return: Успеваете ли Вы до дедлайна (True) или нет (False)

        Примеры:
        >>> course_paper = CoursePaper(120,12)
        >>> course_paper.deadline(12)
        True
        """
        if not days_of_work > 0:
            raise ValueError("Запланированное время для завершения работы не может быть отрицательным")
        if not isinstance(days_of_work, int):
            raise TypeError("Запланированное время для завершения работы должно быть целым числом, выраженным в сутках")
        return self.day_before_the_pass >= days_of_work


class Milk:
    def __init__(self, volume: int, expiration_day: int, expiration_month: int, expiration_year: int):
        """
        Инициализация объекта "Молоко"

        :param volume: Объем упаковки молока, мл
        :param expiration_day: День из даты окончания срока годности
        :param expiration_month: Месяц из даты окончания срока годности
        :param expiration_year: Год из даты окончания срока годности
        Примеры:
        >>> milk1 = Milk(990, 11, 12, 2023)
        """

        if not volume > 0:
            raise ValueError("Объем упаковки молока не может быть отрицательным")
        if not isinstance(volume, int):
            raise TypeError("Объем упаковки молока должен быть целым числом")
        self.volume = volume

        if not expiration_year > 0:
            raise ValueError("Год из даты окончания срока годности не может быть отрицательным")
        if not isinstance(expiration_year, int):
            raise TypeError("Год из даты окончания срока годности должен быть целым числом")
        self.expiration_year = expiration_year

        if not 1 <= expiration_month <= 12:
            raise ValueError("Месяц из даты  срока годности должен быть задан его порядковым номером от 1 до 12")
        if not isinstance(expiration_month, int):
            raise TypeError("Месяц из даты окончания срока годности должен быть целым числом")
        self.expiration_month = expiration_month

        self.calendar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if not 1 <= expiration_day <= self.calendar[expiration_month - 1]:
            raise ValueError("День из даты срока годности должен задаваться его порядковым номером от 1 до 31")
        if not isinstance(expiration_day, int):
            raise TypeError("День из даты окончания срока годности целым числом")
        self.expiration_day = expiration_day

    def amount_of_milk(self, drunk_milk: int):
        """
        Метод определяет количество оставшегося молока

        :param drunk_milk: Количество выпитого молока, мл
        :return: Количество оставшего молока, мл

        Примеры:
        >>> milk1 = Milk(990, 11, 12, 2023)
        >>> milk1.amount_of_milk(900)
        90
        """
        if not drunk_milk > 0:
            raise ValueError("Количество выпитого молока не может быть отрицательным")
        if not isinstance(drunk_milk, int):
            raise TypeError("Количество выпитого молока должно быть целым числом, выраженным в мл")
        if drunk_milk > self.volume:
            raise TypeError("Количество выпитого молока не может превышать объем упаковки")
        self.volume -= drunk_milk
        return self.volume

    def expiration_checking(self, current_day: int, current_month: int, current_year: int):
        """
        Метод проверяет упаковку молока на срок годности
        :param current_day: сегодняшний день
        :param current_month: текущий месяц
        :param current_year: текущий год
        :return: Просрочено(False), еще годен (True)

        Примеры:
        >>> milk1 = Milk(990, 11, 12, 2023)
        >>> milk1.expiration_checking(14, 12, 2023)
        False
        """
        if not current_year > 0:
            raise ValueError("Текущий год не может быть отрицательным")
        if not isinstance(current_year, int):
            raise TypeError("Текущий год должен быть целым числом")

        if not 1 <= current_month <= 12:
            raise ValueError("Текущий месяц должен быть задан его порядковым номером от 1 до 12")
        if not isinstance(current_month, int):
            raise TypeError("Текущий месяц должен быть целым числом")

        if not 1 <= current_day <= self.calendar[current_month - 1]:
            raise ValueError("Текущий день должен быть задан его порядковым номером от 1 до 31")
        if not isinstance(current_day, int):
            raise TypeError("Текущий день должен быть целым числом")

        if self.expiration_year > current_year:
            return True
        if self.expiration_year == current_year:
            if self.expiration_month > current_month:
                return True
            if self.expiration_month == current_month:
                return self.expiration_day >= current_day
        else:
            return False
        # Сделано, чтобы не было проблем при случае, когда, например, срок годности 01.01.2023, текущая дата 31.12.2022


if __name__ == "__main__":
    doctest.testmod()
