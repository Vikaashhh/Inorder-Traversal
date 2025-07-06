class Solution:
    def inOrder(self, root):
        result = []
        current = root

        while current:
            if current.left is None:
                # Agar left nahi hai toh node ko visit karo
                result.append(current.data)
                current = current.right
            else:
                # Left subtree ke rightmost node ko dhoondo (predecessor)
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    # Link current node to rightmost node of left subtree
                    predecessor.right = current
                    current = current.left
                else:
                    # Agar link already bana hua hai, toh tod do aur node visit karo
                    predecessor.right = None
                    result.append(current.data)
                    current = current.right

        return result
