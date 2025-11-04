import sys
import re
from PyQt5.QtGui import QColor
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication


DVD_PATH = "/Users/juanjo/Local/UC/Extracurricular/IIC2233-T-2025-2/IIC2233-Tutoria/Sesiones/S10/Actividad/resources/DVD_logo.svg"


class DVDLogo(QSvgWidget):
    def __init__(self, svg_path):
        super().__init__()
        self.resize(105, 60)
        self.svg_path = svg_path
        self.current_color = QColor("white")
        self._apply_color(self.current_color)

    def _apply_color(self, color):
        """Recolor the SVG by modifying the global fill attribute in the <svg> tag."""
        with open(self.svg_path, "r") as f:
            svg_data = f.read()

        hex_color = color.name()

        svg_colored = re.sub(
            r'fill\s*=\s*["\']#[0-9A-Fa-f]{3,6}["\']',
            f'fill="{hex_color}"',
            svg_data,
            count=1
        )

        self.load(svg_colored.encode("utf-8"))

    def set_color(self, color):
        self.current_color = color
        self._apply_color(color)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = DVDLogo(DVD_PATH)
    ventana.show()
    sys.exit(app.exec_())
