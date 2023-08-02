import math

# HTML Template
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{km} km to mph</title>
    <link rel="icon" href="img/favicon.ico" sizes="any">
    <link rel="icon" href="img/favicon.svg" type="image/svg+xml">
    <link rel="apple-touch-icon" href="img/favicon.png">
    <link href="https://kmtomph.online/{km}km-to-mph.html" rel="canonical"/>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
  <div class="logo">
<a href="https://kmtomph.online/">
<img alt="Logo" src="img/kmtomph.png" width="280"/>
</a>
</div>
    
  <h1>{km} km to mph</h1>
  <div class="container">
    <p>To convert {km} kilometers per hour to miles per hour, Multiply {km} km/h by 0.621371. {km} km/h times 0.621371 gives you {mph} mph. Therefore, a speed of {km} km/h is equivalent to {mph} mph.</p>
    <h2>Formula for {km} km/h to mph</h2>
    <p>Given a speed of {km} km/h, the conversion to miles per hour (mph) can be expressed as:</p>
    <p>v = 0.621371 * u</p>
    <p>Where:</p>
    <ul>
        <li>v is the speed in mph,</li>
        <li>u is the speed in km/h.</li>
    </ul>
    <p>Substituting the given speed into the formula:</p>
    <p>v = 0.621371 * {km} km/h</p>
    <p>Therefore,</p>
    <p>v = {mph} mph</p>
    <h2>km/h to mph Converter</h2>
    <div class="calculator-wrapper">
        <div class="calculator">
            <div class="inputGroup">
                <label for="speed">Kilometers per hour (km/h):</label>
                <input type="number" id="speed" min="0" required>
            </div>
            <div class="buttonGroup">
                <button class="calculator-button" id="calculate">Calculate</button>
                <button class="calculator-button" id="reset">Reset</button>
            </div>
            <div class="inputGroup">
                <label for="result">Result (mph):</label>
                <input type="text" id="result" readonly>
            </div>
            <p id="error-message" style="display: none;">Invalid input. Please enter a positive number.</p>
        </div>
    </div>
    <script>
        const speedInput = document.getElementById('speed');
        const resultInput = document.getElementById('result');
        const calculateButton = document.getElementById('calculate');
        const resetButton = document.getElementById('reset');
        const errorMessage = document.getElementById('error-message');
        calculateButton.addEventListener('click', function() {{
          const speed = parseFloat(speedInput.value);
          if (isNaN(speed) || speed < 0) {{
            errorMessage.style.display = 'block';
            resultInput.value = '';
          }} else {{
            errorMessage.style.display = 'none';
            resultInput.value = (0.621371 * speed).toFixed(2) + ' mph';
          }}
        }});
        resetButton.addEventListener('click', function() {{
          speedInput.value = '';
          resultInput.value = '';
          errorMessage.style.display = 'none';
        }});
    </script>

    <h2>FAQs</h2>
    <h3>How fast is {km} km/h in mph?</h3>
    <p>A speed of {km} km/h is equivalent to a speed of approximately {mph} mph.</p>
    <h3>How do you convert {km} km/h to mph?</h3>
    <p>To convert a speed from kilometers per hour (km/h) to miles per hour (mph), you need to use the conversion factor 0.621371. In this case, you would multiply {km} km/h by 0.621371 to get the equivalent speed in mph. So, {km} km/h is approximately {mph} mph.</p>
    <h2>Other conversions</h2>
    {conversion_table}
    <div class="related">
    <h2>Related Articles</h2>
    {related_articles_html}
  </div>
  </div>
<footer>
    <div class="footer">
        <div class="copyright">
            &copy; km/h to mph
        </div>
        <nav>
            <ul>
                <li><a href="Privacy-Policy.html">Privacy Policy</a></li>
                <li><a href="Help.html">Help</a></li>
                <li><a href="contact-us.html">Contact Us</a></li>
            </ul>
        </nav>
    </div>
  </footer>
  
</body>
</html>
"""

related_article = """
    <div class="article-preview">
        <a href="{next_km}km-to-mph.html">
          <h3>{next_km} km to mph</h3>
        </a>
        <p>This article explains how to convert a speed of {next_km} km/h to miles per hour.</p>
    </div>
"""

start = int(input("Enter start: "))
end = int(input("Enter end: "))

for km in range(start, end+1):
    mph = 0.621371 * km

    conversion_table = '<table class="km-mph-table"><tr><th>Km/h</th><th>mph</th></tr>'
    for i in range(1, 10):
        kph_decimal = km + (i/10)
        mph_decimal = round(kph_decimal * 0.621371, 2)
        conversion_table += '<tr><td>{}</td><td>{}</td></tr>'.format(kph_decimal, mph_decimal)
    conversion_table += '</table>'

    related_articles_html = ""
    for i in range(1, min(end - km + 1, 5)):
        next_km = km + i 
        related_articles_html += related_article.format(next_km=next_km)
    
    # Filling the HTML Template with values
    html = template.format(km=km, mph=round(mph, 2), related_articles_html=related_articles_html, conversion_table=conversion_table)
    
    # Writing the HTML file
    with open(f"{km}km-to-mph.html", "w", encoding="utf-8") as file:
        file.write(html)
