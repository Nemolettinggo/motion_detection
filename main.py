from motion_detection import motion_detection


#This the the init part of the app, the parameter will be used follows:

#gs_window : indicate the size of the Gaussian filter window, recmd : 25 for a 800*600 frame

#gs_sig : the sigma value for the Gaussian filter , no need to very large or small, default：3

#diff_thresh : the threshold for the difference of the mask , if you have a high resolution and quality(I mean stable,
#less noisy) camera, you could set it low, like 10-30, but your camera quality low as my test cam, please tune up
#default value： 100

#min_area : the min area the motion detector could detect, usually to voild the light etc, tune it up to at least 1500
#default :1500

#mod : 0 is off for the alarm by sms system, 1 is on.

gs_window = 25
gs_sig = 3
diff_thresh = 100
min_area = 1500
mod = 0

motion_detection(gs_window,gs_sig,diff_thresh,min_area,mod)

