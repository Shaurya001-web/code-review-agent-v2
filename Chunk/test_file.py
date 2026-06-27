class DataProcessor:
    def __init__(self, data):
        self.data = data

    def clean(self):
        return [x for x in self.data if x is not None]

    def transform(self, factor):
        return [x * factor for x in self.clean()]

def load_data(path):
    with open(path) as f:
        return f.readlines()

def save_results(results, path):
    with open(path, "w") as f:
        f.write(str(results))