from sdarotApi import download_episode, get_episode_url_from_data, get_episode_data
from Episode import Episode
from time import sleep
from TokenPool import TokenPool


def get_episode_from_user():
    return Episode("2513", "taagad", "2", "43")


def download_promt(url, cookie, chosen):
    download = input("Download?: (yes/no) ")
    if download == "yes":
        download_episode(url, cookie, chosen)


def main():
    print("Generating pool")
    token_pool = TokenPool(5)

    print("Getting Episode")
    episode = get_episode_from_user()

    print("Sleeping 30")
    sleep(30)

    while True:
        token = token_pool.get_token()

        try:
            ep_data = get_episode_data(episode, token)

        except ConnectionError as e:
            print(f"Error {e}")

        else:
            url = get_episode_url_from_data(ep_data, episode)
            print(url, token.cookie)
            break


main()
