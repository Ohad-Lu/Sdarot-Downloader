import requests
from ast import literal_eval
from time import sleep

URL = "https://sdarot.dev"

def getCookie():
    res = requests.get(URL)
    return res.headers["set-cookie"]


def getTokenFromCookie(cookie):
    url = URL + "/ajax/watch"

    headers = {
        "cookie": cookie,
        "Referer": URL
    }

    payload = {
        "preWatch" : "true"
    }

    res = requests.request("POST", url, headers=headers, data=payload)

    return res.text


def getEpisodeData(chosen, token, cookie):
    url = URL + "/ajax/watch"

    headers = {
        "cookie": cookie,
        "Referer": URL + "/watch/"
    }

    payload = {
        "watch": "false",
        "token": token,
        "serie": chosen["series_id"],
        "season": chosen["se"],
        "episode": chosen["ep"],
        "type": "episode"
    }
    

    data = {}
    while "VID" not in data:
        res = requests.request("POST", url, headers=headers, data=payload)
        data = literal_eval(res.text)
        print(data)
        if "error" in data:
            if "status" in data["error"]:
                payload["token"] = getTokenFromCookie(cookie)
        
        sleep(5)
    
    return data


def getEpisodeUrlFromData(data, chosen):
    file_name = f'{data["VID"]}.mp4?token={list(data["watch"].values())[0]}&time={data["time"]}&uid={data["uid"]}'
    url = f'https://{data["url"]}/w/episode/{chosen["series_id"]}/{list(data["watch"].keys())[0]}/{file_name}'

    return url


def getSeriesIdByName(name, cookie):
    headers = {
        "cookie": cookie,
        "Referer": URL + "/watch/"
    }

    found = requests.get(f'{URL}/ajax/index?search={name}', headers=headers).text

    return literal_eval(found)[0]["id"]

def downloadEpisode(url, cookie, chosen):
    res = requests.get(url, headers={"cookie": cookie}, allow_redirects=True)
    open(f'{chosen["series_name"]}_SE{chosen["se"]}EP{chosen["ep"]}.mp4', "wb").write(res.content)
