## Pyinstaller Linux qt recentchanges <br><br>
Added thread and queue for logging system and progress reporting. The last worker wont stall progress and <br>
speeds up execution <br>
New hash collision method which is optimized for accuracy and speed <br>
Changes to gpg key creation and reset logic <br>
New update for launcher script to use the binary for commandline. This included <br>
having the file filter which was filter.py in a toml file. filter.toml. <br><br>

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
chown root:root *.py <br>
chown root:root -R scripts <br>
chown root:root /usr/local/recentchanges <br>

optionally remove src/ and main.py <br><br>
