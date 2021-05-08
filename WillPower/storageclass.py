class storage:
    def __init__(self,memory_size):
        self.memory=memory_size
    def memory_size(self):
	    print(f"The size of memory in storage is {self.memory} GB")
	    return self.memory
		
		
class usb(storage):
    def __init__(self,memory_size):
        super().__init__(memory_size)
    def memory_size(self):
        print(f"The size of memory in USB is {self.memory} GB")
        return self.memory
		
Hard_disk=storage(1)
print(f"Hard disk: {Hard_disk.memory_size()}")
pendrive=usb(14)
print(f"Pendrive: {pendrive.memory_size()}")
