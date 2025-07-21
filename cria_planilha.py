import pandas as pd

dados = {
    "Data": ["2025-07-01", "2025-07-02", "2025-07-03", "2025-07-03"],
    "Tipo": ["Entrada", "Saída", "Entrada", "Saída"],
    "Valor": [1500, 300, 500, 200]
}

df = pd.DataFrame(dados)
df.to_excel("dados/entradas.xlsx", index=False)

print("✅ Planilha criada!")
