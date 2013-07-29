#-*- coding: utf8 -*-
import nltk as k, pylab as p, numpy as n


f=open("../compromisso_nacional_participacao_social.md")
raw=f.read().decode("utf-8")
print("%i caracteres" % (len(raw),))
nletras=len([r for r in raw if r.isalpha()]) # jah inclui acentuacoes e cedilhas
print("%i letras" % (len([r for r in raw if r.isalpha()]),))
nespacos=len([r for r in raw if r.isspace()]) # jah inclui \n e \t
print("%i espacos" % (len([r for r in raw if r.isspace()]),))
nnumeros=len([r for r in raw if r.isdigit()])
print("%i numeros" % (len([r for r in raw if r.isdigit()]),))
nponts=len([r for r in raw if r in u";:'\"*#.,?!%@-\x80\x93"+u'\u2013'])
print("%i pontuacoes e caracteres especiais" % (len([r for r in raw if r in u";:'\"*#.,?!%@-\xe2\x80\x93"+u'\u2013']),))
#nacents=len([r for r in raw if r in u"çÇáãâÂÁÃéêÊÉíÍóôõÕÓÔúûÚÛ"])
#print("%i acentuacoes e cedilhas" % (len([r for r in raw if r in u"çÇáãâÂÁÃéêÊÉíÍóôõÕÓÔúûÚÛ"]),))
nsent=k.tokenize.sent_tokenize(raw)
print(u"%i sentenças"%(len(nsent),))
aa=k.tokenize.sent_tokenize(raw)
bb=[len(k.word_tokenize(a)) for a in aa]
print(u"media: %f, desvio padrão: %f de palavras por sentença" % (n.mean(bb),n.std(bb)))


f=open("../compromisso_nacional_participacao_social.md")
raw=f.read()

tokens = k.word_tokenize(raw)
#raw=raw.decode("utf-8")

print("%i tokens" % (len(tokens),))
print("%i tokens diferentes" % (len(set(tokens),)))


text = k.Text(tokens)

collocations=text.collocations()
#participação social; por meio; Sociedade Civil; sociedade civil;
#entes signatários; CONSIDERANDO que; Articulação Social;
#Participação Social; Secretaria Nacional; movimentos sociais;
#presente Compromisso; cidadania ativa; sociedade civil.; Conferências
#Nacionais; dias após; sobre temas; social como; educação para;
#políticas públicas; bem como

p.subplot(211)
p.title(u"Incidência das letras no Compromisso Nacional de Participação Social")
ff=k.FreqDist([c for c in raw if c.isalpha()])
yy=ff.values()
xx=ff.keys()

p.plot(n.arange(len(yy)),yy,"ro")
p.ylabel(u"incidência")
p.xlabel(u"letra")
p.xticks(n.arange(len(yy)),xx)
p.xlim(-1,len(yy)+1)
p.subplot(212)
p.plot(n.arange(len(yy)),n.log10(yy),"ro")
p.ylabel(r"$\log_{10}{"+u"incidência"+r"}$")
p.xlabel(u"letra")
p.xticks(n.arange(len(yy)),xx)
p.xlim(-1,len(yy)+1)
p.show()


st=k.corpus.stopwords.words("portuguese")
tokens2 = k.word_tokenize(raw)
for t in st:
    while t in tokens2:
        print t
        tokens2.remove(t)

text2 = k.Text(tokens2)
collocations2=text2.collocations()
print "**********"

tokens3 = [tt.lower() for tt in tokens2 if tt not in (".",",",";","-","#",":",'\xe2\x80\x93')]
tokens3 = [tt for tt in tokens3 if "*" not in tt]
for t in st:
    while t in tokens3:
        print t
        tokens3.remove(t)

for i in xrange(len(tokens3)):
    tokens3[i]=tokens3[i].replace(".","").replace(",","")


text3 = k.Text(tokens3)
#participação social; sociedade civil; presidência república;
#secretaria-geral presidência; planejamento orçamento; mecanismos
#participação; educação cidadania; movimentos sociais; deste
#compromisso; cidadania ativa; entes signatários; secretaria nacional;
#conferências nacionais; dias após; nacionais ouvidorias; sobre
#temas; consultas públicas; meio secretaria; presente compromisso;
#organizações sociedade

ff=text3.vocab()
N=80
yy=ff.values()[:N]
xx=ff.keys()[:N]
p.title(u"Ocorrências de palavras")
p.plot(n.arange(len(yy)),yy,"ro")
p.ylabel(u"ocorrências")
p.xlabel(u"palavras")
p.xticks(n.arange(len(yy)),[x.decode("utf-8") for x in xx],rotation=80)
p.xlim(-1,len(yy)+1)
p.show()

import networkx as x
G=x.Graph()

for i in xrange(len(tokens3)-1):
    G.add_edge(tokens3[i].decode("utf-8"),tokens3[i+1].decode("utf-8"))
x.view_pygraphviz(G)
