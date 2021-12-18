from enum import Enum


class note_list(Enum):

    A1 = 'notes/1A.wav'
    A1_sharp = 'notes/1A#.wav'
    B1 = 'notes/1B.wav'
    E1 = 'notes/1E.wav'
    F1_sharp = 'notes/1F#.wav'
    F1 = 'notes/1F.wav'
    G1_sharp = 'notes/1G#.wav'
    G1 = 'notes/1G.wav'
    A2 = 'notes/2A.wav'
    A2_sharp = 'notes/2A#.wav'
    B2 = 'notes/2B.wav'
    C2_sharp = 'notes/2C#.wav'
    C2 = 'notes/2C.wav'
    D2_sharp = 'notes/2D#.wav'
    D2 = 'notes/2D.wav'
    E2 = 'notes/2E.wav'
    F2_sharp = 'notes/2F#.wav'
    F2 = 'notes/2F.wav'
    G2_sharp = 'notes/2G#.wav'
    G2 = 'notes/2G.wav'
    A3_sharp = 'notes/3A#.wav'
    A3 = 'notes/3A.wav'
    B3 = 'notes/3B.wav'
    C3_sharp = 'notes/3C#.wav'
    C3 = 'notes/3C.wav'
    D3_sharp = 'notes/3D.wav'
    E3 = 'notes/3E.wav'
    F3 = 'notes/3F.wav'
    F3_sharp = 'notes/3F#.wav'
    G3 = 'notes/3G.wav'
    C4_sharp = 'notes/4C#.wav'
    C4 = 'notes/4C.wav'
    D4_sharp = 'notes/4D#.wav'
    D4 = 'notes/4D.wav'

    def file_name(self):
        return self.value
