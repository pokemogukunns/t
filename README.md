# YouTube Downloader
Video and Audio downloader from YouTube

It is a video and audio downloader from YouTube with the ability to download videos in different resolutions (360p, 480p, 720p), an audio in mp3 format.

The program has a nice and simple to use command-line interface, so that you can download your videos right from the Terminal.

BONUS: You can create an alias to run this script and give it a fancy name like "ydm" (YouTube Download Manager) by modifying your configuration file as follows.

To create alias for the script, add the following line to the end of the configuration file
```
alias ydm="python3 /path/to/the/script/main.py"
```
After addin this line and reloading the configuration, you can the downloader as follows. ```ydm -u URL```

## Basic Usage:
Clone this repository and go to youtube-downloader directory, then
```
$ python3 main.py -u URL
```
(Download the video with highest resolution, default 720p)
```
$ python3 main.py -a -u URL
```
(Download the audio only)
```
$ python3 main.py -c
```
(get URL from the clipboard and download the video)
```
$ python3 main.py -a -c
```
(get URL from the clipboard and download the audio only)
```
$ python3 main.py -c -r 480p
```
(get URL from clipboard and download the video with 480p resolution.)