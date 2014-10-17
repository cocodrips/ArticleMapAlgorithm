
class RectType:
    def __init__(self, ratio, min_align=1):
        self.ratio = ratio
        self.min_align = min_align

rect_types = {
    'image': [
        RectType(0.9, 1),
        RectType(1.6, 1),
        RectType(3.0, 2),
        RectType(3.8, 2)
    ],
    'text': [
        RectType(1.0, 1),
        RectType(3.8, 1),
        RectType(5, 1)
    ]
}