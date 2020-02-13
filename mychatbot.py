#!/usr/bin/env python3
from nltk.chat.util import Chat
repondeur = {"je suis": "tu es", "moi" : "toi", "il":"elle", "nek":"kecc"}
pairs = [
    [
        r"ismiw (.*)",
        ["Azul %1, Amek i thetilidh assaki ?",]
    ],
     [
        r"amek ikessawalen ?",
        ["ismiw chatty sawalen iyi chatbot ?",]
    ],
    [
        r"amek i thetilidh ?",
        ["aqlih bien\n et kecc amek ?",]
    ],
    [
        r"semhiyi (.*)",
        ["maalich","normal, t'inquiete pas",]
    ],
    [
        r"aqlih (.*) bien  ",
        ["farhagh mikhessligh","Alright :)",]
    ],
    [
        r"saha|aslama|azul",
        ["azul", "alkhir felawen", "amek !"]
    ],
    [
        r"(.*) achehal dh laamrik?",
        ["nekini dh l'ordinateur\nSerieux !",]
        
    ],
    [
        r"amek (.*) achu ithevghidh ?",
        ["fkiyi akhedim oudeqaragh ara ala",]
        
    ],
    [
        r"(.*) ifghed (.*)",
        ["inelmadhen n insim iydikhemen s Python's NLTK library ","secret achkoukou ;)",]
    ],
    [
        r"(.*) (anda izedhghedh|wilaya) ?",
        ['Tizi ouzou, Algeria',]
    ],
    [
        r"amek thella lhala dhina (.*)?",
        ["lhala attah dhaki %1 bien","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"anda ith khedmedh (.*)?",
        ["%1 achkit la company aki, sligh iyess. oumana s3an les problemes lyamath aki.",]
    ],
[
        r"(.*)daggefour dhina (.*)",
        ["deux mois ayaki oudiwith ara %2","dhina houq dayem dagefour %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["hemlagh atas le ballon",]
    ],
    [
        r"anwa (.*) sportsperson ?",
        ["Messy","Ronaldo","Mehrez"]
],
    [
        r"anwa (.*) (moviestar|actor)?",
        ["Leonardo Dicaprio"]
],
    [
        r"ad rouhagh",
        ["BBye ttehela gimanik. See you soon :) ","Farhagh imi hedragh yidek. See you soon :)"]
],
]
def chatty():
    print("Hi, I'm Chatty and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start
    chat = Chat(pairs, repondeur)
    chat.converse()
if __name__ == "__main__":
    chatty()
