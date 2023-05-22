# 참고
https://www.youtube.com/watch?v=URdVXQiLIPc

# 시작
import cv2
import math
import numpy as np
import scipy.ndimage

def orientated_non_max_suppression(mag, ang):
    ang_quant = np.round(ang / (np.pi/4)) % 4
    winE = np.array([[0, 0, 0],[1, 1, 1], [0, 0, 0]])
    winSE = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    winS = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]])
    winSW = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])

    magE = non_max_suppression(mag, winE)
    magSE = non_max_suppression(mag, winSE)
    magS = non_max_suppression(mag, winS)
    magSW = non_max_suppression(mag, winSW)

    mag[ang_quant == 0] = magE[ang_quant == 0]
    mag[ang_quant == 1] = magSE[ang_quant == 1]
    mag[ang_quant == 2] = magS[ang_quant == 2]
    mag[ang_quant == 3] = magSW[ang_quant == 3]
    return mag

def non_max_suppression(data, win):
    data_max = scipy.ndimage.filters.maximum_filter(data, footprint=win, mode='constant')
    data_max[data != data_max] = 0
    return data_max

# start calulcation
gray_image = cv2.imread(r'/Users/qqwaseoke/Downloads/crackDetecion/crack.jpg', 0)

with_nmsup = True #apply non-maximal suppression
fudgefactor = 1.3 #with this threshold you can play a little bit
sigma = 21 #for Gaussian Kernel
kernel = 2*math.ceil(2*sigma)+1 #Kernel size

gray_image = gray_image/255.0
blur = cv2.GaussianBlur(gray_image, (kernel, kernel), sigma)
gray_image = cv2.subtract(gray_image, blur)

# compute sobel response
sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
mag = np.hypot(sobelx, sobely)
ang = np.arctan2(sobely, sobelx)

# threshold
threshold = 4 * fudgefactor * np.mean(mag)
mag[mag < threshold] = 0

# either get edges directly
if with_nmsup is False:
    mag = cv2.normalize(mag, 0, 255, cv2.NORM_MINMAX)
    kernel = np.ones((5,5),np.uint8)
    result = cv2.morphologyEx(mag, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('im', result)
    cv2.waitKey()

# or apply a non-maximal suppression
else:

    # non-maximal suppression
    mag = orientated_non_max_suppression(mag, ang)
    # create mask
    mag[mag > 0] = 255
    mag = mag.astype(np.uint8)

    kernel = np.ones((5,5),np.uint8)
    result = cv2.morphologyEx(mag, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('im', result)
    cv2.waitKey()

# 모델 결과
![crack](https://github.com/QQWaseokE/Today-I-Learned/assets/127533265/c83ce01a-756d-4c85-9000-0e742f5fecfb)
<img width="437" alt="crack;" src="https://github.com/QQWaseokE/Today-I-Learned/assets/127533265/29a9fec5-f5d6-42dd-912e-b759ecdde927">

![crack2](https://github.com/QQWaseokE/Today-I-Learned/assets/127533265/2ba9efcd-109a-498f-a6aa-fd061e0f9918)
<img width="648" alt="crack4;" src="https://github.com/QQWaseokE/Today-I-Learned/assets/127533265/3f21edaf-04b5-4a07-bc30-4a216b120618">

# 교내 도로 적용
<img width="595" alt="crack11" src="https://github.com/QQWaseokE/Today-I-Learned/assets/127533265/0486cf44-3cda-4f3a-ada2-5a6e31d50acb">
<img width="649" alt="crack11;" src="https://github.com/QQWaseokE/Today-I-Learned/assets/127533265/34d40040-6a8a-46a2-ab85-8854d5e4110f">

<img width="691" alt="crack12" src="https://github.com/QQWaseokE/Today-I-Learned/assets/127533265/9060c5b1-cc54-4a50-9f8c-39e7619250c1">
<img width="741" alt="crack12;" src="https://github.com/QQWaseokE/Today-I-Learned/assets/127533265/4e7306db-22d4-4626-bf41-dff170061203">

<img width="597" alt="crack13" src="https://github.com/QQWaseokE/Today-I-Learned/assets/127533265/9d17240d-c7c4-4658-9c4e-9112d47337df">
<img width="637" alt="crack13;" src="https://github.com/QQWaseokE/Today-I-Learned/assets/127533265/2449c5a1-3d93-44b8-a72d-d9df951e39fe">

# 느낀점
opencv를 설치하는 과정에서는 큰 문제가 없었으나 파이썬에서 opencv를 불러오는데 많은 시간을 잡아먹었다.
업데이트도 해보고 기타 등등 다 해봤으나 해결하지 못하다가 아나콘다를 설치하여 그 쪽에서 업데이트를 하니 해결되었다.
교내 도로에 직접 적용해보니 화질도 좋지 않고 선명도가 낮아서 그런지 만족스러운 결과가 아니었기에 다른 모델을 더 조사를 해보기로 했다...
