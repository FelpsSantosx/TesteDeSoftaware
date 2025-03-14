import os
import csv
from datetime import datetime
import time
import matplotlib.pyplot as plt
import pandas as pd


def verificar_disponibilidade(host):
    """
    Verifica se um servidor ou serviço está online via ping.
    :param host: Endereço do host a ser testado.
    """
    resposta = os.system(f"ping -c 1 {host} > /dev/null 2>&1")
    status = "ONLINE" if resposta == 0 else "OFFLINE"
    
    print(f"{host} está {status}")  # Exibe o resultado no terminal
    salvar_log(host, status)  # Registra a informação no log


def salvar_log(host, status):
    """
    Salva o status do servidor em um arquivo CSV.
    :param host: Nome do servidor verificado.
    :param status: Status ONLINE ou OFFLINE.
    """
    with open("log_monitoramento.csv", "a", newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([datetime.now(), host, status])


def gerar_relatorio():

    df = pd.read_csv("log_monitoramento.csv", names=["DataHora", "Host", "Status"])

    df['DataHora'] = pd.to_datetime(df['DataHora'])
    
    
    df['StatusBinario'] = df['Status'].apply(lambda x: 1 if x == "ONLINE" else 0)
    
    
    for host in df['Host'].unique():
        df_host = df[df['Host'] == host]
        plt.plot(df_host['DataHora'], df_host['StatusBinario'], label=host)
    
    plt.xlabel('Data e Hora')
    plt.ylabel('Status (1 = ONLINE, 0 = OFFLINE)')
    plt.title('Monitoramento de Ativos de TI')
    plt.legend()
    plt.grid(True)
    plt.show()

ativos = ["google.com", "github.com", "8.8.8.8", "aws.amazon.com", "microsoft.com"]

print("Monitoramento de Ativos de TI")
while True:
    for ativo in ativos:
        verificar_disponibilidade(ativo)
    
    gerar_relatorio()
    
    time.sleep(600)
