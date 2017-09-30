class Tree():
  def __init__(self, configuration):
    self.root = configuration


  def get_root(self):
    return self.root


  def find_nearest(self, target_q):
    nearest = self.root
    min_distance = nearest.distance_between(target_q)
    for node in nearest.connected_nodes():
      sub_tree = Tree(node)
      candidate = sub_tree.find_nearest(target_q)
      distance = candidate.distance_between(target_q)
      if distance < min_distance:
        nearest = candidate
        min_distance = distance
    return nearest
