class Solution:
	def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		# Store all the values in a list, sort the list, 
        #   and assign new values from the sorted list.
		if not head:
			return None
		values = []
		while head:
			values.append(head.val)
			head = head.next
		values.sort()
		dummy = ListNode(0)
		current = dummy
		for value in values:
			current.next = ListNode(value)
			current = current.next
		return dummy.next