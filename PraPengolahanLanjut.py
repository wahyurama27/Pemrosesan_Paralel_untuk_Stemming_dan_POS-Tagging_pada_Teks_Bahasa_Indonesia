import math

class PraPengolahanLanjut:

    def __init__(self, result_prapengolahan):
        self.temp = result_prapengolahan

    def split_file(self, processor):
        divided_file = math.floor(len(self.temp) / processor)

        index = 0
        length = []
        token = []
        for i in range(0, len(self.temp)):
            length.append(self.temp[i])
            if i % divided_file == 0 and i != 0:
                token.append(length[index:i])
                index = i
        print("data splitted")
        return token
