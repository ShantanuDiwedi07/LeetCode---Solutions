# 142. Linked List Cycle II

**Difficulty:** Medium
**Pattern:** Two Pointers (Slow & Fast) — Floyd's Cycle Detection, Phase 2
**Link:** https://leetcode.com/problems/linked-list-cycle-ii/

---

## Problem Statement

Given the `head` of a linked list, return **the node where the cycle begins**. If there is no cycle, return `null`.

There is a cycle in a linked list if some node in the list can be reached again by continuously following the `next` pointer. Internally, `pos` denotes the index of the node the tail connects to (`-1` if no cycle). `pos` is **not** passed as a parameter — you must detect it from the list structure itself.

**Do not modify** the linked list.

### Example 1
```
Input:  head = [3,2,0,-4], pos = 1   (tail connects to node index 1)
Output: node with value 2
```

### Example 2
```
Input:  head = [1,2], pos = 0
Output: node with value 1
```

### Example 3
```
Input:  head = [1], pos = -1
Output: null (no cycle)
```

### Constraints
- The number of nodes is in the range `[0, 10^4]`.
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked list.

**Follow-up:** Can you solve it using `O(1)` (i.e. constant) memory?

---

## Diagram

![Two-phase Floyd's algorithm: meeting point, then finding the cycle entry](./diagram.svg)

---

## Approach — Floyd's Algorithm, Two Phases

This builds directly on **#141 Linked List Cycle**. Detecting a cycle is only half the problem — now you need the *entry node*.

### Phase 1 — Detect the cycle and find a meeting point
- Same as #141: `slow` moves 1 step, `fast` moves 2 steps.
- If `fast` hits `null`, there's no cycle → return `null`.
- If `slow == fast`, they've met somewhere inside the cycle. Note this meeting point.

### Phase 2 — Find the entry node
- Reset one pointer to `head`. Keep the other at the meeting point.
- Move **both** pointers 1 step at a time.
- The node where they meet again is the **start of the cycle**.

### Why Phase 2 works (the math)
Let:
- `L` = distance from `head` to the cycle's entry node
- `C` = length of the cycle
- `k` = distance from the entry node to where `slow`/`fast` first met

When `slow` and `fast` meet, it can be shown that:

```
L = (a multiple of C) - k
```

Which means: walking `L` steps from `head` lands you on the entry node — and walking `L` steps from the meeting point (wrapping around the cycle as needed) *also* lands you on the entry node. So two pointers moving at the same speed — one from `head`, one from the meeting point — are guaranteed to converge exactly at the cycle's start.

---

## Complexity

| Metric | Complexity |
|---|---|
| Time  | O(n) — each phase is a single bounded pass |
| Space | O(1) — satisfies the follow-up constraint, no hash set |

---

## Pseudocode

```
function detectCycle(head):
    slow = head
    fast = head

    // Phase 1: does a cycle exist?
    while fast is not null and fast.next is not null:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return null   // fast hit the end -> no cycle

    // Phase 2: find the entry node
    ptr1 = head
    ptr2 = slow
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1
```

---

## Notes
- This is the natural next step after #141 — same detection phase, plus the head-reset trick to locate the entry node.
- Common pitfall: forgetting to check whether Phase 1 actually found a cycle before running Phase 2 (running Phase 2 unconditionally on an acyclic list is a bug).
- Worth manually tracing through Example 1 (`[3,2,0,-4]`, `pos = 1`) on paper — watching exactly where `slow`/`fast` first meet, then walking both pointers from `head` and the meeting point, makes the "why" click a lot faster than reading the proof.
