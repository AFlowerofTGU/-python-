# python image median filtering
# f is the image to be filtered,
# KernelSize is the KernelSize of the filter,
# KernelSize is an odd number,
# for example, if KernelSize=3, then the median filter is 3x3

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2


def MedianFilter( f, KernelSize ):
    height = f.shape[0]
    wide = f.shape[1]
    img1 = np.zeros((height, wide), np.uint8)  # 用于存放新的图像
    for i in range(int(KernelSize / 2), height - int(KernelSize / 2)):
        for j in range(int(KernelSize / 2), wide - int(KernelSize / 2)):
            Adjacent_pixels = np.zeros(KernelSize * KernelSize, np.uint8)
            s = 0
            for k in range(-1 * int(KernelSize / 2), int(KernelSize / 2) + 1):
                for l in range(-1 * int(KernelSize / 2), int(KernelSize / 2) + 1):
                    Adjacent_pixels[s] = f[i + k, j + l]
                    s += 1
            Adjacent_pixels.sort()  # 寻找中值
            median = Adjacent_pixels[int((KernelSize * KernelSize - 1) / 2)]  # 将中值代替原来的中心值
            img1[i, j] = median
    return img1

def main( fn1, fn2):
    try:
        f = MedianFilter(fn1,3)
    except:
        return
    f = Image.fromarray(f)
    f.save(fn2)

    plt.imshow(f, plt.cm.gray)
    plt.show()

if __name__=='__main__':
    fn1 = cv2.imread(r'C:\Users\34892\Desktop\python\123\noisyLena.bmp', cv2.IMREAD_GRAYSCALE)
    fn2 = r'C:\Users\34892\Desktop\python\123\noisyLena1.bmp'
    main(fn1, fn2)