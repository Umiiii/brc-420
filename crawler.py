import requests

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en-SG;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'origin': 'https://brc420.io',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://brc420.io/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

params = {
    'page': '1',
    'limit': '20',
    'deploy_inscription_id': 'eafc2caf6775d5468f9f4af995eaffd4019eec48e0b396e8f047c1b4bbdd0253i0',
}

response = requests.get('https://api-1.brc420.io/api/v1/tokens/inscription', params=params, headers=headers)