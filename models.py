"""Модуль c описанием моделей БД для работы приложения."""

from typing import Literal

from database import Database
from settings import db


class Rack:
    """Класс, представлющий стеллаж."""

    db: Database = db

    def __init__(self: "Rack", id_: int, name: str) -> None:
        """Конструктор.

        Args:
        ----
            self (Rack): сам экземпляр.
            id_ (int): id из базы.
            name (str): name из базы.

        """
        self.id = id_
        self.name = name

    @staticmethod
    def get_by(field: Literal["id", "name"], value: int | str) -> "Rack":
        """Получить по названию поля и значению запись из БД.

        Args:
        ----
            field (Literal["id", "name"]): название поля строкой на выбор.
            value (int | str): значение поля.

        Returns:
        -------
            Rack: сам экземляр полученной модели.

        """
        sql_command = f"""
            SELECT id, name
            FROM rack
            WHERE {field} = %s
        """  # noqa: S608
        with Rack.db() as conn:
            cur = conn.cursor()
            cur.execute(sql_command, (value,))
            data = cur.fetchone()
            return Rack(*data)
