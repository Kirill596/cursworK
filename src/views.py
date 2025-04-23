"""
Функции-контроллеры &laquo;страниц&raquo;.
Главная — `index`, События — `events`.
"""

from __future__ import annotations

import logging
from typing import Dict

import pandas as pd

from .utils import json_response, parse_datetime

logger = logging.getLogger(__name__)


def index(datetime_str: str) -> Dict:
    """
    &laquo;Главная&raquo; (короткая демо-страница).

    Parameters
    ----------
    datetime_str:
        Дата/время от клиента (``YYYY-MM-DD HH:MM:SS``).

    Returns
    -------
    dict
        JSON, удовлетворяющий ТЗ.
    """
    ts = parse_datetime(datetime_str)
    greeting = f"Добро пожаловать! Сейчас {ts:%d.%m.%Y %H:%M}"
    return json_response({"message": greeting})


def events(df: pd.DataFrame) -> Dict:
    """
    &laquo;События&raquo; — простейшая выборка из *df* (покажем 5 записей).

    Parameters
    ----------
    df:
        Таблица транзакций (как правило — `load_transactions`).

    Returns
    -------
    dict
        JSON со списком событий.
    """
    selection = (
        df.head()  # в реальном коде здесь бизнес-логика фильтрации
        .assign(date=lambda d: d["date"].dt.strftime("%Y-%m-%d"))
        .to_dict(orient="records")
    )
    return json_response({"events": selection})
