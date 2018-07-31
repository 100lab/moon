from MoonInsta import MoonInsta
import selenium.webdriver as webdriver
import urllib.parse
from WordDB import WordDB
import redis
import operator
import datetime

def main():
    print('***start mooncle crawler***')
    print(datetime.datetime.now())

    # initialize for chrome browser
    #print('initialize for chrome browser')
    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('headless')
    #chrome_options.add_argument('disable-gpu')
    #browser = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

    print('initialize for firefox browser')
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')
    browser = webdriver.Firefox(firefox_options=firefox_options)

    # initialize redis db
    print('initialize redis db')
    r = redis.Redis(db = 0)
    
    # initialize Moon
    print('initialize moon')
    moon = MoonInsta(browser)
    
    #initialize words
    print('initialize words')
    wdb = WordDB()
    word_count_tuples = {}

    #crawling logic
    print('start crawling')
    for word in wdb.get_words():
        count = moon.get_word_count(word) # remove it for faster debug
        # count = 0
        
        #err handling
        if count == 0:
            tmp = r.get(urllib.parse.quote(word))
            if (tmp == None):
                count = 0
            else:
                count = int(tmp.decode("utf-8"))

        word_count_tuples[word] = count
        print(word + ":" + str(count))

    #sort
    word_count_tuples = sorted(word_count_tuples.items(), key=operator.itemgetter(1), reverse=True)
        
    print('show sorted result')
    print(word_count_tuples)

    print('start DB store sequence')
    #store redis
    print("store words count")
    ## word count
    for wct in word_count_tuples:
        word = wct[0]
        count = wct[1]
        encoded_word = urllib.parse.quote(word)
        r.set(encoded_word,count) # remove it for faster debug
        print("(d)" + word + "(e)" + encoded_word + ":" + str(count))

    ## mean
    for wct in word_count_tuples:
        word = wct[0]
        word_mean = "mean_" + word
        encoded_word_mean = urllib.parse.quote(word_mean)
        mean = wdb.get_mean(word)
        r.set(encoded_word_mean, mean)
        print("(d)" + word_mean + "(e)" + encoded_word_mean + ":" + mean)

    ## top 20 word
    r.delete("top20_words")
    r.delete("top20_counts")
    i = 0
    for wct in word_count_tuples:
        if (i == 20):
            break
        r.rpush("top20_words",wct[0])
        r.rpush("top20_counts",wct[1])
        i+=1

    print("check db values")
    tmps = r.lrange("top20_words",0,-1)
    for btmp in tmps:
        word = btmp.decode('utf-8')
        mean_word = "mean_" + word
        encoded_word_mean = urllib.parse.quote(mean_word)
        bmean = r.get(encoded_word_mean)
        mean = bmean.decode('utf-8')
        
        encoded_word = urllib.parse.quote(word)
        bcount = r.get(encoded_word)
        count = int(bcount.decode('utf-8'))
        print(word + " [" + str(count) + "] : " + mean)
        
    
    #finalize
    browser.close()
    
    print('***end mooncle crawler***')
    print(datetime.datetime.now())
    print('\r\n\r\n\r\n')

    pass

if __name__ == '__main__':
    main()
