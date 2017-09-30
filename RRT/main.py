import matplotlib.pyplot as plt
import numpy as np
import random

import configuration as q
import tree

MIN_X = 0
MAX_X = 100
MIN_Y = 0
MAX_Y = 100

def generate_random_configuration():
  random_x = random.uniform(MIN_X, MAX_X)
  random_y = random.uniform(MIN_Y, MAX_Y)
  return q.Configuration(random_x, random_y)


def find_nearest_vertex(graph, target_q):
  return graph.find_nearest(target_q)


def new_configuration(q_near, q_rand, delta_q):
  orientation_vector = q_rand.position() - q_near.position()
  if delta_q < np.linalg.norm(orientation_vector):
    normalized_vector = orientation_vector / np.linalg.norm(orientation_vector)
    new_position = q_near.position() + normalized_vector * delta_q
  else:
    new_position = q_near.position() + orientation_vector
  return q.Configuration(new_position[0], new_position[1])


def build_rrt(q_init, vertices_num, delta_q):
  """
  @param q_init root of tree
  @param vertices_num number of vertices in tree
  @param delta_q incremental distance
  @return rapidly exploring random tree
  """
  rrt = tree.Tree(q_init)
  for i in range(vertices_num):
    q_rand = generate_random_configuration()
    q_near = find_nearest_vertex(rrt, q_rand)
    q_new = new_configuration(q_near, q_rand, delta_q)
    q_near.connect(q_new) # Add vertex q_new and create edge

  return rrt


def draw_rrt(graph):
  plot_whole_tree(graph)
  plt.xlim(MIN_X, MAX_X)
  plt.ylim(MIN_Y, MAX_Y)
  plt.grid(color='black', linestyle='dotted', linewidth=1)
  plt.show()


def plot_whole_tree(graph):
  root = graph.get_root()
  for node in root.connected_nodes():
    draw_line(root.position(), node.position())
    sub_tree = tree.Tree(node)
    plot_whole_tree(sub_tree)


def draw_line(from_pos, to_pos):
  plt.plot([from_pos[0], to_pos[0]], [from_pos[1], to_pos[1]], 'k-')


def main():
  q_init = q.Configuration(50, 50)
  vertices_num = 1000
  delta_q = 1
  rrt = build_rrt(q_init, vertices_num, delta_q)
  draw_rrt(rrt)


if __name__=='__main__':
  main()
