import pandas as pd
import pytest


@pytest.fixture
def sample_df() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "date": pd.to_datetime(
                [
                    "2025-01-10",
                    "2025-02-05",
                    "2025-02-15",
                    "2025-03-01",
                ]
            ),
            "category": ["Кафе", "Кафе", "Магазин", "Кафе"],
            "description": ["Coffee", "Coffee", "Grocery", "Coffee"],
            "amount": [-300, -450, -1500, -200],
        }
    )
