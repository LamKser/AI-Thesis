from urllib.request import urlopen, urlretrieve
from os.path import join
import os

from bs4 import BeautifulSoup
from tqdm import tqdm


def save_image_from_url(url, save_dir='crawl'):
    name = url.split('/')[-1]
    try:
        urlretrieve(url, join(save_dir, name))
    except:
        pass

class UnderwaterPhotographyGuide:

    def __init__(self, save_dir='crawl', home_url='https://www.uwphotographyguide.com'):
        self.save_dir = save_dir
        self.home_url = home_url
        self.sub_urls = [f'/uw-articles?page={i}' for i in range(17)]

        # Create save directory
        if not os.path.exists(save_dir):
            print(f'"{save_dir}" does not exist. Creating {save_dir}.........')
            os.makedirs(save_dir)
        else:
            print(f'"{save_dir}" exists.')
    
    def __crawl(self, tag, tag_name, class_):
        article = tag.find_all(tag_name, class_=class_)
        for even in article:
            a_tag_link = even.find('a').get('href')

            # Get page url and open it
            page_url = self.home_url + a_tag_link
            tmp_page = urlopen(page_url)
            tmp_soup = BeautifulSoup(tmp_page, 'html.parser')
            tmp_div_tag = tmp_soup.find_all('div', class_='field-item even')
            for dt in tmp_div_tag:
                p_tag_src = dt.find_all('p')
                for p_tag in p_tag_src:
                    check_exist_img = p_tag.find('img')
                    if check_exist_img:
                        img_url = check_exist_img.get('src')
                        img_url = self.home_url + img_url if 'https' not in img_url else img_url
                        save_image_from_url(img_url, self.save_dir)

    def __crawl_underwater_photography(self, url):
        page = urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        div_tag = soup.find('div', class_='uw-article').find_all('div', class_='uw-article-in')
        for tag in div_tag:
            self.__crawl(tag, 'div', 'each-article even')
            self.__crawl(tag, 'div', 'each-article odd')

    def __call__(self):
        for sub in tqdm(self.sub_urls):
            url = self.home_url + sub
            self.__crawl_underwater_photography(url)
    

if __name__ == '__main__':
    crawl = UnderwaterPhotographyGuide()
    crawl()
    