#!/usr/bin/env python
# coding: utf-8

# # My Jupyter Notebook on IBM Watson Studio

# **Fabio Martines - Web Designer**

# *I am interested in data science because I want to develop writing games through NLP tools*

# ### PROGRAM: GENERATE RANDOM SENTENCES WITH CFG (Context-free grammar)
# 
# ##### 1. INSTALL AND IMPORT NECESSARY LIBRARIES & DEFINE FUNCTION TO GENERATE RANDOM SENTENCES FROM A CFG GRAMMAR
# ##### 2. LOAD (OR EDIT) THE GRAMMAR
# ##### 3. GENERATE SENTENCES

# In[3]:


# INSTALL NLTK & scikit libraries (take few seconds)
get_ipython().system('pip install nltk')
get_ipython().system('pip install -U scikit-learn')

# IMPORT NECESSARY MODULES
import nltk
import random

# FUNCTION TO GENERATE RANDOM SENTENCES
# CREDITS: https://stackoverflow.com/questions/15009656/how-to-use-nltk-to-generate-sentences-from-an-induced-grammar
def generate_sample(grammar, prod, frags):
    if prod in grammar._lhs_index:
        derivations = grammar._lhs_index[prod]
        derivation = random.choice(derivations)
        for d in derivation._rhs:
            generate_sample(grammar, d, frags)
    elif prod in grammar._rhs_index:
        # terminal
        frags.append(str(prod))


# In[ ]:


# LOAD THE GRAMMAR (YOU CAN EDIT YOURS)

grammar = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V OP
  V -> "afferrò" | "prese" | "preparò" | "bevve" | "trangugiò" | "gli diede" | "gli donò" | "le diede" | "le donò"
  NP -> Det N | Det AggP N | Det N AggP
  OP -> Det O | Det AggO O | Det O AggO
  AggO -> "magica" | "speciale" | "portentosa" | "segreta"
  AggP -> "vecchia" | "piccola" | "malvagia"
  Det -> "la" | "quella" | "una"
  N -> "strega" | "megera" | "stregaccia" | "maghetta" | "maga"
  O -> "pozione" | "bevanda"
  """)


# In[6]:


# GENERATE SENTENCES

for i in range(20):
    frags = []  
    generate_sample(grammar, grammar.start(), frags)
    print(' '.join(frags))
    #print("\n")


# ### REFERENCES
# - [WHAT IS A CFG]("https://en.wikipedia.org/wiki/Context-free_grammar")
# - [CREDITS]("https://stackoverflow.com/questions/15009656/how-to-use-nltk-to-generate-sentences-from-an-induced-grammar")
# 

# In[ ]:




