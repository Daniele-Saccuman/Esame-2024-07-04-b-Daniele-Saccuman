import flet as ft
from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = None
        self._listStates = None
        self._anno = None
        self._state = None

    def fillDD(self):
        self._listYear = self._model.getYears()
        for anno in self._listYear:
            self._view.ddyear.options.append(ft.dropdown.Option(anno))
        self._view.update_page()

    def fillDDShape(self, anno):
        # anno = self._view.ddyear.value
        self._listStates = self._model.getState(anno)
        for shape in self._listStates:
            self._view.ddstate.options.append(ft.dropdown.Option(shape))
        self._view.update_page()

    def read_anno(self, e):
        if e.control.value is None:
            self._anno = None
        else:
            self._anno = e.control.value
            self._view.ddstate.options.clear()
            self.fillDDShape(self._anno)

    def read_state(self, e):
        if e.control.value is None:
            self._state = None
        else:
            self._state = e.control.value

    def handle_graph(self, e):
        anno = self._view.ddyear.value
        state = self._view.ddstate.value
        if anno is None:
            self._view.create_alert("Anno non inserito")
            return
        if state is None:
            self._view.create_alert("State non inserito")
            return

        self._model.buildGraph(anno, state)
        self._view.txt_result1.controls.append(ft.Text(f"Numero di vertici: {self._model.getNumNodi()}"))
        self._view.txt_result1.controls.append(ft.Text(f"Numero di archi: {self._model.getNumArchi()}"))

        components = self._model.get_connected_components()
        num_components = len(components)
        self._view.txt_result1.controls.append(
            ft.Text(f"Numero totale di componenti connesse: {num_components}"))

        # 2. Identificare la componente di dimensione maggiore
        largest_component = max(components, key=len)
        largest_size = len(largest_component)

        self._view.txt_result1.controls.append(
            ft.Text(f"La componente più grande contiene {largest_size} nodi."))
        self._view.txt_result1.controls.append(
            ft.Text(f"Nodi della componente più grande: "))
        for component in largest_component:
            self._view.txt_result1.controls.append(ft.Text(component))
        self._view.update_page()


    def handle_path(self, e):
        pass

