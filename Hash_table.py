class Hash_table:
    def __init__(self):
        self.MAX=100
        self.arr=[None for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for i in key:
            h += ord(i)
        return h%self.MAX

    def __getitem__(self,key):
        hash_val = self.get_hash(key)
        return self.arr[hash_val]

    def __setitem__(self,key,value):
        hash_val = self.get_hash(key)
        self.arr[hash_val] = value

    def __delitem__(self,key):
    
