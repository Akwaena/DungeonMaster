def parse_txt(mode, path):
    """
    Парс текстового файла с конфигами или файла с очками
    mode = config => парс конфигов
    mode = score => парс рекорда по очкам
    """
    if mode == 'config':
        config_dictionary = {}

        for line in open(path, 'r'):
            config_dictionary[line.split('=')[0]] = line.split('=')[1].rstrip()

        return config_dictionary
    elif mode == 'score':
        return int(open(path, 'r').read())


def format_resolution(resolution):
    """
    Переводит код формата WIDTHxHEIGHT в кортеж
    """
    return int(resolution.split('x')[0]), int(resolution.split('x')[1])


def change_max_score(score):
    """
    Смена рекорда в файле
    """
    open('score.txt', 'w').write(str(score))
