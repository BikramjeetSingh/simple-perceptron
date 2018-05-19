def signum(num):
    if num > 0:
        return 2.0
    else:
        return 1.0


def weight_correction(weights, inputs, actual_response, desired_response, learning_rate):
    for index in range(len(inputs)):
        weights[index] = weights[index] + float(inputs[index]) * learning_rate * (desired_response - float(actual_response))
    return weights


def train(inputs, weights, bias, train_rate):
    incorrect = 0
    for example in inputs:
        desired = float(example[len(example) - 1])
        u = 0
        for i in range(len(example) - 1):
            u += weights[i] * float(example[i])

        v = u + bias
        actual = signum(v)

        if actual != desired:
            incorrect += 1
            weights = weight_correction(weights, example, actual, desired, train_rate)

    print incorrect
    return weights


def test(inputs, weights, bias):
    correct = 0
    incorrect = 0

    for example in inputs:
        desired = float(example[len(example) - 1])
        u = 0
        for i in range(len(example) - 1):
            u += weights[i] * float(example[i])

        v = u + bias
        actual = signum(v)

        if actual != desired:
            incorrect += 1
        else:
            correct += 1

    return (float(correct) / float(len(inputs))) * 100
