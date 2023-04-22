import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            args_str = ', '.join(map(str, args))
            kwargs_str = ', '.join([f"{key}={value}" for key, value in kwargs.items()])
            signature = f"{old_function.__name__}({args_str}, {kwargs_str})"
            result = old_function(*args, **kwargs)
            with open(path, mode='a', encoding='utf-8') as file:
                file.write(f"{date} | {signature} | {result}\n")
            return result
        return new_function
    return __logger