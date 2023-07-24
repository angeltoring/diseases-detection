#assuming you are already updated with your environment

sudo apt-get install v4l-utils

# make 1080p a default for webcam
v412-ctl --set-fmt-video=width=1920, height=1080

sudo fswebcam