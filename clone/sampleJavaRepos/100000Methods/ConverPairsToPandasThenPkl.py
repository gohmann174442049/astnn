import pandas as pd

data= pd.read_csv("possiblePairs.csv")
data.to_pickle("possiblePairs_ids.pkl")
