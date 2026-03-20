class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    cur = head
    for x in arr[1:]:
        cur.next = Node(x)
        cur = cur.next
    return head

def print_list(head):
    cur = head
    result = []
    while cur:
        result.append(str(cur.data))
        cur = cur.next
    print("[" + "][".join(result) + "]")

def rearrange(head):
    arr = []
    cur = head
    while cur:
        arr.append(cur.data)
        cur = cur.next

    n = len(arr) // 2
    odd = arr[0::2]   # node[1], node[3], ...
    even = arr[1::2]  # node[2], node[4], ...
    new_arr = odd + even

    cur = head
    for x in new_arr:
        cur.data = x
        cur = cur.next
    return head

arr = list(map(int, input("Nhap 0 de dung: ").split()))
if 0 in arr:
    arr = arr[:arr.index(0)]

head = create_list(arr)
print("List goc: ", end="")
print_list(head)

head = rearrange(head)
print("List moi: ", end="")
print_list(head)
