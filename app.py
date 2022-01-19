from cgitb import text
from operator import truediv
from pickle import TRUE
from sqlite3.dbapi2 import connect
from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)

#FUNZIONE PER CONNESSIONE A DB SQLITE
def dbconnection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection

#FUNZIONE PER ASSEGNAMENTO VARIABILI DA PAGINA HTML
def inizializza(sede, item):
    operatore = request.form['operatore']
    piastreAdulto = request.form.get('piastreAdulto', 'Non OK')
    piastrePediatriche = request.form.get('piastrePediatriche', 'Non OK')
    batteria = request.form.get('batteria', 'Non OK')
    note = request.form['note']
    return sede, item, operatore, piastreAdulto, piastrePediatriche, batteria, note

#FUNZIONE PER CONTROLLO ESISTENZA SEDE
def controllo_sede(sede):
    connection = dbconnection()
    cs1 = connection.cursor()
    cs1.execute(
        'SELECT sede FROM sedi WHERE sede = ?',
        (sede,)
    )
    sedi = cs1.fetchone()
    if sedi == None:
        connection.close()
        return False
    else:
        connection.close()
        return True

#FUNZIONE PER CONTROLLO ESISTENZA DISPOSITIVO
def controllo_dispositivo(dispositivo):
    connection = dbconnection()
    cs1 = connection.cursor()
    cs1.execute(
        'SELECT dispositivo FROM dispositivi WHERE dispositivo = ?',
        (dispositivo,)
    )
    dispositivi = cs1.fetchone()
    if dispositivi == None:
        connection.close()
        return False
    else:
        connection.close()
        return True

#CODICE PAGINE INDEX
@app.route('/pisa.html')
def pisa():
    connection = dbconnection()
    controlli = connection.execute('SELECT STRFTIME("%d/%m/%Y", dataControllo) AS dataControllo, sede, dispositivo, operatore, piastreAdulto, piastrePediatriche, batteria, note FROM controlli WHERE sede = "Pisa"').fetchall()
    connection.close()
    return render_template('/pisa.html', controlli=controlli)

@app.route('/riglione.html')
def riglione():
    connection = dbconnection()
    controlli = connection.execute('SELECT STRFTIME("%d/%m/%Y", dataControllo) AS dataControllo, sede, dispositivo, operatore, piastreAdulto, piastrePediatriche, batteria, note FROM controlli WHERE sede = "Riglione"').fetchall()
    connection.close()
    return render_template('/riglione.html', controlli=controlli)

#CODICE PAGINA SUCCESS
@app.route('/success.html')
def success():
    return render_template('/success.html')

#CODICE PAGINA ERROR
@app.route('/error.html')
def error():
        return render_template('/error.html')

#CODICE PAGINA CREATE
@app.route('/create/sede=<sede>&dispositivo=<dispositivo>', methods=('GET','POST'))
def create_pisa(sede, dispositivo):
    if controllo_sede(sede) == True and controllo_dispositivo(dispositivo) == True:
        if request.method == 'POST':
            variabili = inizializza(sede, dispositivo)
            connection = dbconnection()
            connection.execute(
                'INSERT INTO controlli (dataControllo, sede, dispositivo, operatore, piastreAdulto, piastrePediatriche, batteria, note) VALUES (CURRENT_DATE, ?, ?, ?, ?, ?, ?, ?)',
                (variabili)
            )
            connection.commit()
            connection.close()
            return redirect('/success.html')
        return render_template('create.html')
    else:
        return redirect('/error.html')

if __name__ == "__main__":
   app.run(host='3.123.164.183', port=5000)