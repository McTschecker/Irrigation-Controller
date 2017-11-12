def update(temperature, humidity, moisture):
    channel_id = "337034"
    write_key  = "PDCMJ7FI8E3GRKS5"
    import requests
    url = "https://api.thingspeak.com/update?api_key="+ write_key + "&field1=" + str(temperature) + "&field2=" + str(humidity) + "&field3=" + str(moisture)
    r = requests.get(url)

