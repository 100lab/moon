class WordDB(object):
    """word controller"""

    def __init__(self):
        self.words = {}
        self.words['핑프'] = '(핑)거 (프)린세스손가락 공주라는 뜻으로, 조금만 검색해봐도 쉽게 찾을 수 있는 정보를 찾아보지도 않고 바로 남에게만 물어보는 진상을 뜻한다.'
        self.words['ㄱㅇㄷ'] = '개이득. 뜻하지 않은 횡재'
        self.words['ㅇㅈ'] = '인정. 특정한 사건을 동의 및 인정한다는 의미'
        pass

    def get_words(self):
        return self.words.keys()


