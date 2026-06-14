class BPlusTreeNode:
  def __init__(self, leaf=True):
    self.leaf = leaf
    self.keys = []

    # internal node에서만 사용
    self.children = []

    # leaf node에서만 사용
    self.next = None


class BPlusTree:
  def __init__(self):
    self.t = 2
    self.root = BPlusTreeNode(leaf=True)

  def search(self, key):
    # internal node에 있는 key는 길 안내용 key임.
    # 중간에 key와 일치하는 값이 internal node에 있더라도, 항상 leaf node 끝까지 내려가야 함.

    leaf = self._find_leaf(self.root, key)
    return key in leaf.keys

  def _find_leaf(self, node, key):
    """
    key가 들어있을 가능성이 있는 leaf node까지 내려가는 함수
    B+Tree는 검색이 항상 leaf에서 끝남.
    """

    if node.leaf:
      return node
    else:
      idx = self._find_child_index(node, key)
      return self._find_leaf(node.children[idx], key)

  def insert(self, key: int):
    root = self.root
    if len(root.keys) == 3:
      # root가 꽉 차 있다면, 새로운 root를 만들고 split
      new_root = BPlusTreeNode(leaf=False)
      new_root.children.append(root)

      self._split_child(new_root, 0)
      self.root = new_root

      self._insert_non_full(root, key)
    else:
      self._insert_non_full(root, key)

  def _insert_non_full(self, node: BPlusTreeNode, key: int):
    if node.leaf:
      if key in node.keys:
        print(f"Key {key} already exists in the tree.")
        return

      node.keys.append(key)
      node.keys.sort()
      return

    # leaf가 아니라면, 어느 child로 내려갈지 찾아야 함.
    idx = self._find_child_index(node, key)

    # 내려갈 child가 꽉 차 있다면, 먼저 분할해야 함.
    if len(node.children[idx].keys) == 3:
      self._split_child(node, idx)

      # split 후 어느 child로 내려갈지 다시 찾아야 함.
      idx = self._find_child_index(node, key)

    self._insert_non_full(node.children[idx], key)

  def _find_child_index(self, node: BPlusTreeNode, key: int) -> int:
    # B+tree에서는 key == n_key인 경우, 오른쪽 child로 내려감.
    # B+tree에서 internal node의 key는 길 안내용 key이기 때문임.

    # internal node 전용 함수
    if node.leaf:
      raise ValueError("Node is a leaf, cannot find child index.")

    for i, n_key in enumerate(node.keys):
      if key < n_key:
        return i

    return len(node.keys)

  def _split_child(self, parent: BPlusTreeNode, idx: int):
    child = parent.children[idx]

    if child.leaf:
      self._split_child_leaf(parent, idx)
    else:
      self._split_child_internal(parent, idx)

  def _split_child_leaf(self, parent: BPlusTreeNode, idx: int):
    # B-tree에서는 leaf node가 꽉 차면, 가운데 key를 parent로 올리고, 오른쪽 절반을 새로운 leaf node로 만듦.
    # B+Tree에서는 leaf node가 꽉 차면, 오른쪽 절반을 새로운 leaf node로 만들고, parent에는 오른쪽 절반의 첫 번째 key를 올림.

    child = parent.children[idx]

    new_child = BPlusTreeNode(leaf=True)

    # [10|20|30] -> [10], [20|30]
    new_child.keys = child.keys[1:]
    child.keys = child.keys[:1]

    # leaf linked list 연결
    new_child.next = child.next
    child.next = new_child

    # parent에 new_child 추가
    parent.children.insert(idx + 1, new_child)

    # 부모의 자식 목록에 새 child를 삽입
    parent.keys.insert(idx, new_child.keys[0])


  def _split_child_internal(self, parent: BPlusTreeNode, idx: int):
    # 내부 노드는 부모로 key를 이동 시켜야 함(move-up).
    child = parent.children[idx]

    new_child = BPlusTreeNode(leaf=False)

    # [10|20|30] -> [10], 20은 부모로, [30]
    promote_key = child.keys[1]
    new_child.keys = child.keys[2:]
    child.keys = child.keys[:1]

    # child 분할
    new_child.children = child.children[2:]
    child.children = child.children[:2]

    # parent에 new_child 추가
    parent.children.insert(idx + 1, new_child)

    # 부모의 자식 목록에 새 child를 삽입
    parent.keys.insert(idx, promote_key)


"""
      [20 | 40]
    /  |   \
 [5|10] -> [20|30] -> [40|50]
"""

tree = BPlusTree()
keys_to_insert = [10, 20, 5, 6, 12, 30, 25, 15, 18, 22]
for key in keys_to_insert:
  tree.insert(key)



