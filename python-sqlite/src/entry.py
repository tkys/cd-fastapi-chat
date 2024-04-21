from js import Response

import sqlite3

# データベースに接続
#con = sqlite3.connect(':memory:')

# 拡張機能のロードを有効化
#con.enable_load_extension(True)

# 拡張機能を保持する辞書
#loaded_extensions = {}

def load_extension(path):
    try:
        con.load_extension(path)
        loaded_extensions[path] = "enabled"
        print(f"Extension {path} loaded successfully.")
    except sqlite3.DatabaseError as e:
        print(f"Failed to load extension {path}: {e}")

def list_extensions():
    for ext, status in loaded_extensions.items():
        print(f"Extension {ext}: {status}")

# 拡張機能をロードする例（実際のパスを適宜変更してください）
#load_extension('mod_spatialite')

# 拡張機能のリストを表示
#list_extensions()

# 拡張機能のロードを無効化（セキュリティ上の理由

def creat_fts(con):
    query = f"""
    CREATE VIRTUAL TABLE trigram_fts USING fts5(text, tokenize='trigram');
    """
    cur = con.cursor()
    result = cur.execute(query,)
    return result

def insert_fts(con):
    query = f"""
    INSERT INTO trigram_fts( text ) VALUES ('実務者の為の開発改善ガイドブック');
    """
    cur = con.cursor()
    result = cur.execute(query,)
    return result

def select_fts(con):
    query = f"""
    SELECT * FROM trigram_fts WHERE trigram_fts MATCH ('ガイド');
    """
    cur = con.cursor()
    result = cur.execute(query,).fetchall()
    return result

async def on_fetch(request, env):
    # データベースに接続
    con = sqlite3.connect(':memory:')
    
    creat_fts(con)
    insert_fts(con)
    
    return Response.new(select_fts(con))
