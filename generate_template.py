from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Diploma', 'assets/Diploma.ttf'))

W, H = 1190.55, 841.89
c = canvas.Canvas('assets/template.pdf', pagesize=(W, H))

# Background (cream)
c.setFillColorRGB(0.992157, 0.988235, 0.972549)
c.rect(0, 0, W, H, fill=1, stroke=0)

# Outer border (dark red, 2.5pt)
c.setStrokeColorRGB(0.545098, 0, 0)
c.setLineWidth(2.5)
c.rect(25.5, 25.5, W - 51, H - 51, fill=0, stroke=1)

# Inner border (tan, 0.8pt)
c.setStrokeColorRGB(0.784314, 0.658824, 0.509804)
c.setLineWidth(0.8)
c.rect(35.4, 35.4, W - 70.8, H - 70.8, fill=0, stroke=1)

DARK = (0.101961, 0.101961, 0.101961)
BLUE = (0.05882,  0.40784,  0.65098)   # #0f68a6

def draw_mixed_centered(c, cx, y, parts, font, size):
    """Render (text, color) parts centred on cx."""
    total_w = sum(pdfmetrics.stringWidth(t, font, size) for t, _ in parts)
    x = cx - total_w / 2
    c.setFont(font, size)
    for text, color in parts:
        c.setFillColorRGB(*color)
        c.drawString(x, y, text)
        x += pdfmetrics.stringWidth(text, font, size)

# "The colleagues of Codestar hereby celebrate" — centred on page, y=696
draw_mixed_centered(c, W/2, 696, [
    ("The colleagues of ",       DARK),
    ("C",                        BLUE),
    ("odestar hereby celebrate", DARK),
], 'Diploma', 36)

# "presented at Codestar HQ, Nieuwegein" — centred on page, y=433
draw_mixed_centered(c, W/2, 433, [
    ("presented at ",            DARK),
    ("C",                        BLUE),
    ("odestar HQ, Nieuwegein",   DARK),
], 'Diploma', 36)

# "Rector Magnificus" — on top, centred at X=943, y=250; "R" in blue
draw_mixed_centered(c, 943, 250, [
    ("R",                        BLUE),
    ("ector Magnificus",         DARK),
], 'Diploma', 16)

# No signature line

c.save()
print("Done: assets/template.pdf")
