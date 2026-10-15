
import datetime
from django.http import HttpResponse


def page_template(title, content):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>{title}</title>

        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            body {{
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: #f1f5f9;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
            }}

            /* Navigation */
            .navbar {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 22px 8%;
                background: #111827;
                border-bottom: 1px solid #334155;
            }}

            .logo {{
                font-size: 25px;
                font-weight: bold;
                color: #a78bfa;
            }}

            .nav-links {{
                display: flex;
                gap: 25px;
                list-style: none;
            }}

            .nav-links a {{
                color: #cbd5e1;
                text-decoration: none;
                transition: 0.3s;
            }}

            .nav-links a:hover {{
                color: #a78bfa;
            }}

            /* Main content */
            .container {{
                width: 85%;
                max-width: 1000px;
                margin: auto;
                padding: 70px 0;
                flex: 1;
            }}

            h1 {{
                font-size: 45px;
                color: #a78bfa;
                margin-bottom: 20px;
            }}

            h2 {{
                margin-bottom: 15px;
            }}

            p {{
                color: #cbd5e1;
                line-height: 1.8;
                margin-bottom: 20px;
            }}

            /* Card */
            .card {{
                background: #1e293b;
                padding: 30px;
                border-radius: 15px;
                border: 1px solid #334155;
                margin-top: 25px;
            }}

            /* Button */
            .button {{
                display: inline-block;
                padding: 12px 22px;
                background: #8b5cf6;
                color: white;
                border-radius: 8px;
                text-decoration: none;
                transition: 0.3s;
            }}

            .button:hover {{
                background: #7c3aed;
                transform: translateY(-2px);
            }}

            /* Footer */
            .footer {{
                text-align: center;
                padding: 25px;
                background: #111827;
                border-top: 1px solid #334155;
                color: #94a3b8;
            }}

            /* Mobile */
            @media (max-width: 600px) {{
                .navbar {{
                    flex-direction: column;
                    gap: 20px;
                }}

                .nav-links {{
                    gap: 15px;
                    flex-wrap: wrap;
                    justify-content: center;
                }}

                .container {{
                    width: 90%;
                    padding: 45px 0;
                }}

                h1 {{
                    font-size: 34px;
                }}
            }}
        </style>
    </head>

    <body>

        <nav class="navbar">
            <div class="logo">MyWebsite.</div>

            <ul class="nav-links">
                <li><a href="/">Home</a></li>
                <li><a href="/datetime/">Date & Time</a></li>
                <li><a href="/contact/">Contact</a></li>
            </ul>
        </nav>

        <main class="container">
            {content}
        </main>

        <footer class="footer">
            &copy; 2026 MyWebsite. Built with Django.
        </footer>

    </body>
    </html>
    """


def index(request):
    content = """
        <h1>Welcome to MyWebsite</h1>

        <p>
            Welcome to my website built with Django, HTML and CSS.
            Explore the pages and discover what this website offers.
        </p>

        <div class="card">
            <h2>Explore My Website</h2>

            <p>
                Check the current date and time or visit our contact page.
            </p>

            <a href="/datetime/" class="button">
                View Date & Time
            </a>

            <a href="/contact/" class="button">
                Contact Us
            </a>
        </div>
    """

    return HttpResponse(page_template("Home", content))


def current_datetime(request):
    now = datetime.datetime.now()

    content = f"""
        <h1>Current Date & Time</h1>

        <p>Here is the current date and time from your Django server.</p>

        <div class="card">
            <h2>Current Timestamp</h2>

            <p style="font-size: 25px; color: #a78bfa;">
                {now}
            </p>

            <a href="/" class="button">Back to Home</a>
        </div>
    """

    return HttpResponse(page_template("Date & Time", content))


def contact(request):
    content = """
        <h1>Contact Us</h1>

        <p>
            Thank you for visiting our website!
            We are happy to have you here.
        </p>

        <div class="card">
            <h2>Get in Touch</h2>

            <p>
                This is the contact page. You can add your contact
                information or a contact form here later.
            </p>

            <a href="/" class="button">Back to Home</a>
        </div>
    """

    return HttpResponse(page_template("Contact", content))

