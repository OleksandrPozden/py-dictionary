from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.size = 8
        self.lenght = 0
        self.hash_table = [None]*self.size
    
    def __setitem__(self, key, value) -> None:
        index = hash(key) % self.size
        while True:
            dict_item = self.hash_table[index]
            if dict_item is None:
                self.hash_table[index] = [key, hash(key), value]
                self.lenght += 1
                break
            if dict_item[0] == key and dict_item[1] == hash(key):
                self.hash_table[index][2] = value
                break
            index += 1
            index %= self.size
        if self.lenght/self.size > 2/3:
            self._resize()

    def __getitem__(self, key) -> Any:
        index = hash(key) % self.size
        while True:
            dict_item = self.hash_table[index]
            if dict_item is None:
                raise KeyError(f"key {key!r} does not exist in the {self!r}")
            if key == dict_item[0] and hash(key) == dict_item[1]:
                return self.hash_table[index][2]
            index += 1
            index %= self.size
    
    def __delitem__(self, key) -> int:
        index = hash(key) % self.size
        iterations = 0
        while iterations < self.size:
            dict_item = self.hash_table[index]
            if (
                dict_item is not None 
                and key == dict_item[0] 
                and hash(key) == dict_item[1]
            ):
                del dict_item
                self.hash_table[index] = None
                self.lenght -= 1
                return
            index += 1
            index %= self.size
            iterations += 1
        raise KeyError(f"key {key!r} does not exist in the {self!r}")
    
    def _resize(self) -> None:
        hash_table_copy = self.hash_table
        self.size *= 2
        self.hash_table = [None]*self.size
        self.lenght = 0
        for dict_item in hash_table_copy:
            if dict_item is not None:
                self.__setitem__(dict_item[0],dict_item[2])

    def __str__(self) -> str:
        return (
                f"{{" 
                + ", ".join(f"{item[0]!r}: {item[2]!r}" for item in self.hash_table if item is not None) 
                + f"}}"
        )
    def __repr__(self) -> str:
        return f"Dictionary <lenght={self.lenght}, size={self.size}>"

    def __iter__(self):
        self.index = 0
        self.n = 0
        return self
    
    def __next__(self) -> Any:
        if self.n == self.lenght:
            raise StopIteration
        while True:
            dict_item = self.hash_table[self.index]
            self.index += 1
            if dict_item is not None:
                self.n += 1
                return dict_item[0]
    
    def __len__(self) -> int:
        return self.lenght

if __name__ == "__main__":
    d = Dictionary()
    d[1] = [1,2,3] 
    d[2] = 12
    d[1] = 10
    d["key"] = 13
    d["key"] = 10
    d[9] = 11
    d[17] = 10
    d[17] = 0
    d["Element 5"] = 5
    print(d)
    for key in d:
        print(key)

