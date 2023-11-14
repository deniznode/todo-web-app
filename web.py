import streamlit as st
import functions


#callback functions
def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    if todo not in st.session_state:
        todos.append(todo)
        functions.update_todos(todos)
        st.session_state["new_todo"] = ""
        if st.session_state["duplicate_notice"]:
            st.session_state["duplicate_notice"] = False
    else:
        change_notice()


def change_notice():
    st.session_state["duplicate_notice"] = True


def complete_todo():
    for i in st.session_state["completed_items"]:
        for idx, todo in enumerate(todos):
            if todo == i:
                todos.pop(idx)
                # completed.remove(i)
                st.session_state["completed_items"].remove(todo)
                # del st.session_state[todo]
    functions.update_todos(todos)


def edit_todo(button_id):
    st.session_state["item_uncheck"] = True
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
    st.session_state["item_uncheck"] = False


def cancel_edit():
    st.session_state["in_edit"] = False


todos = functions.get_todos()
notices = ["Please remember to check the completed todos promptly.",
          "Edit todo to keep your life on track.",
          "Todo already exists."]

if "item_to_edit" not in st.session_state:
    st.session_state["item_to_edit"] = 0
if "in_edit" not in st.session_state:
    st.session_state["in_edit"] = False
if "item_uncheck" not in st.session_state:
    st.session_state["item_uncheck"] = True
if "completed_items" not in st.session_state:
    st.session_state["completed_items"] = []
if "duplicate_notice" not in st.session_state:
    st.session_state["duplicate_notice"] = False

#webpage
placeholder = st.empty()
st.title("My Todo App")
# st.subheader("Keep your life organized.")
notice = st.write()
if st.session_state["in_edit"]:
    notice = st.write(notices[1])
elif st.session_state["duplicate_notice"]:
    notice = st.write(notices[2])
else:
    notice = st.write(notices[0])

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
        if todo not in st.session_state["completed_items"]:
            # completed.append(todos[idx])
            st.session_state["completed_items"].append(todos[idx])
    else:
        if todo in st.session_state["completed_items"]:
            # completed.remove(todos[idx])
            st.session_state["completed_items"].remove(todos[idx])
if len(st.session_state["completed_items"]) < 1 or st.session_state["in_edit"]:
    st.session_state["item_uncheck"] = True
else:
    st.session_state["item_uncheck"] = False
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
