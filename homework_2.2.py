import chardet
def programm_for_one_file(file_name):
    with open(file_name, "rb") as f:
        data = f.read()
        result = chardet.detect(data)
        s = data.decode(result['encoding'])
        s.lower()
        newsafr_list = list()
        newsafr_list.extend(s.split(" "))


    words_list = list()
    for words in newsafr_list:
        if len(words) > 6:
            words_list.append(words)


    words_dictionary = dict()
    for words in words_list:
       words_dictionary[words] = 0

    for words in words_list:
        words_dictionary[words] += 1


    number_list = list()
    top_words_list = list()

    for words, repetition in words_dictionary.items():
        if len(number_list) < 10:
            number_list.append(repetition)
        else:
            index = 1000000000000000000
            for number in number_list:
                if number < index:
                    index = number

            if repetition > index:
                number_list.remove(index)
                number_list.append(repetition)


    for words, repetition in words_dictionary.items():
        for number in number_list:
            if repetition == number:
                top_words_list.append(words)
    defect_list = list()
    for words in top_words_list:
        for word in top_words_list:
            if word == words:
                defect_list.append(word)
        if len(defect_list) > 1:
            top_words_list.remove(words)
        defect_list.clear()
    print(top_words_list)

programm_for_one_file("newsafr.txt")
programm_for_one_file("newscy.txt")
programm_for_one_file("newsit.txt")