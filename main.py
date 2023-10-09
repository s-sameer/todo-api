from fastapi import FastAPI
from models import Todo

app = FastAPI()

# Create a todo app
@app.get("/")
async def root():
    return {"message": "Welcome to my todo app"}

todos = []

# Get all the todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# Get a todo by id
@app.get("/todos/{id}")
async def get_todo_by_id(id: int):
    for todo in todos:
        if todo["id"] == id:
            return todo
    return {"error": "Todo doesn't exist"}

# Create a todo
@app.post("/todos")
async def create_todo(todo: Todo):
    todos.append(todo.dict())
    return {"message": "Todo Created"}

# Update a todo
@app.put("/todos/{id}")
async def update_todo(id: int, todo_obj: Todo):
    for todo in todos:
        if todo["id"] == id:
            todo["description"] = todo_obj.description
            return {"message": "Todo Updated Successfully"}
    return {"error": "Todo doesn't exist"}

# Delete a todo
@app.delete("/todos/{id}")
async def delete_todo_by_id(id: int):
    for index, todo in enumerate(todos):
        if todo["id"] == id:
            todos.pop(index)
            return {"message": "Todo Deleted Successfully"}
    return {"error": "Todo doesn't exist"}