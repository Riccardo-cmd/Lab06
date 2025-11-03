from database.DB_connect import get_connection
from model import automobile
from model.automobile import Automobile
from model.noleggio import Noleggio
import mysql.connector

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """

        # TODO
        try:
            cnx = get_connection()
            if cnx is None:
                print('Errore nella connessione al Database')
                return None

            cursor = cnx.cursor(dictionary=True)

            cursor.execute("SELECT * FROM automobile")

            result_list = cursor.fetchall()

            automobili  =[]
            for row in result_list:
                auto = Automobile(
                    codice=row['codice'],
                    marca=row['marca'],
                    modello=row['modello'],
                    anno=row['anno'],
                    posti=row['posti'],
                    disponibile=row['disponibile']
                )
                automobili.append(auto)

            # chiudo cursor e connessione
            cursor.close()
            cnx.close()
            return automobili
        except mysql.connector.Error as err:
            print(f"Errore: {err}")
            # Mi assicuro che le risorse vengano chiuse anche in caso di errore
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'cnx' in locals() and cnx:
                cnx.close()
            return None

        # In model/model.py, dentro la classe Autonoleggio

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # TODO
        try:
            cnx = get_connection()
            if cnx is None:
                print("Errore nella connessione al database")
                return None

            cursor = cnx.cursor(dictionary=True)

            # Nuova Query Parametrica
            query = "SELECT * FROM automobile WHERE modello = %s"

            cursor.execute(query, (modello,))

            result_list = cursor.fetchall()
            automobili = []
            for row in result_list:
                auto = Automobile(
                    codice=row['codice'],
                    marca=row['marca'],
                    modello=row['modello'],
                    anno=row['anno'],
                    posti=row['posti'],
                    disponibile=row['disponibile']
                )
                automobili.append(auto)

            cursor.close()
            cnx.close()
            return automobili

        except mysql.connector.Error as err:
            print(f"Errore: {err}")
            if 'cursor' in locals() and cursor:
                cursor.close()
            if 'cnx' in locals() and cnx:
                cnx.close()
            return None