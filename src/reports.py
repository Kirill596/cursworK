"""
Отчёт &laquo;Траты по категории за 3 месяца&raquo; (см. ТЗ).
"""

from __future__ import annotations

import logging
from typing import Dict

import pandas as pd

logger = logging.getLogger(__name__)


def spending_by_category(df: pd.DataFrame, category: str, since: str) -> Dict:
    """
    Вернуть JSON-отчёт о тратах *category* за период `[since; since + 3 месяца)`.

    Parameters
    ----------
    df:
        Таблица транзакций (обязательно есть колонки ``date``, ``category``, ``amount``).
    category:
        Интересующая категория (регистр игнорируется).
    since:
        Дата начала отчётного периода ``YYYY-MM-DD``.

    Returns
    -------
    dict
        Итоговая сумма и дневная разбивка.
    """
    start = pd.to_datetime(since)
    end = start + pd.DateOffset(months=3)

    mask = (df["category"].str.lower() == category.lower()) & (df["date"] >= start) & (df["date"] < end)

    subtotal = df.loc[mask, "amount"].sum().round(2)

    daily = (
        df.loc[mask]
        .assign(day=lambda x: x["date"].dt.date)
        .groupby("day")["amount"]
        .sum()
        .reset_index()
        .to_dict(orient="records")
    )

    return {
        "category": category,
        "period": {"from": str(start.date()), "to": str(end.date())},
        "total_spent": float(subtotal),
        "daily_breakdown": daily,
    }
