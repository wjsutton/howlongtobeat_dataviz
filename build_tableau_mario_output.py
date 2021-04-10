import pandas as pd
import numpy as np

# Load csv
mario_df = pd.read_csv('data\\fastest_mario.csv')
mario_df = mario_df[['game_id','game_name','game_image_url','Year','Release Date','gameplay_main','gameplay_main_unit','gameplay_main_label']]

mario_df['gameplay_main'] = mario_df['gameplay_main'].str.replace('½','.5')
mario_df['gameplay_main'] = mario_df['gameplay_main'].astype(float)

game_ids = mario_df['game_id']

for i in range(len(game_ids)):
    row = mario_df.loc[mario_df['game_id'] == game_ids[i]]
    row = row[['game_id','gameplay_main']]
    
    top_pipe = row
    top_pipe.columns = ['game_id','position']
    top_pipe['type'] = 'top_pipe' 

    tiles =[]

    

    for p in range(np.ceil(row['position'][i]).astype(int)):
        tiles.append(p) 

    tile_df = pd.DataFrame({'position':tiles})
    tile_df['type'] = 'tile'
    tile_df['game_id'] = row['game_id'][i]
    tile_df = tile_df[['game_id','position','type']]
    tile_df['position'] = tile_df['position'].astype(float)

    output_df = pd.concat([top_pipe,tile_df])
    
    if i == 0:
        layout_df = output_df
    else:
        layout_df = pd.concat([layout_df,output_df])

tableau_file = pd.merge(mario_df,layout_df, on = 'game_id', how = 'inner')
tableau_file.to_csv('data\\mario_35_anniversery_viz.csv', encoding="utf-8-sig", index=False)
