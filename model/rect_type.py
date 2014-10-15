
class RectType:
    def __init__(self, ratio, min_align=1):
        self.ratio = ratio
        self.min_align = min_align

rect_types = {
    'image': [
        RectType(1.1, 1),
        RectType(0.9, 2),
        RectType(3.0, 2)
        # RectType(0.8, 1),
    ],
    'text': [
        RectType(1.2, 1),
        RectType(3.0, 1)
    ]
}