from base import Base

import pages


class GreedyLayout(Base):
    def layout(self):
        pass

    def show(self):
        root = Tk()
        canvas = Canvas(root, width=self.width, height=self.height)

        self.layout()
        self.draw_page_sets(canvas, self.page_set)
        canvas.pack()
        root.mainloop()
    
    def draw_page_sets(self, canvas, page_sets):
        if not pages.is_group(page_sets):
            self.draw_rectangle(canvas, page_sets)
        else:
            for page_set in page_sets:
                self.draw_page_sets(page_set)


    def draw_rectangle(self, canvas, page):
        canvas.create_rectangle(page.rect.x, page.rect.y, page.rect.x + page.rect.width,
                                page.rect.y + page.rect.height,
                                outline="#555")
        canvas.create_text(page.rect.x + page.rect.width / 2, page.rect.y + 10,
                           text=str(page.original_priority))
        


    def _arrange(self, page_sets, rect):
        if not page_sets:
            return

        if len(page_sets) < 3:
            # self.divide_space(page)
            pass

    def _divide_space(self, page_sets, rect):
        pass

    def _arrange_top_1(self, page_sets, rect):
        pass


