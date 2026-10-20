from flask import Flask, request, render_template_string

app = Flask(__name__)

WHATSAPP_LINK = "https://chat.whatapp.com/IvawQ07zuXp2zJddqcFZq?s=cl&p=a&p=a&mlu=4&ilr=4"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Smart Class Verification</title>
</head>
<body style="text-align:center; font-family:Arial; margin-top:80px;">

    <h1>🎓 Smart Class Verification</h1>
    <p>Enter your index number to check eligibility.</p>

    <form method="POST">
        <input
            type="number"
            name="index_number"
            placeholder="Index number"
            required
        >
        <button type="submit">Check Eligibility</button>
    </form>

    {% if message %}
        <h3>{{ message }}</h3>
    {% endif %}

    {% if eligible %}
        <a href="{{ whatsapp_link }}" target="_blank">
            <button>Join WhatsApp Group 📱</button>
        </a>
    {% endif %}

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    eligible = False

    if request.method == "POST":
        try:
            index_number = int(request.form["index_number"])

            if 5260170200 <= index_number <= 5260170300:
                message = "Congratulations! Your index number is eligible."
                eligible = True
            else:
                message = "Sorry, your index number is outside our range."

        except ValueError:
            message = "Please enter a valid index number."

    return render_template_string(
        HTML,
        message=message,
        eligible=eligible,
        whatsapp_link="https://chat.whatapp.com/IvawQ07zuXp2zJddqcFZq?s=cl&p=a&p=a&mlu=4&ilr=4"
    )

if __name__ == "__main__":
    app.run(debug=True)