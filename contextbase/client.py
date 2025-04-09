import requests

class ContextBase:
    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def set_token(self, token):
        self.token = token

    def _auth_headers(self):
        return {"Authorization": f"Bearer {self.token}"} if self.token else {}

    def signup(self, email, password):
        res = requests.post(f"{self.base_url}/api/auth/signup", json={
            "email": email,
            "password": password
        })
        res.raise_for_status()
        self.token = res.json()["token"]
        return self.token

    def login(self, email, password):
        res = requests.post(f"{self.base_url}/api/auth/login", json={
            "email": email,
            "password": password
        })
        res.raise_for_status()
        self.token = res.json()["token"]
        return self.token

    def set(self, key, value, ttl=86400):
        res = requests.post(f"{self.base_url}/api/memory", headers=self._auth_headers(), json={
            "key": key,
            "value": value,
            "ttl": ttl
        })
        res.raise_for_status()
        return res.json()

    def get(self, key):
        res = requests.get(f"{self.base_url}/api/memory/{key}", headers=self._auth_headers())
        res.raise_for_status()
        return res.json()

    def delete(self, key):
        # Using the POST workaround like TS SDK
        res = requests.post(f"{self.base_url}/api/memory/delete", headers=self._auth_headers(), json={
            "key": key
        })
        res.raise_for_status()
        return res.json()

    def list(self):
        res = requests.get(f"{self.base_url}/api/memory", headers=self._auth_headers())
        res.raise_for_status()
        return res.json()

    def search(self, query):
        res = requests.get(f"{self.base_url}/api/memory/search/{query}", headers=self._auth_headers())
        res.raise_for_status()
        return res.json()
