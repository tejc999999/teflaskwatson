# -*- coding: utf-8 -*-
# 起動コマンド(Windows)
# Flaskアプリケーションのエントリポイント（公開時は使用せず）
# set FLASK_APP=flaskr
# 動作環境
# set FLASK_ENV=development
# flask run
from flask import Flask
import os
import watson

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(watson.bp)

## アプリケーション作成
#def create_app():
#    # Flaskアプリケーションインスタンス作成
#    # __name__:現在のPythonモジュール名
#    # insntace_relative_config=True:設定ファイルがインスタンスフォルダに関連(インスタンスフォルダから相対的にファイル参照)
#    app = Flask(__name__, instance_relative_config=True)
#    
#    import watson
#    app.register_blueprint(watson.bp)
#    # app.add_url_rule('/', endpoint='index')
#    
#    return app
#    
#port = int(os.getenv('PORT', 5000))
#if __name__ == '__main__':
#	app = create_app()
#    # debug=True:デバッグ機能有効（ログ出力等）
#    # host='0.0.0.0':ローカルマシン以外のアプリ接続を許可
#	app.run(host='0.0.0.0', port=port, debug=True)
