"""Модуль для загрузки тестовых данных в бд."""

from database import Database
from migrate import migrate
from settings import settings


def execute_many_command(
    sql_command: str,
    data: list[tuple[str | int]],
) -> None:
    """Выполнить команду c разлиными данными.

    Args:
    ----
        sql_command (str): сама sql команда.
        data (list[tuple[str  |  int]]): данные в нужном формате

    """
    db = Database(settings=settings)
    with db() as conn:
        cur = conn.cursor()
        cur.executemany(sql_command, data)
        conn.commit()


rack_insert = """
INSERT INTO rack(name)
VALUES (%s)
"""
rack_insert_values = [("А",), ("Б",), ("Ж",)]


def load() -> None:
    """Основная функция модуля."""
    migrate()
    execute_many_command(rack_insert, rack_insert_values)


if __name__ == "__main__":
    load()
