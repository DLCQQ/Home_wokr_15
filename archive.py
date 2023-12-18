import argparse
import logging

class Archive:
    _instance = None
    archive_text = []
    archive_number = []

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls.archive_text = []
            cls.archive_number = []
        return cls._instance

    def __init__(self, text, number):
        self.text = text
        self.number = number
        self.archive_text.append(text)
        self.archive_number.append(number)

    def __str__(self):
        return f"Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}"

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


def main():
    # Инициализация логирования
    logging.basicConfig(filename='Archive_logg.log', encoding='utf-8', level=logging.INFO)

    # Создание парсера аргументов командной строки
    parser = argparse.ArgumentParser(description='Archive Application')
    parser.add_argument('--text', type=str, help='Text argument')
    parser.add_argument('--number', type=int, help='Number argument')

    args = parser.parse_args()

    try:
        # Создание объекта архива
        archive = Archive(args.text, args.number)

        # Вывод архива
        print(archive)

        # Логирование информации
        logging.info(f"Archive created: {archive}")

    except Exception as e:
        # Логирование ошибки
        logging.error(f"An error occurred: {e}")


if __name__ == '__main__':
    main()