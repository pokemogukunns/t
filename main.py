"""
YouTube video and audio downloader.

It is a command-line based video and audio downloader from YouTube in various
video resolutions (360p, 480p, 720p) and audio in mp3 format. It has an easy to
use command-line interface so that we can use it right from the Terminal.

Author: Alemnew M.
Date: Jul 2013 E.C
"""

import os
import sys
import argparse
import pyperclip
from pytube import YouTube
from pytube.cli import on_progress
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip


file_size = 0

def build_cli():
    """ Build Command-line interface for the downloader."""
    parser = argparse.ArgumentParser(prog='main.py',
                                    usage='ydm {-u URL | -c} ',
                                    description='YouTube video and Audio downloader.',
                                    epilog='Enjoy the program :)'
                                    )
    group_one = parser.add_mutually_exclusive_group()
    group_one.add_argument('-u',
                        '--url',
                        action='store',
                        help='URL of the video from YouTube'
                        )
    group_one.add_argument('-c',
                        '--clipboard',
                        action='store_true',
                        help='copy URL from clipboard'
                        )
    group_two = parser.add_mutually_exclusive_group()
    group_two.add_argument('-a',
                        '--audio-only',
                        action='store_true',
                        help='download audio only in mp3 format'
                        )
    group_two.add_argument('-r',
                        '--resolution',
                        action='store',
                        choices=['360p','480p', '720p'],
                        help='resolution (quality) of the video.'
                        )
    parser.version = '2.0'
    parser.add_argument('-v',
                        '--version',
                        action='version'
                        )
    return parser.parse_args()

def on_complete(stream, filepath):
    """ A function to be triggered when the file is fully downloaded."""
    global cli
    if cli.audio_only:
        print('Converting audio to mp3. This might take some time.\n')
        mp4_to_mp3(filepath)
        print("\nDownload has completed.\n")


def size_in_mb(size_in_bytes):
    """ Convert file size bytes to MB or kB."""
    if size_in_bytes < 10**6:
        return size_in_bytes // 1000
    else:
        return size_in_bytes // 10**6


def mp4_to_mp3(filepath):
    """ Convert mp4 audios to mp3."""
    audio_clip = AudioFileClip(filepath)
    mp3_filename = filepath[:-3] + 'mp3'
    audio_clip.write_audiofile(mp3_filename)
    os.remove(filepath)
    audio_clip.close()


def download_audio(audio):
    """ Download audio from YouTube."""
    global file_size
    file_size = size_in_mb(audio.filesize)
    
    home_dir = os.environ['HOME']
    path = f'{home_dir}/Downloads/Music'

    print('-'*60)
    print(f'Filename:\t{audio.title}')
    print(f'Location:\t{path}')
    print(f'Size:\t\t{file_size} MB\n')

    audio.download(path, audio.title + '.mp4') 



cli = build_cli()
if cli.clipboard:
    video_url = pyperclip.paste()
elif cli.url:
    video_url = cli.url
else:
    print('\nPlease provide the URL of the video.')
    print('\nUsage: "python3 main.py --help" to get more info\n')
    sys.exit()