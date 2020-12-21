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
sum = gamelog_bron_df.sum()

def getPlayerId(full_name):
    player = [player for player in player_dict if player['full_name'] == full_name][0]
    return player['id']

def comparePlayers(p1_full_name, p2_full_name):
    p1_id = getPlayerId(p1_full_name)
    p2_id = getPlayerId(p2_full_name)
    p1_gamelog = playergamelog.PlayerGameLog(player_id = p1_id, season = '2019')
    p1_df = p1_gamelog.get_data_frames()[0]
    p2_gamelog = playergamelog.PlayerGameLog(player_id = p2_id, season = '2019')
    p2_df = p2_gamelog.get_data_frames()[0]
    p1_sum = p1_df.sum()
    p2_sum = p2_df.sum()
    return p2_sum['PTS']


    
    