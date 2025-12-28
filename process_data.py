import pandas as pd
from pathlib import Path

data_folder = Path("data") 

csv_file = data_folder.glob("*.csv")

dataFrames = []

for file in csv_file:
    df = pd.read_csv(file)
    
    df = df[df["product"]=="Pink Morsel"]
    
    df["sales"] = df["price"]*df["quantity"]
    
    df = df[["sales", "date", "region"]]
    
    dataFrames.append(df)
    
final_df = pd.concat(dataFrames, ignore_index=True)
final_df.to_csv(data_folder / "pink_morsel_sales.csv", index=False)

print("✅ Data processing complete. Output saved as pink_morsels_sales.csv")