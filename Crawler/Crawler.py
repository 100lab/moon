from MoonInsta import MoonInsta
import selenium.webdriver as webdriver
from WordList import get_words

def main():
    print('***start mooncle crawler***')
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('disable-gpu')
    browser = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

    moon = MoonInsta(browser)

    words = get_words()

    for word in words:
        count = moon.get_word_count(word)
        print(word + " : " + count)

    #ret = moon.get_word_count('존맛탱')
    #print("존맛탱:" + ret)
    #ret = moon.get_word_count('jmt')
    #print('jmt:' + ret)    
    #ret = moon.get_word_count('osaka')
    #print('osaka:' + ret)

    browser.close()
    pass

if __name__ == '__main__':
    main()
