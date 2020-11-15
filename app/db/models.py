from pony.orm import *


db = Database()


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    password = Optional(str)
    email = Required(str, unique=True)



def is_DB_created(path):
    from os.path import (
        join as os_join,
        isfile
    )
    from settings.config import cfg

    name_db = cfg.get("db", "name")
    if not isfile(os_join(path, "db", name_db)):
        db.bind(provider=cfg.get("db", "type"), filename=name_db, create_db=True)
        db.generate_mapping(create_tables=True)
        print('create db')
    else:
        db.bind(provider=cfg.get("db", "type"), filename=name_db)
        try:
            db.generate_mapping()
        except Exception as e:
            print('при создании бд произошла какая-то ошибка (видимо, структура БД была изменена)\n', e)
            print('попытка исправить.....')
            db.generate_mapping(create_tables=True)

if __name__ == '__main__':
    from os import getcwd
    from os.path import split as os_split

    path = os_split(getcwd())
    path = os_split(path[0])[0] if not bool(path[-1]) else path[0]
    is_DB_created(path)
else:
    from os import getcwd

    is_DB_created(getcwd())