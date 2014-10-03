# -*- coding: utf-8 -*-
import math
from rect_type import rect_types
import itertools
import types


def init(page_sets, width, height):
    for i in xrange(len(page_sets)):
        page_sets[i].id = i

    page_sets = [[d] for d in page_sets]

    page_sets.sort(cmp=page_cmp)
    page_sets.reverse()
    set_ideal_area(page_sets, width, height)
    return page_sets


def priority_sum(page_sets):
    if not is_group(page_sets):
        return page_sets.priority
    if is_group(page_sets[0]):
        return sum([sum([page.priority for page in page_set]) for page_set in page_sets])
    return sum([page.priority for page in page_sets])


def is_group(page_set):
    return type(page_set) == types.ListType


def ideal_area_sum(page_set):
    return sum([page.ideal_area for page in page_set])


def page_cmp(x, y):
    """Cmp function to page"""
    return cmp(sum([page.priority for page in x]),
               sum([page.priority for page in y]))


def get_top_1(page_sets):
    """ Get page_set which have the first priority """

    top = None
    for page_set in page_sets:
        if not top or priority_sum(top) < priority_sum(page_set):
            top = page_set
    return top


def get_optimum_set(page_sets, rect):
    # TODO: 2つ以上の組み合わせも可にする
    s = rect.width * rect.height

    match = 0
    optimum_set = None
    for page_set in page_sets:
        area_sum = sum([page.ideal_area for page in page_set])
        if not optimum_set or abs(s - area_sum) < abs(s - match):
            optimum_set = page_set
            match = area_sum

    for a, b in itertools.combinations(page_sets, 2):
        area_sum = sum([page.ideal_area for page in a])
        area_sum += sum([page.ideal_area for page in b])

        if abs(s - area_sum) < abs(s - match):
            optimum_set = [a, b]
            match = area_sum

    return optimum_set


def set_ideal_area(page_sets, width, height):
    total_priority = sum([priority_sum(page_set)
                          for page_set in page_sets])
    all_area = width * height

    for page_set in page_sets:
        for page in page_set:
            page.ideal_area = page.priority * all_area // total_priority


def grouping_page_sets(page_sets, RANGE=1.5):
    """ Create groups [1,2,3,4,5] -> [[1,2,3][4,5]] """
    RANGE = 1.4

    groups = []
    for key in rect_types.keys():
        pages = [page_set for page_set in page_sets if page_set[0].type == key]

        if not pages:
            continue

        if len(pages) < 2:
            # TODO: typeのpagesの数が2以下の場合どうする？
            groups.append(pages)
            continue


        while pages:
            base = pages.pop()
            max_priority = int(math.ceil(base[0].priority * RANGE))

            array = base
            for page in pages:
                if page[0].priority <= max_priority:
                    array += page
                    pages.remove(page)


            # array = base + [page[0] for page in pages if page[0].priority < max_priority]

            if len(array) < 2:
                groups.append(array)
            else:
                group = [list(a) for a in zip(array[::2], array[1::2])]
                if len(array) % 2 == 1:
                    group[-1].append(array[-1])

                for g in group:
                    groups.append(g)

    return groups


def flatten(arrays):
    if is_group(arrays[0]):
        flat = []
        for array in arrays:
            flat += flatten(array)
        return flat
    else:
        return arrays


def page_in(target, array):
    for t in target:
        for a in array:
            if t == a:
                break
        else:
            return False
    return True


def contract_priorities(page_sets, width, height, min_width, min_height):
    priority_sum = sum([page[0].priority for page in page_sets])
    area_sum = width * height
    area_min = min_width * min_height
    x = float(float(area_sum / area_min)) / priority_sum

    for page_set in page_sets:
        page_set[0].priority = int(math.ceil(x * page_set[0].priority))

