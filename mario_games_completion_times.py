# Howlongtobeat Custom Class
# Details available here:
# https://github.com/ScrappyCocco/HowLongToBeat-PythonAPI/blob/master/howlongtobeatpy/howlongtobeatpy/HowLongToBeatEntry.py

from howlongtobeatpy import HowLongToBeat
import pandas as pd

def get_game_data(id):
    result = HowLongToBeat().search_from_id(id)
    columns = ['game_id','game_name','game_image_url','game_web_link','gameplay_main','gameplay_main_unit','gameplay_main_label',
    'gameplay_main_extra','gameplay_main_extra_unit','gameplay_main_extra_label','gameplay_completionist','gameplay_completionist_unit','gameplay_completionist_label']

    rows = [[result.game_id,result.game_name,result.game_image_url,result.game_web_link,result.gameplay_main,result.gameplay_main_unit,result.gameplay_main_label,
    result.gameplay_main_extra,result.gameplay_main_extra_unit,result.gameplay_main_extra_label,result.gameplay_completionist,result.gameplay_completionist_unit,result.gameplay_completionist_label]]

    df = pd.DataFrame(rows, columns = columns)
    return df


# Load csv
games = pd.read_csv('data\\mario_games.csv')

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

output_df.to_csv('data\\fastest_mario.csv', encoding="utf-8-sig", index=False)

