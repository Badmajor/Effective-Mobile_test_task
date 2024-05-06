import argparse
import csv
import os.path


from constants import FIELDS, MANY_ROWS, CHOICE, SUCCESS


class Wallet:
    filename = "wallet.csv"
    data = []

    def __init__(self):
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                reader = csv.DictReader(f)
                self.data = list(reader)

    def show(self, *args, **kwargs):
        """Метод выводит баланс в консоль."""
        incomes: int = sum(
            float(record['amount'])
            for record in self.data if record['category'] == 'доход'
        )
        expenses: int = sum(
            float(record['amount'])
            for record in self.data if record['category'] == 'расход'
        )
        balance: int = incomes - expenses
        print(balance)

    def add(self, namespace: argparse.Namespace):
        """Метод добавляет запись файл."""
        namespace.category = namespace.category.lower()
        self.data.append(namespace.__dict__)
        self.save()
        print(SUCCESS)

    def save(self):
        """Метод сохраняет self.data в файл."""
        with open(self.filename, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS.keys())
            writer.writeheader()
            writer.writerows(self.data)

    def search(self, namespace: argparse.Namespace):
        result = self._search(namespace)
        print(*result[1], sep='\n')

    def _search(self, namespace: argparse.Namespace | dict):
        """Метод ищет совпадения полученных ключей и значений в self.data."""
        result = []
        if isinstance(namespace, argparse.Namespace):
            namespace: dict = namespace.__dict__
        for i, record in enumerate(self.data):
            for key, value in namespace.items():
                if value and value != record[key]:
                    break
            else:
                result.append((i, record))
        return result

    def update(self, namespace: argparse.Namespace, choice=None):
        """Метод обновляет значение строки."""
        dict_args: dict = namespace.__dict__
        field = dict_args.pop('field')
        new_value = dict_args.pop('new')
        rows = self._search(dict_args)
        if len(rows) > 1:
            print(MANY_ROWS)
            for row in rows:
                print(f'{row[0]} - {row[1]}')
            choice = int(input(CHOICE))
        row_idx = choice or rows[0][0]
        self.data[row_idx][field] = new_value
        self.save()
        print(SUCCESS)
