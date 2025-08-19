from zuu.scoop import SCOOP_PATH
import os

def get_gauto_index():
    for path in os.listdir(SCOOP_PATH / 'buckets' / 'gauto' / 'bucket'):
        yield os.path.splitext(os.path.basename(path)[3:])[0]
        