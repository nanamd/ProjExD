

from cProfile import label
from http.client import TOO_MANY_REQUESTS


def count_up():
    global tmr
    tmr = tmr+1
    label["text"]= tmr
    root.after(1000, count_up)