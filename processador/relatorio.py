import pandas as pd

def calcular_saldo(df: pd.DataFrame) -> float:
    entradas = df[df["Tipo"] == "Entrada"]["Valor"].sum()
    saidas = df[df["Tipo"] == "Saída"]["Valor"].sum()
    return entradas - saidas

def gerar_relatorio(df: pd.DataFrame, saldo: float) -> pd.DataFrame:
    total_entradas = df[df["Tipo"] == "Entrada"]["Valor"].sum()
    total_saidas = df[df["Tipo"] == "Saída"]["Valor"].sum()
    
    resumo = pd.DataFrame([{
        "Total Entradas": total_entradas,
        "Total Saídas": total_saidas,
        "Saldo Final": saldo
    }])

    return resumo
