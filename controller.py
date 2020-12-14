from flask import Flask, Response
import sdarotApi
from TokenPool import TokenPool
from time import sleep
from Episode import Episode

app = Flask(__name__)
token_pool = TokenPool(5)
print(1)


@app.route('/getSeriesIdByName/<name>')
def get_series_id_by_name(name):
    return sdarotApi.get_series_id_by_name(name, sdarotApi.get_cookie())


@app.route('/getEpisode/<series_id>/<season>/<episode>')
def get_episode(series_id, season, episode):
    res = ""

    while res == "":
        t = token_pool.get_token()
        e = Episode(series_id, "", season, episode)
        try:
            res = sdarotApi.get_episode_data(e, t)

        except ConnectionError:
            print("Token error")
            pass

        else:
            return {
                "url": sdarotApi.get_episode_url_from_data(res, e),
                "cookie": t.cookie
            }


if __name__ == "__main__":
    sleep(30)
    app.run(host='0.0.0.0', port=5000, debug=True)
