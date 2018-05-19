import random, numpy, csv
import perceptron

def load_csv(filename):
    file = open(filename, "rb")
    lines = csv.reader(file)
    dataset = list(lines)
    random.shuffle(dataset)
    return dataset


inputs = load_csv("iris.csv")
weights = [numpy.random.random_sample() for i in range(len(inputs))]
bias = 0
learning_rate = 0.01

weights = perceptron.train(inputs, weights, bias, learning_rate)
c = perceptron.test(inputs, weights, bias)
print c