import requests
from ast import literal_eval

URL = "https://sdarot.dev"


def get_cookie():
    res = requests.get(URL)
    return res.headers["set-cookie"]


def get_token_for_cookie(cookie):
    url = URL + "/ajax/watch"

    headers = {
        "cookie": cookie,
        "Referer": URL
    }

    payload = {
        "preWatch": "true"
    }

    res = requests.request("POST", url, headers=headers, data=payload)

    return res.text


def get_episode_data(episode, token):
    url = URL + "/ajax/watch"

    headers = {
        "cookie": token.cookie,
        "Referer": URL + "/watch/"
    }

    payload = {
        "watch": "false",
        "token": token.token,
        "serie": episode.series_id,
        "season": episode.season,
        "episode": episode.episode,
        "type": "episode"
    }

    res = requests.request("POST", url, headers=headers, data=payload)
    data = literal_eval(res.text)

    if "VID" not in data:
        raise ConnectionError(f"Server not responded with right values: \n{data}")

    return data


def get_episode_url_from_data(data, episode):
    file_name = f'{data["VID"]}.mp4?token={list(data["watch"].values())[0]}&time={data["time"]}&uid={data["uid"]}'
    url = f'https://{data["url"]}/w/episode/{episode.series_id}/{list(data["watch"].keys())[0]}/{file_name}'

    return url


def get_series_id_by_name(name, cookie):
    headers = {
        "cookie": cookie,
        "Referer": URL + "/watch/"
    }

    found = requests.get(f'{URL}/ajax/index?search={name}', headers=headers).text

    return literal_eval(found)[0]["id"]


def download_episode(url, cookie, episode):
    res = requests.get(url, headers={"cookie": cookie}, allow_redirects=True)
    open(f'{episode.series_name}_SE{episode.season}EP{episode.episode}.mp4', "wb").write(res.content)
