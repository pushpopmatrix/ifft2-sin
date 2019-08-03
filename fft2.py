# coding: UTF-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

class Sin:
    def __init__(self, fshift):
        self.fshift = fshift
    
    def show(self):
        fig.add_subplot(224), plt.imshow(self.sin, cmap = 'gray')
        plt.title('sin_curve'), plt.xticks([]), plt.yticks([])
    
    def update(self, x, y):
        self.sin = np.zeros((self.fshift.shape))
        self.sin[y, x] = 1
        self.sin = self.fshift * self.sin
        self.sin = np.fft.fftshift(self.sin)
        self.sin = np.fft.ifft2(self.sin)
        self.sin = np.uint8(self.sin.real)
        self.show()

class Inverse:
    def __init__(self, fshift):
        self.fshift = fshift
    
    def show(self):
        fig.add_subplot(223), plt.imshow(self.inv, cmap = 'gray')
        plt.title('inverse'), plt.xticks([]), plt.yticks([])
    
    def update(self, f):
        self.inv = self.fshift*f
        self.inv = np.fft.fftshift(self.inv)
        self.inv = np.fft.ifft2(self.inv)
        self.inv = np.uint8(self.inv.real)
        self.show()

class Filter:
    def __init__(self,y,x):
        self.f = np.zeros((y, x))

    def update(self, x, y):
        h,w = self.f.shape
        N = 1
        if y-N<0:
            if x-N<0:
                self.f[0:y+N, 0:x+N] = 1
            elif x+N>=w:
                self.f[0:y+N, x-N:w] = 1
            else:
                self.f[0:y+N, x-N:x+N] = 1
        elif x-N<0:
            if y+N>=h:
                self.f[y-N:h, 0:x+N] = 1
            else:
                self.f[y-N:y+N, 0:x+N] = 1
        elif h<=y+N:
            if x+N>=w:
                self.f[y-N:h,x-N:w] = 1
            else:
                self.f[y-N:h, x-N:x+N] = 1
        elif x+N>=w:
            self.f[y-N:y+N, x-N:w] = 1
        else:
            self.f[y-N:y+N, x-N:x+N] = 1

        self.show()
    
    def show(self):
        cv2.imshow("filterWindow", filter.get())
    
    def get(self):
        return self.f


draw = False
def mouse_event(event, x, y, flags, param):
    global draw
    if event == cv2.EVENT_LBUTTONDOWN:                                  # 左ボタンを押下したとき
        draw = True
        filter.update(x, y)
        sin.update(x, y)
        inverse.update(filter.get())
    elif event == cv2.EVENT_LBUTTONUP:                                  # 左ボタンを上げたとき
        draw = False
    elif event == cv2.EVENT_MOUSEMOVE and draw:                        # マウスが動いた時
        filter.update(x, y)
        sin.update(x, y)
        inverse.update(filter.get())

fig = plt.figure()

if __name__=='__main__':
    plt.ion()
    img = cv2.imread('marilyn.jpg',0)
    fig.add_subplot(221),plt.imshow(img, cmap = 'gray')
    
    fimg = np.fft.fft2(img)
    fshift = np.fft.fftshift(fimg)
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    fig.add_subplot(222),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    '''
        #to certain rightness of inverse forier transform
    img = fshift
    img = np.fft.fftshift(img)
    img = np.fft.ifft2(img)
    img = np.uint8(img.real)
    fig.add_subplot(221),plt.imshow(img, cmap = 'gray')
    '''
    h,w = img.shape
    filter = Filter(h,w)
    sin = Sin(fshift)
    inverse = Inverse(fshift)
    
    cv2.namedWindow("filterWindow", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("filterWindow", mouse_event)

    while True:
        cv2.imshow("filterWindow", filter.get())
        plt.draw()
        plt.pause(0.01)
        if cv2.waitKey(0) == 27:
            cv2.destroyAllWindows()
            break
