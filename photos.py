from sys import argv
import random

class Photo:
    def __init__(self, id, o, tags):
        self.id = [id]
        self.oreintation = o
        self.tags = tags
        self.used = False

class Bin:
    def __init__(self, n):
        self.num_tags = n
        self.photos = set()

def score(current, next):
    pass

fname = argv[1]

with open(fname, 'r') as f:
    data = [line.strip() for line in f]

num_photos = int(data[0])
id = 0
photos = set()
v_photos = set()

for entry in data[1:]:
    temp = entry.split(' ')
    o = temp[0]
    n_tags = temp[1]
    tags = set(temp[2:])
    if o == 'H':
        photos.add(Photo(id, o, tags))
    else:
        v_photos.add(Photo(id, o, tags))
    id += 1

# Naive recombination of vertical photos
print("Num hphotos : {} | vphotos {}".format(len(photos), len(v_photos)))
unused = []
if v_photos:
    unused = [v_photos.pop()]
    while v_photos:
        current = v_photos.pop()
        matched = False
        if unused:
            for u in unused:
                if current.tags.isdisjoint(u.tags):
                    temp = Photo([current.id, u.id], 'H', current.tags | u.tags)
                    photos.add(temp)
                    unused.remove(u)
                    matched = True
                    break
        if not matched:
            for p in v_photos:
                if current.tags.isdisjoint(p.tags):
                    temp = Photo([current.id, u.id], 'H', current.tags | u.tags)
                    photos.add(temp)
                    v_photos.remove(p)
                    matched = True
                    break
        if not matched:
            unused.append(current)

while len(unused) > 1:
    current = unused.pop()
    max_val = None
    max_ind = None
    for i in range(len(unused)):
        if max_val == None:
            max_val = len(current.tags | u.tags)
            max_ind = i
        else:
            m = len(current.tags | u.tags)
            if m > max_val:
                max_val = m
                max_ind = i
    photos.add(Photo([current.id, unused[max_ind].id], 'H', current.tags | unused[max_ind].tags))
    unused.pop(max_ind)
print(len(unused))
print(len(photos))
max_tags = 0
for p in photos:
    if len(p.tags) > max_tags:
        max_tags = len(p.tags)
print(max_tags)
