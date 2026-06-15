@echo off
setlocal enabledelayedexpansion

REM ===========================================
REM  Rockin'on アーティスト一覧抽出バッチ
REM  出力: artist_list_from_rockinon.txt
REM  作者: ChatGPT
REM ===========================================

echo.
echo [1/3] Rockin'on アーティスト一覧を取得しています...
powershell -Command "(Invoke-WebRequest -Uri 'https://rockinon.com/artist/list' -UseBasicParsing).Content" > rockinon_raw.html

if not exist rockinon_raw.html (
    echo 取得に失敗しました。ネット接続やURLを確認してください。
    pause
    exit /b
)

echo [2/3] HTMLからアーティスト名を抽出しています...

REM 出力ファイル初期化
> artist_list_from_rockinon.txt echo.

for /f "usebackq delims=" %%A in (`findstr /r /c:"/artist/" rockinon_raw.html`) do (
    set "line=%%A"
    REM タグからテキスト部分だけ抜き出す
    for /f "tokens=2 delims=>^<" %%B in ("!line!") do (
        set "text=%%B"

        REM HTML特殊文字をPowerShellで除去
        for /f "usebackq delims=" %%C in (`powershell -Command "[System.Net.WebUtility]::HtmlDecode('%text%')"`) do (
            set "decoded=%%C"
        )

        REM 日本語または英数字を含む行だけを対象
        echo !decoded!| findstr /r "[A-Za-z0-9一-龠ぁ-んァ-ヶ]" >nul
        if !errorlevel! == 0 (
            REM 余計な空白を削除
            set "decoded=!decoded:　=!"
            set "decoded=!decoded: =!"
            if not "!decoded!"=="" (
                echo !decoded!>> artist_list_from_rockinon.txt
            )
        )
    )
)

echo [3/3] 整形が完了しました。
echo 出力ファイル: artist_list_from_rockinon.txt
echo.
echo 作成されたファイルを開いてご確認ください。
pause
