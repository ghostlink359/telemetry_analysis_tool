import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QVBoxLayout, QPushButton, QLabel
)

import pandas as pd

df = pd.read_csv(r'C:\Users\908430\Desktop\calculadoraCient\telemetry_calc\files\formulaOneLaps.csv')

# 1. Todo app PySide6 precisa iniciar com o QApplication
app = QApplication(sys.argv)

# 2. Criamos a Janela Principal (Moldura do Software)
janela_principal = QMainWindow()
janela_principal.setWindowTitle("Telemetry Analysis Tool")
janela_principal.resize(400, 200) # Largura e altura inicial

# 3. Criamos um QWidget para ser a "Área Central" da janela
# A QMainWindow precisa obrigatoriamente de um widget central
widget_central = QWidget()
janela_principal.setCentralWidget(widget_central)

# 4. Criamos os Componentes Visuais (Widgets)
texto_informativo = QLabel("Choose a option.")
botao_um = QPushButton("test csv")
botao_dois = QPushButton("Analysis")
botao_tres = QPushButton("Compare")
botao_quatro = QPushButton("Graphs")
botao_cinco = QPushButton("Exit")

# 5. Criamos o Organizador (Layout) e adicionamos os componentes nele
# O QVBoxLayout vai alinhar o texto e o botão um embaixo do outro
layout_vertical = QVBoxLayout()
layout_vertical.addWidget(texto_informativo)
layout_vertical.addWidget(botao_um)
layout_vertical.addWidget(botao_dois)
layout_vertical.addWidget(botao_tres)
layout_vertical.addWidget(botao_quatro)
layout_vertical.addWidget(botao_cinco)

# 6. Atribuímos o layout para o nosso widget central
widget_central.setLayout(layout_vertical)

# --- SISTEMA DE EVENTOS (Signals & Slots) ---
# Esta função será chamada quando o usuário interagir com o botão
def ao_clicar_no_botao():
    texto_informativo.setText(df.head(5))
    # Usando uma função exclusiva da QMainWindow (Barra de status no rodapé)
    janela_principal.statusBar().showMessage("Ação executada!", 3000) # Some em 3 segundos

def ao_clicar_em_sair():
    janela_principal.show()
    sys.exit(app.exec())

botao_um.clicked.connect(ao_clicar_no_botao)
botao_cinco.clicked.connect(ao_clicar_em_sair)
