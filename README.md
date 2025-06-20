
📝 Task List Manager (Python CLI)

This is a simple command-line task manager built in Python. It allows you to:

✅ View your task list
➕ Add a new task
✏️ Update a task by its index
❌ Remove a task by its index
⏳ Includes short delays for a better user experience
📦 Requirements

  Python 3.x

  No external libraries needed (only time module)

🚀 How It Works

  The program starts by showing a default task list.

  You can add a new task.

  Update a task using its index.

  Delete a task using its index.

  The program uses time.sleep() to add smooth pauses between actions for a more interactive experience.

  At the end, it shows your final updated task list and a motivational message.

______________________________________________________________________________________________________________________________________________________________

  📸 Sample Output

------------------------------
your task list

wakeup
------------------------------
clean your face
------------------------------
drink coffee
------------------------------

add your new task >>> study python

updated list

wakeup
------------------------------
clean your face
------------------------------
drink coffee
------------------------------
study python
------------------------------

which index do you want to update? >>> 2
enter your new task >>> brush teeth

updated list

wakeup
------------------------------
brush teeth
------------------------------
drink coffee
------------------------------
study python
------------------------------

enter the index of the task to remove >>> 3

final list

wakeup
------------------------------
brush teeth
------------------------------
study python
------------------------------
enjoy for your day, always im here to help you
