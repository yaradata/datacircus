import pickle

def read_pickle_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
    

def write_to_pickle_file(filename, model):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)

