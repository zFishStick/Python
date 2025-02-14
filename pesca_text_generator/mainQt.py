from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QFrame, QDialog, QMainWindow, QPushButton, QVBoxLayout
from PyQt6.QtGui import QFont, QPixmap, QFontDatabase
from PyQt6.QtCore import Qt, QRect
from PIL import ImageGrab
import sys

mobile_width = 1080 / 3
mobile_height = 1920 / 3

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        print("Inizializzazione finestra")

        self.setWindowTitle("La Pesca del Giorno")
        self.setGeometry(100, 100, int(mobile_width), int(mobile_height))  
        self.load_fonts()

        # Font personalizzati
        self.title_font = QFont("Marykate", 22, QFont.Weight.Bold)
        self.text_font = QFont("Bryndan Write", 18, QFont.Weight.Bold)

        # Frame principale (equivalente a auxFrame)
        self.auxFrame = QFrame(self)
        self.auxFrame.setStyleSheet("background-color: #f2b28c; border-radius: 16px;")
        self.auxFrame.setGeometry(30, 30, 300, 520)

        # Titolo (equivalente a label_frame)
        self.label_frame = QFrame(self)
        self.label_frame.setStyleSheet("background-color: #d2665a; border-radius: 16px;")
        self.label_frame.setGeometry(55, 5, 250, 50)

        self.title_label = QLabel("La Pesca del Giorno", self.label_frame)
        self.title_label.setFont(self.title_font)
        self.title_label.setStyleSheet("color: white;")
        self.title_label.setGeometry(25, 10, 200, 30)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Textbox (equivalente a CTkTextbox)
        self.textbox = QTextEdit(self.auxFrame)
        self.textbox.setFont(self.text_font)
        self.textbox.setStyleSheet("background-color: #f2b28c; border: none;")
        self.textbox.setGeometry(10, 30, 290, 460)
        self.textbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Bottone (equivalente a CTkButton)
        self.button = QPushButton("Scarica", self)
        self.button.setFont(self.text_font)
        self.button.setStyleSheet("background-color: #d2665a; color: white; border-radius: 8px; padding: 8px;")
        self.button.setGeometry(130, 570, 100, 40)
        self.button.clicked.connect(self.button_callback)

        # Immagine (equivalente a CTkImage)
        try:
            pixmap = QPixmap("peach_king.png")
            if pixmap.isNull():
                print("Immagine non trovata o non valida.")
            else:
                self.image_label = QLabel(self.auxFrame)
                self.image_label.setPixmap(pixmap.scaled(220, 250, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
                self.image_label.setGeometry(40, 250, 220, 250)
        except Exception as e:
            print(f"Errore nel caricare l'immagine: {e}")

    def load_fonts(self):
        font_path = "Bryndan_Write.ttf"  # Modifica questo con il percorso effettivo
        if QFontDatabase.addApplicationFont(font_path) == -1:
            print("Errore nel caricare il font 'Bryndan_Write'. Verifica il percorso del file.")

    def button_callback(self):
        screenshot = self.grab(QRect(0, 5, 350, 550))  # Area che comprende titolo e textbox
        screenshot.save("screenshot.png", "PNG")
        dlg = QDialog(self)
        dlg.setWindowTitle("Conferma")
        dlg.setGeometry(200, 200, 200, 100)
        confirm_button = QPushButton("OK", dlg)
        confirm_button.clicked.connect(dlg.accept)
        
        layout = QVBoxLayout()   
        message = QLabel("Screenshot salvato come screenshot.png")
        layout.addWidget(message)
        layout.addWidget(confirm_button)
        dlg.setLayout(layout)
        
        dlg.exec()

if __name__ == "__main__":
    print("Avvio dell'applicazione...")  # Debug per vedere se si avvia
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
