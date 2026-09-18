Analisador de Logs SSHD
Script em Python para analisar logs de autenticação do SSH e identificar tentativas de invasão ou ataques de força bruta.

A ideia do projeto é automatizar a leitura do arquivo auth.log, filtrar os acessos que falharam e gerar um resumo dos IPs mais problemáticos, seja no terminal ou exportado em arquivo.

O que o projeto faz
Filtra falhas de login: Usa Regex para localizar linhas com Failed password e extrair os endereços IP.

Conta e rankeia: Usa collections.Counter para somar o total de falhas e listar os maiores ofensores.

Menu no terminal: Mostra o resultado de forma limpa e pergunta se você quer salvar um relatório.

Exportação flexível: Salva o relatório formatado em .txt ou em .csv para abrir em planilhas.

Multiplataforma: Feito com pathlib, funciona no Windows, Linux ou macOS sem quebrar caminhos de pasta.

Tecnologias e Módulos
Projetado usando apenas bibliotecas nativas do Python (sem necessidade de instalar pacotes externos):

Python 3

re (Expressões Regulares)

collections.Counter

pathlib

csv O projeto tem como objetivo automatizar a identificação de possíveis ataques de força bruta (Brute Force) e acessos não autorizados através do processamento de arquivos de log no formato auth.log.
