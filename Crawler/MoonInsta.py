from Moon import Moon
from bs4 import BeautifulSoup
from urllib import parse
import time

class MoonInsta(Moon):
    """Implementation of Moon for Instagram"""
    def get_word_count(self, word):
        url_tmp = "www.instagram.com/explore/tags/" + word
        url = "http://" + parse.quote(url_tmp)
        self.browser.get(url)
        
        for i in range(1,11):
            soup = BeautifulSoup(self.browser.page_source, "html.parser")
            tag = soup.find("span",{"class": "g47SY "})
            if not tag:
                time.sleep(1)
            else:
                break


        count = tag.text
        return count




