# YouTube Downloader
Video and Audio downloader from YouTube

It is a video and audio downloader from YouTube with a nice CLI (command-line interface).

## Basic Usage:
$ python3 main.py -u URL
(Download the video with highest resolution, default 720p)

$ python3 main.py -a -u URL
(Download the audio only)

$ python3 main.py -c
(get URL from the clipboard and download the video)

$ python3 main.py -a -c
(get URL from the clipboard and download the audio only)

$ python3 main.py -c -r 480p
(get URL from clipboard and then download the video with 480p resolution.)