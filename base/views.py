from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
import stripe
stripe.api_key = "sk_test_51MIV7TSAgy4lpJXcQ1m6TDw78apz028GZMB2CjQDg7eJficTXmkXOs1AkbHiOOJM0JWwRUrFEui6aAF6K9kxs3dF00qzFzXo0I"
# Create your views here.

def index(request):
	return render(request, 'base/index.html')


def charge(request):
	amount = 5
	if request.method == 'POST':
		print('Data:', request.POST)

	return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'base/success.html', {'amount':amount})