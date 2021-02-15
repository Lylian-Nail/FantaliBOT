import requests
import shutil

def download_img(url, name=None, path='./'):

    if name is None:
        name = url.split('/')[-1]
    name = path.rstrip('/') + '/' + name

    r = requests.get(url, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True

        with open(name, 'wb') as fd:
            shutil.copyfileobj(r.raw, fd)

if __name__ == "__main__":
   download_img('https://thispersondoesnotexist.com/image')
