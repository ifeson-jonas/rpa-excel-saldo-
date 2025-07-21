# 🤖 RPA Excel Saldo

Automação desenvolvida em Python para leitura, processamento e geração de planilhas Excel, com foco em tarefas administrativas repetitivas.

## 📌 Objetivo

O projeto tem como finalidade automatizar a rotina de conferência e organização de dados em planilhas Excel, reduzindo erros manuais e aumentando a produtividade em processos administrativos.

## ⚙️ Funcionalidades

- 📥 Lê automaticamente a planilha de entradas: \`dados/entradas.xlsx\`
- 🔍 Processa os dados (saldos, categorias, valores, etc.)
- 📤 Gera uma nova planilha de saída organizada: \`saidas/resultado.xlsx\`
- 📁 Estrutura de pastas organizada e fácil de manter
- 🧩 Modularizado para facilitar manutenção e expansão

## 🗂️ Estrutura de Pastas

rpa_excel_saldo/
│
├── dados/ # Planilhas de entrada
│ └── entradas.xlsx
│
├── saidas/ # Planilhas geradas
│ └── resultado.xlsx
│
├── processador/ # Funções auxiliares para processamento
│ └── leitor.py
│
├── main.py # Script principal de execução
├── cria_planilha.py # Gera planilha de entrada (opcional)
├── requirements.txt # Dependências do projeto
└── README.md # Documentação

## 🚀 Como Executar

### 1. Clone o repositório

\`\`\`bash
git clone https://github.com/seu-usuario/rpa_excel_saldo.git
cd rpa_excel_saldo
\`\`\`

### 2. Crie e ative o ambiente virtual

\`\`\`bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
\`\`\`

### 3. Instale as dependências

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. (Opcional) Gere a planilha de entrada

\`\`\`bash
python cria_planilha.py
\`\`\`

### 5. Execute o script principal

\`\`\`bash
python main.py
\`\`\`

