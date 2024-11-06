import requests
import json
import csv

file = open('house_data.csv', mode='w', newline='', encoding='utf-8')
flatData = []
pg = 1
while pg <= 20:
    url = f"https://www.zillow.com/async-create-search-page-state"
    headers = {
        'authority': 'www.zillow.com',
        'method': 'PUT',
        'path': '/async-create-search-page-state',
        'scheme': 'https',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/json',
        'Origin': 'https://www.zillow.com',
        'Priority': 'u=1, i',
        'Referer': 'https://www.zillow.com/atlanta-ga/',
        'Sec-Ch-Ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    }
    payload = json.loads('{"searchQueryState":{"pagination":{"currentPage":'+f'{pg}'+'},"isMapVisible":false,"mapBounds":{"west":-84.68105020019532,"east":-84.20726479980469,"south":33.58815313610265,"north":33.960859253663784},"regionSelection":[{"regionId":37211,"regionType":6}],"filterState":{"sortSelection":{"value":"globalrelevanceex"}},"isListVisible":true,"mapZoom":11},"wants":{"cat1":["listResults"],"cat2":["total"]},"requestId":'+f'{pg}'+',"isDebugRequest":false}')

    response = requests.put(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()

        for house in data['cat1']['searchResults']['listResults']:
            if all(key in house for key in ['unformattedPrice', 'addressZipcode', 'beds', 'baths', 'area', 'latLong']):
                # Additional check for 'latitude' and 'longitude' inside 'latLong'
                latLong = house['latLong']
                if 'latitude' in latLong and 'longitude' in latLong:
                    flatHouse = {
                        'price': house['unformattedPrice'],
                        'zipCode': house['addressZipcode'],
                        'beds': house['beds'],
                        'baths': house['baths'],
                        'sqft': house['area'],
                        'latitude': latLong['latitude'],
                        'longitude': latLong['longitude']
                    }
                    flatData.append(flatHouse)
    else:
        print(f"Request failed with status code {response.status_code}")

    pg += 1

columns = flatData[0].keys()
writer = csv.DictWriter(file, fieldnames=columns)
writer.writeheader()
for house in flatData:
    writer.writerow(house)

file.close()