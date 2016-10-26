# Import Qt modules
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QGraphicsView


class GarphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super(GarphicsView, self).__init__(parent)
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.setRenderHint(QPainter.Antialiasing)
        self.setRenderHint(QPainter.TextAntialiasing)

    def wheelEvent(self, event):
        point = event.angleDelta()
        factor = 1.41 ** (-point.y() / 240.0)
        self.scale(factor, factor)




