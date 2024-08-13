from flask import Flask

from ..shared import score_config

score_website: Flask = Flask(__name__)


@score_website.route("/")
def main_page() -> str:
    # try to parse score. if passes, display score on web page, of not, display erroron web page.
    try:
        with open(score_config.SCORE_FILE_NAME, encoding="UTF-8") as scores_file:
            score: str = scores_file.read()
            int(score)

            return f"""
<html>
    <head>
        <title> Scores Game</title>
    </head>s
    <body>
        <h1>The score is:</h1>
        <div id="score">{score}</dev>
    </body>
</html>"""
    except (ValueError, FileNotFoundError):
        return f"""
<html>
    <head>
        <title>Scores Game</title>
    </head>
    <body>
        <h1>ERROR:</h1>
        <div id="score" style="color:red">{score_config.BAD_RETURN_CODE}</div>
    </body>
</html>"""


score_website.run("0.0.0.0")
