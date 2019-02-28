from photos import Photo
from photos import Bin
from photos import preprocessor

# BINS
#FIXME add method for getting max tags
MAX_TAGS = 51

def sort_bins(photo_set, max_tags):
  """ Returns bins, sorted in descending order. Note bins are labeled at index +1 (index 0 count, bins -> index +1) """
  bins = [Bin(i+1) for i in range(MAX_TAGS)].reverse()
  # assign photos to bins
  photo_set = preprocessor('b_lovely_landscapes.txt')

  while photo_set:
    curr_p = photo_set.pop()
    idx = len(curr_p.tags)
    bins[idx -1] = bins[idx-1].add(curr_p)
  return bin
