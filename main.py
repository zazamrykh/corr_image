import numpy as np
from PIL import Image

def calculate_corr(first_image, second_image, eps=1e-8):
    first_image = first_image.astype(np.float64)
    second_image = second_image.astype(np.float64)

    first_means = np.full((first_image.shape[0], first_image.shape[1], 3), np.mean(first_image, axis=(0,1)), dtype=np.float64)
    second_means = np.full((second_image.shape[0], second_image.shape[1], 3), np.mean(second_image, axis=(0,1)), dtype=np.float64)

    first_stds = np.full((first_image.shape[0], first_image.shape[1], 3), np.std(first_image, axis=(0,1)), dtype=np.float64)
    second_stds = np.full((second_image.shape[0], second_image.shape[1], 3), np.std(second_image, axis=(0,1)), dtype=np.float64)

    corr = np.mean((first_image-first_means)*(second_image-second_means)/(first_stds * second_stds + eps))
    return corr



if __name__ == '__main__':
    first_image = np.array(Image.open("elon.jpg"))
    second_image = np.array(Image.open("caat.png"))
    corr = calculate_corr(first_image, second_image)
    print(corr)
