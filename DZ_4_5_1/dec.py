from datetime import datetime


def logger(old_function):
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        log_string = f'{datetime.now()}|{old_function.__name__}({args},{kwargs}) -> {result}\n'
        with open('main.log', 'a') as file:
            file.write(log_string)
        print(log_string) # Добавить вывод в консоль
        return result
    return new_function