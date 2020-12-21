# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 22:45:35 2020

@author: muhes
"""
import pandas as pd

from nba_api.stats.static import players
player_dict = players.get_players()

bron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]
bron_id = bron['id']

from nba_api.stats.endpoints import playergamelog

gamelog_bron = playergamelog.PlayerGameLog(player_id = '2544', season = '2019')
gamelog_bron_df = gamelog_bron.get_data_frames()[0]