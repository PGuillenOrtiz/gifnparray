import numpy as np
from PIL import Image

width, height = 800, 1000
build = []

for i in range(6):
    #draw the sky and the groud
    img = np.zeros((height, width, 3), dtype=np.uint8)
    img[:] = (35,29,43)
    img[int(height*0.85):height, 0:width] = (35,55,43)

    #draw building
    img[int(height*0.1):int(height*0.9), int(width*0.2):int(width*0.8)] = (94,101,107)

    #draw windows
    for row in range(6):
        for column in range(6):
            if np.random.randint(0,8) == 5:
                windows_color = (240,230,140)
            else:
                windows_color = (28, 23, 35)
            img[
                int(height*0.1+ 125*row + 20):int(height*0.1+125*row + 60 + 20),
                int(width*0.2+83*column + 15):int(width*0.2+83*column + 30 + 15)
            ] = windows_color
    img01 = Image.fromarray(img)
    build.append(img01)
build[0].save("my_building.gif", save_all=True, append_images=build[1:], duration=1000, loop=0)