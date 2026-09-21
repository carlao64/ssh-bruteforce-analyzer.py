# Analisador de Logs SSHD

Script em Python para analisar logs de autenticação do **SSH (SSHD)** e identificar possíveis tentativas de invasão, incluindo ataques de **força bruta (Brute Force)**.

O projeto automatiza a leitura do arquivo `auth.log`, filtra tentativas de autenticação que falharam e gera um resumo dos endereços IP com maior número de falhas.

## O que o projeto faz

### Filtra falhas de login

Utiliza **Regex (`re`)** para localizar linhas contendo `Failed password` e extrair os endereços IP associados às tentativas de autenticação malsucedidas.

### Conta e classifica os IPs

Utiliza `collections.Counter` para contabilizar o número de falhas por endereço IP e identificar quais IPs apresentaram mais tentativas de autenticação malsucedidas.

### Menu no terminal

Apresenta os resultados no terminal de forma organizada e permite escolher se o relatório será salvo em arquivo.

### Exportação de relatórios

Permite exportar os resultados em:

* `.txt`
* `.csv`

O formato CSV pode ser utilizado posteriormente em ferramentas de planilhas ou outras ferramentas de análise.

### Multiplataforma

Utiliza `pathlib` para trabalhar com caminhos de arquivos, evitando dependência de caminhos específicos do sistema operacional.

## Tecnologias e módulos

O projeto utiliza apenas bibliotecas nativas do Python, sem necessidade de instalação de pacotes externos.

* **Bibliotecas**
* `re` — Expressões Regulares
* `collections.Counter` — Contagem e classificação dos eventos
* `pathlib` — Manipulação de caminhos e arquivos
* `csv` — Exportação dos resultados

## Objetivo

O objetivo do projeto é automatizar uma tarefa básica de análise de segurança: processar arquivos de log de autenticação e identificar padrões de tentativas malsucedidas de acesso ao SSH.

A quantidade elevada de falhas originadas de um mesmo IP pode indicar uma possível tentativa de **Brute Force**, embora o resultado do script, por si só, não confirme que um ataque ocorreu.

## Estrutura do projeto

```text
log-analyzer/
│
├── src/
│   └── analyzer.py
│
├── logs/
│   └── auth.log
│
├── reports/
│   └── report.txt
│
├── README.md

```

## Como executar

Com o Python 3 instalado:

```bash
python src/analyzer.py
```

O programa solicitará o arquivo de log a ser analisado e apresentará os resultados no terminal.

## Exemplo de resultado

```text
IP: 192.168.1.10
Tentativas falhas: 37

IP: 10.0.0.15
Tentativas falhas: 21

IP: 172.16.0.8
Tentativas falhas: 14
```

O resultado também pode ser exportado para um relatório `.txt` ou `.csv`.

## Objetivo de aprendiza
