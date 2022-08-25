## Annotation tools for ESD Data
Tools for converting *.xml in CVAT into mask.

### Usage example
```shell
python converter --image-dir /path/to/raw/images  --cvat-xml /path/to/annotations.xml --output-dir /path/to/output-mask
```

* Save raw video at specific phase under 2 FPS: `raw2image.py`

* Combine all clips at specific phase into one video: `clip_video.py`

* Convert CVAT annotation into mask: `converter.py`

* Downsample and save video as image sequence: `video2image.py`