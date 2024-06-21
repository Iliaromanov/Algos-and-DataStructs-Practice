"""
facts:
    m = 3.28 ft 
    ft = 12 in
    hr = 60 min
    min = 60 sec
examples:
    2 m = ? in -> 78.72
    13 in = ? m -> 0.330
    13 in = ? h -> "not convertable"
"""

from typing import List, Tuple, Dict
from collections import deque

eg_facts = [
    ('m', 3.28, 'ft'),
    ('ft', 12.0, 'in'),
    ('hr', 60.0, 'min'),
    ('min', 60.0, 'sec'),
]

eg_target = (2, 'm', 'in')

def get_adj_list_from_facts(facts: List[Tuple[float | str]]) -> Dict[str, List[Tuple[str | float]]]:
    adj_list = {}
    for fact in facts:
        frm, conv, to = fact
        if frm not in adj_list:
            adj_list[frm] = []
        adj_list[frm].append((to, conv))
        
        if to not in adj_list:
            adj_list[to] = []
        adj_list[to].append((frm, 1 / conv))
    return adj_list

def find_conversion(adj_list: dict, query: tuple) -> float | str:
    amount, frm, to = query
    if frm not in adj_list or to not in adj_list:
        return "not convertable"
    q = deque()
    q.append((frm, amount))
    visited = set()
    while q:
        cur_unit, cur_amount = q.popleft()
        for neighbor_unit, conversion_factor in adj_list[cur_unit]:
            if neighbor_unit == to:
                return cur_amount * conversion_factor
            if neighbor_unit not in visited:
                q.append((neighbor_unit, cur_amount * conversion_factor))
                visited.add(neighbor_unit)
    return "not convertable"

    


def convert(facts: List[Tuple[float | str]], query: Tuple[float | str]) -> float | str:
    adj_list = get_adj_list_from_facts(facts)
    return find_conversion(adj_list, query)


print(convert(eg_facts, (13, 'in', 'min')))