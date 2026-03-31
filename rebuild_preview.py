from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

random.seed(99)
W, H = 1200, 630
card = Image.new('RGB', (W, H), (4, 8, 20))
draw = ImageDraw.Draw(card)

for x in range(0, W, 55):
    draw.line([(x, 0), (x, H)], fill=(0, 30, 50), width=1)
for y in range(0, H, 55):
    draw.line([(0, y), (W, y)], fill=(0, 30, 50), width=1)

try:
    nf = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 11)
except:
    nf = ImageFont.load_default()

for col, x in [(0, 18), (1, 580), (2, 1155)]:
    for row in range(35):
        ch = str(random.randint(0, 9))
        y = row * 18 + 5
        alpha = random.randint(60, 140)
        draw.text((x, y), ch, font=nf, fill=(0, alpha, alpha // 2))

LX, LY = 270, 318
glow = Image.new('RGB', (W, H), (4, 8, 20))
gd = ImageDraw.Draw(glow)
gd.ellipse([LX - 200, LY - 210, LX + 200, LY + 210], fill=(0, 60, 80))
glow = glow.filter(ImageFilter.GaussianBlur(60))
card = Image.blend(card, glow, 0.7)
draw = ImageDraw.Draw(card)

BW, BH = 240, 200
BX, BY = LX - BW // 2, LY - 60

body_glow = Image.new('RGB', (W, H), (4, 8, 20))
bgd = ImageDraw.Draw(body_glow)
bgd.rounded_rectangle([BX - 8, BY - 8, BX + BW + 8, BY + BH + 8], radius=28, fill=(0, 100, 120))
body_glow = body_glow.filter(ImageFilter.GaussianBlur(18))
card = Image.blend(card, body_glow, 0.6)
draw = ImageDraw.Draw(card)
draw.rounded_rectangle([BX, BY, BX + BW, BY + BH], radius=20, fill=(0, 55, 70))

for _ in range(280):
    cx = random.randint(BX + 8, BX + BW - 8)
    cy = random.randint(BY + 8, BY + BH - 8)
    ch = random.choice(list('0123456789ABCDEFabcdef_/\\|><=-+'))
    alpha = random.randint(80, 200)
    draw.text((cx, cy), ch, font=nf, fill=(0, alpha, min(255, alpha + 30)))

bg2 = Image.new('RGB', (W, H), (4, 8, 20))
bg2d = ImageDraw.Draw(bg2)
bg2d.rounded_rectangle([BX, BY, BX + BW, BY + BH], radius=20, outline=(0, 245, 255), width=5)
bg2 = bg2.filter(ImageFilter.GaussianBlur(8))
card = Image.blend(card, bg2, 0.8)
draw = ImageDraw.Draw(card)
draw.rounded_rectangle([BX, BY, BX + BW, BY + BH], radius=20, outline=(0, 245, 255), width=3)

SR = 82
shackle_cx, shackle_cy = LX, BY
sg = Image.new('RGB', (W, H), (4, 8, 20))
sgd = ImageDraw.Draw(sg)
sgd.arc([shackle_cx - SR - 10, shackle_cy - SR - 10, shackle_cx + SR + 10, shackle_cy + SR + 10],
        180, 0, fill=(0, 200, 220), width=38)
sg = sg.filter(ImageFilter.GaussianBlur(12))
card = Image.blend(card, sg, 0.7)
draw = ImageDraw.Draw(card)
draw.arc([shackle_cx - SR, shackle_cy - SR, shackle_cx + SR, shackle_cy + SR],
         180, 0, fill=(0, 245, 255), width=28)
draw.arc([shackle_cx - SR + 8, shackle_cy - SR + 8, shackle_cx + SR - 8, shackle_cy + SR - 8],
         185, 355, fill=(180, 252, 255), width=8)
leg_x_l, leg_x_r = shackle_cx - SR, shackle_cx + SR
draw.line([(leg_x_l, shackle_cy), (leg_x_l, BY + 30)], fill=(0, 245, 255), width=28)
draw.line([(leg_x_r, shackle_cy), (leg_x_r, BY + 30)], fill=(0, 245, 255), width=28)
draw.line([(leg_x_l + 8, shackle_cy), (leg_x_l + 8, BY + 30)], fill=(180, 252, 255), width=8)
draw.line([(leg_x_r - 8, shackle_cy), (leg_x_r - 8, BY + 30)], fill=(180, 252, 255), width=8)

KX, KY = LX, int(BY + BH * 0.48)
kg = Image.new('RGB', (W, H), (4, 8, 20))
kgd = ImageDraw.Draw(kg)
kgd.ellipse([KX - 30, KY - 30, KX + 30, KY + 30], fill=(0, 200, 200))
kg = kg.filter(ImageFilter.GaussianBlur(15))
card = Image.blend(card, kg, 0.8)
draw = ImageDraw.Draw(card)
draw.ellipse([KX - 22, KY - 22, KX + 22, KY + 22], fill=(4, 8, 20), outline=(0, 245, 255), width=3)
draw.rounded_rectangle([KX - 9, KY + 8, KX + 9, KY + 38], radius=5, fill=(4, 8, 20), outline=(0, 245, 255), width=2)
kh_g = Image.new('RGB', (W, H), (4, 8, 20))
khgd = ImageDraw.Draw(kh_g)
khgd.ellipse([KX - 22, KY - 22, KX + 22, KY + 22], outline=(0, 245, 255), width=4)
kh_g = kh_g.filter(ImageFilter.GaussianBlur(6))
card = Image.blend(card, kh_g, 0.7)
draw = ImageDraw.Draw(card)

draw.line([(580, 40), (580, 590)], fill=(0, 60, 80), width=1)

try:
    fb  = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf', 68)
    fm  = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 28)
    fs  = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 18)
    fb2 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf', 24)
    fxs = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 12)
    f14 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 16)
except:
    fb = fm = fs = fb2 = fxs = f14 = nf

tg = Image.new('RGB', (W, H), (4, 8, 20))
ImageDraw.Draw(tg).text((608, 90), 'DAIZYX402', font=fb, fill=(0, 245, 255))
tg = tg.filter(ImageFilter.GaussianBlur(16))
card = Image.blend(card, tg, 0.6)
draw = ImageDraw.Draw(card)
draw.text((608, 90), 'DAIZYX402', font=fb, fill=(0, 245, 255))
draw.text((610, 180), 'AI Security Research API', font=fm, fill=(220, 240, 248))
draw.text((610, 232), 'Smart contract vulnerability research', font=fs, fill=(100, 150, 175))
draw.text((610, 256), 'powered by Aetheris \u00b7 Base Mainnet', font=fs, fill=(100, 150, 175))

draw.rounded_rectangle([610, 300, 778, 358], radius=7, outline=(0, 245, 255), width=2, fill=(4, 18, 32))
draw.text((626, 312), '$0.05 USDC', font=fb2, fill=(0, 245, 255))
draw.text((626, 338), 'RESEARCH', font=fxs, fill=(60, 130, 160))

ag = Image.new('RGB', (W, H), (4, 8, 20))
ImageDraw.Draw(ag).rounded_rectangle([792, 300, 980, 358], radius=7, fill=(0, 210, 160))
ag = ag.filter(ImageFilter.GaussianBlur(6))
card = Image.blend(card, ag, 0.5)
draw = ImageDraw.Draw(card)
draw.rounded_rectangle([792, 300, 980, 358], radius=7, fill=(0, 210, 160))
draw.text((808, 312), '$0.50 USDC', font=fb2, fill=(2, 20, 30))
draw.text((808, 338), 'ANALYSTS', font=fxs, fill=(2, 40, 30))

draw.text((610, 420), 'x402 Protocol \u00b7 No Signup \u00b7 No API Keys', font=f14, fill=(60, 100, 120))

card.save('/var/www/html/preview.png', 'PNG')
print('Done!')
