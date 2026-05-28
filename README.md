## Pyinstaller Linux qt recentchanges <br>
in preparing to build <br>

to reduce the final size comment out line 8 and 9 in main.spec <br>
#tmp_ret = collect_all('PySide6') <br>
#datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2] <br><br>
check owner of app install: chown guest:users /usr/local/recentchanges <br>

cd /usr/local/recentchanges <br>
python -m venv .venv <br>
source .venv/bin/activate <br>
python -m pip install --upgrade pip <br>
pip install -r requirements.txt <br>
pip install pyinstaller <br>
python3 -m PyInstaller --clean --noconfirm main.spec <br><br>
deactivate

if there is an error about webengine add to main.spec <br>
    excludes=[
    'tkinter',
    'PySide6.QtWebEngine',
    'PySide6.QtWebEngineWidgets',
    'PySide6.QtWebEngineCore',
    'PySide6.QtNetworkAuth',
    'PySide6.QtQml',
    'PySide6.QtMultimedia',
    'PySide6.QtCharts',
    'PySide6.QtPrintSupport',
    ], <br>
<br>
copy main and _internal from dist/main folder to /usr/local/recentchanges ./main <br>
chown root:root main <br>
chown root:root /usr/local/recentchanges <br>

optionally remove src/ and main.py or make into .xzm <br><br>


will later take steps to reduce size later on but this doesnt appear to be needed
/usr/local/recentchanges/internal_/libicudata.so.77 31 mb

![Alt text](https://i.imgur.com/xK10DuX.png) <br>
![Alt text](https://i.imgur.com/3dXwKzW.png)<br><br>
