from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QTextBrowser, QPushButton

_ABOUT_HTML = """
<style>
  body  { background: #0d0d1a; color: #c0c0d8; font-family: sans-serif; }
  h1    { color: #aaaaff; font-size: 22px; margin-bottom: 4px; }
  h2    { color: #8888cc; font-size: 16px; margin-top: 18px; margin-bottom: 6px; }
  h3    { color: #7070aa; font-size: 13px; margin-top: 14px; margin-bottom: 4px; }
  p     { font-size: 13px; line-height: 1.6; margin: 4px 0; }
  table { border-collapse: collapse; width: 100%; margin: 8px 0; }
  th    { color: #7070aa; font-size: 12px; text-align: left; padding: 3px 8px; }
  td    { font-size: 12px; padding: 3px 8px; border-bottom: 1px solid #222240; }
  .gold { color: #ffd700; } .green { color: #44bb88; }
  .muted { color: #7070a0; } .dim { color: #555; }
  .label { font-weight: bold; }
</style>

<h1>Pythia</h1>
<p>A natal chart and transit tool built with Python, PyQt6, and Skyfield.</p>

<h2>Transit Rankings</h2>
<p>
Each active transit receives a <b>score</b> (0–1) based on four factors:
planet weight, natal-point sensitivity, aspect power, and orb tightness.
The default sort uses <b>peak score</b> — the score the transit would reach
at exactness — so an incoming Pluto conjunction at 7° orb ranks above
a fading Moon sextile at 1° orb.
</p>

<h3>Scoring formula</h3>
<p>
<code>orb_strength = cos(orb / max_orb × π/2)</code><br>
<code>base_score   = t_weight × n_weight × a_weight × applying_bonus × station_bonus × house_bonus</code><br>
<code>current_score = orb_strength × base_score</code><br>
<code>peak_score    = base_score</code> &nbsp;(score at orb = 0)
</p>

<h3>Transiting planet weights</h3>
<table>
  <tr><th>Weight</th><th>Planets</th></tr>
  <tr><td>1.0</td><td>Pluto, Neptune, Uranus</td></tr>
  <tr><td>0.9</td><td>Saturn</td></tr>
  <tr><td>0.8</td><td>Jupiter</td></tr>
  <tr><td>0.5</td><td>Mars</td></tr>
  <tr><td>0.4</td><td>Sun, North Node, South Node</td></tr>
  <tr><td>0.3</td><td>Venus, Mercury</td></tr>
  <tr><td>0.1</td><td>Moon</td></tr>
</table>

<h3>Natal point weights</h3>
<table>
  <tr><th>Weight</th><th>Points</th></tr>
  <tr><td>1.0</td><td>Sun, Moon, ASC, MC</td></tr>
  <tr><td>0.8</td><td>DSC, IC</td></tr>
  <tr><td>0.7</td><td>Mercury, Venus, Mars</td></tr>
  <tr><td>0.6</td><td>North Node, South Node</td></tr>
  <tr><td>0.5</td><td>Jupiter, Saturn</td></tr>
  <tr><td>0.3</td><td>Uranus, Neptune, Pluto</td></tr>
</table>
<p>The natal point ruled by the chart's ASC sign gets +0.2 bonus (modern rulerships).</p>

<h3>Aspect weights</h3>
<table>
  <tr><th>Weight</th><th>Aspect</th></tr>
  <tr><td>1.0</td><td>Conjunction</td></tr>
  <tr><td>0.9</td><td>Opposition, Square</td></tr>
  <tr><td>0.8</td><td>Trine</td></tr>
  <tr><td>0.6</td><td>Sextile</td></tr>
</table>

<h3>Bonuses</h3>
<p><b>Applying bonus:</b> ×1.15 when the transit is still approaching exactness.</p>
<p><b>Station bonus:</b> up to ×1.5 for outer planets near stationary (speed &lt; 0.05°/day).</p>
<p><b>House bonus:</b> ×1.10 for angular houses (1, 4, 7, 10); ×0.95 for cadent (3, 6, 9, 12).</p>
<p><b>Fast-planet orb halving:</b> Moon, Mercury, Venus, and Sun use half the standard max orb
before filtering, keeping the score list focused on longer-lasting influences.</p>

<h3>Categories</h3>
<table>
  <tr><th>Category</th><th>Score threshold</th></tr>
  <tr><td><span class='gold label'>Major</span></td><td>≥ 0.70</td></tr>
  <tr><td><span class='green label'>Notable</span></td><td>≥ 0.40</td></tr>
  <tr><td><span class='muted label'>Minor</span></td><td>≥ 0.20</td></tr>
  <tr><td><span class='dim label'>Background</span></td><td>&lt; 0.20</td></tr>
</table>
<p>Use <b>Significant only</b> in the Transits tab to hide Minor and Background rows.</p>

<h3>Timescales</h3>
<table>
  <tr><th>Group</th><th>Planets</th></tr>
  <tr><td>Long</td><td>Pluto, Neptune, Uranus, Saturn</td></tr>
  <tr><td>Medium</td><td>Jupiter, Mars</td></tr>
  <tr><td>Short</td><td>Sun, Mercury, Venus</td></tr>
  <tr><td>Daily</td><td>Moon</td></tr>
</table>

<h3>A note on tuning</h3>
<p>
The weights above reflect a reasonable default. The scoring module
(<code>app/astrology/scoring.py</code>) exposes a <code>DEFAULT_CONFIG</code>
dict — all constants live there and can be adjusted without touching any other file.
Future versions may support user-selectable weighting profiles.
</p>
"""


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Pythia")
        self.setMinimumSize(640, 560)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 8)

        browser = QTextBrowser()
        browser.setOpenExternalLinks(False)
        browser.setHtml(_ABOUT_HTML)
        browser.setStyleSheet("background: #0d0d1a; border: none;")
        layout.addWidget(browser)

        close_btn = QPushButton("Close")
        close_btn.setFixedWidth(100)
        close_btn.clicked.connect(self.accept)
        layout.addWidget(close_btn, alignment=Qt.AlignmentFlag.AlignCenter)
