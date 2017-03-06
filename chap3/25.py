# -*- coding: utf-8 -*-

"""
Pig Latin is a simple transformation of English text. Each word of the text is converted as follows: move any consonant (or consonant cluster) that appears at the start of the word to the end, then append ay, e.g. string → ingstray, idle → idleay.  http://en.wikipedia.org/wiki/Pig_Latin

a. Write a function to convert a word to Pig Latin.
b. Write code that converts text, instead of individual words.
c. Extend it further to preserve capitalization, to keep qu together (i.e. so that quiet becomes ietquay), and to detect when y is used as a consonant (e.g. yellow) vs a vowel (e.g. style).
"""

from __future__ import absolute_import
import re, unittest, nltk


def pig_latin_a(s):
    finds = re.findall(r"(^[^aieuoAIEOU]*)(.*$)", s)[0]
    new_s = finds[1] + finds[0] + "ay"
    return new_s


def pig_latin_b(text):
    words = nltk.word_tokenize(text)
    new_words = []
    for word in words:
        if word.isalpha():
            new_words.append(pig_latin_a(word))
    return " ".join(new_words)


def pig_latin_c(text):
    words = nltk.word_tokenize(text)
    new_words = []
    for word in words:
        if word.isalpha():
            finds = re.findall(r"(^(?:qu|[^aieuo])*)(.*$)", word.lower())[0]
            finds2 = re.findall(r"(^.*?)(y.+$)", finds[0])
            if finds2:
                new_word = finds2[0][1] + finds[1] + finds2[0][0] + "ay"
            else:
                new_word = finds[1] + finds[0] + "ay"

            if word[0].isupper():
                new_word = new_word[0].upper()+new_word[1:]

            new_words.append(new_word)

    return " ".join(new_words)


class Test(unittest.TestCase):

    def test_a(self):
        self.assertEqual(pig_latin_a("string"), "ingstray")
        self.assertEqual(pig_latin_a("idle"), "idleay")

    def test_b(self):
        text = "This is an example of Pig Latin"
        result = 'isThay isay anay exampleay ofay igPay atinLay'
        self.assertEqual(pig_latin_b(text), result)

    def test_c(self):
        self.assertEqual(pig_latin_c("quiet"), "ietquay")
        self.assertEqual(pig_latin_c("style"), "ylestay")
        text = "This is an example of Pig Latin"
        result = 'Isthay isay anay exampleay ofay Igpay Atinlay'
        self.assertEqual(pig_latin_c(text), result)

if __name__ == "__main__":
    unittest.main()
