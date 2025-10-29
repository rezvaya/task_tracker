class Task:
    def __init__(self, title, status):
        self.title = title
        self.status = status 
    
    def str_to_file(self):
        return f"{self.title}-{self.status}"
    
    def show_task(self):
        if self.status == True:
            return f"Задача: {self.title}. ✔️"
        else:
            return f"Задача: {self.title}. ❌"
        
    def mark_done(self):
        self.status = True
