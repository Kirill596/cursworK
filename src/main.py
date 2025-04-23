from __future__ import annotations

import json
import logging
from pathlib import Path


from .reports import spending_by_category
from .services import simple_search
from .utils import load_transactions
from .views import events, index

logging.basicConfig(level=logging.INFO)


def main() -> None:
    """Запустить демонстрацию."""
    data_path = Path(__file__).parents[1] / "data" / "operations.xlsx"
    df = load_transactions(data_path)
    txns = df.to_dict(orient="records")

    print("— index —")
    print(json.dumps(index("2025-04-23 12:00:00"), ensure_ascii=False, indent=2))
    print("\n— events —")
    print(json.dumps(events(df), ensure_ascii=False, indent=2))
    print("\n— simple_search —")
    print(json.dumps(simple_search("coffee", txns), ensure_ascii=False, indent=2))
    print("\n— spending_by_category —")
    print(
        json.dumps(
            spending_by_category(df, "Кафе", "2025-01-01"),
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
