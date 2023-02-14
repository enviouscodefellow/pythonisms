class PythonismCollection:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return f'PythonismCollection({self.data})'

    def __str__(self):
        return f'[{", ".join(map(str, self.data))}]'

    def __add__(self, other):
        return PythonismCollection(self.data + other.data)

    def __eq__(self, other):
        return self.data == other.data

    def __lt__(self, other):
        return len(self.data) < len(other.data)

    def __le__(self, other):
        return len(self.data) <= len(other.data)

    def __gt__(self, other):
        return len(self.data) > len(other.data)

    def __ge__(self, other):
        return len(self.data) >= len(other.data)

    def __ne__(self, other):
        return self.data != other.data

    def __hash__(self):
        return hash(self.data)

    def __bool__(self):
        return bool(self.data)

    def __contains__(self, value):
        return value in self.data

    def __reversed__(self):
        return PythonismCollection(reversed(self.data))

    def __call__(self, *args, **kwargs):
        return self.data(*args, **kwargs)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def __del__(self):
        print('PythonismCollection object deleted')

    def generator(self):
        for value in self.data:
            yield value
