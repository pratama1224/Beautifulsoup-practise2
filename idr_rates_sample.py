# json_data = requests.get('http://www.floatrates.com/daily/idr.json')

json_data = {
    "usd": {"code": "USD", "alphaCode": "USD", "numericCode": "840", "name": "U.S. Dollar", "rate": 7.0840686024829e-5,
            "date": "Wed, 24 Feb 2021 12:00:01 GMT", "inverseRate": 14116.181760994},
    "eur": {"code": "EUR", "alphaCode": "EUR", "numericCode": "978", "name": "Euro", "rate": 5.8300287927229e-5,
            "date": "Wed, 24 Feb 2021 12:00:01 GMT", "inverseRate": 17152.573950376}}

for data in json_data.values():
    print(data['name'])
    print(data['code'])
    print(data['date'])
    print(data['inverseRate'])
