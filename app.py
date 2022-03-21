import sys
from validacpf import valida_cpf
from geracpf import gera_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow
import design_cpf

class GeraValidaCPF(QMainWindow, design_cpf.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setFixedSize(600, 200)
        self.centralwidget.setStyleSheet('* {background: #1C1C1C;}')

        self.btnGeraCPF.clicked.connect(self.gera)
        self.btnValidaCPF.clicked.connect(self.valida)

        self.labelRetorno.setStyleSheet('* {background: #363636; color: #ADFF2F;}')
        self.label.setStyleSheet('* {color: #a9a9a9;}')
        self.label_2.setStyleSheet('* {color: #a9a9a9;}')
        self.btnValidaCPF.setStyleSheet('* {color: #a9a9a9;}')
        self.btnGeraCPF.setStyleSheet('* {color: #a9a9a9;}')
        self.inputValidaCPF.setStyleSheet('* {background: #363636; color: #a9a9a9;}')


    def valida(self):
        cpf = self.inputValidaCPF.text()
        self.labelRetorno.setText(str(valida_cpf(cpf)))
        

    def gera(self):
        self.labelRetorno.setText(str(gera_cpf()))
        

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_cpf = GeraValidaCPF()
    gera_valida_cpf.show()
    qt.exec_()
