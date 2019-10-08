from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import main

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1749, 902)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.OpenImage = QtWidgets.QPushButton(self.centralwidget)
        self.OpenImage.setMinimumSize(QtCore.QSize(200, 40))
        self.OpenImage.setStyleSheet("font: 16pt \"Georgia\";")
        self.OpenImage.setObjectName("OpenImage")
        self.horizontalLayout_3.addWidget(self.OpenImage)
        self.OpenDataSet = QtWidgets.QPushButton(self.centralwidget)
        self.OpenDataSet.setMinimumSize(QtCore.QSize(200, 40))
        self.OpenDataSet.setStyleSheet("font: 16pt \"Georgia\";")
        self.OpenDataSet.setObjectName("Open CSS Data")
        self.horizontalLayout_3.addWidget(self.OpenDataSet)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.OriginalImage = QtWidgets.QLabel(self.centralwidget)
        self.OriginalImage.setMinimumSize(QtCore.QSize(600, 500))
        self.OriginalImage.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.OriginalImage.setText("")
        self.OriginalImage.setScaledContents(True)
        self.OriginalImage.setObjectName("OriginalImage")
        self.horizontalLayout.addWidget(self.OriginalImage)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.AlteredImage = QtWidgets.QLabel(self.centralwidget)
        self.AlteredImage.setMinimumSize(QtCore.QSize(600, 500))
        self.AlteredImage.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.AlteredImage.setText("")
        self.AlteredImage.setScaledContents(True)
        self.AlteredImage.setObjectName("AlteredImage")
        self.horizontalLayout.addWidget(self.AlteredImage)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.Convert = QtWidgets.QPushButton(self.centralwidget)
        self.Convert.setMinimumSize(QtCore.QSize(150, 30))
        self.Convert.setStyleSheet("font: 16pt \"Georgia\";")
        self.Convert.setObjectName("Convert")
        self.horizontalLayout_4.addWidget(self.Convert)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)



        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.OpenImage.clicked.connect(self.openFileNameDialog)
        self.Convert.clicked.connect(self.convert_clicked)
        self.OpenDataSet.clicked.connect(self.openDataSetfun)
        # self.openFileNameDialog()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","Image files (*.jpg *.png *.jpeg)", options=options)
        if fileName:
            print(fileName)
            self.fileName=fileName
            pixmap=QtGui.QPixmap(self.fileName)
            self.OriginalImage.setPixmap(pixmap)
            self.progressBar.setValue(0)         
    
    css=0

    def openDataSetfun(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","Text Files (*.txt *.csv)", options=options)
        if fileName:
            print(fileName)
            self.CSSData=fileName
            self.css=1
            points = []
            with open(self.CSSData, 'r')as f:
                data = main.csv.reader(f, quoting=main.csv.QUOTE_NONNUMERIC)
                for row in data:
                    row = [int(x) for x in row]
                    points.append(row)
            for i in range(len(points)):
                main.t.root = main.t.insert(main.t.root, points[i])
            QtWidgets.QMessageBox.about(None,"Import","Imported the Data Successfully")
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.OpenImage.setText(_translate("MainWindow", "Select Image"))
        self.Convert.setText(_translate("MainWindow", "Convert"))
        self.OpenDataSet.setText(_translate("MainWindow", "Open CSS Data"))

    prog=0

    def convert_clicked(self): 
        try:
            im = main.Image.open(self.fileName)    
        except :
            QtWidgets.QMessageBox.about(None,"Error","Please Provide the Correct Image")
            return
        if(self.css==0):
            QtWidgets.QMessageBox.about(None,"Error","Please Provide the CSS DATA")
            return
       
        pix = im.load()
        tot=im.size[0]*im.size[1]
        cur=0
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                m = pix[x, y]
                # file.write(str(m)+' ')
                n = main.t.nearestNeighbour(main.t.root, m[0],m[1],m[2], 0, 1000000)
                pix[x, y] = tuple(n[0])
                cur+=1
                val=int((cur/tot)*100)
                self.progressBar.setValue(val)
                # file.write(str(pix[x,y])+'\n')
        im.save('Output.png')
        print("Completed")
        pixmap=QtGui.QPixmap('Output.png')
        # self.verticalLayout_2.removeWidget(self.progressBar)
        # self.progressBar.deleteLater()
        # self.progressBar=None
        # self.prog==0
        self.AlteredImage.setPixmap(pixmap)
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

