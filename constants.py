FIELDS = {
    'timestamp': 'Дата в формате ГГГГ-ММ-ДД',
    'amount': 'Сумма',
    'category': 'Категория. доход или расход',
    'description': 'Описание'
}


COMMANDS = {
    "show": {
        'help': "Показать баланс",
        'fields': dict(),
        'required': False,
        'cursor': False,
    },
    "search": {
        'help': "Найти запись",
        'fields': FIELDS,
        'required': False,
        'cursor': False,
    },
    "add": {
        'help': "Добавить запись",
        'fields': FIELDS,
        'required': True,
        'cursor': False,
    },
    "update": {
        'help': "Изменить запись",
        'fields': FIELDS,
        'required': False,
        'cursor': True,
    },
}

DOCS = 'Консольного приложения "Личный финансовый кошелек"'
SUCCESS = 'Успешно!'
MANY_ROWS = 'Найдено больше одной записи'
CHOICE = 'Какую запись редактируем: '
NAME = "Личный финансовый кошелек"
