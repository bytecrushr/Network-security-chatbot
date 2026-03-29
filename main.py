"""
Network Security Chatbot — Flask Web App
IBM Internship | BCAIN661C | Piyush Sahu | 24-BCA-3209
Run on Replit: python main.py
"""

from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# ══════════════════════════════════════════════
#  KNOWLEDGE BASE — 15 Q&A (Network Security)
# ══════════════════════════════════════════════
QA = [
    ("what is network security",
     "🛡️ <b>Network Security</b><br><br>Network Security refers to the policies, practices, and technologies used to protect the <b>integrity, confidentiality, and accessibility</b> of computer networks and data from attacks, damage, or unauthorized access.<br><br>Key goals: Prevent unauthorized access · Detect threats · Ensure data privacy"),

    ("what is a firewall",
     "🔥 <b>Firewall</b><br><br>A Firewall is a network security device or software that <b>monitors and controls</b> incoming/outgoing network traffic based on predetermined security rules.<br><br>It acts as a barrier between trusted internal networks and untrusted external networks.<br><br>Types: Packet Filtering · Stateful Inspection · Application Layer · Next-Gen Firewall"),

    ("what is vpn",
     "🌐 <b>VPN (Virtual Private Network)</b><br><br>A VPN creates a <b>secure, encrypted tunnel</b> over the internet. It protects your data and masks your IP address — like a private road on a public highway.<br><br>Use cases: Remote work security · Bypassing geo-restrictions · Protecting public Wi-Fi connections"),

    ("what is encryption",
     "🔒 <b>Encryption</b><br><br>Encryption converts readable data (<i>plaintext</i>) into an unreadable format (<i>ciphertext</i>) using an algorithm and key.<br><br>Only authorized parties with the correct key can decrypt and read it.<br><br>Common algorithms: <b>AES-256 · RSA · SHA-256 · ChaCha20</b>"),

    ("what is ddos attack",
     "💣 <b>DDoS Attack (Distributed Denial of Service)</b><br><br>A DDoS attack floods a target server/network with massive traffic from thousands of compromised systems, making it <b>unavailable to legitimate users</b>.<br><br>Prevention: Rate limiting · CDN · Traffic filtering · DDoS protection services"),

    ("what is phishing",
     "🎣 <b>Phishing</b><br><br>Phishing is a social engineering attack where attackers send <b>fraudulent emails/messages</b> disguised as trusted sources to steal sensitive data like passwords or card numbers.<br><br>Types: Email Phishing · Spear Phishing · Smishing (SMS) · Vishing (Voice)"),

    ("what is ssl tls",
     "🔐 <b>SSL / TLS</b><br><br>SSL (Secure Sockets Layer) and TLS (Transport Layer Security) are cryptographic protocols that <b>encrypt data between web browsers and servers</b>.<br><br>This is why websites use HTTPS — the 'S' stands for Secure.<br><br>Current standard: <b>TLS 1.3</b> (fastest & most secure)"),

    ("what is ids",
     "👁️ <b>IDS (Intrusion Detection System)</b><br><br>An IDS monitors network traffic for <b>suspicious activity and known threats</b>, generating real-time alerts when potential intrusions are detected.<br><br>IDS vs IPS:<br>• IDS — Detects and alerts<br>• IPS — Detects, alerts AND blocks"),

    ("what is malware",
     "🦠 <b>Malware (Malicious Software)</b><br><br>Malware is any software intentionally designed to cause disruption or gain unauthorized access.<br><br>Types:<br>• <b>Virus</b> — attaches to files and spreads<br>• <b>Worm</b> — self-replicates across networks<br>• <b>Trojan</b> — disguised as legitimate software<br>• <b>Ransomware</b> — encrypts files for ransom<br>• <b>Spyware</b> — secretly collects user data"),

    ("what is 2fa",
     "🔑 <b>Two-Factor Authentication (2FA)</b><br><br>Adds an extra security layer by requiring <b>two verification steps</b>:<br><br>1️⃣ Something you <b>KNOW</b> → Password / PIN<br>2️⃣ Something you <b>HAVE</b> → OTP / Authenticator app<br><br>Even if your password is stolen, attackers can't log in without the second factor."),

    ("what is proxy server",
     "🔄 <b>Proxy Server</b><br><br>A proxy server acts as an <b>intermediary gateway</b> between a user and the internet. It hides the user's real IP address and can filter or cache web traffic.<br><br>Types: Forward Proxy · Reverse Proxy · Transparent Proxy · Anonymous Proxy"),

    ("what is sql injection",
     "💉 <b>SQL Injection</b><br><br>SQL Injection inserts malicious SQL code into a query, letting attackers <b>view, modify, or delete database data</b> without authorization.<br><br>Example Attack:<br><code>Input: admin' OR '1'='1</code><br><br>Prevention: Parameterized queries · Input validation · ORM frameworks"),

    ("what is zero day",
     "⚠️ <b>Zero-Day Vulnerability</b><br><br>A zero-day is a software flaw <b>unknown to the vendor</b>. Attackers exploit it before a patch is released — giving defenders ZERO days to respond.<br><br>Protection: Behavior-based detection · Network segmentation · Threat intelligence"),

    ("what is cia triad",
     "📐 <b>CIA Triad — Foundation of Information Security</b><br><br>🔵 <b>CONFIDENTIALITY</b><br>&nbsp;&nbsp;Protect data from unauthorized access<br><br>🟢 <b>INTEGRITY</b><br>&nbsp;&nbsp;Ensure data accuracy and trustworthiness<br><br>🔴 <b>AVAILABILITY</b><br>&nbsp;&nbsp;Ensure systems are accessible when needed"),

    ("what is mitm attack",
     "🕵️ <b>Man-in-the-Middle (MITM) Attack</b><br><br>An attacker secretly <b>intercepts and alters communication</b> between two parties who believe they're talking directly to each other.<br><br>Scenario: You connect to 'FreeWifi' at a café — the attacker reads all your traffic.<br><br>Prevention: Use HTTPS · VPN · Avoid public Wi-Fi"),
]

GLOSSARY = {
    "ransomware":   "Ransomware encrypts your files and demands a payment (ransom) to restore access.",
    "trojan":       "A Trojan is malware disguised as legitimate software to trick users into installing it.",
    "worm":         "A Worm is self-replicating malware that spreads across networks without user action.",
    "spyware":      "Spyware secretly monitors and collects user information without consent.",
    "patch":        "A Patch is a software update released to fix known security vulnerabilities.",
    "authentication": "Authentication is the process of verifying the identity of a user or system.",
    "authorization":  "Authorization determines what an authenticated user is allowed to do.",
    "https":        "HTTPS is the secure version of HTTP — it uses SSL/TLS to encrypt all web traffic.",
    "honeypot":     "A Honeypot is a decoy system designed to attract and detect attackers.",
    "exploit":      "An Exploit is code used to take advantage of a software vulnerability.",
    "vulnerability":"A Vulnerability is a weakness in software/hardware that attackers can exploit.",
    "hacker":       "A Hacker finds and exploits weaknesses. Can be ethical (white-hat) or malicious (black-hat).",
}

QUIZ_POOL = [
    {"q": "What does CIA stand for in cybersecurity?",             "a": "Confidentiality, Integrity, Availability",  "hints": ["confidential", "integrity", "availab", "cia"]},
    {"q": "Which protocol secures web traffic (HTTP → HTTPS)?",    "a": "SSL / TLS",                                 "hints": ["ssl", "tls"]},
    {"q": "What attack floods a server with traffic to crash it?", "a": "DDoS — Distributed Denial of Service",      "hints": ["ddos", "denial", "distributed"]},
    {"q": "What is a fake email trick to steal passwords called?", "a": "Phishing",                                  "hints": ["phish"]},
    {"q": "Name the malware that encrypts files for ransom.",       "a": "Ransomware",                                "hints": ["ransom"]},
    {"q": "What hides your IP and encrypts your connection?",       "a": "VPN — Virtual Private Network",             "hints": ["vpn", "virtual private"]},
    {"q": "What system detects suspicious network activity?",       "a": "IDS — Intrusion Detection System",          "hints": ["ids", "intrusion"]},
    {"q": "What is an unknown software flaw called?",               "a": "Zero-Day Vulnerability",                    "hints": ["zero", "0day"]},
]

quiz_sessions = {}

def find_answer(text):
    t = text.lower().strip()

    if any(g in t for g in ["hi", "hello", "hey", "namaste", "hii"]):
        return {"type": "greeting", "msg": "👋 <b>Hello! I'm SecureBot</b> — your Network Security assistant.<br><br>I can answer <b>15 Network Security topics</b>, run a <b>quiz</b>, and explain security terms.<br><br>Try typing a topic or click a quick button below! 👇"}

    if t in ["help", "menu", "?"]:
        return {"type": "info", "msg": "📌 <b>What I can do:</b><br><br>🔍 Ask any question → e.g. <i>What is Firewall?</i><br>🎯 Type <b>quiz</b> → Start an interactive quiz<br>📋 Type <b>topics</b> → See all 15 topics<br>📖 Type any term → e.g. <i>ransomware</i>, <i>trojan</i>"}

    if any(w in t for w in ["all topic", "topics", "list", "show all", "all question"]):
        lines = "📋 <b>All 15 Network Security Topics:</b><br><br>"
        for i, (q, _) in enumerate(QA, 1):
            label = q.replace("what is a ", "").replace("what is ", "").title()
            lines += f"&nbsp;&nbsp;<b>{i:02d}.</b> {label}<br>"
        return {"type": "info", "msg": lines}

    for q_key, answer in QA:
        keywords = [w for w in q_key.replace("what is a ", "").replace("what is ", "").split() if len(w) > 2]
        matched = sum(1 for k in keywords if k in t)
        if matched >= max(1, len(keywords) - 1):
            return {"type": "answer", "msg": answer}

    for term, definition in GLOSSARY.items():
        if term in t:
            return {"type": "glossary", "msg": f"📖 <b>{term.title()}</b><br><br>{definition}"}

    return {"type": "not_found", "msg": f"🤔 I couldn't find info on <b>'{text}'</b>.<br><br>Try: <i>help</i> · <i>topics</i> · <i>quiz</i> · or any security term!"}


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "").strip()
    session_id = data.get("session_id", "default")

    if not user_msg:
        return jsonify({"reply": "Please type a message!", "type": "error"})

    t = user_msg.lower().strip()

    if session_id in quiz_sessions:
        sess = quiz_sessions[session_id]
        q = sess["questions"][sess["index"]]
        hints = q["hints"]
        correct = any(h in t for h in hints)
        sess["index"] += 1
        if correct:
            sess["score"] += 1
            feedback = f"✅ <b>Correct!</b> Well done! 🎉<br><i>Answer: {q['a']}</i>"
        else:
            feedback = f"❌ Not quite!<br>✅ <b>Correct Answer:</b> {q['a']}"

        if sess["index"] >= len(sess["questions"]):
            score = sess["score"]
            total = len(sess["questions"])
            del quiz_sessions[session_id]
            if score == total:      grade = "🌟 Outstanding! Perfect Score! You're a Network Security Expert!"
            elif score >= total-1:  grade = "🥇 Excellent! Almost perfect!"
            elif score > total//2:  grade = "👍 Good work! Keep practicing."
            else:                   grade = "📖 Keep studying! You'll improve!"
            result = f"{feedback}<br><br>🏆 <b>Quiz Complete! Score: {score}/{total}</b><br>{grade}"
            return jsonify({"reply": result, "type": "quiz_result"})
        else:
            next_q = sess["questions"][sess["index"]]
            next_msg = f"{feedback}<br><br>❓ <b>Q{sess['index']+1}/{len(sess['questions'])}:</b> {next_q['q']}"
            return jsonify({"reply": next_msg, "type": "quiz"})

    if t in ["quiz", "start quiz", "take quiz", "test"]:
        questions = random.sample(QUIZ_POOL, 5)
        quiz_sessions[session_id] = {"questions": questions, "index": 0, "score": 0}
        first_q = questions[0]
        reply = f"🎯 <b>Quiz Started!</b> 5 questions on Network Security.<br>Type your answer and press Enter. 💪<br><br>❓ <b>Q1/5:</b> {first_q['q']}"
        return jsonify({"reply": reply, "type": "quiz"})

    result = find_answer(user_msg)
    return jsonify({"reply": result["msg"], "type": result["type"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
