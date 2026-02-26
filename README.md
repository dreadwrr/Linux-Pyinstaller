# Pyinstaller Linux qt <br><br>
cd /usr/local/recentchanges <br>
chown guest:users /usr/local/recentchanges <br>
python -m venv .venv <br>
source .venv/bin/activate <br>
python -m pip install --upgrade pi <br>
pip install -r requirements.txt <br>
pip install pyinstaller <br>
pyinstaller --onedir main.py --collect-all=libshiboken <br>
copy main and _internal from dist/main folder to /usr/local/recentchanges ./main <br> 
optionally remove src/ and main.py <br><br>

compatibility if the above fails again from the venv<br>
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
