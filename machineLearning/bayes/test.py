from  sklearn import datasets

def get_data():

    return datasets.load_iris()


if __name__ == "__main__":

    iris = get_data();

    x = iris.data
    y = iris.target

    print(x.shape)