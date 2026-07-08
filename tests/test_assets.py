from app.modules.assets.repository import AssetRepository


def test_create_asset():
    repository = AssetRepository()

    asset = repository.create(
        name="Bitcoin",
        symbol="BTC",
        category="Crypto",
    )

    assert asset.name == "Bitcoin"
    assert asset.symbol == "BTC"


def test_get_assets():
    repository = AssetRepository()

    assets = repository.get_all()

    assert len(assets) > 0