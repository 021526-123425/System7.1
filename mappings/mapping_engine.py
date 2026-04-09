import json

class MappingEngine: 
    def __init__(self, mapping_file):
        with open(mapping_file) as f:
            self.mapping = json.load(f)

    def get_button_for_key(self, key):
        for button, mapped_key in self.mapping["buttons"].items():
            if key == mapped_key:
                return button
        return None

    def get_axis_for_key(self, key):
        for axis, pair in self.mapping["axes"].items():
            if key in pair:
                direction = -1 if key == pair[0] else 1
                return axis, direction
        return None, None


import json

class MappingEngine:
    def __init__(self, mapping_file):
        self.load(mapping_file)

    def load(self, mapping_file):
        with open(mapping_file) as f:
            self.mapping = json.load(f)

    def get_button_for_key(self, key):
        for button, mapped_key in self.mapping["buttons"].items():
            if key == mapped_key:
                return button
        return None

    def get_axis_for_key(self, key):
        for axis, pair in self.mapping["axes"].items():
            if key in pair:
                direction = -1 if key == pair[0] else 1
                return axis, direction
        return None, None

import json

class MappingEngine:
    def __init__(self, mapping_file):
        self.load(mapping_file)

    def load(self, mapping_file):
        with open(mapping_file) as f:
            self.mapping = json.load(f)

    def get_button_for_key(self, key):
        for button, mapped_key in self.mapping["buttons"].items():
            if key == mapped_key:
                return button
        return None

