from Moon import Moon
from bs4 import BeautifulSoup
import urllib.parse
import time

class MoonInsta(Moon):
    """Implementation of Moon for Instagram"""
    def get_word_count(self, word):
        url_tmp = "www.instagram.com/explore/tags/" + word
        url = "http://" + urllib.parse.quote(url_tmp)
        self.browser.get(url)
        
        for i in range(1,11):
            soup = BeautifulSoup(self.browser.page_source, "lxml")
            tag = soup.find("span",{"class": "g47SY "})
            if not tag:
                time.sleep(1)
            else:
                break
        if not tag:
            print("err:" + word)
            return 0

        count = int(tag.text.replace(',',''))
        return count




