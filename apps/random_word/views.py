from django.shortcuts import render, redirect, HttpResponse
import string
import random


def index(request):
	return render(request, 'random_word/index.html')
	

def get_num(request):
	
	if request.method == "POST":

		random_word = ''
		for a in range(1,15):
			if a == 1:
				random_word += random.choice(string.letters).upper()
			else:
				random_word += random.choice(string.letters).lower()

		try:
			request.session['times'] += 1
		except:
			request.session['times'] = 0

		request.session['word'] = random_word
		return redirect('/')
		
	else:
		return redirect('/')

