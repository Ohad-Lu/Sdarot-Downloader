from sdarotApi import *

def getChosenEpisode(cookie):
    return {
            "series_id": getSeriesIdByName("taagad", cookie),
            "series_name": "taagad",
            "se": "2", 
            "ep": "43"
           }


def chooseDownload(url, cookie, chosen):
    download = input("Download?: (yes/no) ")
    if download == "yes":
        downloadEpisode(url, cookie, chosen)


def main():
    c = getCookie()
    t = getTokenFromCookie(c)
    chosen = getChosenEpisode(c)
    ep_data = getEpisodeData(chosen, t, c)
    url = getEpisodeUrlFromData(ep_data, chosen)
    print(url, c)

    chooseDownload(url, c, chosen)


main()
