import constants
from vocab import DescriptionVocab
import torch

def control_ordinal_attributes(description, delta=1, attribute_key=constants.MEAN_PITCH_KEY, n_bins=33):
    desc_vocab = DescriptionVocab()
    description = desc_vocab.decode(description[0])
    print("Given description", description)
    result = []
    for token in description:
        tmp = token
        if len(token.split('_')) == 2 and token.split('_')[0] == attribute_key:
            index = int(token.split('_')[1])
            new_index = index + delta

            # Clip the values
            new_index = min(n_bins-1, max(0, new_index))

            tmp = f'{attribute_key}_{new_index}'

        result.append(tmp)

    print("Altered description", result)
    
    result = desc_vocab.encode(result)
    return torch.Tensor([result])

def transpose_the_chord_progression(description, delta=1):
    pass

def remove_some_instruments(description, delta=1):
    pass




# FIXME: Only supports BATCH_SIZE=1
def change_mean_pitch(description, delta=1):
    desc_vocab = DescriptionVocab()
    description = desc_vocab.decode(description[0])
    print("Given description", description)
    result = []
    for token in description:
        tmp = token
        if len(token.split('_')) == 2 and token.split('_')[0] == constants.MEAN_PITCH_KEY:
            index = int(token.split('_')[1])
            new_index = index + delta

            # Clip the values
            new_index = min(32, max(0, new_index))

            tmp = f'{constants.MEAN_PITCH_KEY}_{new_index}'

        result.append(tmp)

    print("Altered description", result)
    
    result = desc_vocab.encode(result)
    return torch.Tensor([result])


def change_mean_duration(description, delta=1):
    pass

def change_mean_velocity(description, delta=1):
    pass

def change_note_density(description, delta=1):
    pass
