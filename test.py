Sent from Mail for Windows

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

from nltk.corpus import wordnet

from bs4  import BeautifulSoup as bs

import warnings

import nltk

import random

import string

import re

warnings.filterwarnings('ignore')

synonyms = []

for syn in wordnet.synsets('Hey!!'):

    for lem in syn.lemmas():

        lem_name = re.sub(r'\[[0-9]*\]','',lem.name())

        greeting_inputs = ['hey','hello']

        greeting_inputs = greeting_inputs+synonyms

        covo_inputs =['how are you','how are you doing?']