from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Diploma', 'assets/Diploma.ttf'))

# A3 landscape
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

# Static text colour
c.setFillColorRGB(0.101961, 0.101961, 0.101961)

# "The colleagues of Codestar hereby celebrate"
c.setFont('Diploma', 40)
c.drawCentredString(W / 2, 693, "The colleagues of Codestar hereby celebrate")

# "presented at Codestar HQ, Nieuwegein"
c.setFont('Diploma', 40)
c.drawCentredString(W / 2, 430, "presented at Codestar HQ, Nieuwegein")

# "Rector Magnificus" (lower right)
c.setFont('Diploma', 18)
c.drawString(863, 316, "Rector Magnificus")

# Signature line under Rector Magnificus
c.setStrokeColorRGB(0.2, 0.2, 0.2)
c.setLineWidth(1.0)
c.line(840, 298, 1005, 298)

c.save()
print("Done: assets/template.pdf")
