# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 22:45:35 2020

@author: muhes
"""
import pandas as pd
import numpy as np

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

# this function grabs only the necesary stats (9 categories) for each player with the id
def get9CatStats(id):
    p_gamelog = playergamelog.PlayerGameLog(player_id = id, season = '2019')
    p_df = p_gamelog.get_data_frames()[0]
    # this line extract all of the necessary counting stats from the sum
    p_9cat = p_df[['PTS', 'STL', 'AST', 'BLK', 'REB', 'TOV', 'FG3M']].sum()
    # these lines get percentages
    p_9cat['FG%'] = (p_df['FGM'].sum())/(p_df['FGA'].sum())
    p_9cat['3P%'] = (p_df['FG3M'].sum())/(p_df['FG3A'].sum())
    return p_9cat

# this function compares 2 players from their full name and returns boolean values on whether 
# the first player is better than the second player in each category
def comparePlayers(p1_full_name, p2_full_name):
    p1_id = getPlayerId(p1_full_name)
    p2_id = getPlayerId(p2_full_name)
    p1_9cat = get9CatStats(p1_id)
    p2_9cat = get9CatStats(p2_id)
    p1_9cat = p1_9cat.to_frame()
    p2_9cat = p2_9cat.to_frame()
    p1_9cat['p2'] = p2_9cat[0]
    p1_9cat['comparison'] = np.where(p1_9cat[0] > p1_9cat['p2'], 'True', 'False')
    return p1_9cat



    
    