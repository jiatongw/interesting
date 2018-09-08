class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

# If there is a circle, print it and return; else print "no circle"
def findCircle(head):
    if head is None:
        print("There is no circle in linkedList")
        return None

    slow = head
    fast = head
    loopExist = False

    while fast.next is not None and fast.next.next is not None:
# Two pointers. If there is a circle, the fast and slow pointers
# will meet somewhere in the circle
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            loopExist = True
            print("There is a circle in linkedList")
            break
# Find the entry point of the circle
    if loopExist == True:
        slow = head
        while slow != fast:
            fast = fast.next
            slow = slow.next
        return slow

    print("There is no circle in linkedList")
    return None


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
# The circle starts from node2
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2

    node = findCircle(node1)
    if node is not None:
        print("The circle starts from node:", node.val)