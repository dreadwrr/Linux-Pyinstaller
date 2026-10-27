
first check app install is owned by guest: chown guest:users /usr/local/recentchanges <br>

As well ensure in clean environment recommend using always fresh mode. This is to avoid conflicts <br>
with pyinstaller failing to build <br>

## Pyinstaller Linux qt recentchanges <br><br>

cd /usr/local/recentchanges <br>
python -m venv .venv <br>
source .venv/bin/activate <br>
python -m pip install --upgrade pip <br>
pip install -r requirements.txt <br>
pip install pyinstaller <br>

if not using the pyinstaller main.spec python3 -m PyInstaller --onedir --clean --strip main.py <br>
otherwise with the pyinstaller one: python3 -m PyInstaller --clean --noconfirm main.spec <br>

deactivate <br><br>

copy main and _internal from dist/main folder to /usr/local/recentchanges <br>
chown root:root main <br>
chown root:root /usr/local/recentchanges <br>

optionally remove src/ and main.py or make into .xzm <br><br>

## Adjust size
if wanting to reduce some size <br>

to reduce further remove a few libraries<br><br>
/usr/local/recentchanges/internal_/libicudata.so.77 31 mb <br>
/usr/local/recentchanges/internal_/libcrypto.so.3 6 mb <br>
/usr/local/recentchanges/dist/main/_internal/PySide6/Qt/lib/libQt6Quick.so.6 7.9mb <br>
/usr/local/recentchanges/dist/main/_internal/PySide6/Qt/lib/libQt6Qml.so.6 6.6mb <br>
/usr/local/recentchanges/dist/main/_internal/PySide6/Qt/lib/libQt6Pdf.so.6 5.5mb <br>

remove folder /usr/local/recentchanges/dist/main/_internal/PySide6/Qt/translations/ 13.6mb <br>

After removing and strip the final size was 203mb <br>

## Nuitka
Requires python <= 3.12.11. 3.13 doesnt work <br>
so the following was done on porteus alpha 3 <br><br>
Found a suitable build and looks promising as the compressed size is 53mb and is compiled to c

get patchelf-0.14.3 from pkgs.org <br>
activate patchelf

from venv

pip install nuitka <br>
pip install zstandard


``` python -m nuitka --onefile --output-filename=main --onefile-tempdir-spec="{TEMP}/onefile_$$_118624_YD1fmvHJ_Qc" --remove-output --enable-plugin='pyside6' --noinclude-qt-plugins=printsupport --include-qt-plugins=sensible,platforms,sqldrivers,multimedia --jobs=4 main.py ```

remove main.build and main.dist

There is an alternative to using onefile above --standalone which would put the output into main.dist folder. However it is not as organized as pyinstaller onedir. This can be overcome with adding a symlink in app install to main.dist.

first ln 3652 in main.py add another .parent as well as configfunctions.py ln 18 add another .parent. <br><br>

```
nuitka main.py --mode=standalone --output-filename=main --enable-plugin='pyside6' --remove-output --include-qt-plugins=sqldrivers,multimedia
```
create a symlink to the executable in app install in terminal: <br>
ln -s ./main.dist/main main <br><br>


![Alt text](https://i.imgur.com/xK10DuX.png) <br>
![Alt text](https://i.imgur.com/3dXwKzW.png)<br><br>
![Alt text](https://i.imgur.com/9A2sa7v.png)
