Title: Why I love FFMPEG
Date: 2018-12-02 0835
Authors: Ken McGonigal
Slug: why-I-love-ffmpeg
Category: blog
Summary: FFMPEG can be used for so many project



FFMPEG is so useful I am not where to start! I use it almost every time I 
am working with video.  

You can use it make videos smaller to fit on your website. Youtube uses it
in the backend sytem.

### Basic conversion from one container to another

	ffmpeg -i input.avi output.mpg

### Make Video Filesize Smaller

Scenario: You just finished editing that awesome video and now its too big to add to your website.
How can you shrink the file size while maintaining the quality and aspect ratio? 

Calculate thit bitrate you need by dividing 1GB by the video length in
seconds. 

	ffmpeg -i input.mp4 -b 1000000 output.mp4

You can also change the CRF to 18 or 20. The lower the number the better the
quality; but 18-20 seems to work well for me.

	ffmpeg -i input.mp4 -vcodec libx264 -crf 20 output.mp4

FFMPEG can do many things which are too numerous for one blog post.

I hope this helps with your next web project. 

