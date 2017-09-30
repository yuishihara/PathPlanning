#  MIT License
#
#  Copyright (c) 2017 Yu Ishihara
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
import matplotlib.pyplot as plt
import numpy as np
import random

import configuration as q
from tree import Tree
from fasttree import FastTree

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
  rrt = FastTree(q_init)
  for i in range(vertices_num):
    q_rand = generate_random_configuration()
    q_near = find_nearest_vertex(rrt, q_rand)
    q_new = new_configuration(q_near, q_rand, delta_q)
    q_near.connect(q_new) # Add vertex q_new and create edge
    rrt.add_node(q_new)

  return rrt


def draw_rrt(graph):
  plot_whole_tree(graph.get_root())
  plt.xlim(MIN_X, MAX_X)
  plt.ylim(MIN_Y, MAX_Y)
  plt.grid(color='black', linestyle='dotted', linewidth=1)
  plt.show()


def plot_whole_tree(root):
  for node in root.connected_nodes():
    draw_line(root.position(), node.position())
    plot_whole_tree(node)


def draw_line(from_pos, to_pos):
  plt.plot([from_pos[0], to_pos[0]], [from_pos[1], to_pos[1]], 'k-')


def main():
  q_init = q.Configuration(50, 50)
  vertices_num = 500
  delta_q = 1
  rrt = build_rrt(q_init, vertices_num, delta_q)
  print 'finish'
  draw_rrt(rrt)


if __name__=='__main__':
  main()
