from sklearn.feature_extraction.txt import TfidfVectirizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import wordnet
import bs4as as bs
import warnings
import nltk
import random
import string
import re
warnings.filterwarnings(&#39;ignore&#39;)
synonyms = []
for syn in wordnet.synsets(&#39;Hey!!&#39;):
    for lem in syn.lemmas():
        lem_name = re.sub(r&#39;\[[0-9]*\]&#39;,&#39;&#39;,lem.name())
        greeting_inputs = [&#39;hey&#39;,&#39;hello&#39;]
        greeting_inputs = greeting_inputs+synonyms
        covo_inputs =[&#39;how are you&#39;,&#39;how are you doing?&#39;]