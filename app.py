from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Predefined lyric templates with username and Under25
LYRIC_TEMPLATES = [
    "Under the {keyword} sky, we dance so free,\nA melody of love, just you and me.\nSung by e/kashi55, Under25 vibes in the air.",
    "Walking through the {keyword} rain,\nMemories wash away my pain.\nWith e/kashi55's song, Under25 keeps me strong.",
    "The {keyword} moon shines bright above,\nWhispering tales of endless love.\nLyrics of e/kashi55, Under25 in every line.",
    "Riding the {keyword} waves at dawn,\nSinging a tune that carries on.\nUnder25 echoes, e/kashi55 leads the song."
]

@app.route("/")
def index():
    return render_template("lyrics_generator_bot.html")  # ✅ Match the actual file name


@app.route("/generate_lyrics", methods=["POST"])
def generate_lyrics():
    data = request.get_json()
    keyword = data.get("keywords", "dream")  # Default if no keyword is given

    # Pick a random template and replace {keyword}
    chosen_template = random.choice(LYRIC_TEMPLATES)
    generated_lyrics = chosen_template.replace("{keyword}", keyword)

    return jsonify({"lyrics": generated_lyrics})

if __name__ == "__main__":
    app.run(debug=True)
