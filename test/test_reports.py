from src.reports import spending_by_category


def test_spending_by_category(sample_df):
    report = spending_by_category(sample_df, "Кафе", "2025-01-01")
    assert report["total_spent"] == -950  # -300-450-200
    assert len(report["daily_breakdown"]) == 3
