from flask import Flask, render_template_string, redirect

app = Flask(__name__)

# ファイル情報（Google Drive 直接ダウンロードリンク + アイコン指定）
files = [
    {
        "name": "Fnf Ryouse1 Engine 1.0 Linux.zip",
        "url": "https://drive.google.com/uc?export=download&id=14uRL7YQ3e0h6OiBwrDzVpvOoCpoUHoV1",
        "icon": "linux.JPG"
    },
    {
        "name": "Fnf Ryouse1 Engine 1.0 macOS.app",
        "url": "https://drive.google.com/uc?export=download&id=1lhIoQY_GW-hFkQ0_OM5_lU4CysL7iIwX",
        "icon": "macos.PNG"
    },
    {
        "name": "Fnf Ryouse1 Engine 1.0 windows.exe",
        "url": "https://drive.google.com/uc?export=download&id=1dUhyTDyhWSzrsXCZ5qVwDCHsLJ2rT4B7",
        "icon": "windows.PNG"
    },
    {
        "name": "Fnf Ryouse1 Engine 1.0.sb3",
        "url": "https://drive.google.com/uc?export=download&id=1TJHboBty14ZZvxKxreDPUXmcHvCGlFwb",
        "icon": "generic.PNG"
    }
]

@app.route("/")
def index():
    file_cards = ''
    for f in files:
        file_cards += f'''
        <div class="file-card">
            <img src="/static/icons/{f["icon"]}" alt="icon" class="file-icon">
            <div class="file-info">
                <div class="file-name">{f["name"]}</div>
            </div>
            <a class="download-btn" href="/files/{f["name"]}">Download</a>
        </div>
        '''
    return render_template_string(f'''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>Fnf Ryouse1 Engine ダウンロード</title>
<style>
body {{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: #f4f6f8;
    margin: 0;
    padding: 20px;
}}
h1 {{
    text-align: center;
    color: #333;
}}
.file-card {{
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    padding: 15px;
    margin: 15px auto;
    max-width: 600px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}}
.file-icon {{
    width: 40px;
    height: 40px;
    margin-right: 15px;
}}
.file-info {{
    flex-grow: 1;
}}
.file-name {{
    font-weight: bold;
    font-size: 16px;
    color: #444;
}}
.download-btn {{
    background: #007bff;
    color: #fff;
    text-decoration: none;
    padding: 8px 15px;
    border-radius: 5px;
    transition: 0.3s;
}}
.download-btn:hover {{
    background: #0056b3;
}}
@media (max-width: 600px) {{
    .file-card {{
        flex-direction: column;
        align-items: flex-start;
    }}
    .download-btn {{
        margin-top: 10px;
        width: 100%;
        text-align: center;
    }}
    .file-icon {{
        margin-bottom: 10px;
    }}
}}
</style>
</head>
<body>
<h1>Fnf Ryouse1 Engine ダウンロード</h1>
{file_cards}
</body>
</html>
''')

@app.route("/files/<filename>")
def download(filename):
    file = next((f for f in files if f["name"] == filename), None)
    if file:
        return redirect(file["url"])
    return "File not found", 404

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
