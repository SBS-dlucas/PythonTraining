# PythonTraining
A repo for testing and training skills

## Sockettesting notes
- The version of flaskwebgui (0.3.7) used is very important, later versions remove some critical options (close_server_on_exit and idle_interval)
- We also modify the installation to use allow_unsafe_werkzeug=True in the socketio.run call, which is also necessary. We may want to consider forking the package for this reason.
- We can modify the flaskwebgui code to allow logging to file to help debug some cryptic errors
- pyinstaller.py can be run to package the app for windows
