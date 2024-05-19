# from sys import setrecursionlimit 
# setrecursionlimit(10**9)
from sys import stdin

class Node:
    def __init__(self, value:int=None, left=None, right=None):
        self.value_ = value
        self.left_ = left
        self.right_ = right

    def print(self):
        print(f"{self.value_}, {self.left_}, {self.right_}")


class BST():
    def __init__(self):
        self.root_ = None
    
    # root부터 시작
    def insert(self, cur_node:Node, new_node: Node):
        if (self.root_ == None):
            self.root_ = new_node

        if (cur_node == None):
            return 

        if (new_node.value_ < cur_node.value_):
            if (cur_node.left_ == None):
                cur_node.left_ = new_node
            else:
                self.insert(cur_node.left_, new_node)
        elif (new_node.value_ > cur_node.value_):
            if (cur_node.right_ == None):
                cur_node.right_ = new_node
            else:
                self.insert(cur_node.right_, new_node)
        # else: # 같은 키 값, 에러
        #     raise Exception('같은 키값')
    
    def iter_insert(self, new_node: Node):

        if (self.root_ == None):
            self.root_ = new_node
            return 
        cur_node = self.root_
        while (cur_node):
            if (new_node.value_ > cur_node.value_):
                if (cur_node.right_ == None):
                    cur_node.right_ = new_node
                    break
                cur_node = cur_node.right_
            else:
                if (cur_node.left_ == None):
                    cur_node.left_ = new_node
                    break
                cur_node = cur_node.left_
        
    #  root - left - right
    def pre_order(self, node: Node):
        # to remove
        if (node == None):
            return 
        # print(str(node.value_) + '\n')
        print(node.value_, sep=' ')
        self.pre_order(node.left_)
        self.pre_order(node.right_)
    
    def post_order(self, node: Node):
        # to remove
        if (node == None):
            return 
        self.post_order(node.left_)
        self.post_order(node.right_)
        print(node.value_, sep=' ')
        # print(str(node.value_) + '\n')

    '''
    stack 이용
    root가 마지막에 출력되어야하므로 root가 먼저 stack에 들어가야한다.
    root를 스택에 넣고 오른쪽 왼쪽 순서로 스택에 넣는다?
           30
       25      50
    20   27  40  60

    post-queue 30 50 25 60 40
    post-stack 30 50 60 40 25 27 20 
    post 20 27 25 40 60 50 30
    pre  30 25 20 27 50 40 60

    pre  50 30 24 5 28 45 98 52 60
    post 50 98 52 60 30 45 24 28 5

    Queue 50 98 30
    Stack 50 

    A 50
      30 98 

      24 45 None 

    Stack 50 98 52

    98


    '''
    def iter_post_order(self, node: Node):
        stack = []

        if (node is None):
            return 
        stack.append(node.value_)

        left_node = node.left_
        right_node = node.right_
        node = right_node
        prev_node = node
        while (node):
            stack.append(node.value_)
            if (node.right_):
                node = node.right_
            elif (node.left_):
                node = node.left_
            else:
                node = prev_node 

        node = left_node
        prev_node = left_node
        while (node):
            stack.append(node.value_)
            prev_node = node
            if (node.right_):
                node = node.right_
            elif (node.left_):
                node = node.left_
            else:
                node = prev_node 
        print(f"{stack=}")

# arr = []
bst = BST()
# lines = stdin.readlines()
for line in stdin.readlines():
    number = line[:-1]
    if (number):
        value = int(number)
        # bst.insert(bst.root_, Node(value))
        bst.iter_insert(Node(value))
        # arr.append(node)
    # print(f"#{node=}")
# print("\npre-order")
# bst.pre_order(bst.root_)
# print("\npost-order")
# bst.post_order(bst.root_)
bst.iter_post_order(bst.root_)


'''
# C++ unlimit input 

#include <iostream>
int number;

do {
    std::cin >> number;
} while (getc(stdin) == ' ');

'''