# Howlongtobeat Custom Class
# Details available here:
# https://github.com/ScrappyCocco/HowLongToBeat-PythonAPI/blob/master/howlongtobeatpy/howlongtobeatpy/HowLongToBeatEntry.py

from howlongtobeatpy import HowLongToBeat

#results = HowLongToBeat().search("Super Mario Bros.")
result = HowLongToBeat().search_from_id(9371)
print(result.game_id)
print(result.game_name)
