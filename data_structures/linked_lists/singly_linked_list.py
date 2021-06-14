from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        # NOTE if list is empty
        if not self.head:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def delete(self, data):
        cur = self.head
        # NOTE check if element is head
        if cur.data == data:
            self.head = cur.next
        # NOTE advance and create prev elem
        prev = self.head
        cur = cur.next
        while cur:
            if cur.data == data:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

    def length_itr(self):
        ln = 0
        cur = self.head
        while cur:
            ln += 1
            cur = cur.next
        return ln

    def length_rec(self, cur):
        if not cur:
            return 0
        return 1 + self.length_rec(cur.next)

    def count_occurences(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def swape_nodes(self, data1, data2):
        def _get_prev_and_cur(data):
            cur = self.head
            prev = None
            while cur and cur.data != data:
                prev = cur
                cur = cur.next
            return prev, cur
        # NOTE get previous and current nodes of data
        prev1, cur1 = _get_prev_and_cur(data1)
        prev2, cur2 = _get_prev_and_cur(data2)
        # NOTE check previous node if NONE --> head
        if prev1:
            prev1.next = cur2
        else:
            self.head = cur2
        if prev2:
            prev2.next = cur1
        else:
            self.head = cur1
        # NOTE swap next nodes
        cur1.next, cur2.next = cur2.next, cur1.next

    def merge_lists(self, ls):
        """ merge sorting lists"""
        cur = self.head
        ls_cur = ls.head
        # NOTE if one of the lists is empty
        if not cur:
            return ls_cur
        elif not ls_cur:
            return cur
        # NOTE check head first
        if cur.data < ls_cur.data:
            min_node = cur
            cur = cur.next
        else:
            min_node = ls_cur
            ls_cur = cur.next
        while cur and ls_cur:
            # NOTE check the minimum node
            # # point to the minimum
            # # move current minimum node to the new minimum node
            # # proceed with the current node having the minimum
            if cur.data < ls_cur.data:
                min_node.next = cur
                min_node = cur
                cur = cur.next
            else:
                min_node.next = ls_cur
                min_node = ls_cur
                ls_cur = ls_cur.next
        # NOTE check which list end
        if not cur:
            min_node.next = ls_cur
        else:
            min_node.next = cur
    
    def reverse_list_itr(self):
        cur = self.head
        prev = None
        # NOTE use nxt to store current next node
        # # put previous node as your current next
        # # put previous node as current node
        # # move forward as current is next
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # NOTE put last node - previous - as your head
        self.head = prev

    def reverse_list_rec(self):
        def _reverse_list_rec(cur, prev):
            # NOTE same as iterative method, but return previous node as your head
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_list_rec(cur, prev) 
        self.head = _reverse_list_rec(self.head, None)

    def rotate_list(self, k):
        # NOTE create 3 var to track nodes
        # # current node, will become the last node
        # # last node, we need it to point to the current head
        # # previous node, we need it to become the new head
        cur = self.head
        last = self.head
        prev = None
        count = 0
        while (cur or last) and count < k:
            prev = cur
            cur = cur.next
            last = last.next
            count += 1
        cur = prev
        # NOTE continue to the last element
        while last:
            prev = last
            last = last.next
        last = prev
        last.next = self.head
        self.head = cur.next
        cur.next = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
