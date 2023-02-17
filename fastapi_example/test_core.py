# Use a TestClient here

from fastapi.testclient import TestClient
# You import from your main app file
# This would normally be done where your app is in an app directory like app/main.py
# In this case you would say from app.main import xxx
from main_test import app1

client = TestClient(app1)

def test_root():
    resp = client.get("/")
    print("Resp code: %d" % resp.status_code)
    print("Text: %s" % resp.json())


