import json
import requests
from texttospeech import texttospeech
url = 'https://manhict.tech/xsmb'
result = requests.get(url)
x = result.json()
data = x["data"]
print(data)
texttospeech(data)