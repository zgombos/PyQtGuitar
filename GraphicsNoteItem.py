# Import Qt modules
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QRadialGradient, QFont, QColor
from PyQt5.QtWidgets import QGraphicsItem


class GraphicsNoteItem(QGraphicsItem):
    """ QGraphicsItem to represent a musical note on a scene """
    Type = QGraphicsItem.UserType + 1

    def __init__(self, name, color):
        QGraphicsItem.__init__(self)
        self.name = name
        self.color = color

    def type(self):
        return GraphicsNoteItem.Type

    def boundingRect(self):
        return QRectF(0, 0, 30, 30)

    def paint(self, painter, option, widget):
        ellipse = self.boundingRect()
        gradient = QRadialGradient(0, 8, 20, 0, 8)
        gradient.setColorAt(0.0, Qt.white)
        gradient.setColorAt(0.8, self.color)
        painter.setBrush(gradient)
        painter.setPen(self.color)
        painter.drawEllipse(ellipse)
        painter.setFont(QFont("Verdana", 8))
        painter.setPen(QColor(Qt.white))
        painter.drawText(ellipse, Qt.AlignCenter, self.name)