"""
Вспомогательные функции, используемые во всех слоях приложения.
"""

from __future__ import annotations

import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def parse_datetime(value: str, fmt: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """
    Преобразовать строку *value* в объект :class:`datetime.datetime`.

    Parameters
    ----------
    value:
        Строка вроде ``"2025-04-23 15:47:10"``.
    fmt:
        Формат строки (по умолчанию — `YYYY-MM-DD HH:MM:SS`).

    Raises
    ------
    ValueError
        При неверном формате даты.
    """
    try:
        return datetime.strptime(value, fmt)
    except ValueError as exc:  # pragma: no cover  # тестируем happy-path
        logger.error("parse_datetime: %s", exc, exc_info=exc)
        raise


def json_response(payload: Any) -> Dict[str, Any]:
    """
    Обернуть *payload* в стандартный JSON-ответ API.

    Возвращается словарь вида::

        {
            "result": <payload>,
            "generated_at": "2025-04-23T16:02:13.379352"
        }
    """
    return {"result": payload, "generated_at": datetime.now().isoformat()}


def load_transactions(xls_path: str | Path) -> pd.DataFrame:
    """
    Загрузить Excel-файл *operations.xlsx* и вернуть :class:`pandas.DataFrame`.

    Такой &laquo;тонкий&raquo; слой позволяет позже поменять источник данных
    (например, на PostgreSQL или REST-API) без изменения бизнес-логики.
    """
    path = Path(xls_path)
    if not path.exists():  # pragma: no cover
        raise FileNotFoundError(f"{path} not found")
    return pd.read_excel(path)
