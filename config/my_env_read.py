# Не знаю чем обусловлено требование никаких сторонних библиотек, но в таком случае сделал так.
import os


# Функция для чтения переменных окружения из файла .env
def read_env(env_file='.env'):
    with open(env_file, 'r') as f:
        for line in f:
            key, value = line.strip().split('=', 1)
            os.environ.setdefault(key, value)