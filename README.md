# 💳 Fintech Payment Utility API (Django)

A production-ready **Fintech Utility API** built with **Django REST Framework** that provides essential payment-related services required by e-commerce platforms, POS systems, SaaS billing tools, and mobile money applications.

This API is designed to be **lightweight, fast, and easy to integrate** and is prepared for **RapidAPI monetisation**.

---

## 🚀 Features

* ✅ Transaction processing with fee calculation
* ✅ Unique transaction reference generation
* ✅ Currency conversion (KES, USD, EUR)
* ✅ Mobile money number validation
* ✅ Transaction logging in PostgreSQL
* ✅ Ready for deployment on Render
* ✅ RapidAPI ready

---

## 🛠 Tech Stack

* Django
* Django REST Framework
* PostgreSQL (production) / SQLite (local)
* Gunicorn + WhiteNoise
* Hosted on Render

---

## 📦 Project Structure

```
├── core/
├── payments/
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Local Setup

### 1) Clone the project

```bash
git clone <your-repo-url>
cd fintech_api
```

### 2) Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run migrations

```bash
python manage.py migrate
```

### 5) Run server

```bash
python manage.py runserver
```

App runs at:

```
http://127.0.0.1:8000
```

---

## 🔌 API Endpoints

### ✅ Process Transaction

**POST** `/api/transaction/`

Body (JSON):

```json
{
  "amount": 500,
  "currency": "KES"
}
```

Response:

```json
{
  "reference": "abc123xyz",
  "amount": 500,
  "fee": 7.5,
  "total": 507.5
}
```

---

### ✅ Currency Conversion

**GET**

```
/api/convert/?amount=100&from_currency=KES&to_currency=USD
```

Response:

```json
{
  "amount": 100,
  "from": "KES",
  "to": "USD",
  "converted_amount": 0.76923
}
```

---

### ✅ Validate Mobile Money Number

**GET**

```
/api/validate-number/?number=0712345678
```

Response:

```json
{
  "valid": true
}
```

---

## 🌍 Deployment on Render

1. Push project to GitHub
2. Create a **Web Service** on Render
3. Add environment variable:

```
DATABASE_URL=<PostgreSQL URL from Render>
```

4. Build command:

```bash
pip install -r requirements.txt && python manage.py migrate
```

5. Start command:

```bash
gunicorn core.wsgi
```

---

## 🗄 Database

* SQLite for local development
* PostgreSQL for production (Render)

---

## 💰 RapidAPI Monetisation

This API is designed to be published on RapidAPI as a **Payment Utility API** for developers building:

* E-commerce platforms
* POS systems
* SaaS billing tools
* Mobile money applications
* Fintech MVPs

Endpoints can be directly connected to RapidAPI using the Render base URL.

---

## 🎯 Use Cases

* Payment simulations
* Fee calculations
* Currency pricing systems
* Mobile money validation
* Transaction reference generation

---

## 👨‍💻 Author

Built by **Ian M** — Web Developer focused on practical, monetisable APIs.
