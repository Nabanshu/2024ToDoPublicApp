import streamlit as sl
import backend

todos_list = backend.get_todos()

def add_todo():
    todo = sl.session_state["new_todo"].strip()
    if todo:
        todos_list.append(todo + '\n')
        backend.write_todos(todos_list)
        sl.session_state["new_todo"] = ""  # Clear input field
    
sl.title("My ToDo WebApp")
sl.subheader("This is my ToDo app")
sl.write("This app is to increase your Productivity.")

for index, todo in enumerate(todos_list):
    col1, col2 = sl.columns([3, 1])
    with col1:
        sl.write(todo)
    with col2:
        if sl.button("Delete", key=f"delete_{index}"):
            todos_list.remove(todo)
            backend.write_todos(todos_list)
            sl.rerun()

sl.text_input("Enter a todo: ", placeholder="Add new todo.....",on_change=add_todo,key="new_todo")

sl.download_button(label="Download your ToDo list",data=str(todos_list),file_name="ToDoList.txt",icon=":material/download:")

