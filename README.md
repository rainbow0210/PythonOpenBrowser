# PythonOpenBrowser

# 日本語

### 概要
`OpenBrowser.py` は、ローカルに簡易HTTPサーバーを起動し、既定のブラウザで `index.html` を自動的に開くためのシンプルなPythonスクリプトです。静的ファイルの確認やローカル開発時の簡易プレビューに適しています。デフォルトのポートは8000です。

### 使用技術
- 言語: Python（標準ライブラリ）
- ライブラリ/フレームワーク: `http.server`, `socketserver`, `webbrowser`

### 使い方
#### 前提条件
- Python 3 がインストールされていること。
- 作業ディレクトリに表示したい `index.html`（または静的ファイル群）が存在すること。

#### インストール方法
```bash
git clone https://github.com/username/PythonOpenBrowser.git
cd PythonOpenBrowser
```

#### 基本的な使い方
```bash
python OpenBrowser.py
```

### 主な機能
- ローカルにHTTPサーバーを立て、既定のブラウザで `index.html` を開く。

### 設定
- ポート番号はスクリプト内の `PORT` 変数で変更可能（デフォルト: 8000）。
- 必要に応じて `index.html` を追加してください。

# English

### Overview
`OpenBrowser.py` is a simple Python script that starts a local HTTP server and automatically opens `index.html` in the default web browser. It is intended for quick previews of static files during local development. The default port is 8000.

### Tech stack
- Language: Python (standard library)
- Libraries: `http.server`, `socketserver`, `webbrowser`

### Usage
#### Prerequisites
- Python 3 installed.
- An `index.html` (or other static files) present in the working directory.

#### Install
```bash
git clone https://github.com/username/PythonOpenBrowser.git
cd PythonOpenBrowser
```

#### Basic usage
```bash
python OpenBrowser.py
```

### Main features
- Starts a local HTTP server and opens `index.html` in the default browser automatically.

### Configuration
- Change the port by editing the `PORT` variable inside `OpenBrowser.py` (default: 8000).
- Add `index.html` as needed for content to display.