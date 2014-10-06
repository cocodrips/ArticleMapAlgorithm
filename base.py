import page_generator

# Rename
class Base():
    def __init__(self, filename):
        generator = page_generator.PageGenerator()
        self.page_set = generator.generate_from_jsonfile(filename)

    def layout(self):
        pass