from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.tag import CRFTagger
import time


class PemrosesanSerial:

    def __init__(self, result_praprengolahan):
        self.temp = result_praprengolahan

    def serial_stemming(self):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        result = []
        start = time.perf_counter()
        for word in self.temp:
            result.append(stemmer.stem(word))
        finish = time.perf_counter()
        print("Stemming Process Finish!")
        return round(finish - start)

    def serial_pos_tagging(self):
        ct = CRFTagger()
        ct.set_model_file('all_indo_man_tag_corpus_model.crf.tagger')
        data = [self.temp]
        start = time.perf_counter()
        ct.tag_sents(data)
        print("POS-Tagging Process Finish!")
        finish = time.perf_counter()
        return round(finish - start)
