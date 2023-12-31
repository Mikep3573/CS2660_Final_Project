"""
Launch Flask App
Michael Piscione
CS 2660/Fall 2023

This constitutes the 'main' function. Use this to launch the flask app.

NOTE: Same launcher as used in bank labs with minor changes.
"""

# Dependencies
import traceback
from database_funcs import *
from app import app


def main():
    """ Creating a main for aesthetic purposes. """
    try:
        # Attempt to create users table and signal to run app
        if create_db():
            # Run the Flask app using localhost, port 8097 (temporary port)
            app.run(debug=True, host='localhost', port=8097)
    except Exception:  # Print any errors that occur on launch
        traceback.print_exc()


if __name__ == '__main__':
    main()
