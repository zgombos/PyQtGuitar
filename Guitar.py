from itertools import cycle
from Scale import Note, Scale


class Guitar:
    """ Represent a guitar object.
        Input parameters:
            1. frets:   number of frets
            2. tune:    list of Note objects for tuning """
    def __init__(self, frets, tune):
        self.strings = []
        self.frets = frets + 1  # Add one extra fret for the open string
        self.__notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        self.tuning(tune)

    def __generate_note(self, start_note, num=None):
        """ Generate Note objects starting from the start_note and given octave up to "num".
            If num is not given, up to the the fret number.
            Return a list of Note objects. """
        result = []
        octave = start_note.octave
        index = (self.__notes.index(start_note.name))

        # Define the num value
        if num is None:
            num = self.frets

        # Iterate till the start note
        pool = cycle(self.__notes)
        for i in range(index):
            next(pool)

        # Iterate up to the fret number plus the root note index
        for i in range(index, index + num):
            name = next(pool)
            if name == "C":
                octave += 1
            result.append(Note(name, octave))
        return result

    def __generate_scale_note(self, scale, start_note, num):
        """ Return a list of Note objects from the scale
            using the start_note up to the num """
        result = []
        # Call the  __generate_note function to have a note pool
        note_pool = self.__generate_note(start_note, num)

        # From the note_pool create a list based on the scale
        for note in note_pool:
            if note.name in scale:
                result.append(note)
        return result

    def tuning(self, tune):
        """ Call the self.generate_note function for tuning
            and populate the self.strings object with Note objects based on the tune list"""

        # Remove all elements in self.strings
        del self.strings[:]

        # Fil out the list with new items
        for note in tune:
            string = self.__generate_note(note)
            self.strings.append(string)

    def get_all_scale_notes(self, scale):
        """ Return a list of all notes per string from a scale
            with its position on the guitar fretboard:
            """
        result = []
        # Iterate over the strings object notes, if the guitar note in the scale
        # determinate the position and add it to the list
        for string_number, string in enumerate(self.strings):
            tmp = []
            for note in string:
                if note.name in scale:
                    index = self.strings[string_number].index(note)
                    item = (note, index)
                    tmp.append(item)
            result.append(tmp)
        return result

    def get_three_notes(self, scale, start_note):
        """ Return a list of three notes pattern per string from the scale generator """
        result = []

        # Call the generate_scale_note to have a scale note pool
        # It generate around 35 notes based on the scale type
        scale_note_pool = self.__generate_scale_note(scale, Note('E', 2), 60)

        # Call get_all_scale_notes to get all the notes on the fretboard based on the scale
        notes = self.get_all_scale_notes(scale)

        # Create a generator on the scale notes
        # Iterate till the start_note
        note_pool = cycle(scale_note_pool)
        for i in range(start_note):
            next(note_pool)

        for i in range(6):
            tmp = []
            for j in range(3):
                    note = next(note_pool)
                    for item in notes[i]:
                        if note == item[0]:
                            tmp.append(item)
                            break
            result.append(tmp)
        return result

    def get_four_notes(self, scale, start_note):
        """ Return a list of three notes pattern per string from the scale generator """
        result = []

        # Call the generate_scale_note to have a scale note pool
        # It generate around 35 notes based on the scale type
        scale_note_pool = self.__generate_scale_note(scale, Note('E', 2), 60)

        # Call get_all_scale_notes to get all the notes on the fretboard based on the scale
        notes = self.get_all_scale_notes(scale)

        # Create a generator on the scale notes
        # Iterate till the start_note
        note_pool = cycle(scale_note_pool)
        for i in range(start_note):
            next(note_pool)

        for i in range(6):
            tmp = []
            for j in range(4):
                    note = next(note_pool)
                    for item in notes[i]:
                        if note == item[0]:
                            tmp.append(item)
                            break
            result.append(tmp)
        return result

    def get_box_pattern(self, scale, start_note):
        """ Return a list of notes box pattern per string from the scale
            Notes are not far than 4 frets on a string

        [(("E(2)"), 0), (("F(2)"), 1), (("G(2)"), 3)]
        [(("A(2)"), 0), (("B(2)"), 2), (("C(3)"), 3)]
        [(("D(3)"), 0), (("E(3)"), 2), (("F(3)"), 3)]
        [(("G(3)"), 0), (("A(3)"), 2), (("B(3)"), 4)]
        [(("B(3)"), 0), (("C(4)"), 1), (("D(4)"), 3)]
        [(("E(4)"), 0), (("F(4)"), 1), (("G(4)"), 3)]

        """
        result = []

        # Call get_all_scale_notes to get all the notes on the fretboard
        notes = self.get_all_scale_notes(scale)

        # Get the start note from the first string
        index = notes[0][start_note]

        # Find positions between (-1 < startNote < 3)
        for i in range(6):
            result.append([note for note in notes[i] if (note[1] - index[1] >= -1) and (note[1] - index[1] <= 3)])
        return result

    def get_one_string_pattern(self, scale, start_string):
        """ Return a list of notes pattern on a string """
        result = []

        # Call get_all_scale_notes to get all the notes on the fretboard based on the scale
        notes = self.get_all_scale_notes(scale)
        # Get the notes from the right string
        result.append(notes[start_string])
        return result


def TEST():
    standard_tuning = (Note("E", 2), Note("A", 2), Note("D", 3), Note("G", 3), Note("B", 3), Note("E", 4))
    Gibson = Guitar(23, standard_tuning)
    Ibanez = Guitar(25, standard_tuning)

    Major = Scale("Major", (2, 2, 1, 2, 2, 2), 'three_notes')
    Natural_minor = Scale("Natural Minor", (2, 1, 2, 2, 1, 2), 'three_notes')

    c_major_scale = Major.get_scale_notes("C")
    a_natural_minor_scale = Natural_minor.get_scale_notes("A")

    print('Gibson:')
    # for s in Gibson.strings:
    #     for note in s:
    #         print(note, end="")
    #     print("\n")

    print('Gibson C major all notes:')
    c_all = Gibson.get_all_scale_notes(c_major_scale)
    for i in c_all:
        print(i)
    print('\n')

    print('Gibson C major three notes per string:')
    c_three = Gibson.get_three_notes(c_major_scale, 0)
    for i in c_three:
        print(i)
    print('\n')

    print('Gibson C major box pattern:')
    c_five = Gibson.get_box_pattern(c_major_scale, 1)
    for i in c_five:
        print(i)
    print('\n')

    print('Gibson C major one string pattern:')
    c_five = Gibson.get_one_string_pattern(c_major_scale, 1)
    for i in c_five:
        print(i)

    print('\nIbanez:')
    # for s in Ibanez.strings:
    #     for note in s:
    #         print(note, end="")
    #     print("\n")

    print('Ibanez A natural minor all notes:')
    c_all = Ibanez.get_all_scale_notes(a_natural_minor_scale)
    for i in c_all:
        print(i)
    print('\n')

    print('Ibanez A natural minor three notes per string:')
    c_three = Ibanez.get_three_notes(a_natural_minor_scale, 0)
    for i in c_three:
        print(i)
    print('\n')

    print('Ibanez A natural minor box pattern:')
    c_five = Ibanez.get_box_pattern(a_natural_minor_scale, 1)
    for i in c_five:
        print(i)
    print('\n')

    print('Ibanez A natural minor box pattern:')
    c_five = Ibanez.get_one_string_pattern(a_natural_minor_scale, 3)
    for i in c_five:
        print(i)

if __name__ == "__main__":
    TEST()