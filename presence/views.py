from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone
import django.utils
import sqlite3
from presence.models import Presence
#import dbhandler
def db(query):
    conn = sqlite3.connect("C:/Users/Éloi/Desktop/projet python/projet site/CADL2 - Copie/db.sqlite3")
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.close()
    conn.commit()
def presence_quit(user):
    conn = sqlite3.connect("C:/Users/Éloi/Desktop/projet python/projet site/CADL2 - Copie/db.sqlite3")
    cursor = conn.cursor()
    is_present = False
    cursor.execute(f"UPDATE presence_presence SET is_present = {is_present}")
    cursor.close()
    conn.commit()
def index(request):
    eloi = "9338674"
    if request.method == "POST":
        card_number = request.POST.get("cardnumber")
        if str(card_number) == eloi:
            is_present = True
            user = f"Éloi Léger"
            user_id = f"{eloi}"
            time = str(django.utils.timezone.now())
            tim = time.split(".")
            t = tim[0]
            query = f"INSERT INTO presence_presence (user, user_id, is_present, hour_of_presence) VALUES ('{user}', '{user_id}', {is_present}, '{t}');"
            db(query)



    return render(request, 'presence/index.html')
    #return HttpResponse("Salut! C'eat la page index, elle est en construction...")
def accueil(request):
    times = timezone.localtime()
    date = str(times).split(" ")
    dat = date[0]
    heure = str(date[1]).split(".")
    heur = heure[0]
    html = f"Salut! La page est en construction. Aujourd'hui, on est le {dat} . Il est présentement {heur} ."
    return HttpResponse(html)

