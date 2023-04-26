import pandas as pd
print("reading in pandas")
data= pd.read_csv("mergedClonePairs.csv", index_col = [0])
#data= pd.read_csv("mergedClonePairs.csv",)
print(data)
print("write pickle")
data.to_pickle("possiblePairs_ids_sample.pkl")
