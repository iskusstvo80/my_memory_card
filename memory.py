#создай приложение для запоминания информации 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QPushButton, QLabel, QVBoxLayout,QMessageBox,QRadioButton,QHBoxLayout,QButtonGroup
from random import shuffle
from random import randint
app = QApplication([])
class Quvasho():
    def __init__ (self,qwestion,right_anser,wroung1,wroung2,wroung3):
        self.qwestion = qwestion
        self.right_anser = right_anser
        self.wroung1 = wroung1
        self.wroung2 = wroung2
        self.wroung3 = wroung3

qwestion_list = []


window = QWidget()
window.move(1000,500)


btn_ok = QPushButton('Ответить')
Lb_Question = QLabel('')


RafdioGroupBox = QGroupBox('Варианты ответов:')
rbtn_1 = QRadioButton('1 Октебря')
rbtn_2 = QRadioButton('1 Сентября')
rbtn_3 = QRadioButton('8 Марты')
rbtn_4 = QRadioButton('31 Декабря')


Radigrup = QButtonGroup()
Radigrup.addButton(rbtn_1)
Radigrup.addButton(rbtn_2)
Radigrup.addButton(rbtn_3)
Radigrup.addButton(rbtn_4)



layout_1 = QHBoxLayout()
layout_2 = QVBoxLayout()
layout_3 = QVBoxLayout()
layout_2.addWidget(rbtn_1)
layout_2.addWidget(rbtn_2)
layout_3.addWidget(rbtn_3)
layout_3.addWidget(rbtn_4)

layout_1.addLayout(layout_2)
layout_1.addLayout(layout_3)

RafdioGroupBox.setLayout(layout_1)


AnsGruopBox = QGroupBox('Результвты теста:')
lb_Result = QLabel('')
Lb_Correct = QLabel('')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment= (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(Lb_Correct, alignment= Qt.AlignHCenter, stretch = 2)
AnsGruopBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(Lb_Question,alignment = (Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RafdioGroupBox)
layout_line2.addWidget(AnsGruopBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch = 2)
layout_line3.addStretch(1)



Layout_card = QVBoxLayout()

Layout_card.addLayout(layout_line1,stretch=2)
Layout_card.addLayout(layout_line2,stretch=8)
Layout_card.addStretch(1)
Layout_card.addLayout(layout_line3,stretch=1)
Layout_card.addStretch(1)
Layout_card.setSpacing(5)

def show_result():
    RafdioGroupBox.hide()
    AnsGruopBox.show()
    btn_ok.setText('Следующий вопрос')



def show_question():
    RafdioGroupBox.show()
    AnsGruopBox.hide()
    btn_ok.setText('Ответить')

    Radigrup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    Radigrup.setExclusive(True)
    
def start_test():
    if btn_ok.text() == 'Ответить':
        show_result()
    else:
        show_question()

anser = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q):
    shuffle(anser)
    anser[0].setText(q.right_anser)
    anser[1].setText(q.wroung1)
    anser[2].setText(q.wroung2)
    anser[3].setText(q.wroung3)
    Lb_Question.setText(q.qwestion)
    Lb_Correct.setText(q.right_anser)
    show_question()


def shw_answer():
    if anser[0].isChecked():
        shw_correct('Правильно')
        window.score += 1
    else:
        shw_correct('Не правильно')
    print('Задано вопросов:',window.total,'\nВерный ответов:',window.score,'\nРейтинг:', window.score/window.total * 100,'%')
def next_qustion():
    window.total +=1
    # window.cur_questio +=1
    #if window.cur_questio == len(qwestion_list):
     #   window.cur_questio = 0
    cur_questio = randint(0,len(qwestion_list)-1)
    q = qwestion_list[cur_questio]
    ask(q)
    
def click_OK():
    if btn_ok.text() == 'Ответить':
        shw_answer()
    else:
        next_qustion()

def shw_correct(res):
    lb_Result.setText(res)
    show_result()


q = Quvasho('Как называеют день девушик','8 марта','6 марта','1 октебря','1 апреля') 
q1 = Quvasho('Как зовут призидента Росси:','Путин','Укашенка','Зеленский','Абама')
q2 = Quvasho('Как самая быстрая машина в мире:','Бугатти','Ламбаргини','Ферари','матиз')
qwestion_list.append(q)
qwestion_list.append(q1)
qwestion_list.append(q2)


btn_ok.clicked.connect(click_OK)


window = QWidget()
#window.cur_questio = -1
window.total = 0
window.score = 0
next_qustion()
window.setLayout(Layout_card)
window.setWindowTitle('Memory Card')
window.show()


app.exec_()
