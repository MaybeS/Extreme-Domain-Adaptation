import numpy as np


def corrupt(labels, size=.4, label_size=31):
    labels[np.random.choice(np.arange(labels.size),
                            int(labels.size * size)).astype(np.int)] \
        = np.random.randint(1, label_size, int(labels.size * size))

    return labels


def blindfold(labels, keep=10):
    labels[labels > keep] = keep+1

    return labels
