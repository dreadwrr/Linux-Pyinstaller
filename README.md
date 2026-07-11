07/11/2026 <br>
repo is 6.2.0 testing pyinstall before releasing <br><br>

first check app install is owned by guest: chown guest:users /usr/local/recentchanges <br>
## Pyinstaller Linux qt recentchanges <br><br>

cd /usr/local/recentchanges <br>
python -m venv .venv <br>
source .venv/bin/activate <br>
python -m pip install --upgrade pip <br>
pip install -r requirements.txt <br>
pip install pyinstaller <br>
python3 -m PyInstaller --clean --noconfirm main.spec <br>
deactivate <br><br>


if there is an error about webengine add to main.spec <br>
    excludes=[ <br>
    'tkinter', <br>
    'PySide6.QtWebEngine', <br>
    'PySide6.QtWebEngineWidgets', <br>
    'PySide6.QtWebEngineCore', <br>
    'PySide6.QtNetwork', <br>
    'PySide6.QtQml', <br>
    'PySide6.QtCharts', <br>
    'PySide6.QtPrintSupport', <br>
    ], <br>
<br>
copy main and _internal from dist/main folder to /usr/local/recentchanges <br>
chown root:root main <br>
chown root:root /usr/local/recentchanges <br>

optionally remove src/ and main.py or make into .xzm <br><br>

## Adjust size
if wanting to reduce some size <br>
replace line 5 <br> 
datas = [('Resources', 'Resources')] <br>
with data = [] <br><br>
comment out line 8 and 9 in main.spec <br>
#tmp_ret = collect_all('PySide6') <br>
#datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2] <br><br>


will later take steps to reduce size but these dont appear to be needed: <br><br>
run with excludes above to remove size further. Qml and WebEngine taking size <br><br> 
and to reduce further remove a few libraries<br><br>
/usr/local/recentchanges/internal_/libicudata.so.77 31 mb <br>
/usr/local/recentchanges/internal_/libcrypto.so.3 6 mb <br>
/usr/local/recentchanges/dist/main/_internal/libQt6Network.so.6 symlink<br>
/usr/local/recentchanges/dist/main/_internal/PySide6/Qt/lib/libQt6Network.so.6 2.1 mb <br>

remove folder /usr/local/recentchanges/dist/main/_internal/PySide6/Qt/translations/ 13.6mb <br>
try with setting strip=True 

## Nuitka
Requires python <= 3.12.11. 3.13 doesnt work <br>
Found a suitable build and looks promising as the compressed size is 53mb and is compiled to c

get patchelf-0.14.3 from pkgs.org <br>
activate patchelf

from venv

pip install nuitka <br>
pip install zstandard


``` python -m nuitka --onefile --output-filename=main --onefile-tempdir-spec="{TEMP}/onefile_$$_118624_YD1fmvHJ_Qc" --remove-output --enable-plugin='pyside6' --noinclude-qt-plugins=printsupport --include-qt-plugins=sensible,platforms,sqldrivers,multimedia --jobs=4 main.py ```

remove main.build and main.dist



![Alt text](https://i.imgur.com/xK10DuX.png) <br>
![Alt text](https://i.imgur.com/3dXwKzW.png)<br><br>
