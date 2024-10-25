import requests
from PIL import Image
from io import BytesIO

WEATHER_API_KEY = '9c9b46711ffc5930547a7e8a82bd084b'
IMAGE_API_KEY = 'ptOiEf2rqn144-_oYNmP78mEj9Ji1hENqoKc_sekQS0'

def get_weather(city):

    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    