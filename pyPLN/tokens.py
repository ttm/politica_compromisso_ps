#-*- coding: utf8 -*-
import operator

f=open("../compromisso_nacional_participacao_social.md")
l=f.readlines()
d={}
ntokens=0
for ll in l: # para cada linha de texto
    t=ll.split()
    for tt in t:
        ntokens+=1
        tt=tt.replace(".","") # limpe
        tt=tt.replace(",","")
        tt=tt.replace(";","")
        tt=tt.replace("-","")
        tt=tt.replace('\xe2\x80\x93',"")
        tt=tt.replace("#","")
        tt=tt.lower()
        if tt and "*" not in tt: # se for palavra
            if tt in d.keys(): # registra incidência
                d[tt]+=1
            else:
                d[tt]=1 # ou nova palavra

# palavras em sequência
sorted_x = sorted(d.iteritems(), key=operator.itemgetter(1))
print sorted_x[::-1][:30]
# 30 palavras mais frequentes:
# 
#        [('de', 77),
#        ('e', 65),
#        ('da', 44),
#        ('participa\xc3\xa7\xc3\xa3o', 29),
#        ('a', 29),
#        ('social', 28),
#        ('do', 20),
#        ('o', 19),
#        ('como', 16),
#        ('dos', 13),
#        ('as', 13),
#        ('sociedade', 13),
#        ('mecanismos', 12),
#        ('para', 12),
#        ('compromisso', 12),
#        ('os', 11),
#        ('civil', 10),
#        ('por', 10),
#        ('meio', 10),
#        ('p\xc3\xbablicas', 9),
#        ('das', 9),
#        ('que', 9),
#        ('cl\xc3\x81usula', 9),
#        ('entre', 8),
#        ('nacional', 7),
#        ('articula\xc3\xa7\xc3\xa3o', 7),
#        ('presente', 7),
#        ('sociais', 6),
#        ('pol\xc3\xadticas', 6),
#        ('pela', 6)]
#

