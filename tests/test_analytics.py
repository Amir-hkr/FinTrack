from app.modules.analytics.service import AnalyticsService


def test_analytics_summary():

    service = AnalyticsService()

    result = service.get_summary()

    assert "total_invested" in result
    assert "current_value" in result
    assert "total_profit_loss" in result
    assert "profit_percentage" in result
    assert "assets_count" in result

    assert result["assets_count"] >= 0