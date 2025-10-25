import random
import time
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


def range_sum_no_cache(array, left, right):
    return sum(array[left:right + 1])


def update_no_cache(array, index, value):
    array[index] = value


def range_sum_with_cache(array, left, right, cache):
    key = (left, right)
    cached = cache.get(key)
    if cached != -1:
        return cached
    result = sum(array[left:right + 1])
    cache.put(key, result)
    return result


def update_with_cache(array, index, value, cache):
    array[index] = value
    keys_to_remove = [key for key in cache.cache if key[0] <= index <= key[1]]
    for key in keys_to_remove:
        del cache.cache[key]


def make_queries(n, q, hot_pool=30, p_hot=0.95, p_update=0.03):
    hot = [(random.randint(0, n//2), random.randint(n//2, n-1)) for _ in range(hot_pool)]
    queries = []
    for _ in range(q):
        if random.random() < p_update:
            idx = random.randint(0, n-1)
            val = random.randint(1, 100)
            queries.append(("Update", idx, val))
        else:
            if random.random() < p_hot:
                left, right = random.choice(hot)
            else:
                left = random.randint(0, n-1)
                right = random.randint(left, n-1)
            queries.append(("Range", left, right))
    return queries


def main():
    N = 100_000
    Q = 50_000
    array1 = [random.randint(1, 100) for _ in range(N)]
    array2 = array1.copy()
    queries = make_queries(N, Q)

    start = time.time()
    for query in queries:
        if query[0] == "Range":
            range_sum_no_cache(array1, query[1], query[2])
        else:
            update_no_cache(array1, query[1], query[2])
    no_cache_time = time.time() - start

    cache = LRUCache(1000)
    start = time.time()
    for query in queries:
        if query[0] == "Range":
            range_sum_with_cache(array2, query[1], query[2], cache)
        else:
            update_with_cache(array2, query[1], query[2], cache)
    cache_time = time.time() - start

    print(f"Без кешу : {no_cache_time:.2f} c")
    print(f"LRU-кеш  : {cache_time:.2f} c  (прискорення ×{no_cache_time / cache_time:.1f})")


if __name__ == "__main__":
    main()
