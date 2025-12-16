# 🚀 Django Crypto Vault

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-5.0-green?style=for-the-badge&logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap)

**The Crypto Vault** is a full-stack web application built to explore the "Batteries-Included" philosophy of Django. It connects to the CoinGecko API to fetch real-time Bitcoin data, stores it in a relational database using Django's ORM, and presents it via a responsive Bootstrap UI.

## 🌟 Key Features

* **Real-Time Data Pipeline:** Fetches live market data from CoinGecko API.
* **Django ORM:** No raw SQL. Database interactions are handled purely through Python Models.
* **Admin Dashboard:** Includes a secure, auto-generated admin panel to manage records manually.
* **Flight Logs:** A historical view of price fluctuations.
* **Persistent Storage:** Uses SQLite for zero-config data persistence.

## 🏗️ Project Structure

Unlike Flask (which is often one file), this project follows the robust Django **MVT (Model-View-Template)** architecture:

```text
my_crypto_project/
├── manage.py           # The CLI Commander
├── db.sqlite3          # The Database
├── templates/          # Global HTML Files
└── crypto/             # The Main App
    ├── models.py       # Database Schema (BitcoinPrice)
    ├── views.py        # Business Logic (API Fetching)
    ├── admin.py        # Admin Panel Configuration
    └── urls.py         # Route Management
