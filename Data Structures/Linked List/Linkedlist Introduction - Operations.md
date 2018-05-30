# LinkedList Introduction - Operations
## Insertion
# At the beginning
  - Inserting items at the beginning pf the linkedlist: very simple, we just have to update the references
  - O(1) time complexity
```linkedList.insertAtStart(10)```

# At he end
  - Inseting items at the end of the linked list: not tha very simple, we have to traverse the whole linkedlist to find the last node
  - How do we find the last node? We know the last node is pointing to a NULL
    - we have to update the references when we get there 
    - O(N) time complexity
```linkedList.insertAtEnd(25)```

## Remove
# At the beginning
  - Remove item at the beginning of the list is always very fast: we do not have to search the item, we just have to uptade the references accordingly
  - 0(1) time complexity
``` linkedList.removeStar()```

# At he end
  - Remove item at given point of the list is not always very fast: we have ti search for the given item which may take lot of time if the item is at the end of the list
  - O(N) time complexity
```linkedList.remove(10)```
```linkedList.removeEND()```

## Resume

|  | Linked List|
| ------ | ------ |
| Insert at the start | O(1) | 
| Insert at the end | O(N) |
| Remove at the start |O(1)|
| Remove at the end | O(N) |

Bruna Santos - January 29, 2018 12:15 pm

