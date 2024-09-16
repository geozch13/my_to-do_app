import streamlit as st
import functions

# Initialize todos from the function and store them in session state
if 'todos' not in st.session_state:
    st.session_state.todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"].strip()  # Remove extra whitespace
    if todo:
        st.session_state.todos.append(todo)
        functions.write_todos(st.session_state.todos)
        st.session_state["new_todo"] = ""  # Clear the input field


def remove_todo(index):
    st.session_state.todos.pop(index)
    functions.write_todos(st.session_state.todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

# Display and manage todos
for index, todo in enumerate(st.session_state.todos):
    st.checkbox(todo, key=f"{index}-{todo}", on_change=lambda idx=index: remove_todo(idx))

st.text_input(
    label="Add new todo",
    placeholder="Type your todo here...",
    on_change=add_todo,
    key="new_todo"
)

# # Print session state for debugging
# st.write(st.session_state)
