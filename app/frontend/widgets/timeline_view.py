import math
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy


class _SpiralCanvas(QWidget):
    """Placeholder spiral — one loop per year, dots for diary entries."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._dates: set[str] = set()
        self.setMinimumSize(400, 400)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    def set_dates(self, dates: set[str]):
        self._dates = dates
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        w, h = self.width(), self.height()
        cx, cy = w / 2, h / 2

        painter.fillRect(0, 0, w, h, QColor("#0d0d1a"))

        # Draw Archimedean spiral (placeholder — each full loop = 1 year)
        painter.setPen(QPen(QColor("#4a4a8a"), 1))
        loops = 8
        steps = loops * 360
        prev = None
        for i in range(steps + 1):
            angle = math.radians(i)
            r = (i / steps) * min(w, h) * 0.45
            x = cx + r * math.cos(angle - math.pi / 2)
            y = cy + r * math.sin(angle - math.pi / 2)
            if prev:
                painter.drawLine(int(prev[0]), int(prev[1]), int(x), int(y))
            prev = (x, y)

        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(QColor("#aaaaff")))
        painter.drawText(int(cx - 120), int(cy + min(w, h) * 0.46), 240, 20,
                         Qt.AlignmentFlag.AlignCenter, "Spiral timeline — coming soon")


class TimelineView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._user_id: str | None = None
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)

        title = QLabel("Timeline")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        self.canvas = _SpiralCanvas()
        layout.addWidget(self.canvas)

    def load(self, user_id: str):
        self._user_id = user_id
        from app.frontend.models import diary_model
        from app.frontend.workers.api_worker import ApiWorker
        worker = ApiWorker(diary_model.dates_with_entries, user_id)
        worker.result.connect(self.canvas.set_dates)
        worker.start()
