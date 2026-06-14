# Binary Search Tree 구현하기
# key 보다 크면, 오른쪽으로 이동
# key 보다 작으면, 왼쪽으로 이동

class Node:
    # 현재 노드가 저장할 값.
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        print("Initialize BST")
        self.root = None

    def insert(self, key):
        if self.root is None:
            print(f"Insert {key} as root")
            self.root = Node(key)
            return

        current_node = self.root

        while True:
            if current_node.key == key:
                print(f"{key} already exists in BST")
                return
            elif current_node.key > key:
                if current_node.left is None:
                    print(f"Insert {key} as left child of {current_node.key}")
                    current_node.left = Node(key)
                    return
                current_node = current_node.left
            else:
                if current_node.right is None:
                    print(f"Insert {key} as right child of {current_node.key}")
                    current_node.right = Node(key)
                    return
                current_node = current_node.right

    def search(self, key):
        current_node = self.root

        while current_node:
            if current_node is None:
                print(f"{key} not found in BST")
                return False
            elif current_node.key == key:
                print(f"{key} found in BST")
                return True
            elif current_node.key > key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        print(f"{key} not found in BST")
        return False

    def remove(self, key):
        if self.root is None:
            print("BST is empty")
            return

        parent = None
        current = self.root

        while True:
            if key == current.key:
                break
            elif key < current.key:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right

            if current is None:
                print(f"{key} not found in BST")
                return

        # current의 자식이 0개인 경우
        if current.left is None and current.right is None:
            print(f"Remove {key} from BST with 0 children")
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None

        # current의 자식이 1개인 경우
        if current.left is None and current.right is not None:
            print(f"Remove {key} from BST with 1 child")
            if parent is None:
                self.root = current.right
            elif parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right

        if current.left is not None and current.right is None:
            print(f"Remove {key} from BST with 1 child")
            if parent is None:
                self.root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left

        # current의 자식이 2개인 경우
        if current.left is not None and current.right is not None:
            print(f"Remove {key} from BST with 2 children")
            right = current.right
            right_parent = current

            while right.left:
                right_parent = right
                right = right.left

            if right_parent == current:
                right_parent.right = right.right
            else:
                right_parent.left = right.right

            current.key = right.key
            print(f"Replace {key} with {right.key}")

tree = BST()
tree.insert(5)
tree.insert(5)
tree.insert(1)
tree.insert(6)
tree.insert(8)

tree.search(5)
tree.search(1)
tree.search(6)
tree.search(8)
tree.search(10)

tree.remove(5)
tree.search(5)
