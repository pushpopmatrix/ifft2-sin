## ifft2-sin
- Two dimensional fast fourier transform and inverse fast fourier transform.
- Users can see how sin curves make an image.
  (recommend to click around the center of filter)
- quit to ESC while choosing filter window

# about look and how to use
Window1:

[1][2]

[3][4]

Window2:[f]

[1] is an original image

[2] is magunitude spectrum of [1]

[3] is result of ifft2 made by [2] and [f]

[4] is result of ifft2 made by [2] and current plot of [f]

[f] is a filter : users can draw white point and line with mouse

# about code
fft2.py has 4 classes
- Filter
  - update filter come from mouse_event : filter has every event
  - show filter
  - return current filter
- Sin
  - upadate sin curve come from mouse_event : sin has only  a current event
  - show sin curve
- Inverse
  - update inversed image 
  - show inversed image

other: functions
- mouse_event 
  - judge the state of mouse event and update figures
- main
  - show original image and magnitude spectrum constantly
  - show other images as they are updated
  
# library
opencv(cv2)
numpy
matplotlib

# reference
followed the model
- https://www.youtube.com/watch?v=qB0cffZpw-A

how to show magnitude_spectrum
- https://algorithm.joho.info/image-processing/fourier-transform/
- http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html

how to ifft2
- https://algorithm.joho.info/programming/python/opencv-fft-low-pass-filter-py/

how to draw figure to same window
- https://qiita.com/ynakayama/items/8d3b1f7356da5bcbe9bc

how to get mouse event
- http://rasp.hateblo.jp/entry/2016/01/24/204539

![demo](export.gif)
