Socket Testing
==============

This document provides information on how to test socket connections using Flask-SocketIO and Plotly.

.. contents::
   :local:

Overview
--------

This module demonstrates how to use Flask-SocketIO to update a Plotly chart in real-time.

Code
------------

.. literalinclude:: ../sockettesting.py
   :language: python
   :linenos:

Usage
-----

1. Run the Flask application.
2. Open the web page in a browser.
3. Click the "Update Chart" button to emit a socket event and update the chart with random data.

Dependencies
------------

- Flask
- Flask-SocketIO
- FlaskWebGui
- Plotly
- Socket.IO

Developer Notes
---------------

- The version of flaskwebgui (0.3.7) used is very important, later versions remove some critical options (close_server_on_exit and idle_interval)
    - We also modify the installation to use allow_unsafe_werkzeug=True in the socketio.run call, which is also necessary. We may want to consider forking the package for this reason.
    - We can modify the flaskwebgui code to allow logging to file to help debug some cryptic errors
- pyinstaller.py can be run to package the app for windows
- KillSocketTesting.bat can be used to kill an existing exe
- sys.stdout and sys.stderr need to be mocked because pyinstaller removes them, and the server can crash without them
