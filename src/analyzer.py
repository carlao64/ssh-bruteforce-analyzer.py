import csv
import re 
from collections import Counter
from pathlib import Path

def analisar_logs(caminho_log):
    ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    lista_ip = []
    total_falhas = 0

    with open(caminho_log, "r") as arquivo:
        for linha in arquivo:
            if 'failed password' in linha.lower():
                total_falhas += 1
                resultado = re.search(ip_pattern, linha)
                if resultado:
                    lista_ip.append(resultado.group())

    contagem_ips = Counter(lista_ip)
    return contagem_ips, total_falhas

def exibir_relatorio(contagem_ips, total_falhas):
    print('__relatorio_ips_com_falhas__')
    for ip, quantidade in contagem_ips.most_common(5):
        print(f"IP: {ip} | Tentativas: {quantidade}")
    print(f"Quantidade total de falhas de login: {total_falhas}")

def  exportar_relatorio (contagem_ips, total_falhas, pasta_destino, formato ='txt') :
    if formato=='txt':
        caminho_arquivo = pasta_destino /'relatorio_falhas_txt.'
        with open (caminho_arquivo, 'w', encoding= "utf 8") as f:
            f.write("relatorio de analise de logs (sshd)\n\n")
            f.write(f"Total de falhas detectadas {total_falhas}\n\n")
            f.write("top ip ofensores:\n") 
            for ip, quantidade in contagem_ips.most_common(5):
                f.write (f"IP: {ip:<15} | Tentativas: {quantidade}\n")
        print(f"[+] Relatório em TXT salvo com sucesso em: {caminho_arquivo}")

    elif formato == "csv":
        caminho_arquivo = pasta_destino / "relatorio_falhas.csv"
        with open(
            caminho_arquivo, "w", newline="", encoding="utf-8"
        ) as f:
            writer = csv.writer(f)
            # Escreve o cabeçalho e os dados
            writer.writerow(["IP", "Tentativas_Falhas"])
            for ip, quantidade in contagem_ips.most_common():
                writer.writerow([ip, quantidade])
        print(f"[+] Relatório em CSV salvo com sucesso em: {caminho_arquivo}")

    else:
        print("[-] Formato inválido! O relatório não foi exportado.")

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    log_path = base_dir.parent / "logs" / "auth.log"
    reports_dir = base_dir.parent / "reports"

    contagem, total = analisar_logs(log_path)
    exibir_relatorio(contagem, total)

    # 2. Faz as perguntas no terminal
    print("Deseja exportar o relatório?")
    print("[1] Arquivo Texto (.txt)")
    print("[2] Arquivo Planilha (.csv)")
    print("[0] Não exportar")

    opcao = input("\nEscolha uma opção (0/1/2): ").strip()

    if opcao == "1":
        exportar_relatorio(contagem, total, reports_dir, formato="txt")
    elif opcao == "2":
        exportar_relatorio(contagem, total, reports_dir, formato="csv")
    else:
        print("Finalizado sem exportação.")