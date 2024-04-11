import requests
import time
from datetime import datetime, timedelta
import math

# Variável de controle para verificar se o cabeçalho já foi impresso
cabecalho_arquivo = False

# Imprime cabeçalho dos registros de saída na tela
print("Data/Hora; Va(V); Vb(V); Vc(V); Ia(A); Ib(A); Ic(A); Pa(kW); Pb(kW); Pc(kW); Qa(kvar); Qb(kvar); Qc(kvar); Sa(kVA); Sb(kVA); Sc(kVA); Ptotal(kW); Qtotal(kvar); Stotal(kVA)")

def coletar_dados():
    global cabecalho_arquivo  # Declarando a variável como global dentro da função

    while True:
        # Início do tempo para medir o tempo de execução
        inicio = time.time()

        response = requests.get('https://www.pqsys.com.br/remoteScreen/pq99_6169d4ee0ba83243d39fa0cc/api/fasor')
        #response = requests.get('https://www.pqsys.com.br/remoteScreen/pq78_614a288f580e4c20e5c11d0c/api/fasor')
        data = response.json()

        # Acessa os valores registrados no medidor via API
        tensao_faseA_modulo = data[0]['tensao']['faseA']['modulo']
        tensao_faseA_modulo = round(tensao_faseA_modulo, 2)
        tensao_faseA_angulo = data[0]['tensao']['faseA']['angulo']
        tensao_faseA_angulo = round(tensao_faseA_angulo, 2)

        tensao_faseB_modulo = data[0]['tensao']['faseB']['modulo']
        tensao_faseB_modulo = round(tensao_faseB_modulo, 2)
        tensao_faseB_angulo = data[0]['tensao']['faseB']['angulo']
        tensao_faseB_angulo = round(tensao_faseB_angulo, 2)

        tensao_faseC_modulo = data[0]['tensao']['faseC']['modulo']
        tensao_faseC_modulo = round(tensao_faseC_modulo, 2)
        tensao_faseC_angulo = data[0]['tensao']['faseC']['angulo']
        tensao_faseC_angulo = round(tensao_faseC_angulo, 2)

        corrente_faseA_modulo = data[0]['corrente']['faseA']['modulo']
        corrente_faseA_modulo = round(corrente_faseA_modulo, 2)
        corrente_faseA_angulo = data[0]['corrente']['faseA']['angulo']
        corrente_faseA_angulo = round(corrente_faseA_angulo, 2)

        corrente_faseB_modulo = data[0]['corrente']['faseB']['modulo']
        corrente_faseB_modulo = round(corrente_faseB_modulo, 2)
        corrente_faseB_angulo = data[0]['corrente']['faseB']['angulo']
        corrente_faseB_angulo = round(corrente_faseB_angulo, 2)

        corrente_faseC_modulo = data[0]['corrente']['faseC']['modulo']
        corrente_faseC_modulo = round(corrente_faseC_modulo, 2)
        corrente_faseC_angulo = data[0]['corrente']['faseC']['angulo']
        corrente_faseC_angulo = round(corrente_faseC_angulo, 2)

        ###### Cálculo das potências por fase

        AngVA = tensao_faseA_angulo * math.pi / 180
        AngIA = corrente_faseA_angulo * math.pi / 180
        TetaA = AngVA - AngIA
        Pa = tensao_faseA_modulo * corrente_faseA_modulo * math.cos(TetaA) / 1000
        Qa = tensao_faseA_modulo * corrente_faseA_modulo * math.sin(TetaA) / 1000
        Sa = tensao_faseA_modulo * corrente_faseA_modulo / 1000

        AngVB = tensao_faseB_angulo * math.pi / 180
        AngIB = corrente_faseB_angulo * math.pi / 180
        TetaB = AngVB - AngIB
        Pb = tensao_faseB_modulo * corrente_faseB_modulo * math.cos(TetaB) / 1000
        Qb = tensao_faseB_modulo * corrente_faseB_modulo * math.sin(TetaB) / 1000
        Sb = tensao_faseB_modulo * corrente_faseB_modulo / 1000

        AngVC = tensao_faseC_angulo * math.pi / 180
        AngIC = corrente_faseC_angulo * math.pi / 180
        TetaC = AngVC - AngIC
        Pc = tensao_faseC_modulo * corrente_faseC_modulo * math.cos(TetaC) / 1000
        Qc = tensao_faseC_modulo * corrente_faseC_modulo * math.sin(TetaC) / 1000
        Sc = tensao_faseC_modulo * corrente_faseC_modulo / 1000

        Ptotal = Pa + Pb + Pc
        Qtotal = Qa + Qb + Qc
        Stotal = math.sqrt(Ptotal*Ptotal + Qtotal*Qtotal)

        # Obtém a data e hora atual
        agora = datetime.now()
        # Formata a data e hora no formato desejado
        data_hora_formatada = agora.strftime('%d/%m/%Y %H:%M:%S')

        # Prepara a linha a ser salva no arquivo
        cabecalho_para_salvar = (f"Data/Hora; Va(V); Vb(V); Vc(V); Ia(A); Ib(A); Ic(A); Pa(kW); Pb(kW); Pc(kW); Qa(kvar); Qb(kvar); Qc(kvar); Sa(kVA); Sb(kVA); Sc(kVA); Ptotal(kW); Qtotal(kvar); Stotal(kVA)\n")
        linha_para_salvar = (f"{data_hora_formatada}; {round(tensao_faseA_modulo,2)}; {round(tensao_faseB_modulo,2)}; {round(tensao_faseC_modulo,2)}; "
                             f"{round(corrente_faseA_modulo,2)}; {round(corrente_faseB_modulo,2)}; {round(corrente_faseC_modulo,2)}; "
                             f"{round(Pa,2)}; {round(Pb,2)}; {round(Pc,2)}; "
                             f"{round(Qa,2)}; {round(Qb,2)}; {round(Qc,2)}; "
                             f"{round(Sa,2)}; {round(Sb,2)}; {round(Sc,2)}; "
                             f"{round(Ptotal,2)}; {round(Qtotal,2)}; {round(Stotal,2)}\n")

        # Abre o arquivo em modo de anexação e escreve a linha
        with open('dados_registrados.txt', 'a') as arquivo:
            # Verifica se o cabeçalho já foi impresso, caso contrário, imprime e define a variável de controle como True
            if not cabecalho_arquivo:
                arquivo.write(cabecalho_para_salvar)
                cabecalho_arquivo = True
            arquivo.write(linha_para_salvar)

        print(linha_para_salvar, end='')

        # Fim do tempo de execução
        fim = time.time()

        # Tempo decorrido durante a execução
        tempo_decorrido = fim - inicio

        # Calcula o próximo segundo exato
        proximo_segundo = math.ceil(time.time())

        # Calcula o tempo de espera até o próximo segundo exato
        espera = proximo_segundo - time.time()

        # Aguarda o tempo de espera antes da próxima coleta de dados
        if espera > 0:
            time.sleep(espera)

# Inicia a coleta de dados
coletar_dados()
