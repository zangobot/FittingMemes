# This script has been taken from https://github.com/alpv95/MemeProject.
# I've just done someslight modifications.
# Remember to star it ;-)


from bs4 import BeautifulSoup
import requests
import shutil
import os.path

save_path = 'data'
n_captions = 10     #number of pages for meme
n_templates = 3     #number of pages onthe site
Uerrors = 0


for i in range(1,n_templates):
    if i == 1:
        url = 'https://memegenerator.net/memes/popular/alltime'
    else:
        url = 'https://memegenerator.net/memes/popular/alltime/page/' + str(i)

    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    chars = soup.find_all(class_='char-img')
    links = [char.find('a') for char in chars]
    imgs = [char.find('img') for char in chars]
    assert len(links) == len(imgs)
    for j,img in enumerate(imgs):

        for k in range(1,n_captions):
            if k == 1:
                URL = 'https://memegenerator.net' + links[j]['href']
            else:
                URL = 'https://memegenerator.net' + links[j]['href'] + '/images/popular/alltime/page/' + str(k)

            R = requests.get(URL)
            SOUP = BeautifulSoup(R.text,'html.parser')
            CHARS = SOUP.find_all(class_='char-img')
            IMGS = [char.find('img') for char in CHARS]
            index = (k-1)*15
            img_url = img['src']
            name_of_file = img_url.split('/')[-1]
            completeName = os.path.join(save_path, name_of_file)
            for meme in IMGS:
                
                filename = completeName +'{}'.format(index)
                index = (index+1)
                url = meme['src']
                print(url)
                response = requests.get(url, stream=True)
                print(filename)
                with open(filename,'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                del response


