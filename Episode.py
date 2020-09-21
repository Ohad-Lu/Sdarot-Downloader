class Episode:
    series_id = ""
    series_name = ""
    season = ""
    episode = ""

    def __init__(self, series_id, series_name, season, episode):
        self.series_id = series_id
        self.series_name = series_name
        self.season = season
        self.episode = episode
