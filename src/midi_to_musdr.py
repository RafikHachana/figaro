from miditok import MIDILike
from miditoolkit import MidiFile

file_path = ""

midi = MidiFile(file_path)

tokenizer = MIDILike()

tokens = tokenizer(midi)

print(tokens)

# TODO: Save as CSV here

from midi2audio import FluidSynth

FluidSynth().midi_to_audio(file_path, 'output.wav')

