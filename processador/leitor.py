import pandas as pd

def ler_planilha(caminho: str) -> pd.DataFrame:
    try:
        df = pd.read_excel(caminho)
        return df
    except Exception as e:
        print(f"❌ Erro ao ler planilha: {e}")
        return pd.DataFrame()
