"Score website showing the score from a text file"
from flask import Flask

SCORE_FILE_NAME: str = "Score.txt"
BAD_RETURN_CODE: int = 500

score_website: Flask = Flask(__name__)


@score_website.route("/")
def main_page() -> str:
    """
    Reads score from a text file and displays it on a web page.
    Shows an error page is fais to read file
    """
    # try to parse score. if passes, display score on web page, of not, display erroron web page.
    try:
        with open(SCORE_FILE_NAME, encoding="UTF-8") as scores_file:
            score: str = scores_file.read()
            int(score)

            return f"""
<html>
    <head>
        <title>Scores Game</title>
    </head>
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
        <div id="score" style="color:red">{BAD_RETURN_CODE}</div>
    </body>
</html>"""


score_website.run("0.0.0.0")
