import constants
from vocab import DescriptionVocab
import torch

# FIXME: Only supports BATCH_SIZE=1
def change_mean_pitch(description, delta=1):
    desc_vocab = DescriptionVocab()
    description = desc_vocab.decode(description[0])
    print("Given description", description)
    result = []
    for token in description:
        tmp = token
        if len(token.split('_')) == 2 and token.split('_')[0] == constants.MEAN_PITCH_KEY:
            index = int(token.split('_'))
            new_index = index + delta

            # Clip the values
            new_index = min(32, max(0, new_index))

            tmp = f'{constants.MEAN_PITCH_KEY}_{new_index}'

        result.append(tmp)

    print("Altered description", result)
    
    result = desc_vocab.encode(result)
    return torch.Tensor([result])
