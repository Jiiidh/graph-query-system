import pandas as pd
import os
import glob
DATA_DIR = "graph-query-system/data"

def load_table(folder_name):
    folder_path = os.path.join(DATA_DIR, folder_name)
    files = glob.glob(os.path.join(folder_path, "*"))
    dfs = []
    for file in files:
        try:
            if file.endswith(".csv"):
                df = pd.read_csv(file)
            elif file.endswith(".json") or file.endswith(".jsonl"):
                df = pd.read_json(file, lines=True)
            elif file.endswith(".parquet"):
                df = pd.read_parquet(file)
            else:
                continue
            dfs.append(df)
        except:
            continue
    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()
def load_all_tables():
    tables = {}
    for folder in os.listdir(DATA_DIR):
        folder_path = os.path.join(DATA_DIR, folder)
        if os.path.isdir(folder_path):
            df = load_table(folder)
            if not df.empty:
                tables[folder] = df
    return tables
