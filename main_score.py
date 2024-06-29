from flask import Flask
import utils


score_website: Flask = Flask(__name__)


@score_website.route('/')
def main_page() -> str:
    with open(utils.scores_file_name) as scores_file:
        score: str = scores_file.read()

        # try to parse score. if passes, display score on web page, of not, display erroron web page.
        try:
            int(score)
            return f'''
<html>
    <head>
        <title> Scores Game</title>
    </head>
    <body>
        <h1>The score is:</h1>
        <div id="score">{score}</dev>
    </body>
</html>'''
        except ValueError as error:
            return f'''
<html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <h1>ERROR :< /h1>
        <div id="score" style="color:red">{error}</div>
    </body>
</html>'''
