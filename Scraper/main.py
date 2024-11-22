import requests
import json
import csv
import time
import random

file = open('house_data3.csv', mode='w', newline='', encoding='utf-8')
columns = ['price', 'zipCode', 'beds', 'baths', 'sqft', 'latitude', 'longitude']
writer = csv.DictWriter(file, fieldnames=columns)
writer.writeheader()

#70789, 70809, 70829, 70850, 70890, 70904, 70976, 70988, 71000, 71024
for regionID in range(71024, 71080):
    print('new region')
    flatData = []
    pg = 1
    duplicate = False
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
            'Referer': 'https://www.zillow.com/ga/',
            'Cookie': '', # REPLACE COOKIE
            'Sec-Ch-Ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            #'User-Agent': user_agents[pg%3]
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
        }
        payload = json.loads('{"searchQueryState":{"pagination":{"currentPage":'+f'{pg}'+'},"isMapVisible":false,"mapBounds":{"west":-84.626815,"east":-84.111976,"south":33.429345,"north":34.11682189460908},"regionSelection":[{"regionId":'+f'{regionID}'+',"regionType":7}],"filterState":{"sortSelection":{"value":"globalrelevanceex"}},"isListVisible":true,"mapZoom":13},"wants":{"cat1":["listResults"],"cat2":["total"]},"requestId":'+f'2'+',"isDebugRequest":false}')

        time.sleep(random.randint(1,5))
        response = requests.put(url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            print(f'visited {pg}')
            print(data['searchPageSeoObject']['baseUrl'])

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
                        if flatHouse in flatData:
                            duplicate = True
                            break
                        flatData.append(flatHouse)
            if duplicate:
                break
            lastPage = data
        else:
            print(f"Request failed with status code {response.status_code}")
            print(f'stopped at {regionID}')
            break

        pg += 1

    for house in flatData:
        writer.writerow(house)
    flatData.clear()

file.close()