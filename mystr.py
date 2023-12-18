from datetime import datetime
import argparse
import logging

logging.basicConfig(level=logging.INFO, encoding='utf-8', filename='mystr_logg.log')

class MyStr(str):
    def __new__(cls, value, author):
        obj = super().__new__(cls, value)
        obj.author = author
        obj.time = datetime.now().strftime('%Y-%m-%d %H:%M')
        return obj
        
    def __str__(self):
        return f"{super().__str__()} (Автор: {self.author}, Время создания: {self.time})"
    
    def __repr__(self):
        return f"MyStr({super().__repr__()}, '{self.author}')"

def main():
    parser = argparse.ArgumentParser(description='Пример запуска из командной строки')
    parser.add_argument('value', type=str, help='Значение')
    parser.add_argument('author', type=str, help='Автор')
    args = parser.parse_args()
    
    try:
        my_str = MyStr(args.value, args.author)
        print(my_str)
        logging.info(f"Успешно создан экземпляр MyStr: {my_str}")
    except Exception as e:
        logging.error(f"Ошибка при создании экземпляра MyStr: {str(e)}")

if __name__ == '__main__':
    main()


'''
Пример запуска кода:                     python mystr.py "Hello World" "John"
'''