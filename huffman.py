import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq  # frequency of symbol
        self.symbol = symbol  # symbol name (character)
        self.left = left  # node left of current node
        self.right = right  # node right of current node
        self.huff = ''  # tree direction (0/1)

    def __lt__(self, nxt):  # Check if current frequency is less than next node's frequency
        return self.freq < nxt.freq

def print_nodes(node, val=''):
    new_val = val + str(node.huff)
    if node.left:
        print_nodes(node.left, new_val)
    if node.right:
        print_nodes(node.right, new_val)

    if not node.left and not node.right:
        print("{} -> {}".format(node.symbol, new_val))

if __name__ == "__main__":
    chars = input("Enter characters separated by space: ").split()
    freq = list(map(int, input("Enter corresponding frequencies separated by space: ").split()))
    nodes = []

    for i in range(len(chars)):
        heapq.heappush(nodes, Node(freq[i], chars[i]))

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.huff = '0'
        right.huff = '1'

        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, new_node)

    print("Huffman Codes:")
    print_nodes(nodes[0])

