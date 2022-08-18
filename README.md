## Annotation tools for ESD Data
Tools for converting *.xml in CVAT into mask.

### Usage example
* Transform `.xml` annotation from CVAT into image masks
```shell
python annotation_converter --image-dir /path/to/raw/images  --cvat-xml /path/to/annotations.xml --output-dir /path/to/output-mask
```

* Analysis surgical scores from manual annotations. Comments in `./data_stat.py`
