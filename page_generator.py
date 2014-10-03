import json
import pages

class PageGenerator():

    def generate_from_json(self, filename):
        dictionary = self.json_to_dict(filename)

    def dict_to_page(self, dictionary):
        pass

    def json_to_dict(self, filename):
        with open(filename, 'r') as f:
            json_string = f.read()
            d = json.loads(json_string)
            print d

