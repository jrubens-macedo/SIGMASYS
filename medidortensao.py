import requests
import time
from datetime import datetime

while True:
    response = requests.get('https://www.pqsys.com.br/remoteScreen/pq78_614a288f580e4c20e5c11d0c/api/fasor')
    data = response.json()

    # Acessa os valores registrados no Medidor
    tensao_faseA_modulo = data[0]['tensao']['faseA']['modulo']
    tensao_faseA_modulo = round(tensao_faseA_modulo, 2)

    # Obtém a data e hora atual
    agora = datetime.now()
    # Formata a data e hora no formato desejado
    data_hora_formatada = agora.strftime('%d/%m/%Y %H:%M:%S')

    # Prepara a linha a ser salva no arquivo
    linha_para_salvar = f"{data_hora_formatada} {tensao_faseA_modulo}\n"

    # Abre o arquivo em modo de anexação e escreve a linha
    with open('dados_tensao.txt', 'a') as arquivo:
        arquivo.write(linha_para_salvar)

    print(linha_para_salvar, end='')

    time.sleep(1)

