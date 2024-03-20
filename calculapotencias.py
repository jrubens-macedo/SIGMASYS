import requests
import time
import math
import cmath

from prettytable import PrettyTable

while True:

    response = requests.get('https://www.pqsys.com.br/remoteScreen/pq78_614a288f580e4c20e5c11d0c/api/fasor')
    data = response.json()

    # Acessa os valores registrados no Medidor
    tensao_faseA_angulo_med1 = data[0]['tensao']['faseA']['angulo']
    tensao_faseA_modulo_med1 = data[0]['tensao']['faseA']['modulo']
    tensao_faseB_angulo_med1 = data[0]['tensao']['faseB']['angulo']
    tensao_faseB_modulo_med1 = data[0]['tensao']['faseB']['modulo']
    tensao_faseC_angulo_med1 = data[0]['tensao']['faseC']['angulo']
    tensao_faseC_modulo_med1 = data[0]['tensao']['faseC']['modulo']
    tensao_faseN_angulo_med1 = data[0]['tensao']['faseC']['angulo']
    tensao_faseN_modulo_med1 = data[0]['tensao']['faseC']['modulo']
    corrente_faseA_angulo_med1 = data[0]['corrente']['faseA']['angulo']
    corrente_faseA_modulo_med1 = data[0]['corrente']['faseA']['modulo']
    corrente_faseB_angulo_med1 = data[0]['corrente']['faseB']['angulo']
    corrente_faseB_modulo_med1 = data[0]['corrente']['faseB']['modulo']
    corrente_faseC_angulo_med1 = data[0]['corrente']['faseC']['angulo']
    corrente_faseC_modulo_med1 = data[0]['corrente']['faseC']['modulo']
    corrente_faseN_angulo_med1 = data[0]['corrente']['faseN']['angulo']
    corrente_faseN_modulo_med1 = data[0]['corrente']['faseN']['modulo']

    # Cálculo das grandezas do medidor

    AngVA_med1 = tensao_faseA_angulo_med1 * math.pi / 180
    AngIA_med1 = corrente_faseA_angulo_med1 * math.pi / 180
    TetaA_med1 = AngVA_med1 - AngIA_med1
    Pa_med1 = tensao_faseA_modulo_med1 * corrente_faseA_modulo_med1 * math.cos(TetaA_med1)
    Qa_med1 = tensao_faseA_modulo_med1 * corrente_faseA_modulo_med1 * math.sin(TetaA_med1)

    AngVB_med1 = tensao_faseB_angulo_med1 * math.pi / 180
    AngIB_med1 = corrente_faseB_angulo_med1 * math.pi / 180
    TetaB_med1 = AngVB_med1 - AngIB_med1
    Pb_med1 = tensao_faseB_modulo_med1 * corrente_faseB_modulo_med1 * math.cos(TetaB_med1)
    Qb_med1 = tensao_faseB_modulo_med1 * corrente_faseB_modulo_med1 * math.sin(TetaB_med1)

    AngVC_med1 = tensao_faseC_angulo_med1 * math.pi / 180
    AngIC_med1 = corrente_faseC_angulo_med1 * math.pi / 180
    TetaC_med1 = AngVC_med1 - AngIC_med1
    Pc_med1 = tensao_faseC_modulo_med1 * corrente_faseC_modulo_med1 * math.cos(TetaC_med1)
    Qc_med1 = tensao_faseC_modulo_med1 * corrente_faseC_modulo_med1 * math.sin(TetaC_med1)

    AngVN_med1 = tensao_faseN_angulo_med1 * math.pi / 180
    AngIN_med1 = corrente_faseN_angulo_med1 * math.pi / 180
    TetaN_med1 = AngVN_med1 - AngIN_med1
    Pn_med1 = tensao_faseN_modulo_med1 * corrente_faseN_modulo_med1 * math.cos(TetaN_med1)
    Qn_med1 = tensao_faseN_modulo_med1 * corrente_faseN_modulo_med1 * math.sin(TetaN_med1)

    Pt_med1 = Pa_med1 + Pb_med1 + Pc_med1
    Qt_med1 = Qa_med1 + Qb_med1 + Qc_med1
    St_med1 = math.sqrt(Pt_med1*Pt_med1+Qt_med1*Qt_med1)
    FP_med1 = Pt_med1/St_med1

    # Componentes simétricas

    Va_med1 = complex(tensao_faseA_modulo_med1 * math.cos(AngVA_med1),tensao_faseA_modulo_med1 * math.sin(AngVA_med1))
    Vb_med1 = complex(tensao_faseB_modulo_med1 * math.cos(AngVB_med1), tensao_faseB_modulo_med1 * math.sin(AngVB_med1))
    Vc_med1 = complex(tensao_faseC_modulo_med1 * math.cos(AngVC_med1), tensao_faseC_modulo_med1 * math.sin(AngVC_med1))
    Ia_med1 = complex(corrente_faseA_modulo_med1 * math.cos(AngVA_med1),corrente_faseA_modulo_med1 * math.sin(AngIA_med1))
    Ib_med1 = complex(corrente_faseB_modulo_med1 * math.cos(AngVB_med1), corrente_faseB_modulo_med1 * math.sin(AngIB_med1))
    Ic_med1 = complex(corrente_faseC_modulo_med1 * math.cos(AngVC_med1), corrente_faseC_modulo_med1 * math.sin(AngIC_med1))

    a = complex(-0.5,0.8660254)
    a2 = complex(-0.5, -0.8660254)

    V0_ret_med1 = 1/3 * (Va_med1 + Vb_med1 + Vc_med1)
    V1_ret_med1 = 1/3 * (Va_med1 + a*Vb_med1 + a2*Vc_med1)
    V2_ret_med1 = 1/3 * (Va_med1 + a2*Vb_med1 + a*Vc_med1)
    V0_polar_med1 = cmath.polar(V0_ret_med1)
    V1_polar_med1 = cmath.polar(V1_ret_med1)
    V2_polar_med1 = cmath.polar(V2_ret_med1)

    I0_ret_med1 = 1/3 * (Ia_med1 + Ib_med1 + Ic_med1)
    I1_ret_med1 = 1/3 * (Ia_med1 + a*Ib_med1 + a2*Ic_med1)
    I2_ret_med1 = 1/3 * (Ia_med1 + a2*Ib_med1 + a*Ic_med1)
    I0_polar_med1 = cmath.polar(I0_ret_med1)
    I1_polar_med1 = cmath.polar(I1_ret_med1)
    I2_polar_med1 = cmath.polar(I2_ret_med1)

    P0_med1 = 3 * V0_polar_med1[0] * I0_polar_med1[0] * math.cos(V0_polar_med1[1]-I0_polar_med1[1])
    P1_med1 = 3 * V1_polar_med1[0] * I1_polar_med1[0] * math.cos(V1_polar_med1[1]-I1_polar_med1[1])
    P2_med1 = 3 * V2_polar_med1[0] * I2_polar_med1[0] * math.cos(V2_polar_med1[1]-I2_polar_med1[1])

    FDv_med1 = 100 * (V2_polar_med1[0] / V1_polar_med1[0])
    FDi_med1 = 100 * (I2_polar_med1[0] / I1_polar_med1[0])


    # Tabela de dados para o medidor

    table = PrettyTable()

    table.field_names = ["Medidor", "Fase","V_mod(V)","V_ang(º)","I_mod(A)","I_ang(º)","Pload(W)","Qload(var)","P0load(W)","P+load(W)","P-load(W)", "FDv(%)", "FDi(%)"]

    table.add_row(["Fonte","A", round(tensao_faseA_modulo_med1,3), round(tensao_faseA_angulo_med1,3),
                   round(corrente_faseA_modulo_med1,3), round(corrente_faseA_angulo_med1,3),round(Pa_med1,3),
                   round(Qa_med1,3)," "," "," "," "," "])
    table.add_row(["Fonte","B", round(tensao_faseB_modulo_med1,3), round(tensao_faseB_angulo_med1,3),
                   round(corrente_faseB_modulo_med1,3), round(corrente_faseB_angulo_med1,3),round(Pb_med1,3),
                   round(Qb_med1,3)," "," "," "," "," "])
    table.add_row(["Fonte","C", round(tensao_faseC_modulo_med1,3), round(tensao_faseC_angulo_med1,3),
                   round(corrente_faseC_modulo_med1,3), round(corrente_faseC_angulo_med1,3),round(Pc_med1,3),
                   round(Qc_med1,3),round(P0_med1,3),round(P1_med1,3),round(P2_med1,3),round(FDv_med1,3),round(FDi_med1,3)])
    table.add_row(["Fonte","N", round(tensao_faseN_modulo_med1,3), round(tensao_faseN_angulo_med1,3),
                   round(corrente_faseN_modulo_med1,3), round(corrente_faseN_angulo_med1,3),round(Pn_med1,3),
                   round(Qn_med1,3)," "," "," "," "," "])
    table.add_row(["Fonte","TOTAL", "-", "-", "-", "-",round(Pt_med1,3),round(Qt_med1,3)," "," "," "," "," "])


    print(table)


    time.sleep(2)  # espera 1 segundo antes de atualizar novamente
