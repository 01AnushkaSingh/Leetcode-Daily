from typing import List, Optional


class Node:

    __slots__ = "l", "r", "lmx", "rmx", "mx"
  
    def __init__(self, l: int, r: int):
        self.l = l       
        self.r = r   
        self.lmx = 1      
        self.rmx = 1      
        self.mx = 1     


class SegmentTree:
   
    __slots__ = "chars", "tree"
  
    def __init__(self, s: str):
        self.chars = list(s)
        n = len(s)
        self.tree: List[Optional[Node]] = [None] * (n * 4)
        self.build(1, 1, n)
  
    def build(self, node_idx: int, left: int, right: int) -> None:
        
        self.tree[node_idx] = Node(left, right)
      
        if left == right:
          
            return
      
        mid = (left + right) // 2
    
        self.build(node_idx << 1, left, mid)
      
        self.build(node_idx << 1 | 1, mid + 1, right)
       
        self.pushup(node_idx)
  
    def query(self, node_idx: int, query_left: int, query_right: int) -> int:
        
        current_node = self.tree[node_idx]
      
       
        if current_node.l >= query_left and current_node.r <= query_right:
            return current_node.mx
      
        mid = (current_node.l + current_node.r) // 2
        result = 0
      
        if query_left <= mid:
            result = self.query(node_idx << 1, query_left, query_right)
      
        
        if query_right > mid:
            result = max(result, self.query(node_idx << 1 | 1, query_left, query_right))
      
        return result
  
    def modify(self, node_idx: int, position: int, new_char: str) -> None:
    
        current_node = self.tree[node_idx]
      
        if current_node.l == current_node.r:
            
            self.chars[position - 1] = new_char
            return
      
        mid = (current_node.l + current_node.r) // 2
      
        if position <= mid:
            
            self.modify(node_idx << 1, position, new_char)
        else:
          
            self.modify(node_idx << 1 | 1, position, new_char)
      
       
        self.pushup(node_idx)
  
    def pushup(self, node_idx: int) -> None:
       
        root = self.tree[node_idx]
        left_child = self.tree[node_idx << 1]
        right_child = self.tree[node_idx << 1 | 1]
      
        root.lmx = left_child.lmx
        root.rmx = right_child.rmx
        root.mx = max(left_child.mx, right_child.mx)
      
        left_range_size = left_child.r - left_child.l + 1
        right_range_size = right_child.r - right_child.l + 1
      
        
        if self.chars[left_child.r - 1] == self.chars[right_child.l - 1]:
           
            if left_child.lmx == left_range_size:
                root.lmx += right_child.lmx
          
            
            if right_child.rmx == right_range_size:
                root.rmx += left_child.rmx
          
            
            root.mx = max(root.mx, left_child.rmx + right_child.lmx)


class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:
      
        
        segment_tree = SegmentTree(s)
        results = []
      
        
        for index, char in zip(queryIndices, queryCharacters):
            
            segment_tree.modify(1, index + 1, char)
            
            max_repeating = segment_tree.query(1, 1, len(s))
            results.append(max_repeating)
      
        return results
