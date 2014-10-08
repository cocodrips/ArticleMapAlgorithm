from Tkinter import Canvas, Tk
from page_utils import PageUtils


class Display():
    def __init__(self, layout):
        self.layout = layout

    def show(self):
        root = Tk()
        canvas = Canvas(root, width=self.layout.width, height=self.layout.height)
        self.layout.layout()
        self.draw_page_sets(canvas, self.layout.page_set)
        canvas.pack()
        root.mainloop()

    def draw_page_sets(self, canvas, page_sets):
        if not PageUtils.is_group(page_sets):
            self.draw_rectangle(canvas, page_sets)
        else:
            for page_set in page_sets:
                self.draw_page_sets(canvas, page_set)


    def draw_rectangle(self, canvas, page):
        canvas.create_rectangle(page.rect.x, page.rect.y, page.rect.x + page.rect.width,
                                page.rect.y + page.rect.height,
                                outline="#555")
        canvas.create_text(page.rect.x + page.rect.width / 2, page.rect.y + 10,
                           text=str(page.original_priority))
