import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QVBoxLayout, QPushButton, QLabel
)

# 1. Todo app PySide6 precisa iniciar com o QApplication
app = QApplication(sys.argv)

# 2. Criamos a Janela Principal (Moldura do Software)
janela_principal = QMainWindow()
janela_principal.setWindowTitle("Meu Guia de Estudos PySide6")
janela_principal.resize(400, 200) # Largura e altura inicial

# 3. Criamos um QWidget para ser a "Área Central" da janela
# A QMainWindow precisa obrigatoriamente de um widget central
widget_central = QWidget()
janela_principal.setCentralWidget(widget_central)

# 4. Criamos os Componentes Visuais (Widgets)
texto_informativo = QLabel("Clique no botão para atualizar o status.")
botao_acao = QPushButton("Clique Aqui")

# 5. Criamos o Organizador (Layout) e adicionamos os componentes nele
# O QVBoxLayout vai alinhar o texto e o botão um embaixo do outro
layout_vertical = QVBoxLayout()
layout_vertical.addWidget(texto_informativo)
layout_vertical.addWidget(botao_acao)

# 6. Atribuímos o layout para o nosso widget central
widget_central.setLayout(layout_vertical)

# --- SISTEMA DE EVENTOS (Signals & Slots) ---
# Esta função será chamada quando o usuário interagir com o botão
def ao_clicar_no_botao():
    texto_informativo.setText("O botão foi clicado com sucesso! 🎉")
    # Usando uma função exclusiva da QMainWindow (Barra de status no rodapé)
    janela_principal.statusBar().showMessage("Ação executada!", 3000) # Some em 3 segundos

# Conectamos o sinal de clique do QPushButton à nossa função Python
botao_acao.clicked.connect(ao_clicar_no_botao)
# --------------------------------------------

# 7. Exibimos a janela e iniciamos o loop de execução do programa
janela_principal.show()
sys.exit(app.exec())
