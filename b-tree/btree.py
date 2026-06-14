# Binary Tree 구현하기
# t=2를 기준으로 구현하였음. 각 노드는 최대 3개의 키를 가질 수 있음.
# t 일반화 하지 X

class BTreeNode:
    def __init__(self, leaf=True):
        # leaf 여부는 len(children) == 0으로도 판단할 수 있음.
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self):
        # 각 노드는 최대 3(=2t-1)개의 키를 가질 수 있음.
        self.t = 2
        self.root = BTreeNode(leaf=True)

    def insert(self, key):
        # 내려가기 전에 root가 꽉 차 있는지 확인해야 함.
        root = self.root

        if len(root.keys) < 3:
            self.insert_non_full(root, key)
        elif len(root.keys) == 3:
            new_root = BTreeNode(leaf=False)
            new_root.children.append(root)

            self.root = new_root
            self.split_child(new_root, 0)

            # 이제 새로운 key insert 가능.
            self.insert_non_full(new_root, key)

    def insert_non_full(self, node, key):
        if node.leaf:
            if key in node.keys:
                print(f"Key {key} already exists in the tree.")
                return
            node.keys.append(key)
            node.keys.sort()
            return

        # leaf가 아니라면, 어느 child로 내려갈지 찾아야 함.
        idx = None
        for i in range(len(node.keys)):
            n_key = node.keys[i]

            if key < n_key:
                idx = i
                break
            elif key == n_key:
                print(f"Key {key} already exists in the tree.")
                return

        if idx is None:
            # key가 node의 모든 key보다 크다면, 마지막 child로 내려감.
            idx = len(node.keys)

        if len(node.children[idx].keys) == 3:
            # 내려갈 child가 꽉 차 있다면, 먼저 분할해야 함.
            self.split_child(node, idx)

            # 분할 후에 다시 어느 child로 내려갈지 찾아야 함.
            if key > node.keys[idx]:
                idx += 1
            elif key == node.keys[idx]:
                print(f"Key {key} already exists in the tree.")
                return

        self.insert_non_full(node.children[idx], key)

    def split_child(self, parent, idx):
        # parant의 idx 번째 자식 노드를 분할해 parent의 자식 노드로 추가하는 함수
        child = parent.children[idx]

        mid_key = child.keys[1]

        new_child = BTreeNode(leaf=child.leaf)

        # key 분할
        new_child.keys = child.keys[2:]
        child.keys = child.keys[:1]

        # child가 내부 노드라면, children도 분할
        if not child.leaf:
            new_child.children = child.children[2:]
            child.children = child.children[:2]

        # 부모의 mid key를 삽입
        parent.keys.insert(idx, mid_key)

        # 부모의 자식 목록에 새 child를 삽입
        parent.children.insert(idx + 1, new_child)

    def search(self, key):
        return self._search_node(self.root, key)

    def _search_node(self, node, key):
        if key in node.keys:
            return True
        elif node.leaf:
            return False
        else:
            idx = None
            for i, n_key in enumerate(node.keys):
                if key < n_key:
                    idx = i
                    break

            if idx is None:
                idx = len(node.keys)

            return self._search_node(node.children[idx], key)

    def print_tree(self):
        self._print_node(self.root, "", True)

    def _print_node(self, node, prefix, is_last):
        connector = "└── " if is_last else "├── "

        print(prefix + connector +
            "[" + "|".join(map(str, node.keys)) + "]")

        for i, child in enumerate(node.children):
            last = (i == len(node.children) - 1)

            self._print_node(
                child,
                prefix + ("    " if is_last else "│   "),
                last
            )

tree = BTree()

tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(8)
tree.insert(1)

tree.print_tree()

print(tree.search(5))  # True
print(tree.search(4))  # False
