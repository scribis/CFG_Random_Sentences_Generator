#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# GENERATE RANDOM SENTENCES WITH CFG (Context-free grammar)
# 1. INSTALL AND IMPORT LIBRARIES
# 2. DEFINE FUNCTION TO GENERATE RANDOM SENTENCES FROM A GRAMMAR
# 3. BUILD YOUR GRAMMAR
# 4. GENERATE SENTENCES


# In[ ]:


# INSTALL NLTK library (take few seconds)
get_ipython().system('pip install nltk')


# In[ ]:


# IMPORT NECESSARY MODULES
import nltk
import random


# In[ ]:


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


# BUILD YOUR GRAMMAR

grammar = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V OP
  V -> "afferrò" | "prese" | "preparò"
  NP -> Det N | Det AggP N | Det N AggP
  OP -> Det O | Det AggO O | Det O AggO
  AggO -> "magica" | "speciale" | "portentosa" | "segreta"
  AggP -> "vecchia" | "piccola" | "malvagia"
  Det -> "la" | "quella" | "una"
  N -> "strega" | "megera" | "stregaccia" | "maghetta" | "maga"
  O -> "pozione" | "bevanda"
  """)


# In[23]:


# GENERATE SENTENCES

for i in range(10):
    frags = []  
    generate_sample(grammar, grammar.start(), frags)
    print(' '.join(frags))
    #print("\n")


# In[ ]:




