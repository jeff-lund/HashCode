from photos import Photo
from photos import Bin
from photos import preprocessor

# BINS
#FIXME add method for getting max tags
MAX_TAGS = 51

def sort_bins():
  """ Returns bins, sorted in descending order. Note bins are labeled at index +1 (index 0 count, bins -> index +1) """
  bins = [Bin(i+1) for i in range(MAX_TAGS)].reverse()
  # assign photos to bins
  photo_set = preprocessor('b_lovely_landscapes.txt')

  while photo_set:
    curr_p = photo_set.pop()
    idx = len(curr_p.tags)
    bins[idx -1] = bins[idx-1].add(curr_p)
  return bins


# start both lists from same seed image
slideshow_front = []
slideshow_back = []

# choose first image, P_1
# --> choose randomly from highest bin, b
# set current_bin to b

# (int division)

# make sure to calculate n/2 - x based on A and B:
# --> if B has 9, and A has 10 tags, use 9/2 - x (not 10/2 -x)

# choose next image, n_i
# alternate between two slideshow lists:
# walk over b, try to find image that best intersects with P_1
# --> Best intersection is n/2 number of tags, allow for solution with n/2 - 1 (can change to n/2 -2 if needed)
# if best intersection not in current_bin, go to next highest bin
# repeat until best solution found
# --> if not found, end list
# append n_i to slideshow list

# Change current bin, b to next highest bin once b is empty.


