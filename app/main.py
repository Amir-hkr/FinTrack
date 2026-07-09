from fastapi import FastAPI
from app.modules.transactions.api import router as transactions_router
from app.core.config import settings
from app.modules.assets.api import router as assets_router
from app.modules.portfolio.api import router as portfolio_router
from app.modules.market.api import router as market_router
from app.modules.analytics.api import router as analytics_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
def root() -> dict[str, str]:
    """Health check endpoint."""
    return {
        "message": f"Welcome to {settings.app_name}",
    }


app.include_router(assets_router)
app.include_router(transactions_router)
app.include_router(portfolio_router)
app.include_router(market_router)
app.include_router(analytics_router)