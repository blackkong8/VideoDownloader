from bs4 import BeautifulSoup
import requests

url = "https://vanfem.com/"


def download_file(url, file_name):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return file_name


class Downloader:
    def __init__(this, id):
        this.id = id

    def getSource(this):
        this.source = requests.post(
            url + f"api/source/{this.id}").json()
    
    def getTitle(this):
        html = requests.get(url + "f/{}".format(this.id)).text
        bsObject = BeautifulSoup(html, "html.parser", from_encoding='utf-8')

        title = bsObject.select("h1[class='title']")[0].text
        return title

    def getPoster(this):
        html = requests.get(url + "f/{}".format(this.id)).text
        bsObject = BeautifulSoup(html, "html.parser", from_encoding='utf-8')

        posterURL = bsObject.select("#download-poster>img")[0]["src"]
        return posterURL
        #download_file(url + posterURL, "data/{}.png".format(this.id))
