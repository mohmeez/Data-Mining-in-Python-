from collections import Counter

import wikipedia
import warnings
warnings.catch_warnings()
warnings.simplefilter("ignore")

class Wiki:
    """Class that downloads a 100 wikipedia articles and writes them to a text file in the local folder"""
    def __init__(self, title):
        self.title = title

    def get_wiki(self):
        """function that """
        wiki_articles = wikipedia.search(self.title, results=4)
        with open('text_file.txt', 'w', encoding='utf-8') as f:
            for article in wiki_articles:
                try:
                    f.write(wikipedia.page(str(article), auto_suggest=False).content)
                except wikipedia.exceptions.DisambiguationError as e:
                    f.write(str(e.options))
        f.close()


class TextProcessor():
    """A class that processes the text and cleans it for frequent pattern mining"""
    def __init__(self):
        self.stopWordsList = []
        self.filteredText = []
        self.word_frequency = {}
        self.itemset = {}
        self.itemset_ordered_desc = {}
        self.final_trans_pattern = {}

    def split_words(self):
        """
        :return: a list of dictionaries with key as words in a sentence and value as their frequencies
        """
        with open('text_file.txt', 'r', encoding='utf-8') as f:
            subList = f.read().split('.')  # split on a period first
        for items in subList:
            self.filteredText.append(items.lower().split(" "))  # split on spaces

        self.word_frequency = [dict(Counter(x)) for x in self.filteredText]
        return self.word_frequency

    def setStopWords(self, received=["0o", "0s", "3a", "3b", "3d", "6b", "6o", "a", "a1", "a2", "a3", "a4", "ab", " ",
                                     '{\\begin{cases}{\\text{nil}}&{\\text{if}}\\', "l={\\text{cons}}\\,a\\,l'\\end{cases}}}\n",
                                     '1\n', '{l+r}{2}}}\n', '2\n', '\n', "able", "about", "above", "abst", "ac", "accordance",
                                     "across", "act", "actually", "ad", "added", "adj", "ae", "af", "affected", "",
                                     "affecting", "affects", "after", "afterwards", "ag", "again", "against", "ah",
                                     "ain", "ain't", "aj", "al", "all", "allow", "allows", "almost", "alone", "along",
                                     "already", "also", "although", "always", "am", "among", "amongst", "amoungst",
                                     "amount", "an", "and", "announce", "another", "any", "anybody", "anyhow",
                                     "anymore", "anyone", "anything", "anyway", "anyways", "anywhere", "ao", "ap",
                                     "apart", "apparently", "appear", "appreciate", "appropriate", "approximately",
                                     "ar", "are", "aren", "arent", "aren't", "arise", "around", "as", "a's", "aside",
                                     "ask", "asking", "associated", "at", "au", "auth", "av", "available", "aw",
                                     "away", "awfully", "ax", "ay", "az", "b", "b1", "b2", "b3", "ba", "back", "bc",
                                     "bd", "be", "became", "because", "become", "becomes", "becoming", "been",
                                     "before", "beforehand", "begin", "beginning", "beginnings", "begins", "behind",
                                     "being", "believe", "below", "beside", "besides", "best", "better", "between",
                                     "beyond", "bi", "bill", "biol", "bj", "bk", "bl", "bn", "both", "bottom", "bp",
                                     "br", "brief", "briefly", "bs", "bt", "bu", "but", "bx", "by", "c", "c1", "c2",
                                     "c3", "ca", "call", "came", "can", "cannot", "cant", "can't", "cause", "causes",
                                     "cc", "cd", "ce", "certain", "certainly", "cf", "cg", "ch", "changes", "ci",
                                     "cit", "cj", "cl", "clearly", "cm", "c'mon", "cn", "co", "com", "come", "comes",
                                     "con", "concerning", "consequently", "consider", "considering", "contain",
                                     "containing", "contains", "corresponding", "could", "couldn", "couldnt",
                                     "couldn't", "course", "cp", "cq", "cr", "cry", "cs", "c's", "ct", "cu",
                                     "currently", "cv", "cx", "cy", "cz", "d", "d2", "da", "date", "dc", "dd",
                                     "de", "definitely", "describe", "described", "despite", "detail", "df", "di",
                                     "did", "didn", "didn't", "different", "dj", "dk", "dl", "do", "does", "doesn",
                                     "doesn't", "doing", "don", "done", "don't", "down", "downwards", "dp", "dr",
                                     "ds", "dt", "du", "due", "during", "dx", "dy", "e", "e2", "e3", "ea", "each",
                                     "ec", "ed", "edu", "ee", "ef", "effect", "eg", "ei", "eight", "eighty", "either",
                                     "ej", "el", "eleven", "else", "elsewhere", "em", "empty", "en", "end", "ending",
                                     "enough", "entirely", "eo", "ep", "eq", "er", "es", "especially", "est", "et",
                                     "et-al", "etc", "eu", "ev", "even", "ever", "every", "everybody", "everyone",
                                     "everything", "everywhere", "ex", "exactly", "example", "except", "ey", "f",
                                     "f2", "fa", "far", "fc", "few", "ff", "fi", "fifteen", "fifth", "fify", "fill",
                                     "find", "fire", "first", "five", "fix", "fj", "fl", "fn", "fo", "followed",
                                     "following", "follows", "for", "former", "formerly", "forth", "forty", "found",
                                     "four", "fr", "from", "front", "fs", "ft", "fu", "full", "further",
                                     "furthermore", "fy", "g", "ga", "gave", "ge", "get", "gets", "getting", "gi",
                                     "give", "given", "gives", "giving", "gj", "gl", "go", "goes", "going", "gone",
                                     "got", "gotten", "gr", "greetings", "gs", "gy", "h", "h2", "h3", "had", "hadn",
                                     "hadn't", "happens", "hardly", "has", "hasn", "hasnt", "hasn't", "have", "haven",
                                     "haven't", "having", "he", "hed", "he'd", "he'll", "hello", "help", "hence",
                                     "her", "here", "hereafter", "hereby", "herein", "heres", "here's", "hereupon",
                                     "hers", "herself", "hes", "he's", "hh", "hi", "hid", "him", "himself", "his",
                                     "hither", "hj", "ho", "home", "hopefully", "how", "howbeit", "however", "how's",
                                     "hr", "hs", "http", "hu", "hundred", "hy", "i", "i2", "i3", "i4", "i6", "i7",
                                     "i8", "ia", "ib", "ibid", "ic", "id", "i'd", "ie", "if", "ig", "ignored", "ih",
                                     "ii", "ij", "il", "i'll", "im", "i'm", "immediate", "immediately", "importance",
                                     "important", "in", "inasmuch", "inc", "indeed", "index", "indicate", "indicated",
                                     "indicates", "information", "inner", "insofar", "instead", "interest", "into",
                                     "invention", "inward", "io", "ip", "iq", "ir", "is", "isn", "isn't", "it", "itd",
                                     "it'd", "it'll", "its", "it's", "itself", "iv", "i've", "ix", "iy", "iz", "j",
                                     "jj", "jr", "js", "jt", "ju", "just", "k", "ke", "keep", "keeps", "kept", "kg",
                                     "kj", "km", "know", "known", "knows", "ko", "l", "l2", "la", "largely", "last",
                                     "lately", "later", "latter", "latterly", "lb", "lc", "le", "least", "les",
                                     "less", "lest", "let", "lets", "let's", "lf", "like", "liked", "likely", "line",
                                     "little", "lj", "ll", "ll", "ln", "lo", "look", "looking", "looks", "los", "lr",
                                     "ls", "lt", "ltd", "m", "m2", "ma", "made", "mainly", "make", "makes", "many",
                                     "may", "maybe", "me", "mean", "means", "meantime", "meanwhile", "merely", "mg",
                                     "might", "mightn", "mightn't", "mill", "million", "mine", "miss", "ml", "mn",
                                     "mo", "more", "moreover", "most", "mostly", "move", "mr", "mrs", "ms", "mt",
                                     "mu", "much", "mug", "must", "mustn", "mustn't", "my", "myself", "n", "n2", "na",
                                     "name", "namely", "nay", "nc", "nd", "ne", "near", "nearly", "necessarily",
                                     "necessary", "need", "needn", "needn't", "needs", "neither", "never",
                                     "nevertheless", "new", "next", "ng", "ni", "nine", "ninety", "nj", "nl", "nn",
                                     "no", "nobody", "non", "none", "nonetheless", "noone", "nor", "normally", "nos",
                                     "not", "noted", "nothing", "novel", "now", "nowhere", "nr", "ns", "nt", "ny", "o",
                                     "oa", "ob", "obtain", "obtained", "obviously", "oc", "od", "of", "off", "often",
                                     "og", "oh", "oi", "oj", "ok", "okay", "ol", "old", "om", "omitted", "on", "once",
                                     "one", "ones", "only", "onto", "oo", "op", "oq", "or", "ord", "os", "ot", "other",
                                     "others", "otherwise", "ou", "ought", "our", "ours", "ourselves", "out", "outside",
                                     "over", "overall", "ow", "owing", "own", "ox", "oz", "p", "p1", "p2", "p3", "page",
                                     "pagecount", "pages", "par", "part", "particular", "particularly", "pas", "past",
                                     "pc", "pd", "pe", "per", "perhaps", "pf", "ph", "pi", "pj", "pk", "pl", "placed",
                                     "please", "plus", "pm", "pn", "po", "poorly", "possible", "possibly",
                                     "potentially",
                                     "pp", "pq", "pr", "predominantly", "present", "presumably", "previously",
                                     "primarily",
                                     "probably", "promptly", "proud", "provides", "ps", "pt", "pu", "put", "py", "q",
                                     "qj",
                                     "qu", "que", "quickly", "quite", "qv", "r", "r2", "ra", "ran", "rather", "rc",
                                     "rd",
                                     "re", "readily", "really", "reasonably", "recent", "recently", "ref", "refs",
                                     "regarding", "regardless", "regards", "related", "relatively", "research",
                                     "research-articl", "respectively", "resulted", "resulting", "results", "rf",
                                     "rh", "ri", "right", "rj", "rl", "rm", "rn", "ro", "rq", "rr", "rs", "rt", "ru",
                                     "run", "rv", "ry", "s", "s2", "sa", "said", "same", "saw", "say", "saying",
                                     "says", "sc", "sd", "se", "sec", "second", "secondly", "section", "see",
                                     "seeing", "seem", "seemed", "seeming", "seems", "seen", "self", "selves",
                                     "sensible", "sent", "serious", "seriously", "seven", "several", "sf", "shall",
                                     "shan", "shan't", "she", "shed", "she'd", "she'll", "shes", "she's", "should",
                                     "shouldn", "shouldn't", "should've", "show", "showed", "shown", "showns",
                                     "shows", "si", "side", "significant", "significantly", "similar", "similarly",
                                     "since", "sincere", "six", "sixty", "sj", "sl", "slightly", "sm", "sn", "so",
                                     "some", "somebody", "somehow", "someone", "somethan", "something", "sometime",
                                     "sometimes", "somewhat", "somewhere", "soon", "sorry", "sp", "specifically",
                                     "specified", "specify", "specifying", "sq", "sr", "ss", "st", "still", "stop",
                                     "strongly", "sub", "substantially", "successfully", "such", "sufficiently",
                                     "suggest", "sup", "sure", "sy", "system", "sz", "t", "t1", "t2", "t3", "take",
                                     "taken", "taking", "tb", "tc", "td", "te", "tell", "ten", "tends", "tf", "th",
                                     "than", "thank", "thanks", "thanx", "that", "that'll", "thats", "that's",
                                     'structures\nchapter',
                                     "that've", "the", "their", "theirs", "them", "themselves", "then", "thence",
                                     "there", "thereafter", "thereby", "thered", "therefore", "therein", "there'll",
                                     "thereof", "therere", "theres", "there's", "thereto", "thereupon", "there've",
                                     "these", "they", "theyd", "they'd", "they'll", "theyre", "they're", "they've",
                                     "thickv", "thin", "think", "third", "this", "thorough", "thoroughly", "those",
                                     "thou", "though", "thoughh", "thousand", "three", "throug", "through",
                                     "throughout",
                                     "thru", "thus", "ti", "til", "tip", "tj", "tl", "tm", "tn", "to", "together",
                                     'tree\nsuffix',
                                     "too", "took", "top", "toward", "towards", "tp", "tq", "tr", "tried", "tries",
                                     '(example',
                                     "truly", "try", "trying", "ts", "t's", "tt", "tv", "twelve", "twenty", "twice",
                                     "two", "tx", "u", "u201d", "ue", "ui", "uj", "uk", "um", "un", "under",
                                     "unfortunately",
                                     "unless", "unlike", "unlikely", "until", "unto", "uo", "up", "upon", "ups", "ur",
                                     "us",
                                     "use", "used", "useful", "usefully", "usefulness", "uses", "using", "usually",
                                     'graph\ndirected',
                                     "ut", "v", "va", "value", "various", "vd", "ve", "ve", "very", "via", "viz", "vj",
                                     "vo", "vol", "vols", "volumtype", "vq", "vs", "vt", "vu", "w", "wa", "want",
                                     "wants",
                                     "was", "wasn", "wasnt", "wasn't", "way", "we", "wed", "we'd", "welcome", "well",
                                     'tree\nbinary',
                                     "we'll", "well-b", "went", "were", "we're", "weren", "werent", "weren't", "we've",
                                     "what", "whatever", "what'll", "whats", "what's", "when", "whence", "whenever",
                                     'table\nhash',
                                     "when's", "where", "whereafter", "whereas", "whereby", "wherein", "wheres", "(how",
                                     "where's", "whereupon", "wherever", "whether", "which", "while", "whim", "whither",
                                     "who", "whod", "whoever", "whole", "who'll", "whom", "whomever", "whos", "who's",
                                     "whose", "why", "why's", "wi", "widely", "will", "willing", "wish", "with",
                                     "within",
                                     "without", "wo", "won", "wonder", "wont", "won't", "words", "world", "would", '-',
                                     "wouldn", "wouldnt", "wouldn't", "www", "x", "x1", "x2", "x3", "xf", "xi", "xj",
                                     "xk", "xl", "xn", "xo", "xs", "xt", "xv", "xx", "y", "y2", "yes", "yet", "yj",
                                     'location;\nprint',
                                     "yl", "you", "youd", "you'd", "you'll", "your", "youre", "you're", "yours", '–',
                                     "yourself", "yourselves", 'tree\n\n\n===', "you've", "yr", "ys", "yt", "z", "zero",
                                     "zi", "zz", "==\\n\n\n=="]):
        """ set stop words as received in the parameters """
        self.stopWordsList = received

    def getStopWords(self):
        ''' return stop words '''
        return self.stopWordsList

    def getFilteredText(self):
        """
        :return: a dictionary after removing the stop words
        """
        for dict in self.word_frequency:
            for key in list(dict.keys()):  # create a copy of the original list to loop over and delete
                if key in self.getStopWords():
                    del dict[key]
        return self.word_frequency

    def pruned_freq_dict(self, threshold=2):
        """
        :param threshold: delete all the words that appear less than the threshold value --> not important enough
        :return: return the dictionary with words that appear more than twice in a sentence
        """
        for dict in self.word_frequency:
            for key, val in list(dict.items()):
                if val < threshold:
                    del dict[key]
        return self.word_frequency

    def remove_empty_dicts(self):
        """
        :return: a list of dictionaries after removing empty dictionaries from the list
        """
        self.word_frequency = [item for item in self.word_frequency if item]
        return self.word_frequency

    def sort_freq_dict(self):
        """
        :return: a soted dictionary of the words in a sentence as the keys and the value as their frequencies in a sentence
        """
        new = []
        for i in list(self.word_frequency):
            new.append(dict(sorted(i.items(), key=lambda x: x[1], reverse=True)))
        self.word_frequency = new
        return self.word_frequency

    def most_frequent(self):
        for item in self.word_frequency:
            for key in item.keys():
                if key in self.itemset:
                    self.itemset[key] += 1
                else:
                    self.itemset[key] = 1
        return self.itemset

    def sort_desc(self):
        """
        :return: A sorted ditionary with key as words and value as the frequency (The requency pattern itemset)
        """
        self.itemset_ordered_desc = dict(sorted(self.itemset.items()), key=lambda x: x[1], reverse=True)
        return self.itemset_ordered_desc

    def sort_desc_del(self, min_threshold=2):
        """
        :param min_threshold: The limit that decides which item should be deleted from the itemset
        :return: A dictionary with the frequently occuring words that appear more than twice in each transaction
        """
        self.itemset_ordered_desc = dict(sorted(self.itemset.items(), key=lambda x: x[1], reverse=True))
        for key, val in list(self.itemset_ordered_desc.items()):
            if val < min_threshold:
                del self.itemset_ordered_desc[key]

        return self.itemset_ordered_desc

    def create_transaction_pattern(self):
        """
        :return: a frozen set dictionary where the keys are the words in a sentence and values are the words that occur
        most frequently after mining the pattern frequencies
        """
        for trans in self.word_frequency:
            for item in self.itemset_ordered_desc:
                if item in trans:
                    self.final_trans_pattern[frozenset(trans)] = [i for i in self.itemset_ordered_desc.keys() and trans
                                                                  if i in self.itemset_ordered_desc and trans]
        return self.final_trans_pattern




if __name__ == '__main__':
    wiki_object = Wiki("Data Structures and algorithms")
    wiki_object.get_wiki()
    text_object = TextProcessor()
    text_object.setStopWords()
    print("dictionary before cleaning the stop words:\n\t", text_object.split_words())
    print()
    print('*' * 300)
    print()
    print("dictionary after cleaning the stop words:\n\t", text_object.getFilteredText())
    print()
    print('*' * 300)
    print()
    print("STOP WORDS: \n\t", text_object.getStopWords())
    print()
    print('*' * 300)
    print()
    print(text_object.pruned_freq_dict())
    print()
    print('*' * 300)
    print()
    print("The following is after removing the empty dictonaries:\n\t", text_object.remove_empty_dicts())
    print()
    print('*' * 300)
    print()
    print("The following is after sorting the dictionaries based on frequencies:\n\t", text_object.sort_freq_dict())
    print()
    print('*' * 300)
    print()
    print("dict after finding the most frequent: \n\t", text_object.most_frequent())
    print()
    print('*' * 300)
    print()
    print("dict after sorting the most frequent: \n\t", text_object.sort_desc())
    print()
    print('*' * 300)
    print()
    print("These are the frequent pattern words/set: \n\t", text_object.sort_desc_del())
    print()
    print('*' * 300)
    print()
    print("These are the words with their frequencies in a sentences (a dictionary as a key) and the frequent word from,"
          " that sentence that appears in the most frequent pattern \n\t", text_object.create_transaction_pattern())


