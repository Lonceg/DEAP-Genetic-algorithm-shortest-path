def middle(ind1, ind2, indpb):
    import random

    size = min(len(ind1), len(ind2))
    for i in range(size):
        if ind1[i] > ind2[i]:
            ind1[i] = ind2[i] + (abs(ind1[i] + ind2[i]) / 2)
            if random.random() <= indpb:
                ind2[i] = ind2[i] + (abs(ind1[i] + ind2[i]) / 3)
            else:
                ind2[i] = ind2[i] - (abs(ind1[i] + ind2[i]) / 3)
        elif ind2[i] > ind1[i]:
            ind1[i] = ind1[i] + (abs(ind1[i] + ind2[i]) / 2)
            if random.random() <= indpb:
                ind2[i] = ind1[i] + (abs(ind1[i] + ind2[i]) / 3)
            else:
                ind2[i] = ind1[i] - (abs(ind1[i] + ind2[i]) / 3)
        elif ind2[i] == ind1[i]:
            ind1[i] = ind1[i]
            ind2[i] = ind2[i]

    return ind1, ind2