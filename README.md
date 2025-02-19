# 📂 Python File Management System

### 🚀 Simplify File Operations with Python

Manually handling files can be frustrating and time-consuming. This Python-powered File Management System automates common file operations, making your workflow more efficient and organized.

## 🔹 Features

✔️ List all files in a directory  
✔️ Rename files easily  
✔️ Delete files and folders  
✔️ Create new directories  
✔️ Move files between directories  
✔️ Copy files with ease  
✔️ Check file sizes instantly  

## 🏗️ Initial Approach: If-Else Logic

The first version of this project used multiple `if-elif` conditions to match user choices with functions. While it worked, the code became bulky and less maintainable.

### ⚠️ Drawbacks:
- Too many conditions made it difficult to read
- Extending the system required modifying multiple sections
- Execution involved unnecessary comparisons

## 🎯 A Better Approach: Dictionary-Based Menu System

To improve readability and scalability, the system now utilizes a dictionary to map user inputs directly to functions.

```python
menu_actions = {
    "1": list_files,
    "2": rename_file,
    "3": delete_path,
    "4": create_directory,
    "5": move_file,
    "6": copy_file,
    "7": get_file_size,
    "8": exit_program
}
```

Now, executing a function is as simple as:

```python
menu_actions.get(choice, invalid_option)()
```

## 💡 Why Use This Approach?

✔️ Cleaner and more structured code  
✔️ Easily extendable – Just add new functions to the dictionary  
✔️ Faster execution – Eliminates redundant checks  
✔️ Organized exit handling – More elegant termination of the program  

## 🚀 Key Takeaways

📌 The If-Else method works but gets cluttered with multiple conditions.  
📌 A Dictionary-Based approach makes the code neater, scalable, and efficient.  
📌 Using `menu_actions.get(choice, invalid_option)()` streamlines function execution.  
📌 Structured exit handling makes for better readability and maintainability.  

This project lays the foundation for advanced file management automation. Future expansions could include bulk operations, automatic backups, or cloud integration! 🌍

🔗 **Check out my LinkedIn post for more details:** [LinkedIn Post](https://www.linkedin.com/posts/sai-shivani-k_python-filemanagement-coding-activity-7297920461626056704-a9nd?utm_source=share&utm_medium=member_desktop&rcm=ACoAADrojogBVw8NklMaB5iloGRPM4w30qqai80)

