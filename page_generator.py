import json
import model
import types

class PageGenerator():
    def generate_from_jsonfile(self, filename):
        dictionary = self.json_to_dict(filename)
        return self.dict_to_page(dictionary)

    def dict_to_page(self, dictionary):
        if dictionary.get('size'):
            return model.Page(dictionary.get('size'), dictionary.get('type'), dictionary.get('name'))

        pages = []
        for data in dictionary.get('children'):
            pages.append(self.dict_to_page(data))
        return pages

    def json_to_dict(self, filename):
        with open(filename, 'r') as f:
            json_string = f.read()
            d = json.loads(json_string)
            return d

