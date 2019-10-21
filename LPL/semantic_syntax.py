from pymystem3 import Mystem
import re 
!pip install pymystem3
#!pip install git+https://github.com/nlpub/pymystem3

def Collocations(sentence):
    desired_sequence = ['NAN', 'NA', 'VAN']
    return [(m.span(),desired) for desired in desired_sequence for m in re.finditer(desired, sentence)]

def class_word(word_list):
    dict_class = {'A':'A','ADV':'Y',
                'ADVPRO':'Y',
                'ANUM':'A',
                'APRO':'A',
                'COM':'COM',
                'CONJ':'&',
                'INTJ':'!',
                'NUM':'C',
                'PART':'J',
                'PR':'F',
                'S':'N',
                'SPRO':'M',
                'V':'V'}
    list_class=[]
    m = Mystem()
    for word in word_list:
        word_analy = m.analyze(word)
        list_class.append(dict_class[re.match(r'[A-Z]+',word_analy[0]['analysis'][0]['gr']).group(0)])
    return list_class
#пример работы
text = "словосочетание непонятное и кривое словосочетание"
text = text.split()
sent = ''.join(class_word(text))
print(sent)
print(Collocations(sent))
