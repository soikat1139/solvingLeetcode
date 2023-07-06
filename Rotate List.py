class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)
node4=ListNode(4)
node5=ListNode(5)
head.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
curr=head
while curr!=None:
    # print(curr.val)
    curr=curr.next
def getLength(head):
        currentNode=head
        length=0
        while currentNode != None:
            length+=1
            currentNode=currentNode.next
        return length

length=getLength(head)

def getTail(head):
    currNode=head
    while currNode.next != None:
         currNode=currNode.next
    return currNode
# print(getTail(head).val)

toTreverse=length-2
treversedPosition=1
newTail=head
while treversedPosition < toTreverse:
        treversedPosition+=1
        newTail=newTail.next


def getTail(head):

    currNode=head
    while currNode.next != None:
        currNode=currNode.next
    return currNode
tail=getTail(head)

tail.next=head
newHead=newTail.next
newTail.next=None

cur=newHead
while cur!=None:
    print(cur.val)
    cur=cur.next
