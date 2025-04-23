"""
Бизнес-функции сервисного слоя.
Здесь реализован &laquo;Простой поиск&raquo; — фильтрация по `description`.
"""

from __future__ import annotations

import logging
from typing import Dict, List

logger = logging.getLogger(__name__)


def simple_search(query: str, transactions: List[dict]) -> Dict:
    """
    Найти транзакции, где `query` входит в поле `description` (регистр не важен).

    Parameters
    ----------
    query:
        Строка-запрос.
    transactions:
        Коллекция транзакций вида::

            {"description": "Coffee shop", "amount": -300, ...}

    Returns
    -------
    dict
        JSON-объект с полями ``query``, ``count`` и ``items``.
    """
    q = query.lower()
    found = [txn for txn in transactions if q in str(txn.get("description", "")).lower()]
    return {"query": query, "count": len(found), "items": found}
