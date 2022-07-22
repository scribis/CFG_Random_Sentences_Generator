#!/usr/bin/env python
# coding: utf-8

# # My Jupyter Notebook on IBM Watson Studio
# 
#  **Fabio Martines - Web Designer**
# 
#  *I am interested in data science because I want to develop writing games through NLP tools*
# 
# ### PROGRAM: GENERATE RANDOM SENTENCES WITH CFG (Context-free grammar)
# 
# ##### - CELL N.1: INSTALL LIBRARIES
# ##### - CELL N.2: IMPORT LIBRARIES 
# ##### - CELL N.3: DEFINE FUNCTION TO GENERATE RANDOM SENTENCES FROM A CFG GRAMMAR
# ##### - CELL N.4: RUN THE GRAMMAR
# ##### - CELL N.5: GENERATE SENTENCES

# In[ ]:


# CELL N.1
# INSTALL NLTK & scikit libraries (take few seconds)

get_ipython().system('pip install nltk')
get_ipython().system('pip install -U scikit-learn')
 


# In[1]:


# CELL N.2
# IMPORT NECESSARY LIBRARIES
import nltk
import random


# In[2]:


# CELL N.3
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


# In[5]:


# CELL N.4
# RUN THE GRAMMAR

grammar = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V OP
  V -> "afferrò" | "prese" | "preparò" | "bevve" | "trangugiò" | "gli diede" | "gli donò" | "le diede" | "le donò"
  NP -> Det N | Det AggP N | Det N AggP
  OP -> Det O | Det AggO O | Det O AggO
  AggO -> "magica" | "micidiale" | "portentosa" | "segreta"
  AggP -> "orrenda" | "malefica" | "malvagia" | "terribile" | "raccapricciante"
  Det -> "la" | "quella" | "una"
  N -> "strega" | "megera" | "stregaccia" | "maghetta" | "maga"
  O -> "pozione" | "bevanda"
  """)


# In[6]:


# CELL N.5
# GENERATE SENTENCES

for i in range(20):
    frags = []  
    generate_sample(grammar, grammar.start(), frags)
    print(' '.join(frags))



# ## REFERENCES
# #### 1. https://en.wikipedia.org/wiki/Context-free_grammar
# #### 2. https://stackoverflow.com/questions/15009656/how-to-use-nltk-to-generate-sentences-from-an-induced-grammar
# 
# 
# 
# ## VISUAL EXAMPLE OF A CONTEXT FREE GRAMMAR
# ![cfg.png](attachment:cfg.png "CFG example")

# In[ ]:




