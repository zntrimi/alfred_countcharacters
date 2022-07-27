Download Workflow [here](https://github.com/zntrimi/alfred_countcharacters/releases/download/v0.1/Count.characters.alfredworkflow)

# Alfred Character Counter
Japanese follows
文字数を数えるAlfred Workflowです。
任意のキーワード(デフォルトはcount)でtriggerし、好きな文章をペーストしてください。Returnで文字数がLarge Textで表示されます。

## How it works

Alfred Workflowでは任意の値を引数として任意のスクリプトを実行出来ます。今回はPython3で実行しています。

`sys.argv`で引数を受け取ってqueryとして`ys.stdout.write`で出力します。

