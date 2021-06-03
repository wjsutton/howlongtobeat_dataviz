from howlongtobeatpy import HowLongToBeat
import pandas as pd

# Providing search term phrases
search_terms = ['Witcher','Far Cry','Halo']

# Fetching all HLTB search results for multiple search phrases
all_results = []

for i in range(len(search_terms)):
    results = HowLongToBeat().search(search_terms[i])

    all_results += results

# Removing depulicates
all_results = list(set(all_results))

# Extracting HLTB completion time data
for i in range(len(all_results)):
    a = all_results[i].__dict__
    entry_df = pd.DataFrame([a])

    if i == 0:
        hltb_df = entry_df
    else:
        hltb_df = pd.concat([hltb_df,entry_df])

# Print results
print(hltb_df)
    

# List of Xbox Games with some metadata:
# https://www.xbox.com/en-gb/games/all-games?cat=all


# List of MS Big-Ids
# https://reco-public.rec.mp.microsoft.com/channels/Reco/V8.0/Lists/Computed/New?Market=gb&Language=en&ItemTypes=Game&deviceFamily=Windows.Xbox&count=2000&skipitems=800

# One bigId output, more can be added comma seperated
# https://displaycatalog.mp.microsoft.com/v7.0/products?bigIds=BRPVTJKWHBR7&market=GB&languages=en-gb&MS-CV=DGU1mcuYo0WMMp+F.1