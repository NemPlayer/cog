import os
from pathlib import PurePath, Path

FONTS = {}

fonts_dir = PurePath(Path.cwd(), "fonts/")

for file in os.listdir(fonts_dir):
    if file.endswith(".ttf"):
        path_to_file = PurePath(Path.cwd(), f"fonts/{file}")
        FONTS[path_to_file.stem] = str(path_to_file)
