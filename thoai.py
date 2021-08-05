import re
import nltk
nltk.download('punkt')
import urllib.request
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import random


url = 'https://raw.githubusercontent.com/hoangks5/AI-lam-tho-luc-bat/main/data/tho.txt'
with urllib.request.urlopen('https://raw.githubusercontent.com/hoangks5/AI-lam-tho-luc-bat/main/data/tho6chu.txt') as url:
    s = url.read()
    tho6chu = s.decode("utf-8")
    tho6chu = tho6chu.splitlines()
with urllib.request.urlopen('https://raw.githubusercontent.com/hoangks5/AI-lam-tho-luc-bat/main/data/tho8chu.txt') as url:
    s = url.read()
    tho8chu = s.decode("utf-8")
    tho8chu = tho8chu.splitlines()

def xoadau(tu):
  tu = re.sub('[ếềệễể]','ê',tu)
  tu = re.sub('[éèẹẽẻ]','e',tu)
  tu = re.sub('[áàạãả]','a',tu)
  tu = re.sub('[ắằẳẵặ]','ă',tu)
  tu = re.sub('[ấầậẫẩ]','â',tu)
  tu = re.sub('[íìịĩỉ]','i',tu)
  tu = re.sub('[óòỏọõ]','o',tu)
  tu = re.sub('[ớờợỡở]','ơ',tu)
  tu = re.sub('[ốồộổỗ]','ô',tu)
  tu = re.sub('[úùụủũ]','u',tu)
  tu = re.sub('[ứừựữử]','ư',tu)
  tu = re.sub('[ýỳỷỹỵ]','y',tu)
  tu = re.sub(r'[.,~`!@#$%\^&*\(\)\[\]\\|:;\'"?]+', ' ', tu)
  tu = re.sub(r'\s+', ' ', tu).strip()
  return tu

def xoa_phu_am_dau(tu):
  if tu[0] in ['b','c','d','đ','g','h','k','l','m','n','p','q','r','s','t','v','x']:
    tu = tu[1:]
    return xoa_phu_am_dau(tu)
  else:
    return tu



def inracautho(inp):
    random1 = []
    if len(word_tokenize(inp)) == 6:
        van = xoadau(word_tokenize(inp)[5])
        van = xoa_phu_am_dau(van)
        for line in tho8chu:
            goc = xoadau(word_tokenize(line)[7])
            goc = xoa_phu_am_dau(goc)
            if goc == van:
                random1.append(line)
        return random.choice(random1)
    if len(word_tokenize(inp)) == 8:
        van = xoadau(word_tokenize(inp)[5])
        van = xoa_phu_am_dau(van)
        for line in tho6chu:
            goc = xoadau(word_tokenize(line)[5])
            goc = xoa_phu_am_dau(goc)
            if van == goc:
                random1.append(line)
        return random.choice(random1)
    else:
        inp = "Thơ lục bát mà sao có " + str(len(word_tokenize(inp))) + " từ ?????????"
        return inp