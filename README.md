# Parse option dump

mock optparse module to list options.

Usage:

Copy `youtube_dl` lib from site-packages directory. On Linux, run:

`sed -i.bak 's/import optparse/import optparse2 as optparse/' youtube_dl/options.py`

Modify optparse2.py to your own things.

## Example usage

(Again, on Linux)

`pip install youtube_dl`

Note the install directory from the output and replace here:

```sh
cp -r <INSTALL DIRECTORY>/youtube_dl .
sed -i.bak 's/import optparse/import optparse2 as optparse/' youtube_dl/options.py
```

Then you can, **from the current directory**, dump the parsing options.

Part of the output:

```txt
-k --keep-video {'action': 'store_true', 'dest': 'keepvideo', 'default': False, 'help': 'Keep the video file on disk after the post-processing; the video is erased by default'}
--no-post-overwrites None {'action': 'store_true', 'dest': 'nopostoverwrites', 'default': False, 'help': 'Do not overwrite post-processed files; the post-processed files are overwritten by default'}
--embed-subs None {'action': 'store_true', 'dest': 'embedsubtitles', 'default': False, 'help': 'Embed subtitles in the video (only for mp4, webm and mkv videos)'}
--embed-thumbnail None {'action': 'store_true', 'dest': 'embedthumbnail', 'default': False, 'help': 'Embed thumbnail in the audio as cover art'}
--add-metadata None {'action': 'store_true', 'dest': 'addmetadata', 'default': False, 'help': 'Write metadata to the video file'}
```

Modify optparse2.py to your will. print statements are only for demo.

## Contribution

Contributions are welcome. :)


Instructions for Windows are welcome.

