from django.http import  HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def count(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.split()
    word_dictionary = {}

    for word in wordlist:
        if word.lower() in word_dictionary:
            word_dictionary[word.lower()] += 1
        else:
            word_dictionary[word.lower()] = 1
    sorted_words = sorted(word_dictionary.items(), key = lambda word: word[1], reverse = True)
    return render(request, "count.html", {"fulltext": fulltext, "count":len(wordlist), "word_dictionary":sorted_words})