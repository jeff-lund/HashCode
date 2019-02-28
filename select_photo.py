def max_tags(photos):
  max = 0
  for p in photos:
    if len(p.tags) > max_tags:
      max_tags = len(p.tags)
  return max




def select(bins):
  # start both lists from same seed image
  slideshow_front = []
  slideshow_back = []
  # choose first image, P_1
  # --> choose randomly from highest bin, b
  # set current_bin to b
  current_bin = 0
  current_image = bin[curent_bin].pop()
  slideshow_front.append(current_image)
  slideshow_back.append(current_image)

  while bins[current_bin]:
    flag = False
    threshold = bins[current_bin].num_tags // 2 #fix me?
    for image in bins[current_bin]:
      if (current_image.tags & image.tags) > threshold:
        slideshow_front.append(image)
        current_image = image
        bins[current_bin].remove(image)
        flag = True
    
    if not flag or not bins[current_bin]:
      if current_bin == len(bins) - 1:
        return slideshow_front
      current_bin += 1




# choose next image, n_i
# alternate between two slideshow lists:
# walk over b, try to find image that best intersects with P_1
# --> Best intersection is n/2 number of tags, allow for solution with n/2 - 1 (can change to n/2 -2 if needed)
# if best intersection not in current_bin, go to next highest bin
# repeat until best solution found
# --> if not found, end list
# append n_i to slideshow list

# Change current bin, b to next highest bin once b is empty.


