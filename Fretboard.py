# Import Qt modules
from PyQt5.QtCore import Qt, QPoint, QRectF, QLineF
from PyQt5.QtGui import QColor, QPen, QBrush, QGradient, QLinearGradient, QPainterPath, QFont
from PyQt5.QtWidgets import QGraphicsTextItem



class Fretboard:
    def draw_fretboard(self, scene, posX, posY):
        # Real 22 frets Gibson guitar scale length
        SCALE_LENGTH = [0, 35.28, 68.59, 100.02, 129.69, 157.69, 184.13, 209.08,
                        232.63, 254.85, 275.83, 295.63, 314.32, 331.98, 348.61,
                        364.34, 379.17, 393.17, 406.39, 418.86, 430.64, 441.75, 452.24]

        # Increase them for better representation
        self.scaleLength = [i * 3 for i in SCALE_LENGTH]

        # Distance between two strings
        DISTANCE = 34

        # Starting cooridnates
        x = posX
        y = posY

        # Note coordinates of the strings
        # Open position coordinates
        self.sNoteCoordinate1 = [QPoint(x, y)]
        self.sNoteCoordinate2 = [QPoint(x, y + DISTANCE)]
        self.sNoteCoordinate3 = [QPoint(x, y + DISTANCE * 2)]
        self.sNoteCoordinate4 = [QPoint(x, y + DISTANCE * 3)]
        self.sNoteCoordinate5 = [QPoint(x, y + DISTANCE * 4)]
        self.sNoteCoordinate6 = [QPoint(x, y + DISTANCE * 5)]

        # Offset from the open position
        OFFSET = 30

        # The remaining position coordinates
        for i in range(len(self.scaleLength) - 1):
            x = self.scaleLength[i] + ((self.scaleLength[i + 1] - self.scaleLength[i]) / 2) + OFFSET - 14
            self.sNoteCoordinate1.append(QPoint(x, y))
            self.sNoteCoordinate2.append(QPoint(x, y + DISTANCE))
            self.sNoteCoordinate3.append(QPoint(x, y + DISTANCE * 2))
            self.sNoteCoordinate4.append(QPoint(x, y + DISTANCE * 3))
            self.sNoteCoordinate5.append(QPoint(x, y + DISTANCE * 4))
            self.sNoteCoordinate6.append(QPoint(x, y + DISTANCE * 5))

        # Store the strings in a list for better iteration
        self.sNoteCoordinates = []
        self.sNoteCoordinates.append(self.sNoteCoordinate6)
        self.sNoteCoordinates.append(self.sNoteCoordinate5)
        self.sNoteCoordinates.append(self.sNoteCoordinate4)
        self.sNoteCoordinates.append(self.sNoteCoordinate3)
        self.sNoteCoordinates.append(self.sNoteCoordinate2)
        self.sNoteCoordinates.append(self.sNoteCoordinate1)

        # Starting guitar string cooridnates
        x = posX
        y = posY

        # Draw outer fretboard box
        whitePen = QPen(Qt.white)
        whitePen.setWidth(5)
        whitePen.setJoinStyle(Qt.MiterJoin)
        brownBrush = QBrush(QColor(75, 30, 0))
        rect1 = QRectF(x, y, self.scaleLength[-1] + OFFSET, DISTANCE * 6)
        scene.addRect(rect1, whitePen, brownBrush)

        whiteBrush = QBrush(Qt.white)
        rect2 = QRectF(x, y, x + OFFSET, DISTANCE * 6)
        scene.addRect(rect2, whitePen, whiteBrush)

        # Starting inlay cooridnates
        x = posX
        y = posY

        # Trapezoid inlay color
        gradient = QLinearGradient(0, 0, 50, 50)
        gradient.setColorAt(0.0, QColor(200, 200, 200))
        gradient.setColorAt(0.5, Qt.white)
        gradient.setColorAt(1.0, QColor(200, 200, 200))
        gradient.setSpread(QGradient.ReflectSpread)
        grayPen = QPen(QColor(216, 216, 216))
        grayBrush = QBrush(gradient)

        # The 3rd, 5th, 7th and 9th inlay
        leftTrim = 5
        rightTrim = 40
        j = 2
        for i in range(4):
            x1 = x + self.scaleLength[j] + ((self.scaleLength[j + 1] - self.scaleLength[j]) / 2) + leftTrim
            x2 = x + self.scaleLength[j + 1] + ((self.scaleLength[i + 2] - self.scaleLength[i + 1]) / 2) - rightTrim
            path = QPainterPath()
            path.moveTo(x1, y + DISTANCE)
            path.lineTo(x1, y + DISTANCE * 5)
            path.lineTo(x2, y + DISTANCE * 5 - 20)
            path.lineTo(x2, y + DISTANCE + 15)
            path.closeSubpath()
            scene.addPath(path, grayPen, grayBrush)
            leftTrim += 2
            rightTrim -= 5
            j += 2

        # The 12th inlay
        leftTrim = 15
        rightTrim = 8
        x1 = x + self.scaleLength[11] + ((self.scaleLength[12] - self.scaleLength[11]) / 2) + leftTrim
        x2 = x + self.scaleLength[12] + ((self.scaleLength[13] - self.scaleLength[12]) / 2) - rightTrim
        path = QPainterPath()
        path.moveTo(x1, y + DISTANCE)
        path.lineTo(x1, y + DISTANCE * 5)
        path.lineTo(x2, y + DISTANCE * 5 - 20)
        path.lineTo(x2, y + DISTANCE + 15)
        path.closeSubpath()
        scene.addPath(path, grayPen, grayBrush)

        # The 15th, 17th, 19th and 21th inlay
        leftTrim = 15
        rightTrim = 28
        j = 14
        for i in range(4):
            x1 = x + self.scaleLength[j] + ((self.scaleLength[j + 1] - self.scaleLength[j]) / 2) + leftTrim
            x2 = x + self.scaleLength[j + 1] + ((self.scaleLength[i + 2] - self.scaleLength[i + 1]) / 2) - rightTrim
            path = QPainterPath()
            path.moveTo(x1, y + DISTANCE)
            path.lineTo(x1, y + DISTANCE * 5)
            path.lineTo(x2, y + DISTANCE * 5 - 20)
            path.lineTo(x2, y + DISTANCE + 15)
            path.closeSubpath()
            scene.addPath(path, grayPen, grayBrush)
            leftTrim += 2
            rightTrim -= 1 + (i + 1)
            j += 2

        # Starting guitar string cooridnates
        x = posX
        y = posY - 20

        # Draw the guitar strings
        s = QLineF(x, y, x + self.scaleLength[-1] + OFFSET, y)
        whitePen = QPen(Qt.white)
        whitePen.setWidth(1)
        startHPos = DISTANCE
        stringWidth = 1
        for i in range(6):
            whitePen.setWidth(stringWidth)
            guitarString = scene.addLine(s, whitePen)
            guitarString.setPos(0, startHPos)
            startHPos += DISTANCE
            stringWidth += 0.4

        # Starting fret cooridnates
        x = posX
        y = posY

        # Draw the frets
        fretPen = QPen(Qt.white)
        fretPen.setWidth(5)
        fret = QLineF(x + OFFSET, y, x + OFFSET, y + DISTANCE * 6 - 5)
        for i in range(len(self.scaleLength)):
            guitarFret = scene.addLine(fret, fretPen)
            guitarFret.setPos(self.scaleLength[i], 0)

        # Add fret numbers
        for i in range(22):
            fret_num = QGraphicsTextItem(str(i))
            fret_num.setFont(QFont("Verdana", 20))
            fret_num.setDefaultTextColor(QColor(Qt.red))
            fret_num.setPos(self.scaleLength[i], 220)
            scene.addItem(fret_num)