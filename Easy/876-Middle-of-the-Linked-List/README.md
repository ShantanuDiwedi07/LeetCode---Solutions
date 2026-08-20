# 876. Middle of the Linked List

**Difficulty:** Easy
**Pattern:** Two Pointers (Slow & Fast)
**Link:** https://leetcode.com/problems/middle-of-the-linked-list/

---

## Problem Statement

You are given the `head` of a singly linked list. Return the middle node of the linked list.

If there are two middle nodes, return **the second middle node**.

### Example 1
```
Input:  head = [1,2,3,4,5]
Output: [3,4,5]
```

### Example 2
```
Input:  head = [1,2,3,4,5,6]
Output: [4,5,6]
```

### Constraints
- The number of nodes in the list is in the range `[1, 100]`.
- `1 <= Node.val <= 100`

---

## Diagram

![Slow and fast pointer walkthrough](./diagram.svg)

---

## Approach — Slow & Fast Pointers (Tortoise and Hare)

- Start two pointers, `slow` and `fast`, at `head`.
- On every iteration:
  - `slow` moves **1** node forward.
  - `fast` moves **2** nodes forward.
- Since `fast` covers ground twice as quickly, by the time it reaches the end of the list, `slow` has covered exactly half the distance — landing it on the middle node.
- Loop condition: keep going while `fast` and `fast.next` are both non-null (this naturally handles both odd- and even-length lists, returning the second middle for even lengths).

### Why this works
If the list has `n` nodes, `fast` needs `⌈n/2⌉` iterations to hit the end. `slow`, moving at half the speed, ends up exactly at index `⌊n/2⌋` — the middle (or second-middle) node.

---

## Complexity

| Metric | Complexity |
|---|---|
| Time  | O(n) — single pass |
| Space | O(1) — two pointers, no extra structures |

---

## Pseudocode

```
function middleNode(head):
    slow = head
    fast = head
    while fast is not null and fast.next is not null:
        slow = slow.next
        fast = fast.next.next
    return slow
```

---

## Notes
- This is the foundational slow/fast pointer template — the same skeleton (with a small tweak) powers **#141 Linked List Cycle** and **#142 Linked List Cycle II**.
- Common pitfall: checking only `fast != null` and forgetting `fast.next != null` causes a null-pointer dereference on even-length lists.
