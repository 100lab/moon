class WordDB(object):
    """word controller"""

    def __init__(self):
        self.words = {}
        self.words['핑프'] = '(핑)거 (프)린세스손가락 공주라는 뜻으로, 조금만 검색해봐도 쉽게 찾을 수 있는 정보를 찾아보지도 않고 바로 남에게만 물어보는 진상을 뜻한다.'
        self.words['ㄱㅇㄷ'] = '개이득. 뜻하지 않은 횡재'
        self.words['ㅇㅈ'] = '인정. 특정한 사건을 동의 및 인정한다는 의미'
        self.words['무엇'] = '뭐임? 뭥미?'
        self.words['현타'] = '현실 자각 타임'
        self.words['존버'] = '존나 버틴다'
        self.words['할많하않'] = '할말은 많지만 하지 않는다'
        self.words['복세편살'] = '복잡한 세상 편하게 살자'
        self.words['마상'] = '마음의 상처'
        self.words['비담'] = '비주얼 담당'
        self.words['혼코노'] = '혼자 코인 노래방'
        self.words['엄근진'] = '엄격, 근엄, 진지'
        self.words['갑분싸'] = '갑자기 분위기 싸해짐'
        self.words['영고'] = '영원한 고통'
        self.words['이생망'] = '이번 생은 망했다'
        self.words['팬아저'] = '팬이 아니어도 저장'
        self.words['문찐'] = '문화 찐따'
        self.words['갑분띠'] = '갑자기 분위기 띠용'
        self.words['애빼시'] = '애교 빼면 시체'
        self.words['사바사'] = '사람 by 사람'
        self.words['롬곡옾눞'] = '폭풍눈물'
        self.words['렬루'] = 'real루, 리얼루다가'
        self.words['발컨'] = '발로 컨트롤'
        self.words['덕페이스'] = '셀카찍을때 입술을 내미는 표정'
        self.words['번달번줌'] = '번호 달라고하면 번호 줌'
        self.words['괄도네넴띤'] = '팔도 비빔면'
        self.words['법블레스유'] = '법이 아니였으면 너는 이미 칼맞아 죽었다'
        pass

    def get_words(self):
        return self.words.keys()

    def get_mean(self, word):
        return self.words[word]
