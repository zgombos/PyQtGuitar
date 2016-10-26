# m_Scene.setSceneRect(m_QImage.rect());
# m_Scene.addPixmap(QPixmap::fromImage(m_QImage,0));
# m_GraphicsView.setScene(&m_Scene);
# m_GraphicsView.fitInView(m_QImage.rect());


# Import Qt modules
from PyQt5.QtCore import Qt, QRectF, QPoint
from PyQt5.QtGui import QPainter, QFont, QColor, QPen, QPainterPath
from PyQt5.QtWidgets import QGraphicsItem


class GraphicsFretboard(QGraphicsItem):
    """ QGraphicsItem to represent a musical note on a scene """
    Type = QGraphicsItem.UserType + 2

    def __init__(self, fret):
        QGraphicsItem.__init__(self)
        # Add 2 to the fret number to get right bounds between two frets
        self.fret = fret + 2
        self.fret_distance = []

        # Set fret distance
        d = 0
        for i in range(self.fret):
            self.fret_distance.append(d)
            d += 60

        # Distance between two strings
        self.string_dist = 30

        self.note_coordinate1 = []
        self.note_coordinate2 = []
        self.note_coordinate3 = []
        self.note_coordinate4 = []
        self.note_coordinate5 = []
        self.note_coordinate6 = []

        # Note coordinates
        for i in range(len(self.fret_distance) - 1):
            # Deduce with half of the note item (15)
            x = self.fret_distance[i] + ((self.fret_distance[i + 1] - self.fret_distance[i]) / 2) - 15
            y = 0
            self.note_coordinate1.append(QPoint(x, y))
            self.note_coordinate2.append(QPoint(x, y + self.string_dist))
            self.note_coordinate3.append(QPoint(x, y + self.string_dist * 2))
            self.note_coordinate4.append(QPoint(x, y + self.string_dist * 3))
            self.note_coordinate5.append(QPoint(x, y + self.string_dist * 4))
            self.note_coordinate6.append(QPoint(x, y + self.string_dist * 5))

        self.note_coordinates = [self.note_coordinate6, self.note_coordinate5, self.note_coordinate4,
                                 self.note_coordinate3, self.note_coordinate2, self.note_coordinate1]

    def type(self):
        return GraphicsFretboard.Type

    def boundingRect(self):
        return QRectF(-30, 0, self.fret_distance[-1], self.string_dist * 6)

    def paint(self, painter, option, widget):
        painter.setRenderHint(QPainter.Antialiasing, True)

        # Draw background
        rect = QRectF(0, 0, self.fret_distance[-1], self.string_dist * 6)
        painter.setBrush(QColor(51, 25, 0))
        painter.drawRect(rect)

        # Draw inlay
        inlay = QPainterPath

        # Draw string
        string_pen = QPen()
        string_pen.setColor(QColor(Qt.white))
        painter.setPen(QColor(Qt.white))
        for i in range(6):
            string_pen.setWidth(i)
            painter.setPen(string_pen)
            painter.drawLine(0, (self.string_dist * i) + 15, self.fret_distance[-1], (self.string_dist * i) + 15)

        # Draw frets
        fret_pen = QPen()
        fret_pen.setColor(QColor(Qt.white))
        fret_pen.setWidth(4)
        painter.setPen(fret_pen)
        for i in self.fret_distance:
            painter.drawLine(i, 0, i, self.string_dist * 6)

        # Draw fret numbers
        painter.setFont(QFont("Verdana", 12))
        painter.setPen(QColor(Qt.white))
        for i in range(len(self.fret_distance) - 1):
            x = self.fret_distance[i] + ((self.fret_distance[i + 1] - self.fret_distance[i]) / 2) - 8
            painter.drawText(x, self.string_dist * 7, str(i))






