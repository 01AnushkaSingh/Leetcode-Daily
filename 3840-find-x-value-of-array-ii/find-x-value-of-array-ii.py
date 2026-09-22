from typing import List

class Solution:
  def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
    n = len(nums)

    prod = [1] * (4 * n)
    cnt = [[0] * (4 * n) for _ in range(5)]

   
    def pull(node):
      left = node * 2
      right = left + 1

      prod[node] = (prod[left] * prod[right]) % k

      for r in range(k): cnt[r][node] = cnt[r][left]

      for r in range(k):
        nr = (prod[left] * r) % k
        cnt[nr][node] += cnt[r][right]

   
    def build(node, l, r):
      if l == r:
        rem = nums[l] % k

        prod[node] = rem
        cnt[rem][node] = 1

        return

      mid = (l + r) // 2

      build(node * 2, l, mid)
      build(node * 2 + 1, mid + 1, r)

      pull(node)

    def update(node, l, r, index, value):
      if l == r:
        for rem in range(k): cnt[rem][node] = 0

        rem = value % k

        prod[node] = rem
        cnt[rem][node] = 1

        return

      mid = (l + r) // 2

      if index <= mid: update(node * 2, l, mid, index, value)
      else: update(node * 2 + 1, mid + 1, r, index, value)

      pull(node)

    def merge(left, right):
      left_prod, left_cnt = left
      right_prod, right_cnt = right

      counts = left_cnt[:]

      for r in range(k):
        nr = (left_prod * r) % k
        counts[nr] += right_cnt[r]

      return (left_prod * right_prod) % k, counts

    
    def query(node, l, r, ql, qr):
      if ql <= l and r <= qr: return prod[node], [cnt[x][node] for x in range(k)]

      mid = (l + r) // 2

      if qr <= mid: return query(node * 2, l, mid, ql, qr)

      if ql > mid: return query(node * 2 + 1, mid + 1, r, ql, qr)

      left = query(node * 2, l, mid, ql, qr)
      right = query(node * 2 + 1, mid + 1, r, ql, qr)

      return merge(left, right)

    build(1, 0, n - 1)

    result = []

    for index, value, start, x in queries:
      update(1, 0, n - 1, index, value)

     
      _, counts = query(1, 0, n - 1, start, n - 1)
      result.append(counts[x])

    return result       