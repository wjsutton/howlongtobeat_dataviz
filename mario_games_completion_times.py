# Howlongtobeat Custom Class
# Details available here:
# https://github.com/ScrappyCocco/HowLongToBeat-PythonAPI/blob/master/howlongtobeatpy/howlongtobeatpy/HowLongToBeatEntry.py

from howlongtobeatpy import HowLongToBeat
import pandas as pd

def get_game_data(id):
    result = HowLongToBeat().search_from_id(id)
    a = result.__dict__
    df = pd.DataFrame([a])
    return df


# Load csv
games = pd.read_csv('data\\mario_games_v2.csv')

mario_game_ids = games['ID']

for i in range(len(mario_game_ids)):
    print(i)
    print(mario_game_ids[i])

    df = check = get_game_data(mario_game_ids[i])

    if i == 0:
        output_df = df
    else:
        output_df = pd.concat([output_df,df])
    

print(output_df)

output_df.game_id = output_df.game_id.astype(int)
games.ID = games.ID.astype(int)

output_df = pd.merge(output_df, games, left_on='game_id', right_on='ID', how='inner')

# replace halves with 0.5s
output_df = output_df.replace('½','.5', regex=True)

output_df.to_csv('data\\fastest_mario.csv', encoding="utf-8-sig", index=False)

