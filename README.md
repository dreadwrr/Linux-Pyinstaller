## Pyinstaller Linux qt recentchanges <br><br>

New update as some changes had to be made to make it fully independent. This includes <br>
having the file filter which was filter.py in a toml file. filter.toml. Also an update to <br>
the launcher script so commandline runs off executable.<br><br>

cd /usr/local/recentchanges <br>
python -m venv .venv <br>
source .venv/bin/activate <br>
python -m pip install --upgrade pip <br>
pip install -r requirements.txt <br>
pip install pyinstaller <br>
pyinstaller --onedir main.py --collect-all=libshiboken <br>
copy main and _internal from dist/main folder to /usr/local/recentchanges ./main <br>
chown root:root main <br>
chown root:root /usr/local/recentchanges <br>

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
repeat pyinstall from above <br>
