## ifft2-sin
Two dimensional fast fourier transform and inverse fast fourier transform.

Users can see how sin curves make an image.(recognize to click around the center of filter)

# about look
Window1:[1][2]
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
  
