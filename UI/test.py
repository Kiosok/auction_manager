from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication([])
app.setStyle('Fusion')


# Create a window
window = QWidget()
window.setWindowTitle("My Window")

# Add widgets to the window
# ...

# Show the window
window.show()
app.exec()

