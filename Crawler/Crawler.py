from MoonInsta import MoonInsta
from WordList import get_words
import selenium.webdriver as webdriver
from urllib import parse
import redis
import json
import operator

def main():
    print('***start mooncle crawler***')
    
    # initialize for chrome browser
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('disable-gpu')
    browser = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

    # initialize for redis db
    r = redis.Redis(db = 0)
    #r = redis.StrictRedis()

    # initialize for Moon
    moon = MoonInsta(browser)
    
    #initialize for words
    words = get_words()
    dictionary = {}

    #crawling logic
    for word in words:
        count = moon.get_word_count(word)
        encoded_word = parse.quote(word)
        dictionary[word] = count
        #r.set(encoded_word,count)
    
    dictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)

    result = json.dumps(dictionary)
    print(result)

    #r.execute_command('JSON.SET', 'object', '.', result)
    #reply = json.loads(r.execute_command('JSON.GET', 'object'))
    #print(reply)

    #finalize
    browser.close()
    
    pass

if __name__ == '__main__':
    main()
