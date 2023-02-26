class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) -> str:
        """Геттер, защищает атрибуты от изменения"""
        return self._name

    @property
    def author(self) -> str:
        """Геттер, защищает атрибуты от изменения"""
        return self._author


class PaperBook(Book):
    """Дочерний класс Бумажной книги"""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"Бумажная Книга {self._name}. Автор {self._author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"

    @property
    def pages(self) -> int:
        """Геттер, возвращает количество страниц"""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Сеттер, проверяет допустимость введенных данных, устанавливавет новое количество страниц"""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть целым числом (int)")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = new_pages


class AudioBook(Book):
    """Дочерний класс Аудиокниги"""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"Аудиокнига {self._name}. Автор {self._author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"

    @property
    def duration(self) -> float:
        """Геттер, возвращает продолжительность книги"""
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Сеттер, переводит int во float,
        проверяет допустимость введенных данных,
         устанавливает новую продолжительность"""
        if isinstance(new_duration, int):
            new_duration = float(new_duration)
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность книги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность книги должна быть положительным числом")
        self._duration = new_duration