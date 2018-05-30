# Stack and recursive method
There are several situations when recursive methodas are quite handy
  - It is an abstract data type (interface)
  - Basic operations: enqueue() and dequeue() , peek()
  - FIFO structure: first in first out 
  - It can be implemented with dynamic arrays as well as with linked lists
  - Important when implementing BFS algorithm for graphs




## Enqueue
We just simply add the new item to the end of the queue O(1)

```sh
queue.enqueue(10)
```

## Dequeue
We just simply remove the item starting at the beginning of the queue  // FIFO structure 

```sh
queue.dequeue()
```

### Applications
- When a resource is shared with several consumers ( threads ): we store them in a queue
- For example: CPU scheduling
- When data is transferred asynchronously (data not necessarily received at same rate as sent) between two processes
- For example:  IO buffers
- Operational research applications or stochastic models relies heavily on queues !!!

**Bruna Santos - March 30, 2018 10:04 am**