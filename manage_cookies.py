import json


def save_cookies(response):
    cookies = response.request.headers.getlist("Cookie")
    cookies = cookies[0].decode("utf-8").split(' ')
    cookie_json = {}
    for cookie in cookies:
        split_cookie = cookie.split("=")
        name = split_cookie[0]
        value = split_cookie[1]
        if ';' in value:
            value = value.replace(';', '')
        cookie_json[name] = value

    with open("cookies.json", 'w') as write_file:
        json.dump(cookie_json, write_file)


def get_cookies():
    try:
        with open("cookies.json", 'r') as read_file:
            cookies = json.loads(read_file.read())
    except FileNotFoundError:
        cookies = {}
    return cookies
