import requests


def get_address_info(ip_address=None):
    try:
        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url)
        data = response.json()

        # Extract relevant information
        ip = data.get('ip', '')
        city = data.get('city', '')
        region = data.get('region', '')
        country = data.get('country', '')
        location = data.get('loc', '').split(',')

        return {
            'ip': ip,
            'city': city,
            'region': region,
            'country': country,
            'latitude': location[0],
            'longitude': location[1],
        }

    except requests.RequestException as e:
        return {}

