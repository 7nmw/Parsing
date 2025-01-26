import requests


def fetch(url, params):
    headers = params['headers']
    body = params['body']
    if params['method'] == 'GET':
        return requests.get(url, headers=headers)
    if params['method'] == 'POST':
        return requests.post(url, headers=headers, data=body)


audi = fetch("https://auto.ru/kazan/cars/audi/all/", {
  "headers": {
    "accept": "application/json",
    "accept-language": "ru,ru-RU;q=0.9,en;q=0.8",
    "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-csrf-token": "23f595f970094c1617a231c7ab976e11f5cabe8418bc3f77",
    "x-kl-ajax-request": "Ajax_Request",
    "x-requested-with": "XMLHttpRequest",
    "x-susanin-react": "true",
    "cookie": "gdpr=0; _ym_uid=1681571775341159390; _ym_isad=1; suid=bc1b0c055a187640d3059e89eb3b0d4c.a4b3e8b8b332cbf66869ea9257aa6321; _csrf_token=23f595f970094c1617a231c7ab976e11f5cabe8418bc3f77; autoru_sid=a%3Ag643abfd52jtogoas7fjnl0i10ri2bti.4c2dfe2b60a15761fcaf2332b491d16c%7C1681571797661.604800.XjxN8dA-FARGJcMji6RJvw.ZqBwb9v-w_fbn6N0t7WpzwQE_aflFBrkSdbHlaYc3KA; autoruuid=g643abfd52jtogoas7fjnl0i10ri2bti.4c2dfe2b60a15761fcaf2332b491d16c; counter_ga_all7=1; yuidlt=1; yandexuid=6274492841668105617; crookie=viPsqOPsKGxIUX0NlqYo/hGxtXxRqUXcKNM6xszVarJMl922VOi+qYMD68+7HmZUsGuObwhi+sEIjq+7oHyu3lV7GxQ=; cmtchd=MTY4MTU3MTc5OTQyMw==; Session_id=3:1681571800.5.0.1668341631109:exXqvA:49.1.2:1|157076788.12806464.2.2:12806464.3:1681148095|1570172113.956583.2.2:956583|1717937252.1139926.2.2:1139926|61:10012500.883527.jiMQwIWB5kwgSTvhnFvFuotrEhE; yandex_login=slevindin; ys=udn.cDpzbGV2aW5kaW4%3D#c_chck.3603296978; i=U1IJ96atpjiFSkCdkcWBMqmgKvGCR0NuS3vuSiZM+8U4Z7R2xCiVH6IM7oCxupMi/l/KzkBD88QYrRaGMPtjck0SJok=; mda2_beacon=1681571800540; sso_status=sso.passport.yandex.ru:synchronized; popups-popup-pdd-spring-shown-count=1; from=direct; _yasc=F6PoSYT6uwLn4bnkE2bv/k2eh63naFKzF31T7U4w3ZcQQzDqpJu5kUa6UDXsaA==; autoru-visits-count=1; autoru-visits-session-unexpired=1; los=1; bltsr=1; coockoos=4; _ym_visorc=b; spravka=dD0xNjgxNTc1MzQ0O2k9MTg4LjIzNC4zMC4xMDk7RD0zNEMzRTNDMTE3NjI5RUI4NDQyRUQ2OUFGQjUxREIxNUZBQUE5RDA1QjM2MTEzNjdGQUI1QUQ4QkVDNUVGMTY0N0NCQzgyNkQ0NEE1RkM7dT0xNjgxNTc1MzQ0Mjg0NTIzOTY3O2g9YjYyZGMxYmZlNjFkOTAxZTQwNDBjNGFmYTAxOWNkYjA=; _ym_d=1681575344; count-visits=12; from_lifetime=1681575347078; layout-config={\"screen_height\":1080,\"screen_width\":1920,\"win_width\":1065,\"win_height\":937}",
    "Referer": "https://auto.ru/",
    "Referrer-Policy": "no-referrer-when-downgrade"
  },
  "body": None,
  "method": "GET"
})

print(audi.status_code)
print(audi.json().keys())


cars = audi.json()["listing"]["offers"]  # Список машин
[print(car['vehicle_info']['tech_param']['human_name']) for car in cars]