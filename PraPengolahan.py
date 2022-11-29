import nltk


class PraPengolahan:

    def __init__(self, filename):
        self.text = open(filename, "r").read()

    def case_fold_text(self):
        case_fold = self.text.lower()
        return case_fold

    def tokenize_text(self, case_fold):
        tokens = nltk.tokenize.word_tokenize(case_fold)
        return tokens

    def prepro(self):
        preprocess1 = self.case_fold_text()
        preprocess2 = self.tokenize_text(preprocess1)
        print("pra-pengolahan selesai")
        return preprocess2
