# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 22:45:35 2020

@author: Muhes Ariyaratnam
"""
import pandas as pd
import numpy as np

from nba_api.stats.static import players
player_dict = players.get_players()

from nba_api.stats.endpoints import playergamelog

def __getPlayerId(full_name):
    player = [player for player in player_dict if player['full_name'] == full_name]
    try:
        player = player[0]
        print(player['id'])
        return player['id']
    except IndexError:
        print(full_name + 'not found')
        raise Exception(full_name + ' not found')

# this function grabs only the necesary stats (9 categories) for each player with the id
def __get9CatStats(player_name, type, season):
    p_id = __getPlayerId(player_name)
    p_gamelog = playergamelog.PlayerGameLog(player_id = p_id, season = season )
    p_df = p_gamelog.get_data_frames()[0]
    if type == 'total':
    # this line extract all of the necessary counting stats from the sum
        p_9cat = p_df[['PTS', 'STL', 'AST', 'BLK', 'REB', 'TOV', 'FG3M']].sum()
    if type == 'average':
        # this line gets the average of all counting stats
        p_9cat = p_df[['PTS', 'STL', 'AST', 'BLK', 'REB', 'TOV', 'FG3M']].mean()
    # these lines get percentages
    p_9cat['FG%'] = (p_df['FGM'].sum())/(p_df['FGA'].sum())
    p_9cat['FT%'] = (p_df['FTM'].sum())/(p_df['FTA'].sum())
    p_9cat['GP'] = len(p_df)
    return p_9cat

def playerDifferentials(p1_full_name, p2_full_name, type):
    #returns the difference in each category between 2 players
    return True

def __addPlayerToList(player):
        player_id = __getPlayerId(player)
        player_9cat = __get9CatStats(player_id, type)
        team_df[player] = player_9cat
    

def tradeEvaluator(team1_list, team2_list, type, season):
    iteration = 0
    for player in team1_list:
        if iteration == 0:
            team1 = __get9CatStats(player, type, season)
        else:
            p_df = __get9CatStats(player, type, season)
            team1 = team1.add(p_df)
        iteration+= 1
    iteration = 0
    for player in team2_list:
         if iteration == 0:
            team2 = __get9CatStats(player, type, season)
         else:
            p_df = __get9CatStats(player, type, season)
            team2 = team2.add(p_df)
         iteration+= 1
    #create combined dataframe
    combine_df = team1.to_frame()
    combine_df['Team 2'] = team2.to_frame()
    #rename column to team 1
    combine_df.columns = ['Team 1' if x==0 else x for x in combine_df.columns]
    return combine_df

    
    #returns totals for all players in trade
    return True
def booleanComparison(p1_9cat, p2_full_name):
    #adds comparison
    #return p1_9cat['comparison'] = np.where(p1_9cat[0] > p1_9cat[p2_full_name], 'True', 'False')
    return True
    

# this function compares 2 players from their full name and returns boolean values on whether 
# the first player is better than the second player in each category

def comparePlayers(p1_full_name, p2_full_name, type, season):
    p1_9cat = __get9CatStats(p1_full_name, type, season)
    p2_9cat = __get9CatStats(p2_full_name, type, season)
    p1_9cat = p1_9cat.to_frame()
    p2_9cat = p2_9cat.to_frame()
    #combine stats
    p1_9cat[p2_full_name] = p2_9cat[0]
    p1_9cat['Better Player'] = np.where(p1_9cat[0] > p1_9cat[p2_full_name], p1_full_name, p2_full_name)
    #p1_9cat.rename(index={0: p1_full_name})
    #rename column to player name
    p1_9cat.columns = [p1_full_name if x==0 else x for x in p1_9cat.columns]
    return p1_9cat



    
    