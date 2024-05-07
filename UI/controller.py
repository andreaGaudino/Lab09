import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizza(self,e):
        distanza = int(self._view._txtIn.value)
        self._model.loadVoli(distanza)
        self._view._txt_result.clean()
        self._view.update_page()
        self._view._txt_result.controls.append(ft.Text(f"Il grafico ha {len(self._model.grafo.nodes)} vertici"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafico ha {len(self._model.grafo.edges)} archi"))
        for i in self._model.grafo.edges:
            self._view._txt_result.controls.append(ft.Text(f"{i[0]}-{i[1]} distanza media: {self._model.grafo.edges[i[0], i[1]]["media"]}"))
        self._view.update_page()