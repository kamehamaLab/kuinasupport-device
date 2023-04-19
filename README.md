# kuinasupport
[Google Cloud Platform](https://console.cloud.google.com/getting-started)

## 初期設定
GCPにログインして接続用のJsonファイルをダウロードし、フォルダ直下に置く。

現在（2023/04/14）時点でブラウザを介したドライブ初期接続認証を使用しているため、CUIのみの認証ができない。そのため、直下に置くファイルが別のPCなどで生成したtoken.jsonを使用すること。

~~~bash
sudo apt update 
sudo apt upgrade
sudo pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib oauth2client
sudo pip3 install pyaudio
sudo apt install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
python startUp.py
~~~


## pythonでの実装のときに参考にしたURL
[PythonでGoogleDriveAPIを使ってGoogle Driveにファイルを定期的にアップロードする](https://qiita.com/munaita_/items/d03b67b74868c3e4fb2d)  
[mimeTypeの参考元](https://www.tagindex.com/html5/basic/mimetype.html)  
[Google Drive API Delete Python](https://stackoverflow.com/questions/54131041/google-drive-api-delete-python)  
[Google Drive for developers Delete ](https://developers.google.com/drive/api/v2/reference/files/delete)
[Python:GoogleDriveAPIの基本的な使い方](https://zenn.dev/wtkn25/articles/python-googledriveapi-operation)


## 注意事項 
- 認証ファイルはgitには載せない
- トークンの期限が切れないようにプロジェクトを本番環境にしないといけない。
- 音声データは全てwavだと想定してコードが書かれている。もしべつの拡張子を使う場合はGoogleDrivefunc.py内のmimetypeを変更しないといけない。
- 動作させるときはnohupコマンドでバックグラウンドで動かす

