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


def size_in_mb(size_in_bytes):
    """ Convert file size bytes to MB or kB."""
    if size_in_bytes < 10**6:
        return size_in_bytes // 1000
    else:
        return size_in_bytes // 10**6


def mp4_to_mp3(mp4_filename, path):
    """ Convert mp4 audios to mp3."""
    full_mp4_path = os.path.join(path, mp4_filename)

    if os.path.exists(full_mp4_path):
        # getting audio content from the mp4 audio
        audio_clip = AudioFileClip(full_mp4_path)

        # save the audio content in mp3 format
        mp3_filename = mp4_filename[:-3] + 'mp3'
        full_mp3_path = os.path.join(path, mp3_filename)
        audio_clip.write_audiofile(full_mp3_path)

        # after converting to mp3, get rid of the mp4 file
        os.remove(full_mp4_path)
        audio_clip.close()
    else:
        print(f"The path '{full_mp4_path}' doesn't exist.")
        sys.exit()

cli = build_cli()
if cli.clipboard:
    video_url = pyperclip.paste()
elif cli.url:
    video_url = cli.url
else:
    print('\nPlease provide the URL of the video.')
    print('\nUsage: "python3 main.py --help" to get more info\n')
    sys.exit()