import os
import requests
import zipfile

MASTER_DOWNLOAD = "https://github.com/xenia-project/release-builds-windows/releases/latest/download/xenia_master.zip"
CANARY_DOWNLOAD = "https://github.com/xenia-canary/xenia-canary/releases/latest/download/xenia_canary.zip"


def download():
    print('Downloading Xenia...')

    r = requests.get(MASTER_DOWNLOAD)
    r.raise_for_status()
    print(f'Finished downloading Xenia in {r.elapsed.seconds}.{r.elapsed.microseconds} seconds!')
    f = open("xenia_master.zip", "wb")
    f.write(r.content)
    f.close()


def unzip():
    print('Unzipping Xenia archive...')
    file = 'xenia_master.zip'

    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extract('xenia.exe', '.')

    os.remove(file)

    print('Unzipped and deleted Xenia archive!')


if __name__ == '__main__':
    download()
    unzip()
