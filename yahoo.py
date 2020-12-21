import nba_api

from nba_api.stats.endpoints import commonplayerinfo

custom_headers = {
    'Host': 'stats.nba.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://stats.nba.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true'
}

player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544, headers=custom_headers, timeout=100)
df = player_info.available_seasons.get_data_frame()

from nba_api.stats.static import players
players.find_players_by_first_name('lebron')

print(player_info.common_player_info.get_json)
print(df)