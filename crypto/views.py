from django.shortcuts import render, redirect
from .models import BitcoinPrice 
import requests

def home(request):
    # 1. Get all history from the database (ORM Magic!)
    # Equivalent to: SELECT * FROM BitcoinPrice ORDER BY timestamp DESC
    history = BitcoinPrice.objects.all().order_by('-timestamp')[:10]
    
    return render(request, 'home.html', {'history': history})

def fetch_price(request):
    # 1. Get price from API
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    current_price = data['bitcoin']['usd']
    
    # 2. Save to Database (The Django Way - No SQL!)
    BitcoinPrice.objects.create(price=current_price)
    
    # 3. Go back home
    return redirect('home')