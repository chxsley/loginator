import json
from logger_param import loggerParam

class logger:
    @staticmethod
    def json_write_message(data : dict) -> None:
        path_to_file = 'data.json'
        with open(path_to_file, 'a') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def info(message : str,param : loggerParam = None):
        if param is None:
            param = loggerParam(tag='info', message=message)

        logger.json_write_message(param.parse_dict())


def plus(a, b):
    logger.info(f'{plus.__name__} opened with parametres {a} and {b}')
    res = a + b
    logger.info(f'{plus,__name__} finish with result {res}')
    return res


def main():
    plus(1, 5)


if __name__ == '__main__':
    main()