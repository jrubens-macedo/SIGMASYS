import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import HourLocator, DateFormatter
from datetime import datetime
import numpy as np

######################################################################################
# Especificando o dia específico que você deseja plotar
dia_especifico = '2024-04-12'
######################################################################################

# Caminho para o arquivo CSV
caminho_arquivo = r'C:\pythonjr\sigmasys\memomassa_pq99.csv'

# Leitura do arquivo CSV usando pandas
dados = pd.read_csv(caminho_arquivo, delimiter=';')

# Convertendo a coluna "timestampsourcelt" para o formato de data e hora
dados['timestampsourcelt'] = pd.to_datetime(dados['timestampsourcelt'])

# Convertendo a string para um objeto datetime
data_especifica = datetime.strptime(dia_especifico, '%Y-%m-%d')

# Obtendo o dia da semana (0 para segunda-feira, 1 para terça-feira, ..., 6 para domingo)
dia_da_semana = data_especifica.weekday()

# Filtrando os dados para incluir apenas o dia específico
dados_do_dia = dados[dados['timestampsourcelt'].dt.date == pd.to_datetime(dia_especifico).date()]

# Extraindo as colunas de interesse
timestamps = dados_do_dia["timestampsourcelt"]

# Leitura das colunas de dados para a Fase A #############################################################

coluna_mag_tensao_a_h1 = dados_do_dia["harmonicasdefasagemtensao.grupo.vahd1.mag[V]"]
coluna_ang_tensao_a_h1 = dados_do_dia["harmonicasdefasagemtensao.grupo.vahd1.angulo[graus]"]
coluna_mag_corrente_a_h1 = dados_do_dia["harmonicasdefasagemcorrente.grupo.iahd1.mag[A]"]
coluna_ang_corrente_a_h1 = dados_do_dia["harmonicasdefasagemcorrente.grupo.iahd1.angulo[graus]"]

coluna_mag_tensao_a_h3 = dados_do_dia["harmonicasdefasagemtensao.grupo.vahd3.mag[%]"]
coluna_ang_tensao_a_h3 = dados_do_dia["harmonicasdefasagemtensao.grupo.vahd3.angulo[graus]"]
coluna_mag_corrente_a_h3 = dados_do_dia["harmonicasdefasagemcorrente.grupo.iahd3.mag[%]"]
coluna_ang_corrente_a_h3 = dados_do_dia["harmonicasdefasagemcorrente.grupo.iahd3.angulo[graus]"]

coluna_mag_tensao_a_h5 = dados_do_dia["harmonicasdefasagemtensao.grupo.vahd5.mag[%]"]
coluna_ang_tensao_a_h5 = dados_do_dia["harmonicasdefasagemtensao.grupo.vahd5.angulo[graus]"]
coluna_mag_corrente_a_h5 = dados_do_dia["harmonicasdefasagemcorrente.grupo.iahd5.mag[%]"]
coluna_ang_corrente_a_h5 = dados_do_dia["harmonicasdefasagemcorrente.grupo.iahd5.angulo[graus]"]

# Convertendo as tensões e correntes harmônicas para Volt e Ampere #######################################

coluna_mag_tensao_a_h3_volt = (coluna_mag_tensao_a_h3 / 100) * coluna_mag_tensao_a_h1
coluna_mag_tensao_a_h5_volt = (coluna_mag_tensao_a_h5 / 100) * coluna_mag_tensao_a_h1

coluna_mag_corrente_a_h3_ampere = (coluna_mag_corrente_a_h3 / 100) * coluna_mag_corrente_a_h1
coluna_mag_corrente_a_h5_ampere = (coluna_mag_corrente_a_h5 / 100) * coluna_mag_corrente_a_h1


# Convertendo ângulos de graus para radianos
coluna_ang_tensao_a_h1_radianos = np.radians(coluna_ang_tensao_a_h1)
coluna_ang_tensao_a_h3_radianos = np.radians(coluna_ang_tensao_a_h3)
coluna_ang_tensao_a_h5_radianos = np.radians(coluna_ang_tensao_a_h5)

coluna_ang_corrente_a_h1_radianos = np.radians(coluna_ang_corrente_a_h1)
coluna_ang_corrente_a_h3_radianos = np.radians(coluna_ang_corrente_a_h3)
coluna_ang_corrente_a_h5_radianos = np.radians(coluna_ang_corrente_a_h5)


# Criando o gráfico polar #####################################################

plt.figure(figsize=(8, 6))
ax = plt.subplot(111, polar=True)  # Cria um subplot polar

ax.plot(coluna_ang_tensao_a_h3_radianos, coluna_mag_tensao_a_h3_volt, 'o', color='red', markersize=4)

# Ajustando a orientação e os ticks
ax.set_theta_zero_location('E')  # Define o zero para o Norte
ax.set_theta_direction(-1)  # Define a direção dos ângulos como horário

# Adicionando títulos e rótulos
plt.title('Terceira Harmônica de Tensão')

# Configuração das linhas de grade
ax.grid(True)
ax.xaxis.grid(True, color='gray', linestyle='-', linewidth=0.5)  # Linhas radiais
ax.yaxis.grid(True, color='gray', linestyle='dotted', linewidth=0.8)  # Linhas circulares

# Configurando a cor de fundo do gráfico
ax.set_facecolor((0.96, 0.96, 0.96))

# Mostrando o gráfico
plt.show()