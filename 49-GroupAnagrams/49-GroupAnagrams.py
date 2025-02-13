from collections import defaultdict

class Solution:
    def groupAnagrams(self, words):
        len_words = len(words)
        
        
        #words = ["eat","tea","tan","ate","nat","bat"]

        word_to_freq_map = defaultdict(int)
        for i in range(0, len_words):
            word = words[i]
            word_to_freq_map[word] += 1


        #word_to_chrs_map['eat'] = 'aet'
        #word_to_chrs_map['ate'] = 'aet'
        #word_to_chrs_map['tea'] = 'aet'
        #word_to_chrs_map['tan'] = 'ant'
        #word_to_chrs_map['nat'] = 'ant'
        #word_to_chrs_map['bat'] = 'abt'
        #word_to_chrs_map = {
        #  'eat': 'aet'
        #  , 'ate': 'aet'
        #  , 'tea': 'aet'
        #  , ...
        #}

        word_to_chrs_map = {}
        for i in range(0, len_words):
            word = words[i]
            word_to_chrs_map[word] = ''.join(sorted(word))
        

        #chrs_to_words_map['aet'] = ['eat', 'ate', 'tea']
        #chrs_to_words_map['ant'] = ['tan', 'nat']
        #chrs_to_words_map['abt'] = ['bat']

        chrs_to_words_map = defaultdict(list)
        for word in word_to_chrs_map.keys():
            chrs = word_to_chrs_map[word]
            chrs_to_words_map[chrs].extend([word] * word_to_freq_map[word])

        ret_val = []
        for chrs in chrs_to_words_map.keys():
            ret_val.append(chrs_to_words_map[chrs])
        
        return ret_val