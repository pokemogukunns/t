"""
YouTube video and audio downloader.

It is a command-line based video and audio downloader from YouTube in various
video resolutions (360p, 480p, 720p) and audio in mp3 format. It has an easy to
use command-line interface so that we can use it right from the Terminal.

Author: @balewgize
Date: Jul 2013 E.C
"""

import os
import sys
import argparse
import pyperclip
from pytube import YouTube
from pytube.cli import on_progress
from pytube.exceptions import RegexMatchError
from pytube.exceptions import VideoUnavailable
from moviepy.editor import VideoFileClip
from moviepy.editor import AudioFileClip


cli = ''
file_size = 0
adaptive = False
video_path = ''
audio_path = ''


def build_cli():
    """ Build Command-line interface for the downloader."""
    parser = argparse.ArgumentParser(prog='main.py',
                                    usage='python3 main.py {-u URL | -c} ',
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
                        help='copy URL from the clipboard'
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
    """ A function to be triggered whenever a file is fully downloaded."""
    global cli, video_path, audio_path

    if cli.audio_only:
        print('Converting audio to mp3. This might take some time.\n')
        mp4_to_mp3(filepath)
        print("\nDownload has completed.\n")

    if adaptive:
        if '_video.mp4' in filepath:
            video_path = filepath
        if '_audio.mp4' in filepath:
            audio_path = filepath
        if os.path.exists(video_path) and os.path.exists(audio_path):
            merge(video_path, audio_path)
    print()


def size_in_mb(size_in_bytes):
    """ Convert file size in bytes to MB or kB."""
    if size_in_bytes < 10**6:
        return size_in_bytes // 1000
    else:
        return size_in_bytes // 10**6


def merge(video_path, audio_path):
    """ Merge the given video and audio files."""
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)
    final_video = video_clip.set_audio(audio_clip)
    final_video.write_videofile(video_path[:-10] + '.mp4')
    print("\nDownload has completed.\n")
    os.remove(video_path)
    os.remove(audio_path)
    video_clip.close()
    audio_clip.close()


def mp4_to_mp3(filepath):
    """ Convert mp4 audio to mp3."""
    audio_clip = AudioFileClip(filepath)
    mp3_filename = filepath[:-3] + 'mp3'
    audio_clip.write_audiofile(mp3_filename)
    os.remove(filepath)
    audio_clip.close()


def download_audio(audio_stream):
    """ Download audio from YouTube."""
    global file_size
    file_size = size_in_mb(audio_stream.filesize)
    home_dir = os.environ['HOME']
    path = f'{home_dir}/Downloads/Music'
    print('-'*60)
    print(f'Filename:\t{audio_stream.title}')
    print(f'Location:\t{path}')
    print(f'Size:\t\t{file_size} MB\n')

    filename = audio_stream.title + '_audio.mp4'
    audio_stream.download(path, filename)


def download_video(video_stream):
    """ Download video from YouTube."""
    global file_size
    file_size = size_in_mb(video_stream.filesize)
    home_dir = os.environ['HOME']
    path = f'{home_dir}/Downloads/Video'
    print('-'*60)
    print(f'Filename:\t{video_stream.title}')
    print(f'Location:\t{path}')
    print(f'Size:\t\t{file_size} MB\n')

    filename = video_stream.title + '_video.mp4'
    video_stream.download(path, filename)


def get_video_stream(yt, resolution):
    """ Get the video stream with the given resolution."""
    global adaptive

    resolution_itag = {'360p':134, '480p':135, '720p':136}
    progressive_streams = yt.streams.filter(progressive=True)
    video_stream = progressive_streams.get_by_resolution(resolution)

    if video_stream is not None:
        return video_stream
    else:
        adaptive_streams = yt.streams.filter(adaptive=True, type='video')
        video_itag = resolution_itag[resolution]
        video_stream = adaptive_streams.get_by_itag(video_itag)
        adaptive = True
        return video_stream



def main():
    global cli, adaptive
    cli = build_cli()

    if cli.clipboard:
        video_url = pyperclip.paste()
    elif cli.url:
        video_url = cli.url
    else:
        print('\nPlease provide the URL of the video.')
        print('\nUsage: "python3 main.py --help" to get more info\n')
        sys.exit()

    try:
        yt = YouTube(video_url, 
                    on_progress_callback=on_progress,
                    on_complete_callback=on_complete
                    )
        yt.check_availability()

        if cli.audio_only:
            audio_stream = yt.streams.get_audio_only()
            download_audio(audio_stream)

        else:
            default = '720p'
            res = cli.resolution

            if res is not None:
                video_stream = get_video_stream(yt, res)
                download_video(video_stream)
                if adaptive == True:
                    audio_stream = yt.streams.get_audio_only()
                    download_audio(audio_stream)
            else:
                video_stream = get_video_stream(yt, default)
                download_video(video_stream)
                if adaptive == True:
                    audio_stream = yt.streams.get_audio_only()
                    download_audio(audio_stream)

    except RegexMatchError:
        print('\nError: the URL you provide is invalid.\n')
        print('Please provide a valid URL from YouTube.\n')
    except VideoUnavailable:
        print('\nError: this video is not availble.\n')
        print('Try another video.\n')
    except Exception as error_msg:
        print('\nError: something went wrong while trying to download.\n')
        print(error_msg)


if __name__ == '__main__':
    main()