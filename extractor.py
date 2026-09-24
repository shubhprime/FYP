from pathlib import Path
import zipfile

with zipfile.ZipFile("fyp_data.zip", "r") as datas:
    datas.extractall("data")