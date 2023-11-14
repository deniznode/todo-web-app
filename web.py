import streamlit as st
import functions


#callback functions
def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    if todo not in st.session_state:
        todos.append(todo)
        functions.update_todos(todos)

def complete_todo():
    for idx, todo in enumerate(todos):
        for i in completed:
            if idx == i:
                todos.pop(idx)
                completed.remove(i)
                # del st.session_state[todo]
    functions.update_todos(todos)


def edit_todo(button_id):
    edit_idx = int(button_id)
    filler = todos[edit_idx]
    st.session_state["item_to_edit"] = edit_idx
    st.session_state["in_edit"] = True
    st.session_state["edit_todo"] = filler


def confirm_edit():
    print("called")
    editing_idx = st.session_state["item_to_edit"]
    todos[editing_idx] = st.session_state["edit_todo"] + '\n'
    functions.update_todos(todos)
    st.session_state["in_edit"] = False


def cancel_edit():
    st.session_state["in_edit"] = False


todos = functions.get_todos()
completed = []
if "item_to_edit" not in st.session_state:
    st.session_state["item_to_edit"] = 0
if "in_edit" not in st.session_state:
    st.session_state["in_edit"] = False
if "item_uncheck" not in st.session_state:
    st.session_state["item_uncheck"] = True

#webpage
placeholder = st.empty()
st.title("My Todo App")
st.subheader("Keep your life organized.")
if not st.session_state["in_edit"]:
    st.write("Please remember to check the completed todos promptly.")
if st.session_state["in_edit"]:
    st.write("Edit todo to keep your life on track.\n")

for idx, todo in enumerate(todos):
    col1, col2 = st.columns(2)
    with col1:
        if not st.session_state["in_edit"]:
            checkbox = st.checkbox(todo, key=todo, disabled=False)
        else:
            checkbox = st.checkbox(todo, key=todo, disabled=True)
    with col2:
        # button_id = "edit"+str(idx)
        edit_button = st.button("Edit", on_click=edit_todo, args=(idx,), key=idx)
    if checkbox:
        completed.append(idx)
    if st.session_state[todo]:
        st.session_state["item_uncheck"] = False
    else:
        st.session_state["item_uncheck"] = True
        # st.experimental_rerun()

#trigger events
complete_button = st.button("Complete", on_click=complete_todo, disabled=st.session_state.get("item_uncheck"), key='complete')
if not st.session_state["in_edit"]:
    st.text_input(label="", placeholder="Enter a todo", on_change=add_todo, args=(), key='new_todo')
if st.session_state["in_edit"]:
    st.text_input(label="Editing todo", placeholder="Enter a todo", on_change=confirm_edit, args=(), key='edit_todo')
    col1, col2 = st.columns([.15, 1])
    with col1:
        cancel_button = st.button("Cancel", on_click=cancel_edit, key='cancel')
    with col2:
        confirm_button = st.button("Confirm", on_click=confirm_edit, key='confirm')

# create_button = st.button("Create")
# st.session_state
