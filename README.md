#🧪 Projeto Prático: Grafo de Fluxo de Controle (CFG) e Teste de Caixa Branca

##📌 Objetivo
Desenvolver um Grafo de Fluxo de Controle (CFG) para o código que representa uma "operação de saque" contendo todos os nós necessários da operação e realizar o teste de Caixa Branca para avaliar o comportamento interno do sistema, testando lógica, fluxo de dados e caminhos de execução.

---

##📊 1. Mapeamento do Grafo de Fluxo de Controle (CFG)

O diagrama abaixo foi modelado utilizando a ferramenta *Visual Paradigm* (arquivo fonte disponível em [Diagrama_Fluxo_Controle.untitled.vpp](Atividade_Caixa_Branca/ASSETS/Diagrama_Fluxo_Controle.untitled.vpp)):

![Grafo de Fluxo de Controle da Função de Saque](Atividade_Caixa_Branca/ASSETS/Diagrama_Fluxo_Controle_OperacaoSaque%202026-11-11.png)

O grafo ilustra visualmente a estrutura de decisão e os caminhos descritos abaixo:
1. *Caminho 1 (Sucesso via Saldo):* O fluxo passa pelo IF, subtrai do saldo e vai direto para o final (retorna True).
2. *Caminho 2 (Sucesso via Limite):* O fluxo falha no IF, passa pelo ELIF, subtrai do limite e vai para o final (retorna True).
3. *Caminho 3 (Recusa Total):* O fluxo falha em ambas as validações e chega ao fim retornando False.

---

##💻 2. Código Desenvolvido ([atividade_caixaBranca.py](Atividade_Caixa_Branca/atividade_caixaBranca.py))

A função saque(valor, saldo, limite_credito) verifica inicialmente se o valor solicitado é menor ou igual ao saldo disponível. Caso não seja, verifica se a soma do saldo com o limite de crédito cobre o valor, zerando o saldo e descontando a diferença do limite.

---

##🔍 3. Testes de Caixa Branca (Caminhos e Valor Limite)

###✅ Caminho 1: Sucesso Via Saldo
* *Argumentos:* saldo = 1000, limite_credito = 500, valor = 900
* *Comportamento:* Como o valor do saque é menor que o saldo disponível, executa a primeira condicional if e retorna o sucesso da operação (True) com o saldo atualizado (R$ 100) e o limite intacto (R$ 500).

![Execução Caminho 1](Atividade_Caixa_Branca/ASSETS/Valor_Solicitado_Menor_Que_Saldo%202026-11-10.png)

###⚖️ Teste de Valor Limite (Caminho 1 — Fronteira valor == saldo)
* *Argumentos:* saldo = 1000, limite_credito = 500, valor = 1000
* *Comportamento:* Valida o limite exato da condição valor <= saldo. A operação é aprovada (status = True), o saldo é zerado (R$ 0) e o limite_credito permanece intacto (R$ 500).

![Execução Valor Limite](Atividade_Caixa_Branca/ASSETS/Valor_Solicitado_Igual_OSaldo%202026-11-10.png)

###💳 Caminho 2: Sucesso Via Limite
* *Argumentos:* saldo = 1000, limite_credito = 500, valor = 1200
* *Comportamento:* O valor do saque é maior que o saldo disponível, mas coberto pelo limite de crédito. Executa a segunda condicional elif, atualiza o saldo para 0 e debita a diferença (200) do limite de crédito, resultando em limite_credito = 300 e status = True.

![Execução Caminho 2](Atividade_Caixa_Branca/ASSETS/Valor_Solicitado_Maior_Saldo_Mas_No_Limite_Credito%202026-11-10.png)

###❌ Caminho 3: Recusa Total
* *Argumentos:* saldo = 1000, limite_credito = 500, valor = 1600
* *Comportamento:* O valor do saque ultrapassa tanto o saldo disponível quanto o limite de crédito. A função encerra com status = False e mantém o saldo (1000) e o limite_credito (500) sem alterações.

![Execução Caminho 3](Atividade_Caixa_Branca/ASSETS/Valor_Solicitado_Maior_Saldo_Maior_Limite%202026-11-10.png)

## 📁Estrutura de Arquivos

```text
Qualidade_Automação_Testes/
└── Atividade_Caixa_Branca/
    ├── ASSETS/
    │   ├── Código_Cru 2026-11-11.png
    │   ├── Diagrama_Fluxo_Controle_OperacaoSaque 2026-11-11.png
    │   ├── Diagrama_Fluxo_Controle.untitled.vpp
    │   ├── Valor_Solicitado_Igual_OSaldo 2026-11-10.png
    │   ├── Valor_Solicitado_Maior_Saldo_Maior_Limite 2026-11-10.png
    │   ├── Valor_Solicitado_Maior_Saldo_Mas_No Limite_Credito 2026-11-10.png
    │   └── Valor_Solicitado_Menor_Que_Saldo 2026-11-10.png
    ├── atividade_caixaBranca.py
    └── README.md
```
   

## 🧑‍💻 Autor

Desenvolvido por *sergio-santosjr*

🔗 [GitHub](https://github.com/sergio-santosjr/Teste_Caixa_Branca_Opera-o_Saque)

 ---