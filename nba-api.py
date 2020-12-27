# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 22:45:35 2020

@author: muhes
"""
import pandas as pd
import numpy as np

from nba_api.stats.static import players
player_dict = players.get_players()

from nba_api.stats.endpoints import playergamelog

def __getPlayerId(full_name):
    player = [player for player in player_dict if player['full_name'] == full_name][0]
    return player['id']

# this function grabs only the necesary stats (9 categories) for each player with the id
def __get9CatStats(id, type):
    p_gamelog = playergamelog.PlayerGameLog(player_id = id, season = '2019')
    p_df = p_gamelog.get_data_frames()[0]
    if type == 'total':
    # this line extract all of the necessary counting stats from the sum
        p_9cat = p_df[['PTS', 'STL', 'AST', 'BLK', 'REB', 'TOV', 'FG3M']].sum()
    if type == 'average':
        # this line gets the average of all counting stats
        p_9cat = p_df[['PTS', 'STL', 'AST', 'BLK', 'REB', 'TOV', 'FG3M']].mean()
    # these lines get percentages
    p_9cat['FG%'] = (p_df['FGM'].sum())/(p_df['FGA'].sum())
    p_9cat['3P%'] = (p_df['FG3M'].sum())/(p_df['FG3A'].sum())
    p_9cat['GP'] = len(p_df)
    return p_9cat

def __totalToAvgStats(stats):
    return True
    

# this function compares 2 players from their full name and returns boolean values on whether 
# the first player is better than the second player in each category
def comparePlayers(p1_full_name, p2_full_name, type):
    p1_id = __getPlayerId(p1_full_name)
    p2_id = __getPlayerId(p2_full_name)
    p1_9cat = __get9CatStats(p1_id, type)
    print(p1_9cat)
    p2_9cat = __get9CatStats(p2_id, type)
    p1_9cat = p1_9cat.to_frame()
    p2_9cat = p2_9cat.to_frame()
    p1_9cat[p2_full_name] = p2_9cat[0]
    p1_9cat['comparison'] = np.where(p1_9cat[0] > p1_9cat[p2_full_name], 'True', 'False')
    return p1_9cat



    
    