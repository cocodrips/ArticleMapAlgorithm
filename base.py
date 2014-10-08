import page_generator

# Rename
DEFAULT_WIDTH=800
DEFAULT_HEIGHT=600

class Base():

    def __init__(self, filename, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
        generator = page_generator.PageGenerator()
        self.page_set = generator.generate_from_jsonfile(filename)
        self.width = width
        self.height = height

    def layout(self):
        pass

    def new_sets(self, page_sets, target):
        pass
