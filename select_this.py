def select_(bins):
  # start both lists from same seed image
  slideshow_front = []
  slideshow_back = []
  # choose first image, P_1
  # --> choose randomly from highest bin, b
  # set current_bin to b
  current_bin = 0
  max_bin = len(bins)
  x = 0
  while not bins[current_bin].photos:
      current_bin += 1

  current_image = bins[current_bin].photos.pop()
  slideshow_front.append(current_image)
  slideshow_back.append(current_image)

  while bins[current_bin].photos and current_bin < max_bin:
    threshold = bins[current_bin].num_tags // 2  - x#fix me?
    for image in bins[current_bin].photos:
      if (current_image.tags & image.tags) >= threshold:
        slideshow_front.append(image)
        current_image = image
        bins[current_bin].photos.remove(image)
        x = 0
    if not bins[current_bin].photos:
      current_bin += 1
      x += 1
  return slideshow_front
