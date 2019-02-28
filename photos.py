from sys import argv

class Photo:
    def __init__(self, id, o, tags):
        self.id = [id]
        self.oreintation = o
        self.tags = tags
        self.used = False

class Bin:
    def __init__(self, n):
        self.num_tags = n
        self.photos = []

fname = argv[1]

with open(fname, 'r') as f:
    data = [line.strip() for line in f]
num_photos = int(data[0])
id = 0
h_photos = set()
v_photos = set()

for entry in data[1:]:
    temp = entry.split(' ')
    o = temp[0]
    n_tags = temp[1]
    tags = set(temp[2:])
    if o == 'H':
        h_photos.add(Photo(id, o, tags))
    else:
        v_photos.add(Photo(id, o, tags))
    id += 1
