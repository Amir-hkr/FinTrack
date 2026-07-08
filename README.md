# 🚀 FinTrack Backend

A modular investment portfolio management backend built with **FastAPI**.

FinTrack helps users manage assets, record transactions, track portfolio performance, and analyze investments.

---

## ✨ Features

✅ Asset Management  
- Create and manage assets
- Search assets by symbol

✅ Transaction Management  
- Record BUY / SELL transactions
- Transaction history
- Input validation

✅ Portfolio Tracking  
- Calculate current holdings
- Average buy price
- Investment value

✅ Analytics  
- Total investment
- Current portfolio value
- Profit / Loss calculation
- Profit percentage

✅ Testing  
- Automated tests with Pytest

---

## 🏗️ Architecture

Project structure follows a modular architecture:


app/
├── core/
├── modules/
│ ├── assets/
│ ├── transactions/
│ ├── portfolio/
│ └── analytics/
└── main.py


---

## ⚙️ Installation

Clone project:

```bash
git clone <repository-url>
cd FinTrack

Create virtual environment:

python -m venv venv

Install dependencies:

pip install -r requirements.txt
▶️ Run

Start server:

uvicorn app.main:app --reload

API Documentation:

http://127.0.0.1:8000/docs
🧪 Testing

Run tests:

pytest

Current status:

6 tests passed ✅

🛠️ Technologies
Python
FastAPI
Pydantic
Pytest
Uvicorn


🔮 Future Plans
React Dashboard
Database integration
User authentication
Real-time market data
Docker deployment