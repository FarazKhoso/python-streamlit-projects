import streamlit as st
import json

# File to store tasks
tasks_file = "tasks.json"

def load_tasks():
    try:
        with open(tasks_file, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(tasks_file, "w") as f:
        json.dump(tasks, f, indent=4)

def main():
    st.title("📝 To-Do List App")
    st.write("Manage your tasks easily with this simple To-Do App.")
    
    tasks = load_tasks()
    
    new_task = st.text_input("Add a new task:")
    if st.button("Add Task"):
        if new_task:
            tasks.append({"task": new_task, "completed": False})
            save_tasks(tasks)
            st.success("Task added successfully!")
            st.rerun()  # Fix: Changed experimental_rerun() to rerun()
    
    st.subheader("Your Tasks")
    
    for index, task in enumerate(tasks):
        col1, col2, col3 = st.columns([0.7, 0.15, 0.15])
        
        with col1:
            if task["completed"]:
                st.write(f"✅ ~~{task['task']}~~")
            else:
                st.write(f"🔹 {task['task']}")
        
        with col2:
            if st.button("Complete", key=f"comp_{index}"):
                tasks[index]["completed"] = True
                save_tasks(tasks)
                st.rerun()  # Fix applied here as well
        
        with col3:
            if st.button("Delete", key=f"del_{index}"):
                tasks.pop(index)
                save_tasks(tasks)
                st.rerun()  # Fix applied here too

if __name__ == "__main__":
    main()
