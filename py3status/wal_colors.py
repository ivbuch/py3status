# -*- coding: utf-8 -*-
import os
import json
from pathlib import Path
import pprint

def read_wal_colors():
    wal_file = str(Path.home()) + "/.cache/wal/colors.json"
    if not os.path.exists(wal_file):
        return {}

    with open(wal_file) as json_data:
        d = json.load(json_data)
        fg = d['special']['foreground']
        return {'color': fg, 'color_good': fg, 'color_bad': fg, 'color_degraded': fg}

if __name__ == '__main__':
    pprint.pprint(read_wal_colors())
