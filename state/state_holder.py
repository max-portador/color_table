# coding: utf-8
import json
from logic.utils import load_data
from logic.constants import ROOT_DIR


class State_Holder():
    filename = f'{ROOT_DIR}/state/app_state.json'

    def __init__(self):
        self.appState = load_data(self.filename)

    def get_state(self):
        return self.appState

    def update_state(self, data):
        self.appState = {**self.appState, **data}

    def save_state(self):
        with open(self.filename, 'w') as f:
            json.dump(self.appState, f,  ensure_ascii=False)

    def chosen_ids_RU(self):
        result = []
        if 'РФ' in self.appState:
            regions = self.appState['РФ']
            for region, vals in regions.items():
                stations = vals['stations']
                for name, st_id in stations.items():
                    result.append((f'{region}-{name}', st_id))
        return result
