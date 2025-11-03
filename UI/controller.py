import flet as ft
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO

    def handle_mostra_automobili(self, e):
        lista_auto_oggetti = self._model.get_automobili()

        # Controllo errori
        if lista_auto_oggetti is None:
            self._view.show_alert("Errore nel recupero dei dati dal database.")
            return

        self._view.lista_auto.controls.clear()

        # Controllo se la lista è vuota
        if not lista_auto_oggetti:
            self._view.lista_auto.controls.append(
                ft.Text("Nessuna automobile trovata nel database.")
            )
        else:
            for auto in lista_auto_oggetti:
                # Uso il metodo __str__
                self._view.lista_auto.controls.append(
                    ft.Text(str(auto))
                )

        self._view.update()

    def handle_cerca_automobili(self, e):
        modello_da_cercare = self._view.input_modello_auto.value
        # Controllo errori
        if not modello_da_cercare:
            self._view.show_alert("Per favore, inserisci un modello prima di cercare.")
            return
        lista_auto_oggetti = self._model.cerca_automobili_per_modello(modello_da_cercare)
        if lista_auto_oggetti is None:
            self._view.show_alert("Errore nel recupero dei dati dal database.")
            return

        self._view.lista_auto_ricerca.controls.clear()

        # Controllo se la lista è vuota
        if not lista_auto_oggetti:
            self._view.lista_auto_ricerca.append(
                ft.Text(f"Nessuna automobile trovata con il modello: {modello_da_cercare}")
            )
        else:
            # Uso il metodo __str__
            self._view.lista_auto_ricerca.controls.append(
                ft.Text(f"Risultati per {modello_da_cercare}: ", weight=ft.FontWeight.BOLD)
            )
            for auto in lista_auto_oggetti:
                self._view.lista_auto_ricerca.controls.append(ft.Text(str(auto)))

        self._view.update()
