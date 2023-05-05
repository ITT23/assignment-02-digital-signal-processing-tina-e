from pyglet import shapes


class Menu:
    def __init__(self, window_width, window_height):
        self.menu_items = []
        self.item_count = 5
        self.item_width = window_width
        self.item_height = window_height / self.item_count
        self.initial_item_color = (255, 255, 255)
        self.selected_item_color = (156, 0, 75)
        self.selected_item = 0
        self.init_items()

    def init_items(self):
        for i in range(0, self.item_count):
            item = shapes.BorderedRectangle(x=0, y=i*self.item_height, width=self.item_width, height=self.item_height, border=5, border_color=(0, 0, 0))
            self.menu_items.append(item)

    def up(self):
        if self.selected_item < self.item_count:
            self.selected_item += 1

    def down(self):
        if self.selected_item > 0:
            self.selected_item -= 1

    def update(self):
        for i, item in enumerate(self.menu_items):
            if i == self.selected_item:
                item.color = self.selected_item_color
            else:
                item.color = self.initial_item_color

    def draw(self):
        for item in self.menu_items:
            item.draw()