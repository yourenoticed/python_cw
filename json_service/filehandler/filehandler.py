class Filehandler():
    def __init__(self, path: str):
       self.path = path
   
    def write_to_file(self, data: str) -> None:
       with open(self.path, "w") as file:
           file.write(data)
    
    def read_file(self) -> str:
       with open(self.path, "r") as file:
            return "".join(file.readlines())
    
    def append_to_file(self, data: str) -> None:
        with open(self.path, "a") as file:
            file.write(data)