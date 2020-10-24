class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

# Brute Force (compare each head1 node with every head2 node)
def findMergeNode1(head1, head2):
    head2_start = head2
    while head1:
        head2 = head2_start
        while head2:
            if head1 == head2:
                return head1.data
            head2 = head2.next
        head1 = head1.next

# Space/Time tradeoff solution
def findMergeNode2(head1, head2):
    cache = {}

    while head2:
        cache[head2] = True
        head2 = head2.next

    while head1:
        if head1 in cache:
            return head1.data
        head1 = head1.next
