def download_file(url, file_name):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                print(f"write -> {file_name}")
                f.write(chunk)
    return file_name

def getOrgImg(id):
    req = requests.get(f"https://adult.contents.fc2.com/article/{id}/")
    if req.status_code != 200:
        raise NetError
    html = req.text
    bsObject = BeautifulSoup(html, "html.parser", from_encoding='utf-8')
    _ = bsObject.select("div[class='items_article_MainitemThumb'] img")
    if len(_) > 1:
        raise Exception(_)
    elif len(_) < 1:
        raise Exception("NULLLIST")
    return "https:" + _[0]["src"]

err = []
for key, id in di.items():
    try:
        url = getOrgImg(id)
        download_file(url, f"data/{key}.jpg")
        print(key, id)
    except Exception as e:
         print("error :", key, id, e)
         err.append(key)


import re
p = re.compile('[0-9]{5,8}') 

di = {}
err = []
for _ in a:
    try:
        di[_] = p.search(Downloader(_).getTitle()).group()
    except Exception as e:
        err.append(_)
        print("error :", _, e)

url = "https://vanfem.com/"

err = []
com = []
for _ in a:
    try:
        posterURL = Downloader(_).getPoster()
        download_file(url + posterURL, f"data/{_}.png")
        com.append(_)
        print(_)
    except KeyboardInterrupt:
        break
    except Exception as e:
        err.append(_)
        print("err: ", _, e)

def pri(d):
    for _ in d:
        print(_)

def inp():
    d = []
    while True:
        _ = input()
        if _ == "":
            break
        else:
            d.append(_)
    return d