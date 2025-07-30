
from fastapi import APIRouter
import yfinance as yf

router = APIRouter()

@router.get("/company-overview/{symbol}")
def get_company_overview(symbol: str):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        return {
            "symbol": symbol,
            "name": info.get("shortName"),
            "industry": info.get("industry"),
            "sector": info.get("sector"),
            "summary": info.get("longBusinessSummary")
        }
    except Exception as e:
        return {"error": str(e)}
