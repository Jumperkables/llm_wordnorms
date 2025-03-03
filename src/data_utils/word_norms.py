__author__ = "Jumperkables"

pos_translation = {
    # USF notation
    'PP':"prepostion",
    'AD':"adverb",
    'V':"verb",
    'N':"noun",
    'QPS':"cue",
    'P':"pronoun", 
    'AJ':"adjective", 
    'I':"interjection", 
    'C':"conjunction",
    'TPS':"target",
    "ADV":"adverb",
    "AV":"adverb",
    "PRP":"prepostion",
    "ADJ":"adjective",
    "A":"adjective?",
    "INT":"interjection",
    "":None,
}
mrc_pos_trans = {
    # Part of MRC notation
    "N":"noun",
    "J":"adjective",
    "V":"verb",
    "A":"adverb",
    "O":"other",
    "R":"prepostion",
    "C":"conjunction",
    "U":"pronoun",
    "I":"interjection",
    "P":"past participle",
    " ":None,
}
simlex_pos_trans = {
    "A":"adjective",
    "N":"noun",
    "V":"verb"
}
vinson_pos_trans = {
    "object":"noun",
    "actionN":"action-noun",
    "actionV":"verb"
}
simverb_type = {
    'ANTONYMS':"antonyms", 
    'COHYPONYMS':"cohyponyms", 
    'HYPER/HYPONYMS':"hyper/hyponyms", 
    'NONE':None, 
    'SYNONYMS':"synonyms"
}
kup_reilly_pos_trans = ['Conjunction',"Name","Verb","Adverb","Determiner","Pronoun","Adjective","Abbreviation","Interjection","Preposition","Noun","Number"]


def list_avg(lst):
    if len(lst) == 0:
        return 0
    else:
        return sum(lst)/len(lst)


class Word2Norm():
    def __init__(self):
        self.NORMS = {
                'conc-m':   "Mean concreteness", 
                "conc-sd":  "Standard deviation of concreteness", 
                "nphon":    "Number of phonemes", 
                "nsyl":     "Number of syllables",
                "imag-m":   "Mean imagability",
                "imag-sd":  "Standard deviation of imagability",

                "vfreq":    "Verbal frequency",
                "kf_freq":  "Kucera & Francis frequency",

                "fam":      "Familiarity",
                "mean":     "Meaningfullness",
                "pleas":    "Pleasantness",
                "categ":    "Categorisability",
                "emo":      "Emotionality",
                "toglia":   "The 'Toglia & Battig metric (1978)' provided via in Cortese (2004)",
                "dist":     "Distinctiveness as in McRae (excluding taxonomics)",
                "eod":      "Ease of definition",

                "rt-m":     "Mean reaction time (Cortese 2004)",
                "rt-sd":    "Standard deviation of reaction time",
                "rt-nam":   "Naming reaction time (Reilly ELP)",
                "rt-lex_dec":"Alternative reaction time (Reilly ELP)",

                "simlex999-m":  "SimLex999 metric",
                "simlex999-sd": "Standard deviation of SimLex999",
                "assoc":    "Word association metric",
                "str":      "USF directional 'strength'",
                "rstr":     "USF Resonant strength",
                "oastr":    "USF overlapping strength",
                "mstr":     "USF mediated strength",
                "pos":      "Part-of-speech",
                "modal":    "Modality",
                "sim":      "Similarity, the similarity and USF strength metrics may be related",
                "sem_rel":  "Type of semantic relationship e.g. hyponym, antonym etc..",

                "sem_dens": "Semantic density (Reilly ELP)",
                "sem_neig": "Semantic neighbors (Reilly ELP)",
                "sem_div": "Semantic diversity (Reilly ELP)",

                "num_func":     "Number of functional features",
                "num_vis_mot":  "Number of visual-motor features",
                "num_vis_fs":	"number of visual form and surface features",
                "num_vis_col":	"number of visual colour features",
                "num_sound":	"number of sound features",
                "num_taste":	"number of taste features",
                "num_smell":	"number of smell features",
                "num_tact":	"number of tactile features",
                "num_ency":	"number of encyclopedic features",
                "num_tax":	"number of taxonomic features",
                "num_mean":     "number of meanings",

                "mm_vis":       "Kastner's multimodal 'visual' metric",
                "mm_txt":       "Kastner's multimodal 'textual' metric",
                "mm_pho":       "Kastner's multimodal 'phonetic' metric",
                "mm_all":       "Kastner's multimodal 'all' metric",

                # FROM SIANPAR'S INDONESIAN WORD NORMS
                "val-m":        "Mean 'Valence'",
                "val-sd":       "Standard deviation of valence",
                "arou-m":       "Mean 'Arousal'",
                "arou-sd":      "Standard deviation of arousal",
                "dom-m":        "Mean 'Dominance'",
                "dom-sd":       "Standard deviation of dominance",
                "pred-m":       "Mean 'predictability'",
                "pred-sd":      "Standard deviation of predictability",

                # From the 'LNC' dataset in Reilly's compilation
                "lnc-audi":     "Auditory",
                "lnc-gust":     "Gustatory",
                "lnc-hapt":     "Haptic",
                "lnc-interoc":  "Interoceptive",
                "lnc-olfact":   "Olfactory",
                "lnc-foot_leg": "Foot-leg",
                "lnc-hand_arm": "Hand-arm",
                "lnc-head":     "Head",
                "lnc-mouth":    "Mouth",
                "lnc-torso":    "Torso",
                "lnc-dom_sense":"'Dominant' sense (i assume)",
        }
        self.DSETS = {
            "MT40k":    {"norms":["conc-m","conc-sd"], 
                         "description":"Pending"},
            "MRC":      {"norms":["conc-m","imag-m","nphon","nsyl","vfreq","kf_freq","fam","mean","pos"],
                         "description": "Verbal frequency are from 'Brown'. Meaningfullness values are the non-zero average of Paivio and Colarado norms"},
            "USF":      {"norms":["assoc","conc-m","str","rstr","oastr","mstr","pos"],
                         "description": "USF association metrics of some kind were provided by SimLex999 dataset, how to properly normalise them is unclear. I have currently decided to normalise them as if the distribution is ranged 0-10. NOTE, There are plenty more norms we have not added so far"},
            "SimLex999":{"norms":["conc-m","simlex999-m","simlex999-sd"],
                         "description": ""},
            "Vinson":   {"norms":["pos","modal"],
                         "description":"Pending"},
            "McRae":    {"norms":["kf_freq","num_func","num_vis_mot","num_vis_fs","num_vis_col","num_sound","num_taste","num_smell","num_tact","num_ency","num_tax"],
                         "description":"Pending"},
            "SimVerb":  {"norms":["sim","sem_rel"],
                         "description":"The similarity and USF strength metrics may be related"},
            "CP":       {"norms":["conc-m","kf_freq","imag-m","mean","nsyl","emo","pleas","num_mean","fam","eod"],
                         "description":"The Clark-Paivio word norms"},
            "TWP":      {"norms":["imag-m","conc-m","kf_freq"],
                         "description":"TWP Word norms"},
            "Battig":   {"norms":["kf_freq","nsyl"],
                         "description":"Battig Word norms"},
            "Cortese":  {"norms":["rt-m","rt-sd","imag-m","imag-sd","toglia"],
                         "description":"Cortese dataset"},
            "Reilly":   {"norms":["conc-m","imag-m","kf_freq","nphon","nsyl","rt-m","fam"],
                         "description":"2 parts of this dataset exist. One from Reilly and another an updated augmentation of norms also provided by Reilly"},
            "mm_imgblty":{"norm":["mm_vis","mm_txt","mm_pho","mm_all"],
                         "description":"A multimodal imagability feature dataset supplied by one kind Marc Kastner"},
            "sianpar_indo":{"norm":["val-m","val-sd","arou-m","arou-sd","conc-m","conc-sd","dom-m","dom-sd","pred-m","pred-sd"],
                         "description":"Sianpar's dataset of norms for indonesian words, (english translations included)"},
            "yee_chinese":{"norm":["val-m", "arou-m", "imag-m", "conc-m"],
                         "description":"Yee's word norm dataset for Chinese-translated words"},
            "megahr":   {"norm":["conc-m", "imag-m"],
                         "description":"MEGAHR Cross Lingual Database word norms"},
            "glasgow":  {"norm":["conc-m", "imag-m", "arou-m", "val-m", "fam-m", "dom-m"],
                         "description":"Glasgow Norms of 5500 words"},
            "GLS-Reilly":  {"norm":["arou-m", "dom-m", "imag-m", "val-m", "conc-m", "fam"],
                         "description":"The GLS dataset split provided by Reilly"},
            "KUP-Reilly":  {"norm":["pos", "nphon", "nsyl"],
                         "description":"The KUP dataset split provided by Reilly"},
            "ELP-Reilly":  {"norm":["rt-nam","rt-lex_dec","sem_dens","sem_neig","sem_div"], # FINISH THIS
                         "description":"The ELP dataset split provided by Reilly"},
            "BRYS-Reilly":  {"norm":["conc-m", "pos"],
                         "description":"The BRYS dataset split provided by Reilly"},
            "LNC-Reilly":  {"norm":["lnc-audi","lnc-gust","lnc-hapt","lnc-interoc","lnc-olfact","lnc-foot_leg","lnc-hand_arm","lnc-head","lnc-mouth","lnc-torso","lnc-dom_sense"], # FINISH THIS
                         "description":"The LNC dataset split provided by Reilly"},
            "WAR-Reilly":  {"norm":["val-m", "arou-m", "dom-m"],
                         "description":"The WAR dataset split provided by Reilly"},
        }
        self.words = {}
        self.word_pairs = {}

    def __len__(self):
        return(len(self.words)+len(self.word_pairs))

    def __str__(self):
        return_str = ""
        for idx, wrd in enumerate(self.words.keys()):
            if idx>3:
                return_str+="..."
                break
            return_str+=f"'{wrd}':\n"
            for nrm, nrm_dict in self.words[wrd].items():
                return_str+=f"    '{nrm}':\n        'avg': {nrm_dict['avg']}\n        'source': {nrm_dict['sources']}\n"
        return f"{return_str}\n\nContained Norms: {self.NORMS}\nContained Datasets: {self.DSETS}"

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, word):
        if type(word) == tuple and len(word) == 2:
            word0, word1 = word
            return self.word_pairs[f"{word0}|{word1}"]
        else:
            return self.words[word]

    def update(self, word, norm, scaled, original, dset):
        assert norm in self.NORMS.keys(), f"{norm}  is not a recognised norm"
        assert dset in self.DSETS.keys(), f"{dset} is not recognised"
        if (scaled != scaled) or (original != original):
            return None # SKIP NaN values
        if type(word) == tuple and len(word) == 2:
            word = f"{word[0]}|{word[1]}"
            if word not in self.word_pairs.keys():
                self.word_pairs[word] = {}
            if norm not in self.word_pairs[word].keys():
                self.word_pairs[word][norm] = {"avg":None, "sources":{}}
            if dset in self.word_pairs[word][norm]["sources"].keys():
                return None
            self.word_pairs[word][norm]["sources"][dset] = {"scaled":scaled, "original":original}
            current_norms = [ self.word_pairs[word][norm]["sources"][dst]["scaled"] for dst in self.word_pairs[word][norm]["sources"].keys() ]

            if type(scaled) in [float, int]: # The avergage of non-numeric norms isn't considered here
                current_norms = [ele for ele in current_norms if ele != 0]
                self.word_pairs[word][norm]["avg"] = list_avg(current_norms)           
        else:
            if word not in self.words.keys():
                self.words[word] = {}
            if norm not in self.words[word].keys():
                self.words[word][norm] = {"avg":None, "sources":{}}
            if dset in self.words[word][norm]["sources"].keys():
                return None
            self.words[word][norm]["sources"][dset] = {"scaled":scaled, "original":original}
            current_norms = [ self.words[word][norm]["sources"][dst]["scaled"] for dst in self.words[word][norm]["sources"].keys() ]
            
            if type(scaled) in [float, int]: # The avergage of non-numeric norms isn't considered here
                current_norms = [ele for ele in current_norms if ele != 0]
                self.words[word][norm]["avg"] = list_avg(current_norms)