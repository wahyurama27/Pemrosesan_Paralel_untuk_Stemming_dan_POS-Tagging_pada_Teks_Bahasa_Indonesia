from nltk.tag import CRFTagger
from multiprocessing import Process
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import time


class PemrosesanParalel:
    def __init__(self, result_split):
        self.temp = result_split

    def parallel_stemmer(self, stemmer, data):
        result = []
        for word in data:
            result.append(stemmer.stem(word))
        print("finish par_stem")

    def multi_stem(self):
        start = time.perf_counter()
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        list_of_proc = []
        for i in range(0, len(self.temp)):
            worker = Process(target=self.parallel_stemmer, args=(stemmer, self.temp[i]))
            list_of_proc.append(worker)
            worker.start()

        for proc in list_of_proc:
            proc.join()
        print("Parallel Stemming Process Finish!")
        finish = time.perf_counter()
        return round(finish - start)

    def parallel_tagger(self, tagger, data):
        temp2 = [data]
        tagger.tag_sents(temp2)
        print("Finish Par_Tag")

    def multi_tagging(self):
        tagger = CRFTagger()
        tagger.set_model_file('all_indo_man_tag_corpus_model.crf.tagger')
        list_of_proc = []
        start = time.perf_counter()
        for i in range(0, len(self.temp)):
            worker = Process(target=self.parallel_tagger, args=(tagger, self.temp[i]))
            list_of_proc.append(worker)
            worker.start()

        for proc in list_of_proc:
            proc.join()
        print("Parallel POS-Tagging Process Finish!")
        finish = time.perf_counter()
        return round(finish - start)
