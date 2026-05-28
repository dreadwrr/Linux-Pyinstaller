Version 6.0.0 of pyinstaller posted above tested on nemesis will test on porteus and update if finding anything

## Pyinstaller Linux qt recentchanges <br>
chown guest:users /usr/local/recentchanges <br>
cd /usr/local/recentchanges <br>
python -m venv .venv <br>
source .venv/bin/activate <br>
python -m pip install --upgrade pip <br>
pip install -r requirements.txt <br>
pip install pyinstaller <br>
python3 -m PyInstaller --clean --noconfirm main.spec <br><br>
if there is an error about webengine add to main.spec <br>
    excludes=[ <br>
        'tkinter', <br>
        'PySide6.QtWebEngine', <br>
        'PySide6.QtWebEngineWidgets', <br>
        'PySide6.QtWebEngineCore', <br>
        'PySide6.QtMultimedia', <br>
        'PySide6.QtCharts', <br>
        'PySide6.QtPrintSupport', <br>
	], <br>
<br>
copy main and _internal from dist/main folder to /usr/local/recentchanges ./main <br>
chown root:root main <br>
chown root:root /usr/local/recentchanges <br>

optionally remove src/ and main.py as well into an .xzm <br><br>

![Alt text](https://i.imgur.com/xK10DuX.png) <br>
![Alt text](https://i.imgur.com/3dXwKzW.png)<br><br>
