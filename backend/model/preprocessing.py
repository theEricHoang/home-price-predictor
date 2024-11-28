import pandas as pd
import requests
from dotenv import load_dotenv
import os

# preprocess user data for use with model prediction
def preprocess_data(data: dict) -> pd.DataFrame:
    address = data['address']
    zipCode = address.split(' ')[-1]
    encodedAddress = address.replace(' ', '+')
    processedData = pd.DataFrame()

    load_dotenv()
    apiKey = os.getenv("GEOCODE_API_KEY")
    apiUrl = f'https://maps.googleapis.com/maps/api/geocode/json?address={encodedAddress}&key={apiKey}'
    response = requests.get(apiUrl)

    if response.status_code == 200:
        result = response.json()
        latitude = result['results'][0]['geometry']['location']['lat']
        longitude = result['results'][0]['geometry']['location']['lng']
        processedData = pd.DataFrame([{
            'zipCode': zipCode,
            'beds': data['beds'],
            'baths': data['baths'],
            'sqft': data['sqft'],
            'latitude': latitude,
            'longitude': longitude
        }])

    return processedData
