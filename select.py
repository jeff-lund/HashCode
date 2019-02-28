def select(bins):
  # start both lists from same seed image
  slideshow_front = []
  slideshow_back = []
  # choose first image, P_1
  # --> choose randomly from highest bin, b
  # set current_bin to b
  current_bin = 0
  current_image = bins[curent_bin].pop()
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