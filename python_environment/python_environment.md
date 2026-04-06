⏺ Python Environment

A Python environment is the combination of:
- A Python interpreter (the executable that runs .py files) It translates your .py files into machine instructions the CPU  
  can run.
- Installed packages/libraries (e.g., numpy, requests)
- Environment variables and system paths

By default, packages install globally — shared across all projects on your machine.

Virtual Environment

A virtual environment is an isolated, self-contained Python environment for a specific project. It has its own:
- Python interpreter copy/symlink
- pip and installed packages
- site-packages directory

This means project A can use requests==2.28 while project B uses requests==2.31 without conflict.

Creating one

# Create
python -m venv .venv

# Activate (macOS/Linux)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate

# Install packages (now isolated)
pip install requests

# Deactivate
deactivate

Why use virtual environments?

┌───────────────────────────────────────┬─────────────────────────────────────┐
│                Problem                │              Solution               │
├───────────────────────────────────────┼─────────────────────────────────────┤                                                                 
│ Dependency conflicts between projects │ Each project has its own packages   │
├───────────────────────────────────────┼─────────────────────────────────────┤                                                                 
│ "Works on my machine" issues          │ Lock versions with requirements.txt │
├───────────────────────────────────────┼─────────────────────────────────────┤                                                                 
│ Global environment pollution          │ Installs stay contained             │
└───────────────────────────────────────┴─────────────────────────────────────┘

Common tools

- venv — built into Python 3.3+ (standard choice)
- virtualenv — third-party, more features
- conda — manages both Python version and packages (popular in data science)
- poetry / uv — modern tools that manage venvs automatically    


---

`Environment variables` are key-value pairs stored by the OS, available to all running processes.

* export MY_VAR="hello"     # set a variable
* echo $MY_VAR              # read it                                                                                                             
* env                       # list all 

Common Python-relevant ones

┌─────────────┬─────────────────────────────────────────────────────┐                                                                           
│  Variable   │                       Purpose                       │
├─────────────┼─────────────────────────────────────────────────────┤
│ PATH        │ Directories the OS searches when you type a command │
├─────────────┼─────────────────────────────────────────────────────┤
│ PYTHONPATH  │ Extra directories Python searches for modules       │
├─────────────┼─────────────────────────────────────────────────────┤                                                                           
│ VIRTUAL_ENV │ Set automatically when a venv is active             │
├─────────────┼─────────────────────────────────────────────────────┤                                                                           
│ HOME        │ Your home directory                                 │
└─────────────┴─────────────────────────────────────────────────────┘    

##### System PATH

`PATH` is a list of directories separated by `:` (Mac/Linux) or `;` (Windows):

`/usr/local/bin:/usr/bin:/usr/sbin:/bin`

When you type `python`, the OS walks this list left-to-right and runs the first python it finds. `That's why activating a venv works — it prepends
.venv/bin to your PATH, so .venv/bin/python is found first. `