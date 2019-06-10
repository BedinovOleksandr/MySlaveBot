import requests
url = 'https://booking.uz.gov.ua/train_search/'
r = requests.post(url,  data={'from': 2200001, 'to': 2218000, 'date': '2019-06-11', 'time': '00:00'})
print(r.status_code, r.reason)
response = r.json()
print(response)