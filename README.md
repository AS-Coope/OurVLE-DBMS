# OurVLE-DBMS

This is the DBMS All Stars Group's Project to create a course management system.

How to run this program:

This is done by first creating a virtual environment, installing the required dependencies and then running the program.

In the command line, run the following commands:

1. Start by activating the environment.
Using python:

```bash
python -m venv venv 
```

OR

Using python3:

```bash
python3 -m venv venv 
```

2. Now we activate the environment

```bash
source venv/bin/activate
```

OR

If using Windows:

```bash
source .\venv\Scripts\activate
```

3. Next, we install all of our dependencies from our requirements file

```bash
pip install -r requirements.txt
```

4. Finally, we run our program.

```bash
flask --app app --debug run
```

