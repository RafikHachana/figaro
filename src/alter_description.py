import constants


def change_mean_pitch(description, delta=1):
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
    

    return result
