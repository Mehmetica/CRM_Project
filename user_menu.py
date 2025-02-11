from PyQt6 import QtCore, QtGui, QtWidgets

class UserMenuWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Pencere başlığını ve boyutlarını ayarla
        self.setObjectName("UserMenu")
        self.resize(600, 400)
        self.setFixedSize(600, 400)

        # Arka plan ekleme
        self.label = QtWidgets.QLabel(parent=self)
        self.label.setGeometry(QtCore.QRect(0, -5, 601, 451))
        self.label.setPixmap(QtGui.QPixmap("/Users/mehmetgezer/Python Calismalari/Bitirme_Projesi/diger_dosyalar/background.jpg"))
        self.label.setScaledContents(True)

        # Çerçeve (frame) ekleme
        self.frame = QtWidgets.QFrame(parent=self)
        self.frame.setGeometry(QtCore.QRect(80, 100, 441, 241))
        self.frame.setStyleSheet("QFrame { background-color: rgb(239, 238, 236); border: 2px solid black; border-radius: 10px; }")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        # Butonlar
        self.p_Applications = QtWidgets.QPushButton(parent=self.frame)
        self.p_Applications.setGeometry(QtCore.QRect(120, 40, 211, 41))
        self.p_Applications.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid #000000; } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        self.p_Applications.setText("Applications")

        self.p_mentorMeeting = QtWidgets.QPushButton(parent=self.frame)
        self.p_mentorMeeting.setGeometry(QtCore.QRect(120, 90, 211, 41))
        self.p_mentorMeeting.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid #000000; } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        self.p_mentorMeeting.setText("Interviews")

        self.pushButton_exit = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_exit.setGeometry(QtCore.QRect(180, 190, 101, 31))
        self.pushButton_exit.setStyleSheet("QPushButton { background-color: rgb(211, 0, 0); color: white; border-radius: 10px; border: 2px solid #000000; } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        self.pushButton_exit.setText("Exit")
        self.pushButton_exit.clicked.connect(self.close)  # Çıkış butonunu bağladık

        self.p_mentorMeeting_2 = QtWidgets.QPushButton(parent=self.frame)
        self.p_mentorMeeting_2.setGeometry(QtCore.QRect(120, 140, 211, 41))
        self.p_mentorMeeting_2.setStyleSheet("QPushButton { background-color: rgb(2, 50, 90); color: white; border-radius: 10px; border: 2px solid #000000; } QPushButton:hover { background-color: rgb(223, 194, 107); }")
        self.p_mentorMeeting_2.setText("Mentor Meeting")

        # Başlık etiketi
        self.label_title = QtWidgets.QLabel(parent=self)
        self.label_title.setGeometry(QtCore.QRect(130, 80, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("background-color: rgb(223, 194, 107); color: rgb(2, 50, 90); border-radius: 10px; padding: 5px;")
        self.label_title.setText("              User Menu")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UserMenuWindow()
    window.show()
    sys.exit(app.exec())






# # Form implementation generated from reading ui file '/Users/mehmetgezer/Python Calismalari/Bitirme_Projesi/diger_dosyalar/tercihler.ui'
# #
# # Created by: PyQt6 UI code generator 6.4.2
# #
# # WARNING: Any manual changes made to this file will be lost when pyuic6 is
# # run again.  Do not edit this file unless you know what you are doing.


# from PyQt6 import QtCore, QtGui, QtWidgets


# class UserMenuWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         Form.setObjectName("Form")
#         Form.resize(600, 400)
#         Form.setFixedSize(600, 400)
#         # Form.resize(594, 443)
#         self.label = QtWidgets.QLabel(parent=Form)
#         self.label.setGeometry(QtCore.QRect(0, -5, 601, 451))
#         self.label.setText("")
#         self.label.setPixmap(QtGui.QPixmap("/Users/mehmetgezer/Python Calismalari/Bitirme_Projesi/diger_dosyalar/background.jpg"))
#         self.label.setScaledContents(True)
#         self.label.setObjectName("label")
#         self.frame = QtWidgets.QFrame(parent=Form)
#         self.frame.setGeometry(QtCore.QRect(80, 100, 441, 241))
#         self.frame.setStyleSheet("QFrame {\n"
# "    background-color: rgb(239, 238, 236); /* Açık gri arka plan */\n"
# "    border: 2px solid black; /* Siyah kenarlık */\n"
# "    border-radius: 10px; /* Yuvarlatılmış köşeler */\n"
# "}")
#         self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
#         self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
#         self.frame.setObjectName("frame")
#         self.p_Applications = QtWidgets.QPushButton(parent=self.frame)
#         self.p_Applications.setGeometry(QtCore.QRect(120, 40, 211, 41))
#         self.p_Applications.setStyleSheet("QPushButton {\n"
# "    background-color: rgb(2, 50, 90); /* Yeşil arka plan */\n"
# "    color: white; /* Beyaz yazı */\n"
# "    border-radius: 10px; /* Yuvarlak köşeler */\n"
# "    border: 2px solid #000000; /* Siyah kenarlık */\n"
# "   \n"
# "}\n"
# "\n"
# "QPushButton:hover {\n"
# "    background-color: rgb(223, 194, 107); /* Üzerine gelince açık yeşil */\n"
# "}")
#         self.p_Applications.setObjectName("p_Applications")
#         self.p_mentorMeeting = QtWidgets.QPushButton(parent=self.frame)
#         self.p_mentorMeeting.setGeometry(QtCore.QRect(120, 90, 211, 41))
#         self.p_mentorMeeting.setStyleSheet("QPushButton {\n"
# "    background-color: rgb(2, 50, 90); /* Yeşil arka plan */\n"
# "    color: white; /* Beyaz yazı */\n"
# "    border-radius: 10px; /* Yuvarlak köşeler */\n"
# "    border: 2px solid #000000; /* Siyah kenarlık */\n"
# "   \n"
# "}\n"
# "\n"
# "QPushButton:hover {\n"
# "    background-color: rgb(223, 194, 107); /* Üzerine gelince açık yeşil */\n"
# "}")
#         self.p_mentorMeeting.setObjectName("p_mentorMeeting")
#         self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame)
#         self.pushButton_3.setGeometry(QtCore.QRect(180, 190, 101, 31))
#         self.pushButton_3.setStyleSheet("QPushButton {\n"
# "    background-color: rgb(211, 0, 0); /* Yeşil arka plan */\n"
# "    color: white; /* Beyaz yazı */\n"
# "    border-radius: 10px; /* Yuvarlak köşeler */\n"
# "    border: 2px solid #000000; /* Siyah kenarlık */\n"
# "   \n"
# "}\n"
# "\n"
# "QPushButton:hover {\n"
# "    background-color: rgb(223, 194, 107); /* Üzerine gelince açık yeşil */\n"
# "}")
#         self.pushButton_3.setObjectName("pushButton_3")
#         self.p_mentorMeeting_2 = QtWidgets.QPushButton(parent=self.frame)
#         self.p_mentorMeeting_2.setGeometry(QtCore.QRect(120, 140, 211, 41))
#         self.p_mentorMeeting_2.setStyleSheet("QPushButton {\n"
# "    background-color: rgb(2, 50, 90); /* Yeşil arka plan */\n"
# "    color: white; /* Beyaz yazı */\n"
# "    border-radius: 10px; /* Yuvarlak köşeler */\n"
# "    border: 2px solid #000000; /* Siyah kenarlık */\n"
# "   \n"
# "}\n"
# "\n"
# "QPushButton:hover {\n"
# "    background-color: rgb(223, 194, 107); /* Üzerine gelince açık yeşil */\n"
# "}")
#         self.p_mentorMeeting_2.setObjectName("p_mentorMeeting_2")
#         self.label_2 = QtWidgets.QLabel(parent=Form)
#         self.label_2.setGeometry(QtCore.QRect(130, 80, 341, 51))
#         font = QtGui.QFont()
#         font.setFamily("Onyx")
#         font.setPointSize(28)
#         self.label_2.setFont(font)
#         self.label_2.setStyleSheet("background-color: rgb(223, 194, 107);  /* Arka plan rengi */\n"
# "color: rgb(2, 50, 90);  /* Yazı rengi */\n"
# "border-radius: 10px;  /* Köşeleri yuvarlat */\n"
# "padding: 5px;  /* Buton içindeki boşluk */")
#         self.label_2.setObjectName("label_2")
#         self.label_2.setBuddy(self.label_2)

#         self.retranslateUi(Form)
#         QtCore.QMetaObject.connectSlotsByName(Form)

#     def retranslateUi(self, Form):
#         _translate = QtCore.QCoreApplication.translate
#         Form.setWindowTitle(_translate("Form", "Form"))
#         self.p_Applications.setText(_translate("Form", "Applications"))
#         self.p_mentorMeeting.setText(_translate("Form", "Interviews"))
#         self.pushButton_3.setText(_translate("Form", "Exit"))
#         self.p_mentorMeeting_2.setText(_translate("Form", "Mentor Meeting"))
#         self.label_2.setText(_translate("Form", "          Preference Menu"))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = UserMenuWindow()
    
#     Form.show()
#     sys.exit(app.exec())