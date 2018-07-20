from MoonInsta import MoonInsta
from WordList import get_words
import selenium.webdriver as webdriver
from urllib import parse
import redis

def main():
    print('***start mooncle crawler***')
    
    # initialize for chrome browser
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('disable-gpu')
    browser = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

    # initialize for redis db
    r = redis.Redis(db = 0)

    # initialize for Moon
    moon = MoonInsta(browser)
    
    #initialize for words
    words = get_words()

    #crawling logic
    for word in words:
        count = moon.get_word_count(word)
        encoded_word = parse.quote(word)
        r.set(encoded_word,count)
        print(word + " : " + count)
    
    #finalize
    browser.close()
    
    pass

if __name__ == '__main__':
    main()
