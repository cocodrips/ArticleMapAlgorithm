import json
import model
import types

class PageGenerator():

    def generate_from_json(self, filename):
        dictionary = self.json_to_dict(filename)
        print dictionary
        print self.dict_to_page(dictionary)

    def dict_to_page(self, dictionary):
        if type(dictionary.get('data')) != types.ListType:
            return model.Page(dictionary.get('data'), dictionary.get('type'), dictionary.get('name'))

        else:
            pages = []
            for data in dictionary.get('data'):
                pages.append(self.dict_to_page(data))
            return pages

    def json_to_dict(self, filename):
        with open(filename, 'r') as f:
            json_string = f.read()
            d = json.loads(json_string)
            return d

