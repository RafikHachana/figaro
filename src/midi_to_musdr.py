from miditok import MIDILike
from miditoolkit import MidiFile
import os

import glob

# file_path = ""
PATH = os.getenv('SAMPLES_DIR', './samples')
MAX_FILES = int(os.getenv('MAX_FILES', 1))

files = glob.glob(f"{PATH}/**/*.mid")

files = files[:MAX_FILES]

for file_path in files:
    midi = MidiFile(file_path)

    tokenizer = MIDILike()

    tokens = tokenizer(midi)

    print(tokens[0])
    print(tokens)

# TODO: Save as CSV here

# from midi2audio import FluidSynth

# FluidSynth().midi_to_audio(file_path, 'output.wav')

