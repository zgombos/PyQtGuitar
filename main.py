# Import Python modules
import sys

# Import Qt modules
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QGraphicsTextItem

# Import the compiled UI module
# from MainWindow import Ui_MainWindow
from MainWindow import Ui_MainWindow

# Import custom modules
from Guitar import Guitar
from GraphicsFretboard import GraphicsFretboard
from Scale import Note, Scale
from GraphicsNoteItem import GraphicsNoteItem


# Create a class for the main window
class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Setup the ui form
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create a new QGraphicsScene and show it on the ui
        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(QColor(120, 120, 120))
        self.ui.graphicsView.setScene(self.scene)
        self.ui.graphicsView.show()

        # Setup tuning
        self.tuning = [ ('Standard Tuning', [Note("E", 2), Note("A", 2), Note("D", 3), Note("G", 3), Note("B", 3), Note("E", 4)]),
                        ('Dropped D', [Note("D", 2), Note("A", 2), Note("D", 3), Note("G", 3), Note("B", 3), Note("E", 4)]),
                        ('Dropped C', [Note("C", 2), Note("G", 2), Note("C", 3), Note("F", 3), Note("A", 3), Note("D", 4)])]

        t1 = QGraphicsTextItem(); t2 = QGraphicsTextItem(); t3 = QGraphicsTextItem()
        t4 = QGraphicsTextItem(); t5 = QGraphicsTextItem(); t6 = QGraphicsTextItem()
        self.tuning_list = [t1, t2, t3, t4, t5, t6]

        # Define fret number
        self.FRETS = 22

        # Create a new Guitar object
        self.GibsonGuitar = Guitar(self.FRETS, self.tuning[0][1])

        # Create a new Guitar Fretboard object and show it on the scene
        self.GibsonGuitar_Fretboard = GraphicsFretboard(self.FRETS)
        self.GibsonGuitar_Fretboard.setPos(0, 0)
        self.scene.addItem(self.GibsonGuitar_Fretboard)

        # Draw the tuning
        self.draw_tuning(self.tuning[0][1])

        # Populate the notes pool
        self.notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

        # Populate the scales pool
        self.scales = [Scale("Pentatonic Major", [2, 2, 3, 2, 3], 'box_pattern'),
                       Scale("Pentatonic Minor", [3, 2, 2, 3, 2], 'box_pattern'),
                       Scale("Pentatonic Blues", [3, 2, 1, 1, 3, 2], 'box_pattern'),
                       Scale("Major", [2, 2, 1, 2, 2, 2, 1], 'three_notes'),
                       Scale("Ionian", [2, 2, 1, 2, 2, 2, 1], 'three_notes'),
                       Scale("Dorian", [2, 1, 2, 2, 2, 1, 2], 'three_notes'),
                       Scale("Phrygian", [1, 2, 2, 2, 1, 2, 2], 'three_notes'),
                       Scale("Lydian", [2, 2, 2, 1, 2, 2, 1], 'three_notes'),
                       Scale("Mixolydian", [2, 2, 1, 2, 2, 1, 2], 'three_notes'),
                       Scale("Aeolian", [2, 1, 2, 2, 1, 2, 2], 'three_notes'),
                       Scale("Locrian", [1, 2, 2, 1, 2, 2, 2], 'three_notes'),
                       Scale("Minor", [2, 1, 2, 2, 1, 2, 2], 'three_notes'),
                       Scale("Harmonic Minor", [2, 1, 2, 2, 1, 3, 1], 'three_notes'),
                       Scale("Melodic Minor - Ascending", [2, 1, 2, 2, 2, 2, 1], 'three_notes'),
                       Scale("Melodic Minor - Descending", [2, 1, 2, 2, 1, 2, 2], 'three_notes'),
                       Scale("Chromatic", [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'three_notes'),
                       Scale("Whole Tone", [2, 2, 2, 2, 2, 2], 'three_notes'),
                       Scale("Diminished", [2, 1, 2, 1, 2, 1, 2], 'four_notes')
                       ]

        # Add notes and scales to the comboboxes
        for note in self.notes:
            self.ui.rootComboBox.addItem(note)
        for scale in self.scales:
            self.ui.scaleComboBox.addItem(scale.name)
        for item in self.tuning:
            self.ui.tuningComboBox.addItem(item[0])

        # Set the init value to the first item
        self.ui.rootComboBox.setCurrentIndex = 0
        self.ui.scaleComboBox.setCurrentIndex = 0

        # Setup the root note and the current scale to be the first item from the combobox
        self.root_note = self.notes[self.ui.rootComboBox.currentIndex()]
        self.currentScale = self.scales[self.ui.scaleComboBox.currentIndex()]
        self.scale = self.currentScale.get_scale_notes(self.root_note)
        self.update_repr()

        # Signaling if combobox has changed
        self.ui.rootComboBox.currentIndexChanged.connect(self.update_ui)
        self.ui.scaleComboBox.currentIndexChanged.connect(self.update_ui)
        self.ui.tuningComboBox.currentIndexChanged.connect(self.update_tuning)

        # Set the initial position for the scale draw
        self.newPos = 0

        # Set the initial string number for the one sting per scale representation
        self.sting_num = 0

        # Length of the scale
        self.intervalLength = len(self.currentScale.intervals)

        # QTimer object for animation
        self.timer = QTimer()
        self.is_animation_active = False

        # Variable to store the actual scale on the guitar for drawing
        # It based on the Radio Button selection
        self.notes_to_draw = []

    def update_ui(self):
        """ Callback for ComboBox signaling
            Update the root note and the scale """

        self.root_note = self.notes[self.ui.rootComboBox.currentIndex()]
        self.currentScale = self.scales[self.ui.scaleComboBox.currentIndex()]
        self.scale = self.currentScale.get_scale_notes(self.root_note)
        self.intervalLength = len(self.currentScale.intervals)
        self.update_repr()

    def update_tuning(self):
        """ Update the tuning based on the combo box selection"""
        # Get the current tuning from the combobox index
        current_tuning = self.tuning[self.ui.tuningComboBox.currentIndex()]

        # Update the Guitar object
        self.GibsonGuitar.tuning(current_tuning[1])

        # Update the scene
        for note, text in zip(current_tuning[1], self.tuning_list):
            text.setPlainText(note.name)

    def update_repr(self):
        """ Update the scale representation """
        if self.currentScale.get_scale_repr() == 'box_pattern':
            self.ui.boxPatternRadioButton.setChecked(True)
        if self.currentScale.get_scale_repr() == 'three_notes':
            self.ui.threeNotesRadioButton.setChecked(True)
        if self.currentScale.get_scale_repr() == 'four_notes':
            self.ui.fourNotesRadioButton.setChecked(True)

    def update_scale_pos(self, pos):
        """ Update the scale position """
        self.newPos = pos

        if self.ui.boxPatternRadioButton.isChecked():
            self.notes_to_draw = self.GibsonGuitar.get_box_pattern(self.scale, self.newPos)
        if self.ui.threeNotesRadioButton.isChecked():
            self.notes_to_draw = self.GibsonGuitar.get_three_notes(self.scale, self.newPos)
        if self.ui.fourNotesRadioButton.isChecked():
            self.notes_to_draw = self.GibsonGuitar.get_four_notes(self.scale, self.newPos)
        if self.ui.oneStringRadioButton.isChecked():
            self.notes_to_draw = self.GibsonGuitar.get_one_string_pattern(self.scale, self.newPos)

    def clear_fretboard(self):
        """ Delete all GraphicsNoteItem from the scene """
        for item in self.scene.items():
            if item.type() == GraphicsNoteItem.UserType + 1:
                self.scene.removeItem(item)
        self.scene.update()

    def draw_tuning(self, tuning):
        """ Draw the tuning on the scene """
        # Reverse the order
        tuning_notes = tuning[::-1]
        y = 150
        # Iterate over the tuning_notes and the QGraphicsTextItem parallel
        # Set the tuning_notes content for the self.tuning_list QGraphicsTextItems
        for note, text in zip(tuning_notes, self.tuning_list):
            text.setPlainText(note.name)
            text.setFont(QFont("Verdana", 14))
            text.setDefaultTextColor(QColor(Qt.white))
            # Set the position and add it to the scene
            text.setPos(-30, y)
            self.scene.addItem(text)
            y -= 30
        self.scene.update()

    def draw_notes(self, notes):
        """ Draw guitar notes on the scene from the notes list """
        for s, string in enumerate(notes):
            for note in string:
                if note[0].name == self.root_note:
                    note_color = QColor('red')
                else:
                    note_color = QColor('green')
                # First item from the tuple is the Note object
                note_item = GraphicsNoteItem(note[0].name, note_color)
                # Second item from the tuple is the position on the string
                note_index = note[1]
                # Get the note coordinate from the fretboard
                note_item.setPos(self.GibsonGuitar_Fretboard.note_coordinates[s][note_index])
                self.scene.addItem(note_item)

    def draw_one_string_scale(self, notes, string_num):
        """ Draw guitar notes on the scene from the notes list """
        for item in notes:
            for note in item:
                if note[0].name == self.root_note:
                    note_color = QColor('red')
                else:
                    note_color = QColor('green')
                # First item from the tuple is the Note object
                note_item = GraphicsNoteItem(note[0].name, note_color)
                # Second item from the tuple is the position on the string
                note_index = note[1]
                # Get the note coordinate from the fretboard
                note_item.setPos(self.GibsonGuitar_Fretboard.note_coordinates[string_num][note_index])
                self.scene.addItem(note_item)

    def drawFirstPos(self):
        """ Callback function for firstPushButton """
        # If the animation still running stop it
        if self.is_animation_active:
            self.stopAnimation()

        # Clear the fretboard
        self.clear_fretboard()

        # Set the string number back to zero if oneStringRadioButton is checked
        # Get the updated scale notes and draw them
        if self.ui.oneStringRadioButton.isChecked():
            self.sting_num = 0
            self.update_scale_pos(self.sting_num)
            self.draw_one_string_scale(self.notes_to_draw, self.sting_num)
        else:
            # Set the position back to zero
            self.newPos = 0
            # Update the pos and draw the notes on the fretboard
            self.update_scale_pos(self.newPos)
            self.draw_notes(self.notes_to_draw)

    def drawNextPos(self):
        """ Callback function for nextPushButton """
        # If the animation still running stop it
        # if self.is_animation_active:
        #     self.stopAnimation()

        # Clear the fretboard
        self.clear_fretboard()

        # Set the string number back to zero if oneStringRadioButton is checked
        # Get the updated scale notes and draw them
        if self.ui.oneStringRadioButton.isChecked():
            # Increase the string_num by one if possible, if not set it back to zero
            if self.sting_num == 5:
                self.sting_num = 0
            else:
                self.sting_num += 1
            self.update_scale_pos(self.sting_num)
            self.draw_one_string_scale(self.notes_to_draw, self.sting_num)
        else:
            # Check the position, it cannot be larger than the available notes in the scale
            # Increase it by one if possible, if not set it back to zero
            if self.newPos == self.intervalLength:
                self.newPos = 0
            else:
                self.newPos += 1
            # Update the pos and draw the notes on the fretboard
            self.update_scale_pos(self.newPos)
            self.draw_notes(self.notes_to_draw)

    def drawPrevPos(self):
        """ Callback function for prevPushButton """
        # If the animation still running stop it
        if self.is_animation_active:
            self.stopAnimation()

        # Clear the fretboard
        self.clear_fretboard()

        # Set the string number back to zero if oneStringRadioButton is checked
        # Get the updated scale notes and draw them
        if self.ui.oneStringRadioButton.isChecked():
            # Increase the string_num by one if possible, if not set it back to zero
            if self.sting_num <= 0:
                self.sting_num = 5
            else:
                self.sting_num -= 1
            self.update_scale_pos(self.sting_num)
            self.draw_one_string_scale(self.notes_to_draw, self.sting_num)
        else:
            # Check the position, it cannot be larger than the available notes in the scale
            # Decrease it by one if possible
            if self.newPos <= 0:
                self.newPos = self.intervalLength
            else:
                self.newPos -= 1
            # Update the pos and draw the notes on the fretboard
            self.update_scale_pos(self.newPos)
            self.draw_notes(self.notes_to_draw)

    def drawAllPos(self):
        """ Callback function for allPushButton """
        # If the animation still running stop it
        if self.is_animation_active:
            self.stopAnimation()

        # Clear the fretboard
        self.clear_fretboard()

        # Draw all scale notes on the fretboard
        notes = self.GibsonGuitar.get_all_scale_notes(self.scale)
        self.draw_notes(notes)

    def __animate(self):
        """ Callback function for QTimer timeout signal """
        self.is_animation_active = True
        self.drawNextPos()

    def startAnimation(self):
        """ Callback function for startAnimPushButton """
        self.timer.timeout.connect(self.__animate)
        self.timer.start(1000)

    def stopAnimation(self):
        """ Callback function for stopAnimPushButton """
        self.is_animation_active = False
        self.timer.stop()


def main():
    # Show our MainWindow
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
