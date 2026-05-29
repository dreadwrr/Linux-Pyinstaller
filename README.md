## Pyinstaller Linux qt recentchanges <br>
chown guest:users /usr/local/recentchanges <br>
to reduce the final size comment out line 8 and 9 in main.spec <br>
#tmp_ret = collect_all('PySide6') <br>
#datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2] <br><br>

```
cd /usr/local/recentchanges
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller
python3 -m PyInstaller --clean --noconfirm main.spec

deactivate
```

if there is an error about webengine add to main.spec <br>
    excludes=[ <br>
    'tkinter', <br>
    'PySide6.QtWebEngine', <br>
    'PySide6.QtWebEngineWidgets', <br>
    'PySide6.QtWebEngineCore', <br>
    'PySide6.QtNetwork', <br>
    'PySide6.QtQml', <br>
    'PySide6.QtMultimedia', <br>
    'PySide6.QtCharts', <br>
    'PySide6.QtPrintSupport', <br>
    ], <br>
<br>
copy main and _internal from dist/main folder to /usr/local/recentchanges <br>
chown root:root main <br>
chown root:root /usr/local/recentchanges <br>

optionally remove src/ and main.py or make into .xzm <br><br>

##
will later take steps to reduce size but these dont appear to be needed: <br><br>
run with excludes above to remove size further. Qml and WebEngine taking size <br><br> 
and to reduce further<br><br>
/usr/local/recentchanges/internal_/libicudata.so.77 31 mb <br>
/usr/local/recentchanges/internal_/libcrypto.so.3 6 mb <br>
/usr/local/recentchanges/dist/main/_internal/libQt6Network.so.6 <br>
/usr/local/recentchanges/dist/main/_internal/PySide6/Qt/lib/libQt6Network.so.6 2.1 mb <br>

remove folder /usr/local/recentchanges/dist/main/_internal/PySide6/Qt/translations/ 13.6mb <br>
try setting strip=True 

## Nuitka

I found a suitable build but I have to update the pyinstaller module to use the nuitka internal extracted location will post once complete

get patchelf-0.14.3 from pkgs.org <br>
activate patchelf

pip install nuitka
pip install zstandard


``` python -m nuitka --onefile --output-filename=main --onefile-tempdir-spec="/tmp/onefile_$$_118624_YD1fmvHJ_Qc" --product-name=main --remove-output --enable-plugin='pyside6' --noinclude-qt-plugins=printsupport --include-qt-plugins=sensible,platforms,sqldrivers --jobs=4 main.py ```



![Alt text](https://i.imgur.com/xK10DuX.png) <br>
![Alt text](https://i.imgur.com/3dXwKzW.png)<br><br>
