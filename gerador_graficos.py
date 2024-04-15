import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import HourLocator, DateFormatter
from datetime import datetime


######################################################################################
# Especificando o dia específico que você deseja plotar
dia_especifico = '2024-04-10'
######################################################################################

# Caminho para o arquivo CSV
caminho_arquivo = r'C:\pythonjr\vpp_eto\memomassa_pq99.csv'

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

coluna_tensao_a = dados_do_dia["tensao.average.van[V]"]
coluna_corrente_a = dados_do_dia["corrente.average.ia[A]"]
coluna_potativa_a = dados_do_dia["potencia.consumo.average.kwa[kW]"]
coluna_potreativa_a = dados_do_dia["potencia.consumo.average.kvara[kvar]"]
coluna_potaparente_a = dados_do_dia["potencia.consumo.average.kvaa[kva]"]

coluna_tensao_b = dados_do_dia["tensao.average.vbn[V]"]
coluna_corrente_b = dados_do_dia["corrente.average.ib[A]"]
coluna_potativa_b = dados_do_dia["potencia.consumo.average.kwb[kW]"]
coluna_potreativa_b = dados_do_dia["potencia.consumo.average.kvarb[kvar]"]
coluna_potaparente_b = dados_do_dia["potencia.consumo.average.kvab[kva]"]

coluna_tensao_c = dados_do_dia["tensao.average.vcn[V]"]
coluna_corrente_c = dados_do_dia["corrente.average.ic[A]"]
coluna_potativa_c = dados_do_dia["potencia.consumo.average.kwc[kW]"]
coluna_potreativa_c = dados_do_dia["potencia.consumo.average.kvarc[kvar]"]
coluna_potaparente_c = dados_do_dia["potencia.consumo.average.kvac[kva]"]

coluna_potativa_tot = dados_do_dia["potencia.consumo.average.kw[kW]"]
coluna_potreativa_tot = dados_do_dia["potencia.consumo.average.kvar[kvar]"]
coluna_potaparente_tot = dados_do_dia["potencia.consumo.average.kva[kva]"]
coluna_deseqtensao = dados_do_dia["desequilibrio.tensao.[%]"]


#########################################################################################

# Criando uma figura com subplots organizados
fig = plt.figure(figsize=(20, 10))

# Adicionando um nome para a figura
fig.suptitle("Medições PQ79- {} ({})".format(dia_especifico, ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo'][dia_da_semana]))

#########################################################################################

# Plotando os dados de Tensão (V) para Fase A
ax1 = fig.add_subplot(4, 4, 1)
ax1.plot(timestamps, coluna_tensao_a, color='blue')
ax1.set_ylabel("Tensão Eficaz (V)")
ax1.grid(True, linestyle='--')
ax1.set_ylim(180, 240)
ax1.axhspan(202, 231, color='lightgreen', alpha=0.5)
ax1.xaxis.set_major_locator(HourLocator(interval=1))
ax1.xaxis.set_major_formatter(DateFormatter("%H:%M"))
ax1.set_xticklabels([])

# Plotando os dados de Corrente (A) para Fase A
ax2 = fig.add_subplot(4, 4, 5)
ax2.plot(timestamps, coluna_corrente_a, color='red')
ax2.set_ylabel("Corrente Eficaz (A)")
ax2.grid(True, linestyle='--')
ax2.set_ylim(0, 200)
ax2.xaxis.set_major_locator(HourLocator(interval=1))
ax2.xaxis.set_major_formatter(DateFormatter("%H:%M"))
ax2.set_xticklabels([])

# Plotando os dados de Potência Ativa Fase A (kW)
ax3 = fig.add_subplot(4, 4, 9)
ax3.plot(timestamps, coluna_potativa_a, color='green')
ax3.set_ylabel("Potência Ativa (kW)")
ax3.grid(True, linestyle='--')
ax3.set_ylim(-50, 50)
ax3.xaxis.set_major_locator(HourLocator(interval=1))
ax3.xaxis.set_major_formatter(DateFormatter("%H:%M"))
ax3.set_xticklabels([])

# Plotando os dados de Potência Aparente Fase A (kVA)
ax4 = fig.add_subplot(4, 4, 13)
ax4.plot(timestamps, coluna_potaparente_a, color='orange')
ax4.set_ylabel("Potência Aparente (kVA)")
ax4.set_xlabel("Hora do Dia")
ax4.grid(True, linestyle='--')
ax4.set_ylim(0, 60)

# Definindo o locator para mostrar apenas a cada uma hora no último subplot
ax4.xaxis.set_major_locator(HourLocator(interval=1))
# Definindo o formato dos labels para exibir apenas a hora no último subplot
ax4.xaxis.set_major_formatter(DateFormatter("%H:%M"))
plt.xticks(rotation=90)  # Rotaciona os rótulos do eixo x para melhor legibilidade

#####################################################################

# Plotando os dados de Tensão (V) para Fase B
ax5 = fig.add_subplot(4, 4, 2)
ax5.plot(timestamps, coluna_tensao_b, color='blue')
ax5.set_ylabel("Tensão Eficaz (V)")
ax5.grid(True, linestyle='--')
ax5.set_ylim(180, 240)
ax5.axhspan(202, 231, color='lightgreen', alpha=0.5)
ax5.xaxis.set_major_locator(HourLocator(interval=1))
ax5.xaxis.set_major_formatter(DateFormatter("%H:%M"))
ax5.set_xticklabels([])

# Plotando os dados de Corrente (A) para Fase B
ax6 = fig.add_subplot(4, 4, 6)
ax6.plot(timestamps, coluna_corrente_b, color='red')
ax6.set_ylabel("Corrente Eficaz (A)")
ax6.grid(True, linestyle='--')
ax6.set_ylim(0, 200)
ax6.xaxis.set_major_locator(HourLocator(interval=1))
ax6.xaxis.set_major_formatter(DateFormatter("%H:%M"))
ax6.set_xticklabels([])

# Plotando os dados de Potência Ativa Fase B (kW)
ax7 = fig.add_subplot(4, 4, 10)
ax7.plot(timestamps, coluna_potativa_b, color='green')
ax7.set_ylabel("Potência Ativa (kW)")
ax7.grid(True, linestyle='--')
ax7.set_ylim(-50, 50)
ax7.xaxis.set_major_locator(HourLocator(interval=1))
ax7.xaxis.set_major_formatter(DateFormatter("%H:%M"))
ax7.set_xticklabels([])

# Plotando os dados de Potência Aparente Fase B (kVA)
ax8 = fig.add_subplot(4, 4, 14)
ax8.plot(timestamps, coluna_potaparente_b, color='orange')
ax8.set_ylabel("Potência Aparente (kVA)")
ax8.set_xlabel("Hora do Dia")
ax8.grid(True, linestyle='--')
ax8.set_ylim(0, 60)

# Definindo o locator para mostrar apenas a cada uma hora no último subplot
ax8.xaxis.set_major_locator(HourLocator(interval=1))
# Definindo o formato dos labels para exibir apenas a hora no último subplot
ax8.xaxis.set_major_formatter(DateFormatter("%H:%M"))
plt.xticks(rotation=90)  # Rotaciona os rótulos do eixo x para melhor legibilidade

#####################################################################

# Plotando os dados de Tensão (V) para Fase C
ax9 = fig.add_subplot(4, 4, 3)
ax9.plot(timestamps, coluna_tensao_c, color='blue')
ax9.set_ylabel("Tensão Eficaz (V)")
ax9.grid(True, linestyle='--')
ax9.set_ylim(180, 240)
ax9.axhspan(202, 231, color='lightgreen', alpha=0.5)
ax9.xaxis.set_major_locator(HourLocator(interval=1))
ax9.xaxis.set_major_formatter(DateFormatter("%H:%M"))
ax9.set_xticklabels([])

# Plotando os dados de Corrente (A) para Fase C
ax10 = fig.add_subplot(4, 4, 7)
ax10.plot(timestamps, coluna_corrente_c, color='red')
ax10.set_ylabel("Corrente Eficaz (A)")
ax10.grid(True, linestyle='--')
ax10.set_ylim(0, 200)
ax10.xaxis.set_major_locator(HourLocator(interval=1))
ax10.xaxis.set_major_formatter(DateFormatter("%H:%M"))
ax10.set_xticklabels([])

# Plotando os dados de Potência Ativa Fase C (kW)
ax11 = fig.add_subplot(4, 4, 11)
ax11.plot(timestamps, coluna_potativa_c, color='green')
ax11.set_ylabel("Potência Ativa (kW)")
ax11.grid(True, linestyle='--')
ax11.set_ylim(-50, 50)
ax11.xaxis.set_major_locator(HourLocator(interval=1))
ax11.xaxis.set_major_formatter(DateFormatter("%H:%M"))
ax11.set_xticklabels([])

# Plotando os dados de Potência Aparente Fase C (kVA)
ax12 = fig.add_subplot(4, 4, 15)
ax12.plot(timestamps, coluna_potaparente_c, color='orange')
ax12.set_ylabel("Potência Aparente (kVA)")
ax12.set_xlabel("Hora do Dia")
ax12.grid(True, linestyle='--')
ax12.set_ylim(0, 60)

# Definindo o locator para mostrar apenas a cada uma hora no último subplot
ax12.xaxis.set_major_locator(HourLocator(interval=1))
# Definindo o formato dos labels para exibir apenas a hora no último subplot
ax12.xaxis.set_major_formatter(DateFormatter("%H:%M"))
plt.xticks(rotation=90)  # Rotaciona os rótulos do eixo x para melhor legibilidade

#####################################################################

# Plotando os dados de Potência Ativa Total
ax13 = fig.add_subplot(4, 4, 4)
ax13.plot(timestamps, coluna_potativa_tot, color='green')
ax13.set_ylabel("Potência Ativa (kW)")
ax13.grid(True, linestyle='--')
ax13.set_ylim(-150, 100)
ax13.set_facecolor((0.92, 0.92, 0.92))
ax13.xaxis.set_major_locator(HourLocator(interval=1))
ax13.xaxis.set_major_formatter(DateFormatter("%H:%M"))
ax13.set_xticklabels([])

# Plotando os dados de Potência Retiva Total
ax14 = fig.add_subplot(4, 4, 8)
ax14.plot(timestamps, coluna_potreativa_tot, color='red')
ax14.set_ylabel("Potência Reativa (kvar)")
ax14.grid(True, linestyle='--')
ax14.set_ylim(-2, 6)
ax14.set_facecolor((0.92, 0.92, 0.92))
ax14.xaxis.set_major_locator(HourLocator(interval=1))
ax14.xaxis.set_major_formatter(DateFormatter("%H:%M"))
ax14.set_xticklabels([])

# Plotando os dados de Potência Aparente Total (kVA)
ax15 = fig.add_subplot(4, 4, 12)
ax15.plot(timestamps, coluna_potaparente_tot, color='orange')
ax15.set_ylabel("Potência Aparente (kVA)")
ax15.grid(True, linestyle='--')
ax15.set_ylim(0, 150)
ax15.set_facecolor((0.92, 0.92, 0.92))
ax15.xaxis.set_major_locator(HourLocator(interval=1))
ax15.xaxis.set_major_formatter(DateFormatter("%H:%M"))
ax15.set_xticklabels([])

# Plotando os dados de Potência Reativa Fase C (kvar)
ax16 = fig.add_subplot(4, 4, 16)
ax16.plot(timestamps, coluna_deseqtensao, color='brown')
ax16.set_ylabel("Desequilíbrio de Tensão (%)")
ax16.set_xlabel("Hora do Dia")
ax16.grid(True, linestyle='--')
ax16.set_ylim(0, 5)
ax16.set_facecolor((0.92, 0.92, 0.92))
ax16.axhspan(0, 3, color='lightgreen', alpha=0.5)

ax16.xaxis.set_major_locator(HourLocator(interval=1))
ax16.xaxis.set_major_formatter(DateFormatter("%H:%M"))
plt.xticks(rotation=90)

#####################################################################

ax1.set_title('Grandezas - Fase A')
ax5.set_title('Grandezas - Fase B')
ax9.set_title('Grandezas - Fase C')
ax13.set_title('Potências Totais e FDV(%)')

plt.tight_layout()  # Ajusta o layout para evitar sobreposição de rótulos
plt.show()
