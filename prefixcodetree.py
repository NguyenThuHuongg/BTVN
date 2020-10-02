class Node:
    def __init__(s, data):
        s.right = None
        s.left = None
        s.data = data

    def isLeave(s):
        return (s.right is None) and (s.left is None)

class PrefixCodeTree:
    def __init__(s):
        s.root = Node('')

    def insert(s, codeword, symbol):
        node = s.root

        for code in codeword:
            if (code == 0):
                if (node.left is None):
                    node.left = Node('')
                    node = node.left
                else:
                    node = node.left
            else:
                if (node.right is None):
                    node.right = Node('')
                    node = node.right
                else:
                    node = node.right

        node.data = symbol

    def decode(s, encodedData, datalen):
        data = ''
        result = ''
        node = s.root

        # Convert encodedData to bit data
        for byte in encodedData:
            data += f'{byte:08b}'

        # Decode encodedData
        for i in range(datalen):
            if (data[i] == '0'):
                node = node.left
            else:
                node = node.right

            if (node.isLeave()):
                result += node.data
                node = s.root
        return result

if __name__ == '__main__':
    codeTree = PrefixCodeTree()

    codebook = {
        'x1': [0],
        'x2': [1, 0, 0],
        'x3': [1, 0, 1],
        'x4': [1, 1]
    }

    for symbol in codebook:
        codeTree.insert(codebook[symbol], symbol)

    print(codeTree.decode(b'\xd2\x9f\x20', 21))
