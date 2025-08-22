# etl.py
import os
import pandas as pd
from datetime import datetime

RAW_DIR = "data/raw"
CLEAN_DIR = "data/clean"
os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(CLEAN_DIR, exist_ok=True)

def load_raw_data():
    frames = []
    for fname in os.listdir(RAW_DIR):
        if fname.endswith(".csv"):
            df = pd.read_csv(os.path.join(RAW_DIR, fname))
            df["__source_file"] = fname
            frames.append(df)
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df

def basic_validations(df: pd.DataFrame) -> pd.DataFrame:
    # ejemplo: elimina filas vacías en columna clave si existe
    key_cols = [c for c in df.columns if "id" in c or "nombre" in c]
    if key_cols:
        df = df.dropna(subset=[key_cols[0]])
    return df

def write_output(df: pd.DataFrame):
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = os.path.join(CLEAN_DIR, f"dataset_final_{ts}.csv")
    df.to_csv(out, index=False)
    print(f"Grabado: {out}")

def main():
    df = load_raw_data()
    if df.empty:
        print("No hay datos en data/raw. Coloca CSVs para procesar.")
        return
    df = normalize_columns(df)
    df = basic_validations(df)
    write_output(df)

if __name__ == "__main__":
    main()
