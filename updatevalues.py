def update(temperature, humidity, moisture,channe_id, write_key):
    import requests #import the lib for requests
    url = "https://api.thingspeak.com/update?api_key="+ write_key + "&field1=" + str(temperature) + "&field2=" + str(humidity) + "&field3=" + str(moisture) #build the URL
    r = requests.get(url) #open the url
