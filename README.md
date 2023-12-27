# FLASK-UNOCONV

Using Unoconv with Flask to create a microservice that convert a file from PowerPoint (*.pptx) to PDF.

# HOW TO USE

- Project developed and tested on Ubuntu Linux
- Install Python 3.10 or compatible version
- Install the dependencies in the environment ```pip install -r requirements.txt```
- Install *unoconv* and *libreoffice* on your environment
- If needed copy unohelper.py and uno.py to your environment:
    ``` cp /usr/lib/python3/dist-packages/unohelper.py venv/lib/python3.10/site-packages/ ```
    ``` cp /usr/lib/python3/dist-packages/uno.py venv/lib/python3.10/site-packages/```

# WARN

*This project is a simple validation and usage of the Unoconv via Python, please do the needed improvements.*