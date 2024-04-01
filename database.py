"""Модуль классов для работы базы данных."""

from typing import NamedTuple

import psycopg2


class DatabaseSettings(NamedTuple):
    """Именованный кортеж.

    Хранит необходимые настройки для подключения БД.
    """

    host: str
    port: str
    db: str
    user: str
    password: str


class Database:
    """Обьект для создания подключения к базе данных."""

    def __init__(self: "Database", *, settings: DatabaseSettings) -> None:
        """Конструктор класса.

        Args:
        ----
            self (Database): сам обьект.
            settings (DatabaseSettings): кортеж насроек для подключения.

        """
        self._settings = settings

    def __call__(self: "Database") -> "Database.Connection":
        """Создание подключения."""
        return Database.Connection(self._settings)

    class Connection:
        """Подключение к базе(замкнутые настройки подключения)."""

        def __init__(
            self: "Database.Connection",
            settings: DatabaseSettings,
        ) -> None:
            """Конструктор подключения.

            Args:
            ----
                self (Database.Connection): само подключение.
                settings (DatabaseSettings): кортеж настроек для подключения.

            """
            self._settings = settings

        def __enter__(self: "Database.Connection") -> object:
            """Создание подключения."""
            self._connection = psycopg2.connect(
                host=self._settings.host,
                port=self._settings.port,
                dbname=self._settings.db,
                user=self._settings.user,
                password=self._settings.password,
            )
            return self._connection

        def __exit__(self: "Database.Connection", *args: object) -> None:
            """Закрытие подключения."""
            self._connection.close()
