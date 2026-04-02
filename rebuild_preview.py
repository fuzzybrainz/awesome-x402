from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

W, H = 1200, 630
FONT = '/usr/share/fonts/truetype/dejavu/'

# LEFT HALF: scale to fit height, crop from LEFT edge where padlock is
base = Image.open('/home/fuzzy/IMG_0707.png').convert('RGB')
bw, bh = base.size
scale = H / bh
base = base.resize((int(bw * scale), H), Image.LANCZOS)
left = base.crop((0, 0, 580, H))
left = ImageEnhance.Brightness(left).enhance(1.2)
left = ImageEnhance.Color(left).enhance(1.4)

# RIGHT HALF: dark panel
right = Image.new('RGB', (W - 580, H), (4, 8, 20))
rd = ImageDraw.Draw(right)
for x in range(0, W - 580, 55):
    rd.line([(x, 0), (x, H)], fill=(0, 30, 50), width=1)
for y in range(0, H, 55):
    rd.line([(0, y), (W - 580, y)], fill=(0, 30, 50), width=1)

try:
    fb  = ImageFont.truetype(FONT + 'DejaVuSansMono-Bold.ttf', 68)
    fm  = ImageFont.truetype(FONT + 'DejaVuSans.ttf', 28)
    fs  = ImageFont.truetype(FONT + 'DejaVuSansMono.ttf', 18)
    fb2 = ImageFont.truetype(FONT + 'DejaVuSansMono-Bold.ttf', 24)
    fxs = ImageFont.truetype(FONT + 'DejaVuSansMono.ttf', 12)
    f14 = ImageFont.truetype(FONT + 'DejaVuSansMono.ttf', 16)
except:
    fb = fm = fs = fb2 = fxs = f14 = ImageFont.load_default()

tg = Image.new('RGB', (W - 580, H), (4, 8, 20))
ImageDraw.Draw(tg).text((28, 90), 'DAIZYX402', font=fb, fill=(0, 245, 255))
tg = tg.filter(ImageFilter.GaussianBlur(16))
right = Image.blend(right, tg, 0.6)
rd = ImageDraw.Draw(right)

rd.text((28, 90),  'DAIZYX402',                               font=fb,  fill=(0, 245, 255))
rd.text((30, 180), 'AI Security Research API',                 font=fm,  fill=(220, 240, 248))
rd.text((30, 232), 'Smart contract vulnerability research',    font=fs,  fill=(100, 150, 175))
rd.text((30, 256), 'powered by Aetheris · Base Mainnet',  font=fs,  fill=(100, 150, 175))

rd.rounded_rectangle([30, 300, 198, 358], radius=7, outline=(0, 245, 255), width=2, fill=(4, 18, 32))
rd.text((46, 312), '$0.05 USDC', font=fb2, fill=(0, 245, 255))
rd.text((46, 338), 'RESEARCH',   font=fxs, fill=(60, 130, 160))

ag = Image.new('RGB', (W - 580, H), (4, 8, 20))
ImageDraw.Draw(ag).rounded_rectangle([212, 300, 400, 358], radius=7, fill=(0, 210, 160))
ag = ag.filter(ImageFilter.GaussianBlur(6))
right = Image.blend(right, ag, 0.5)
rd = ImageDraw.Draw(right)
rd.rounded_rectangle([212, 300, 400, 358], radius=7, fill=(0, 210, 160))
rd.text((228, 312), '$0.50 USDC', font=fb2, fill=(2, 20, 30))
rd.text((228, 338), 'ANALYSTS',   font=fxs, fill=(2, 40, 30))

rd.text((30, 420), 'x402 Protocol · No Signup · No API Keys', font=f14, fill=(60, 100, 120))

card = Image.new('RGB', (W, H), (4, 8, 20))
card.paste(left, (0, 0))
card.paste(right, (580, 0))

ld = ImageDraw.Draw(card)
for x in range(0, 580, 55):
    ld.line([(x, 0), (x, H)], fill=(0, 40, 60), width=1)
for y in range(0, H, 55):
    ld.line([(0, y), (580, y)], fill=(0, 40, 60), width=1)
ld.line([(580, 40), (580, 590)], fill=(0, 80, 100), width=1)

card.save('/var/www/html/preview.png', 'PNG')
print('Done!')
