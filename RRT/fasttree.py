import kdtree
import numpy as np

from tree import Tree

class FastTree(Tree):
  def __init__(self, node):
    super(FastTree, self).__init__(node)
    self._kdtree = kdtree.create([node], dimensions=2)


  def add_node(self, node):
    self._kdtree.add(node)


  def find_nearest(self, target_q):
    kdnode = self._kdtree.search_nn(target_q)
    return kdnode[0].data
