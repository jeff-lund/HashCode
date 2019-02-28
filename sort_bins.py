from photos import Photo
from photos import Bin
from photos import preprocessor


def sort_bins(photo_set, max_tags):
  """ Returns bins, sorted in descending order. Note bins are labeled at index +1 (index 0 count, bins -> index +1) """
  bins = [Bin(i+1) for i in range(max_tags)]
  bins.reverse()
  # assign photos to bins
  while photo_set:
    curr_p = photo_set.pop()
    idx = len(curr_p.tags)
    for b in bins:
        if b.num_tags == idx:
            b.photos.add(curr_p)
  return bins
