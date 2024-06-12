import requests as req
from alive_progress import alive_it
from openai import OpenAI
import time

client = OpenAI()

token = "sess-m2uhk1f5jJz3aNkjhXM3IsWH2SpqvcBoQqwl39hG"
org = "org-kxjIPtXQTT8EpQGi4gDCBrbt"
url = "https://api.openai.com/v1/threads"

headers = {
    "authorization": f"Bearer {token}", 
    "openai-organization": org,
    "OpenAI-Beta": "assistants=v2"
}
params = {"limit": 20}
resp = req.get(url, headers=headers, params=params)
print(resp.json())
ids = [t['id'] for t in resp.json()['data']]

while len(ids) > 0:
    for tid in alive_it(ids, force_tty=True):
        if tid == "thread_u5It3UjSY9jtKUnMM43R14c2":
            continue
        client.beta.threads.delete(tid)
        time.sleep(1)
    resp = req.get(url, headers=headers, params=params)
    ids = [t['id'] for t in resp.json()['data']]