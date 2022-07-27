Download Workflow here

# Alfred Character Counter

文字数を数えるAlfred Workflowです。
任意のキーワード(デフォルトはcount)でtriggerし、好きな文章をペーストしてください。Returnで文字数がLarge Textで表示されます。

## How it works

Alfred Workflowでは任意の値を引数として任意のスクリプトを実行出来ます。今回はPython3で実行しています。

`sys.argv`で引数を受け取ってqueryとして`ys.stdout.write`で出力します。

