# YouTube Downloader
Video and Audio downloader from YouTube

- It is a video and audio downloader from YouTube with the ability to download videos in different resolutions (360p, 480p, 720p), an audio in mp3 format.

- The program has a nice and simple to use command-line interface, so that you can download videos and audios right from the Terminal.

## Installation:
- Clone this repository to a location you want
- Open a Terminal and navigate to "youtube-downloader" directory
- create a virtual environment with system site packages enabled
- Install all required packages from requirements.txt to the virtual environment you created
```
pip install -r requirements.txt
```


- BONUS: You can create an alias to run this script and give it a fancy name like "ydm" (YouTube Download Manager) by modifying your configuration file. <a href="https://askubuntu.com/questions/17536/how-do-i-create-a-permanent-bash-alias"> Read more </a>

- To create an alias for the script, add the following line to the end of the configuration file (don't forget to add a command to activate the virtual environment for the script before running the actual script)
```
alias ydm="source /path/to/youtube-downloader/venv-name/bin/activate; python3 /path/to/youtube-downloader/main.py"
```
After creating an alias for the script, you can use the downloader as follows. 
```
ydm -u URL
```


## Usage:
Download the video with highest resolution, default 720p
```
$ python3 main.py -u URL
```
Download the audio only
```
$ python3 main.py -a -u URL
```
get URL from the clipboard and download the video
```
$ python3 main.py -c
```
get URL from the clipboard and download the audio only
```
$ python3 main.py -a -c
```
get URL from clipboard and download the video with 480p resolution
```
$ python3 main.py -c -r 480p
```