import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import random

def img2array(array: np.array, num_circles=12, radius=0.5, img_size=(224, 224), edgecolor='black', facecolor='black') -> np.array:
    fig, ax = plt.subplots(figsize=(img_size[0] / 100, img_size[1] / 100), dpi=100)
    ax.set_aspect('equal')
    
    for i in range(num_circles):
        circle = plt.Circle((i * (2 * radius + 1), 0), radius, fill=array, edgecolor=edgecolor, facecolor=facecolor)
        ax.add_artist(circle)

    ax.set_xlim(-1, num_circles * (2 * radius + 1) - 1)
    ax.set_ylim(-1, 1)
    ax.axis('off')

    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))

    image = Image.fromarray(image).resize(img_size)
    image = np.array(image)
    plt.close(fig)
    return image

def reversal(input: list) -> list:
    return [1 - bit for bit in input]

def mirror(input: list) -> list:
    return list(reversed(input))

# def leftphasic(input: list) -> list:
#     return input[1:] + input[:1]

# def rightphasic(input: list) -> list:
#     return input[-1:] + input[:-1]

def randomphasic(input: list) -> list:
    i = random.random()
    if i <= 0.5:
        return input[1:] + input[:1]
    else:
        return input[-1:] + input[:-1]

def randomdelete(input: list) -> list:
    idxs = [i for i, val in enumerate(input) if val == 1]
    i = random.choice(idxs)
    new = input.copy()
    new[i] = 0
    return new

def randominsertion(input: list) -> list:
    idxs = [i for i, val in enumerate(input) if val == 0]
    i = random.choice(idxs)
    new = input.copy()
    new[i] = 1
    return new

HAHN_TRANSFORMATION_COMBOS = [['reversal'], ['mirror'], ['randomphasic'], ['randomdelete'], ['reversal', 'mirror'], ['randomdelete', 'mirror'], 
                              ['reversal', 'randomphasic'], ['randominsertion', 'randomphasic'], ['randomdelete', 'reversal', 'randomphasic'], 
                              ['randomdelete', 'reversal', 'mirror'], ['randominsertion', 'reversal', 'randomphasic'], ['randominsertion', 'reversal', 'mirror']]
# print(reversal(mirror([0,0,1,1,0,1,0,0,1,0,0,1])))    
# print(reversal(mirror([0,1,1,1,1,0,0,1,1,1,0,0])))
# print(reversal(mirror([0,0,0,0,0,1,1,0,0,0,0,1]))) 
# print(reversal(mirror([1,1,1,0,1,0,1,1,0,1,0,0])))       