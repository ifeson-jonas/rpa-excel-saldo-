from processador.leitor import ler_planilha
from processador.relatorio import calcular_saldo, gerar_relatorio

def main():
    df = ler_planilha("dados/entradas.xlsx")
    if df.empty:
        print("⚠️ Planilha vazia ou erro na leitura.")
        return

    saldo = calcular_saldo(df)
    relatorio = gerar_relatorio(df, saldo)

    relatorio.to_excel("saidas/relatorio_saldo.xlsx", index=False)
    print("✅ Relatório de saldo gerado com sucesso!")

if __name__ == "__main__":
    main()

