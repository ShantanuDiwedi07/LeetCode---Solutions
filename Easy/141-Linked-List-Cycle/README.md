# 141. Linked List Cycle

**Difficulty:** Easy
**Pattern:** Two Pointers (Slow & Fast) — Floyd's Cycle Detection
**Link:** https://leetcode.com/problems/linked-list-cycle/

---

## Problem Statement

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if some node in the list can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that the tail's `next` pointer is connected to (`-1` if there is no cycle). **Note that `pos` is not passed as a parameter.**

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

### Example 1
```
Input:  head = [3,2,0,-4], pos = 1   (tail connects to node index 1)
Output: true
```

### Example 2
```
Input:  head = [1,2], pos = 0
Output: true
```

### Example 3
```
Input:  head = [1], pos = -1
Output: false
```

### Constraints
- The number of nodes is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked list.

---

## Diagram

![Slow and fast pointer meeting inside a cycle](./diagram.svg)

---

## Approach — Floyd's Cycle Detection (Tortoise and Hare)

- Two pointers, `slow` and `fast`, both start at `head`.
- Each iteration: `slow` moves 1 step, `fast` moves 2 steps.
- **If there is no cycle**, `fast` reaches `null` first — no cycle.
- **If there is a cycle**, `fast` enters the loop before `slow` and starts "lapping" it. Because `fast` gains exactly 1 step on `slow` per iteration, the gap between them shrinks by 1 every time — they are guaranteed to meet inside the loop eventually.
- So: if `slow == fast` at any point (after the first move), a cycle exists. If `fast` (or `fast.next`) hits `null`, there's no cycle.

### Why this always works
Think of it as a circular race track: once both pointers are inside the cycle, the fast pointer closes the distance to the slow pointer by 1 node every step (relative speed = 1). It cannot "jump over" the slow pointer, so a meeting is inevitable, bounded by the cycle's length.

---

## Complexity

| Metric | Complexity |
|---|---|
| Time  | O(n) — fast pointer meets slow within one full lap of the cycle |
| Space | O(1) — no hash set needed, just two pointers |

---

## Pseudocode

```
function hasCycle(head):
    slow = head
    fast = head
    while fast is not null and fast.next is not null:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return true
    return false
```

---

## Alternative Approach (for comparison, not preferred)
A `HashSet<Node>` visited-set also works: walk the list, and if you ever revisit a node already in the set, there's a cycle. This is O(n) time but **O(n) space**, unlike the pointer method above — good to know, but the two-pointer trick is the expected solution.

---

## Notes
- Same slow/fast skeleton as **#876 Middle of the Linked List**, with the loop condition repurposed to check `slow == fast` instead of just walking to the end.
- Directly sets up **#142 Linked List Cycle II**, which asks *where* the cycle starts, not just *whether* one exists.
