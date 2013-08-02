import random


def random_sample(iterable, sample_size):
    sample = []

    for i, rec in enumerate(iterable):
        if i < sample_size:
            sample.append(rec)
        elif random.random() < SAMPLE_SIZE / float(i + 1):
            replace = random.randint(0, len(sample) - 1)
            sample[replace] = rec
    return sample
