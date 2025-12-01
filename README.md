**Automatizované API testy – Python + Pytest**
Tento projekt obsahuje automatizované testy REST API na základe zadania „Technical Task #2 – API test automation“ 

Testovaným systémom je verejné API: **https://reqres.in/**

**Použité technológie**
- **Python 3**
- **Pytest** – framework pre testovanie
- **Requests** – HTTP klient pre posielanie API požiadaviek
- **JSON fixtures** – externý zdroj testovacích dát (data-driven testing)

Štruktúra projektu
requir_api_tests/
│
├── tests/
│ ├── test_get_users.py # Test scenár 1 – GET /users
│ ├── test_create_user.py # Test scenár 2 – POST /users (data-driven)
│
├── data/
│ └── users.json # Externé testovacie dáta pre POST test
│
├── requirements.txt # Python závislosti

**Inštalácia**
**terminal**
python -m venv venv

**Inštalácia závislostí**
pip install -r requirements.txt

**Spustenie všetkých testov:**
pytest -v  #(pytest tests/test_get_users.py.... -v,q)

 **Testovacie scenáre**

**GET – List Users**
Testuje endpoint:
GET https://reqres.in/api/users?page=2

**Overuje sa:**

- stavový kód odpovede (**200 OK**)  
- či existuje položka **total**
- priezviská prvého a druhého používateľa (**last_name**)
- či počet používateľov v poli **data** zodpovedá počtu **per_page**
- základné validácie dátových typov (voliteľné)

**POST – Create User (data-driven)**
Testuje endpoint:
POST https://reqres.in/api/users


Dáta pre test sú uložené v `data/users.json`.

**Overuje sa:**

- stavový kód odpovede (**201 CREATED**)  
- existencia poľa **id**
- existencia časovej pečiatky **createdAt**
- čas odozvy je menší ako stanovený limit (napr. 100 ms)

**Externé dáta – `users.json`**

```json
[
  { "name": "morpheus", "job": "leader" },
  { "name": "neo", "job": "the one" }
]

Každý záznam predstavuje jednu testovaciu sadu, ktorá spustí samostatný POST test.


