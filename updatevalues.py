def update(temperature, humidity, moisture,channe_id, write_key):
    import requests
    url = "https://api.thingspeak.com/update?api_key="+ write_key + "&field1=" + str(temperature) + "&field2=" + str(humidity) + "&field3=" + str(moisture)
    r = requests.get(url)

