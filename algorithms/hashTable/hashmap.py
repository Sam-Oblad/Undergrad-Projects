class HashMap:
    def __init__(self, capacity= 7):
        self.size = 0
        self.capacity = capacity
        self.hashMap = [[] for _ in range(self.capacity)]

    def keys(self):
        keys = []
        for bucket in self.hashMap:
            if bucket:
                for k, v in bucket:
                    keys.append(k)
        return keys

    def hashing_func(self, key):
        a, b = key
        return a + b % self.capacity

    def set(self, key, value):
        hash_key = self.hashing_func(key) % self.capacity
        if not self.hashMap[hash_key]:
            self.hashMap[hash_key] = []
        for i, (k, v) in enumerate(self.hashMap[hash_key]):
            if key == k:
                self.hashMap[hash_key][i] = (key, value)
                return
        self.hashMap[hash_key].append((key, value))
        self.size += 1
        load_factor = self.size / self.capacity
        if load_factor >= 0.8:
            self.capacity *= 2
            new_hashmap = [None] * self.capacity
            for bucket in self.hashMap:
                if bucket:
                    for k, v in bucket:
                        hash_key = self.hashing_func(k) % self.capacity
                        if not new_hashmap[hash_key]:
                            new_hashmap[hash_key] = []
                        new_hashmap[hash_key].append((k, v))
            self.hashMap = new_hashmap

    def get(self, key):
        hash_key = self.hashing_func(key) % self.capacity
        bucket = self.hashMap[hash_key]
        if not bucket:
            raise KeyError(f"{key} does not exist")
        for k, v in bucket:
            if key == k:
                return v
        raise KeyError(f"{key} does not exist")

    def remove(self, key):
        hash_key = self.hashing_func(key) % self.capacity
        bucket = self.hashMap[hash_key]
        if not bucket:
            raise KeyError(f"{key} does not exist")
        for i, (k, v) in enumerate(bucket):
            if key == k:
                del bucket[i]
                self.size -= 1
                return
        raise KeyError(f"{key} does not exist")

    def clear(self):
        self.hashMap = [[] for _ in range(self.capacity)]
        self.size = 0

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)