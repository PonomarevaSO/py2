class SteamGenerator:
    """Базовый класс Парогенератора АЭС"""

    def __init__(self, pressure: float):
        """
        Создание и подготовка к работе объекта "Парогенератор"

        :param pressure: Давление внутри парогенератора, МПа
        """
        self.pressure = pressure

    def __str__(self):
        return f"Парогенератор с давлением {self.pressure}"

    def __repr__(self):
        return f"{self.__class__.__name__}(pressure={self.pressure!r})"

    def water_level(self, current_level: float, minimum_level: float) -> bool:
        """
        Регулирование уровня теплоносителя 1-го контура в парогенератора (ПГ) для предотвращения кризисом теплообмена

        :param current_level: Показывает действительный уровень теплоносителя в ПГ, мм
        :param minimum_level: Минимальная допускаемая высота телпоносителя в ПГ, исключающая кризис теплообмена, мм
        :return: Критичность теплообмена: показатель меньше 0 (кризис теплообмена наступил), показатель больше 0 (номинальный режим работы ПГ)
        """
        ...
        current_level = ...

        return current_level - minimum_level

    def steam(self) -> None:
        """
        Данный метод отвечает за пуск реактора, который происходит за счет подъема из активной зоны
        нескольких кластеров органов СУЗ
        """
        ...


class GorizontalSteamGenerator(SteamGenerator):
    """Дочерний класс Ядерного реактора с водой под давлением"""

    def __init__(self, capacity: float, pressure_1: float):
        """
        Создание и подготовка к работе объекта "Горизонтальный парогонератор АЭС"
        :param capacity: Тепловая мощность ПГ, МВт
        :param pressure_1: давление 1 контара, МПа
        """
        super().__init__(pressure)
        self.pressure_1 = pressure_1

    def __str__(self):
        return f"Парогенератор горизонтальный с давлением воды {self.pressure_1} и тепловой мощностью {self.capacity}"

    def __repr__(self):
        return f"{self.__class__.__name__}(capacity={self.capacity!r}, pressure_1={self.pressure_1})"

    def steam_humidity(self, steam_tempreture: float, maximum: float) -> bool:
        """
        Регулирование влажности пара на выходе из реактора в схеме АЭС без сепаратора-пароперегревателя.
        Данный метод необходимо перегрузить, т.к. в горизонтальных парогенераторах на уходящего на турбину пар
        влажность влияют и наличие сепарационных устройств в корпусе ПГ, теплофизические показатели теплоносителя
        1-го контура, наличие естественной циркуляции теплоносителя в межтрубном пространстве и отсуствие кризиса
        теплообмена.

        :steam_temperature: Температура пара на линии насвущения, С
        :maximum: Максимально допустимая владность уходящего на турбину пара для данной реакторной установки, %
        :return: Превышает влажность пара максимум (False), не превышает (True)
        """
        ...
        steam_humidity= ...
        return steam_humidity < maximum