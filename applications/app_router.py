"""
Список доступных приложений:
Меню - приложение, которое выводит главное меню.

Открытие смены - дает возможность открыть смену, закрыть смену и вывести отчет за месяц.

Есть проблема - выводит для всех админов задачу в телеграме с проблемой.

Рассрочка - выводит ссылку на страницу, в которой имеется возможность заполнить поля для оформления рассрочки идея-банка.

"""

class AppRouter(object):
    def __init__(self, request):
        pass

    def app_name(self):
        # Отдает название приложения на основании:
        # Если Коллбэк - биндить в кнопки и забирать оттуда же
        # Если это текст - забрать название приложения из ячейки в SQL
        # Если ничего не нашло - то запустить аварийное приложение.
        pass

