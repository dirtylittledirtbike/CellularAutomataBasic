import numpy as np

def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 10)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value


def start_state(w, h, s, state):

    if state == 'pad' and int(w/s) % 3 == 0:
        x = int((w/s)/3)
        y = int(((w/s) - x)/2)
        ab = np.zeros((x, x), dtype=int)
        cd = np.pad(ab, int(y/2), pad_with, padder=1)
        ef = np.pad(cd, int(y/2), pad_with, padder = 0)
        return ef

    elif state == 'cross':
        aa = np.eye(int(w/s), dtype=int)
        bb = np.rot90(aa).copy()
        cc = np.array(aa + bb)
        return cc

    elif state == 'rand':
        return np.random.randint(0, 2, (int(w/s), int(h/s)))

    else:
        print('wrong dimensions')


## game of life
#if ca.current_state[int(i/scl)][int(j/scl)] == 1 and (ca.neighbors < 2 or ca.neighbors == 1):
#    ca.next_state[int(i/scl)][int(j/scl)] = 0
#elif ca.current_state[int(i/scl)][int(j/scl)] == 1 and (ca.neighbors > 3):
#    ca.next_state[int(i/scl)][int(j/scl)] = 0
#elif ca.current_state[int(i/scl)][int(j/scl)] == 0 and (ca.neighbors == 3):
#    ca.next_state[int(i/scl)][int(j/scl)] = 1


# if ca.current_state[int(i / scl)][int(j / scl)] == 1 and (ca.neighbors == 2 or ca.neighbors == 4):
#     ca.next_state[int(i / scl)][int(j / scl)] = 0
# elif ca.current_state[int(i / scl)][int(j / scl)] == 0 and (ca.neighbors == 1 or ca.neighbors == 3 or ca.neighbors == 8):
#     ca.next_state[int(i / scl)][int(j / scl)] = 1
