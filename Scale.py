from itertools import cycle, islice


class Note:
    def __init__(self, name, octave):
        self.name = name
        self.octave = octave

    def name(self):
        return self.name

    def octave(self):
        return self.octave

    def __str__(self):
        return '("%s(%s)")' % (self.name, self.octave)

    def __repr__(self):
        return '("%s(%s)")' % (self.name, self.octave)

    def __eq__(self, other):
        return (self.name == other.name) & (self.octave == other.octave)

    def __hash__(self):
        return hash(self.__repr__())


class Scale:
    def __init__(self, name, intervals, repr):
        self.name = name
        self.intervals = intervals
        self.__notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        self.repr = repr

    def get_scale_notes(self, root):
        """ Get a scale notes starting with a root note.
            Return a list. """
        result = []
        result.append(root)
        index = (self.__notes.index(root))
        for i in self.intervals:
            index += i
            result.append(next(islice(cycle(self.__notes), index, None)))
        return result

    def get_scale_repr(self):
        return self.repr


def TEST():
    Major = Scale("Major", [2, 2, 1, 2, 2, 2, 1], 'three_notes')
    Natural_minor = Scale("Natural Minor", (2, 1, 2, 2, 1, 2), 'three_notes')

    c_major_scale = Major.get_scale_notes("C")
    print('C major scale:', c_major_scale)
    print(Major.get_scale_repr())

    a_natural_minor_scale = Natural_minor.get_scale_notes("A")
    print('A natural minor scale:', a_natural_minor_scale)


if __name__ == "__main__":
    TEST()

