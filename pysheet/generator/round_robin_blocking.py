from collections import deque
from select import select
import socket

tasks = deque()
w_read = {}
