from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import random

W, H = 1200, 630
FONT = '/usr/share/fonts/truetype/dejavu/'

# Load base image and fit to left half
base = Image.open('/mnt/project/IMG_0707.png').convert('RGB')
bw, bh = base.size
scale = max(W / bw, H / bh)
base = base.resize((int(bw * scale), int(bh * scale)), Image.LANCZOS)
bw2, bh2 = base.size
base = base.crop(((bw2 - W) // 2, (bh2 - H) // 2, (bw2 - W) // 2 + W, (bh2 - H) // 2 + H))

card = Image.new('RGB', (W, H), (4, 8, 20))
draw = ImageDraw.Draw(card)

# Grid
for x in range(0, W, 55):
    draw.line([(x, 0), (x, H)], fill=(0, 30, 50), width=1)
for y in range(0, H, 55):
    draw.line([(0, y), (W, y)], fill=(0, 30, 50), width=1)

# Composite base image onto left half with dark overlay
left = base.crop((0, 0, 580, H))
left = ImageEnhance.Brightness(left).enhance(1.1)
card.paste(left, (0, 0))

# Re-draw grid on top of image (subtle)
draw = ImageDraw.Draw(card)
for x in range(0, 580, 55):
    draw.line([(x, 0), (x, H)], fill=(0, 40, 60, 60), width=1)
for y in range(0, H, 55):
    draw.line([(0, y), (580, y)], fill=(0, 40, 60, 60), width=1)

# Dark right panel background
right_bg = Image.new('RGB', (W - 580, H), (4, 8, 20))
card.paste(right_bg, (580, 0))
draw = ImageDraw.Draw(card)
for x in range(580, W, 55):
    draw.line([(x, 0), (x, H)], fill=(0, 30, 50), width=1)
for y in range(0, H, 55):
    draw.line([(580, y), (W, y)], fill=(0, 30, 50), width=1)

# Divider
draw.line([(580, 40), (580, 590)], fill=(0, 60, 80), width=1)

# Fonts
try:
    fb  = ImageFont.truetype(FONT + 'DejaVuSansMono-Bold.ttf', 68)
    fm  = ImageFont.truetype(FONT + 'DejaVuSans.ttf', 28)
    fs  = ImageFont.truetype(FONT + 'DejaVuSansMono.ttf', 18)
    fb2 = ImageFont.truetype(FONT + 'DejaVuSansMono-Bold.ttf', 24)
    fxs = ImageFont.truetype(FONT + 'DejaVuSansMono.ttf', 12)
    f14 = ImageFont.truetype(FONT + 'DejaVuSansMono.ttf', 16)
except:
    fb = fm = fs = fb2 = fxs = f14 = ImageFont.load_default()

# Title glow
tg = Image.new('RGB', (W, H), (4, 8, 20))
ImageDraw.Draw(tg).text((608, 90), 'DAIZYX402', font=fb, fill=(0, 245, 255))
tg = tg.filter(ImageFilter.GaussianBlur(16))
card = Image.blend(card, tg, 0.5)
draw = ImageDraw.Draw(card)

# Right panel text
draw.text((608, 90),  'DAIZYX402',                          font=fb,  fill=(0, 245, 255))
draw.text((610, 180), 'AI Security Research API',            font=fm,  fill=(220, 240, 248))
draw.text((610, 232), 'Smart contract vulnerability research', font=fs, fill=(100, 150, 175))
draw.text((610, 256), 'powered by Aetheris · Base Mainnet', font=fs, fill=(100, 150, 175))

# Box 1: outlined
draw.rounded_rectangle([610, 300, 778, 358], radius=7, outline=(0, 245, 255), width=2, fill=(4, 18, 32))
draw.text((626, 312), '$0.05 USDC', font=fb2, fill=(0, 245, 255))
draw.text((626, 338), 'RESEARCH',   font=fxs, fill=(60, 130, 160))

# Box 2: filled teal
ag = Image.new('RGB', (W, H), (4, 8, 20))
ImageDraw.Draw(ag).rounded_rectangle([792, 300, 980, 358], radius=7, fill=(0, 210, 160))
ag = ag.filter(ImageFilter.GaussianBlur(6))
card = Image.blend(card, ag, 0.5)
draw = ImageDraw.Draw(card)
draw.rounded_rectangle([792, 300, 980, 358], radius=7, fill=(0, 210, 160))
draw.text((808, 312), '$0.50 USDC', font=fb2, fill=(2, 20, 30))
draw.text((808, 338), 'ANALYSTS',   font=fxs, fill=(2, 40, 30))

# Tagline
draw.text((610, 420), 'x402 Protocol · No Signup · No API Keys', font=f14, fill=(60, 100, 120))

card.save('/var/www/html/preview.png', 'PNG')
print('Done!')
