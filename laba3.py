# Singleton (Одиночка)
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def some_method(self):
        return "Singleton method called!"


# Factory Method (Фабричный метод)
from abc import ABC, abstractmethod

# Продукт
class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

# Конкретные продукты
class FileLogger(Logger):
    def log(self, message: str):
        return f"Logging to file: {message}"

class ConsoleLogger(Logger):
    def log(self, message: str):
        return f"Logging to console: {message}"

# Фабрика
class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        pass

class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()

class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()


# Abstract Factory (Абстрактная фабрика)
# Продукты
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class WindowsButton(Button):
    def paint(self):
        return "Windows button painted"

class MacButton(Button):
    def paint(self):
        return "Mac button painted"

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

class WindowsCheckbox(Checkbox):
    def paint(self):
        return "Windows checkbox painted"

class MacCheckbox(Checkbox):
    def paint(self):
        return "Mac checkbox painted"

# Абстрактная фабрика
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


# Builder (Строитель)
class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None

    def __str__(self):
        return f"Pizza with {self.dough} dough, {self.sauce} sauce, and {self.topping} topping."

class PizzaBuilder(ABC):
    @abstractmethod
    def build_dough(self):
        pass

    @abstractmethod
    def build_sauce(self):
        pass

    @abstractmethod
    def build_topping(self):
        pass

    @abstractmethod
    def get_result(self) -> Pizza:
        pass

class HawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self):
        self.pizza.dough = "cross"

    def build_sauce(self):
        self.pizza.sauce = "mild"

    def build_topping(self):
        self.pizza.topping = "ham and pineapple"

    def get_result(self) -> Pizza:
        return self.pizza

class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def construct_pizza(self):
        self.builder.build_dough()
        self.builder.build_sauce()
        self.builder.build_topping()


# Пример использования всех паттернов
if __name__ == "__main__":
    # Singleton
    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)  # True
    print(s1.some_method())

    # Factory Method
    file_logger_factory = FileLoggerFactory()
    console_logger_factory = ConsoleLoggerFactory()
    file_logger = file_logger_factory.create_logger()
    console_logger = console_logger_factory.create_logger()
    print(file_logger.log("File message"))
    print(console_logger.log("Console message"))

    # Abstract Factory
    windows_factory = WindowsFactory()
    mac_factory = MacFactory()

    windows_button = windows_factory.create_button()
    windows_checkbox = windows_factory.create_checkbox()
    mac_button = mac_factory.create_button()
    mac_checkbox = mac_factory.create_checkbox()

    print(windows_button.paint())
    print(windows_checkbox.paint())
    print(mac_button.paint())
    print(mac_checkbox.paint())

    # Builder
    hawaiian_builder = HawaiianPizzaBuilder()
    director = PizzaDirector(hawaiian_builder)
    director.construct_pizza()
    pizza = hawaiian_builder.get_result()
    print(pizza)
