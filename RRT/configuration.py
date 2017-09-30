import numpy as np

class Configuration():
  def __init__(self, x, y):
    self._x = x
    self._y = y
    self._next_nodes = []


  def position(self):
    return np.array((self._x, self._y))


  def connect(self, next_q):
    self._next_nodes.append(next_q)


  def connected_nodes(self):
    return self._next_nodes


  def distance_between(self, another_q):
    return np.linalg.norm(self.position() - another_q.position())
