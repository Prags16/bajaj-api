
# BFHL Flask Starter

## Edit your details
Open `app.py` and change:
```python
FULL_NAME = "john_doe"
DOB_DDMMYYYY = "17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"
```

## Run locally
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
# source venv/bin/activate

pip install -r requirements.txt
python app.py
```
Test:
```bash
curl -X POST http://127.0.0.1:5000/bfhl -H "Content-Type: application/json" -d "{"data":["a","1","334","4","R","$"]}"
```

## Deploy on Render
- Create a new Web Service from your GitHub repo.
- Set **Start Command** to:
```
gunicorn app:app --bind 0.0.0.0:$PORT
```
- Your endpoint will look like: `https://<appname>.onrender.com/bfhl`
