import time
import webbrowser
import requests
from flask import Flask, request, render_template_string
import threading

# === hCaptcha keys ===
HCAPTCHA_SITE_KEY = 'YOUR_SITE_KEY'  # Replace with your public site key
HCAPTCHA_SECRET = 'YOUR_SECRET_KEY'  # Replace with your secret key

# Flask setup
app = Flask(__name__)
captcha_verified = False
captcha_event = threading.Event()

# hCaptcha verification function
def verify_hcaptcha(response_token: str) -> bool:
    """Verify hCaptcha token with hCaptcha API"""
    data = {
        "secret": HCAPTCHA_SECRET,
        "response": response_token
    }
    try:
        response = requests.post("https://hcaptcha.com/siteverify", data=data, timeout=5)
        return response.json().get("success", False)
    except requests.RequestException:
        return False

# Flask routes
@app.route('/')
def captcha_form():
    """Render CAPTCHA verification form"""
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>hCaptcha Verification</title>
    </head>
    <body>
        <h1>Complete CAPTCHA Verification</h1>
        <form action="/verify" method="POST">
            <div class="h-captcha" data-sitekey="{HCAPTCHA_SITE_KEY}"></div>
            <button type="submit">Verify</button>
        </form>
        <script src="https://js.hcaptcha.com/1/api.js" async defer></script>
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/verify', methods=['POST'])
def verify():
    """Handle CAPTCHA verification"""
    global captcha_verified
    token = request.form.get('h-captcha-response')
    
    if token and verify_hcaptcha(token):
        captcha_verified = True
        captcha_event.set()
        return "✅ Verification successful! Return to console"
    return "❌ Verification failed. Refresh page to try again"

def run_flask_app():
    """Run Flask app in separate thread"""
    app.run(port=5000, use_reloader=False)

# === Currencies ===
currency_list = ["USD", "GBP", "JPY", "MYR", "CAD"]
currency_rate = [0.78, 0.58, 115, 3.32, 1.07]

# Start Flask in background thread
flask_thread = threading.Thread(target=run_flask_app)
flask_thread.daemon = True
flask_thread.start()

# Allow server to start
time.sleep(1)

print("""
skibidi converter made by diddy
*accurate as of 1/1/1256
""")

# CAPTCHA verification
print("Opening CAPTCHA verification in browser...")
webbrowser.open("http://127.0.0.1:5000")
print("Please complete the CAPTCHA in your browser window")

# Wait for CAPTCHA verification (timeout after 120 seconds)
captcha_event.wait(timeout=120)

if not captcha_verified:
    print("❌ CAPTCHA verification failed or timed out")
    exit()

# Main application continues after successful CAPTCHA
#YOUR CODE HERE...
