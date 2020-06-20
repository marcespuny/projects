
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter, defaultdict
from helpers import show_model, Dataset
from pomegranate import State, HiddenMarkovModel, DiscreteDistribution

def pair_counts(sequences_A, sequences_B):

    d = {}

    for sent1, sent2 in zip(sequences_A, sequences_B):
        for tag, word in zip(sent1, sent2):
            if tag not in d:
                d[tag] = {}
                inside_d = d[tag]
            if word not in inside_d:
                inside_d[word] = 1
            else:
                inside_d[word] += 1
    return d

emission_counts = pair_counts(data.Y, data.X)

from collections import namedtuple

FakeState = namedtuple("FakeState", "name")


class MFCTagger:
    missing = FakeState(name="<MISSING>")

    def __init__(self, table):
        self.table = defaultdict(lambda: MFCTagger.missing)
        self.table.update({word: FakeState(name=tag) for word, tag in table.items()})

    def viterbi(self, seq):
        """This method simplifies predictions by matching the Pomegranate viterbi() interface"""
        return 0., list(enumerate(["<start>"] + [self.table[w] for w in seq] + ["<end>"]))

words = pair_counts(data.X, data.Y)

mfc_table = {}

for word in data.training_set.vocab:
    mfc_table[word] = max(words[word], key=(lambda tag: words[word][tag]))

mfc_model = MFCTagger(mfc_table)

def replace_unknown(sequence):

    return [w if w in data.training_set.vocab else 'nan' for w in sequence]

def simplify_decoding(X, model):

    _, state_path = model.viterbi(replace_unknown(X))
    return [state[1].name for state in state_path[1:-1]]


def accuracy(X, Y, model):

    correct = total_predictions = 0
    for observations, actual_tags in zip(X, Y):
        try:
            most_likely_tags = simplify_decoding(observations, model)
            correct += sum(p == t for p, t in zip(most_likely_tags, actual_tags))
        except:
            pass
        total_predictions += len(observations)

    return correct / total_predictions

mfc_training_acc = accuracy(data.training_set.X, data.training_set.Y, mfc_model)
print("training accuracy mfc_model: {:.2f}%".format(100 * mfc_training_acc))

mfc_testing_acc = accuracy(data.testing_set.X, data.testing_set.Y, mfc_model)
print("testing accuracy mfc_model: {:.2f}%".format(100 * mfc_testing_acc))


def unigram_counts(sequences):

    d = {}
    for sentence in sequences:
        for tag in sentence:
            if tag in d:
                d[tag] += 1
            else:
                d[tag] = 1

    return d

tag_unigrams = unigram_counts(data.Y)


def bigram_counts(sequences):

    d = {}
    for sentence in sequences:
        for i in range(len(sentence) - 1):
            if (sentence[i], sentence[i + 1]) not in d:
                d[(sentence[i], sentence[i + 1])] = 1
            else:
                d[(sentence[i], sentence[i + 1])] += 1

    return d

tag_bigrams = bigram_counts(data.Y)


def starting_counts(sequences):

    d = {}
    for tags in sequences:

        if tags[0] in d:
            d[tags[0]] += 1
        else:
            d[tags[0]] = 1

    return d

tag_starts = starting_counts(data.Y)


def ending_counts(sequences):

    d = {}
    for tags in sequences:

        if tags[-1] in d:
            d[tags[-1]] += 1
        else:
            d[tags[-1]] = 1

    return d

tag_ends = ending_counts(data.Y)

basic_model = HiddenMarkovModel(name="base-hmm-tagger")

states = {}

for tag in data.tagset:

    emission_prob = {}

    for word, number in emission_counts[tag].items():
        emission_prob[word] = number / tag_unigrams[tag]

    tag_distribution = DiscreteDistribution(emission_prob)
    state = State(tag_distribution, name=tag)
    states[tag] = state
    basic_model.add_state(state)

for tag in data.tagset:

    state = states[tag]
    start_probability = tag_starts[tag] / sum(tag_starts.values())
    basic_model.add_transition(basic_model.start, state, start_probability)
    end_probability = tag_ends[tag] / sum(tag_ends.values())
    basic_model.add_transition(state, basic_model.end, end_probability)

for tag1 in data.tagset:

    state_1 = states[tag1]

    for tag2 in data.tagset:

        state_2 = states[tag2]
        bigram = (tag1, tag2)
        transition_probability = tag_bigrams[bigram] / tag_unigrams[tag1]
        basic_model.add_transition(state_1, state_2, transition_probability)

basic_model.bake()

hmm_training_acc = accuracy(data.training_set.X, data.training_set.Y, basic_model)
print("training accuracy basic hmm model: {:.2f}%".format(100 * hmm_training_acc))

hmm_testing_acc = accuracy(data.testing_set.X, data.testing_set.Y, basic_model)
print("testing accuracy basic hmm model: {:.2f}%".format(100 * hmm_testing_acc))