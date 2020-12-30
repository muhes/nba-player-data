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
        return player['id']
    except IndexError:
        print(full_name + 'not found')
        raise Exception(full_name + ' not found')

# this function grabs only the necesary stats (9 categories) for each player with the id
def __get9CatStats(player_name, type):
    p_id = __getPlayerId(player_name)
    p_gamelog = playergamelog.PlayerGameLog(player_id = p_id, season = '2020' )
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
    

def tradeEvaluator(team1_list, team2_list, type):
    #FINISH
    team1_df = []
    team2_df = []
    for player in team1_list:
        print('yio')
        if team1_df.empty:
            team1_df = __get9CatStats(player, type)
        else:
            p_df = __get9CatStats(player, type)
            team1_df = team1_df.add(p_df)
    for player in team2_list:
        if team2_df.empty:
            team2_df = __get9CatStats(player, type)
        else:
            p_df = __get9CatStats(player, type)
            team2_df = team1_df.add(p_df)
    return team1_df
        

        
    
    #returns totals for all players in trade
    return True
def booleanComparison(p1_9cat, p2_full_name):
    #adds comparison
    #return p1_9cat['comparison'] = np.where(p1_9cat[0] > p1_9cat[p2_full_name], 'True', 'False')
    return True
    

# this function compares 2 players from their full name and returns boolean values on whether 
# the first player is better than the second player in each category

def comparePlayers(p1_full_name, p2_full_name, type):
    #p1_id = __getPlayerId(p1_full_name)
    #p2_id = __getPlayerId(p2_full_name)
    p1_9cat = __get9CatStats(p1_full_name, type)
    print(p1_9cat)
    p2_9cat = __get9CatStats(p2_full_name, type)
    p1_9cat = p1_9cat.to_frame()
    p2_9cat = p2_9cat.to_frame()
    p1_9cat[p2_full_name] = p2_9cat[0]
    p1_9cat['Better Player'] = np.where(p1_9cat[0] > p1_9cat[p2_full_name], p1_full_name, p2_full_name)
    #p1_9cat.rename(index={0: p1_full_name})
    p1_9cat.columns = [p1_full_name if x==0 else x for x in p1_9cat.columns]
    return p1_9cat

ayton = __get9CatStats('Deandre Ayton', 'average')
buddy = __get9CatStats('Buddy Hield', 'average')

team2 = buddy.add(ayton)
#print(team2)
bron = __get9CatStats('LeBron James', 'average')
cap = __get9CatStats('Clint Capela', 'average')
team1 = bron.add(cap)
#print(team1)


    
    