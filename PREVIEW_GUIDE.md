# daizyx402.com — OG Preview Image Guide

## How It Works

The social share preview image (`preview.png`) is served from `/var/www/html/preview.png` on the GCP VM (`aetheris`, `us-west1-c`, project `zeroclaw-rebel`).

The `og:image` meta tag in `/var/www/html/index.html` points to it:
```html
<meta property="og:image" content="https://www.daizyx402.com/preview.png?v=2" />
```

---

## To Update the Preview Image

### Option A — Replace with a new source image (recommended)

1. Put the new image at `/home/fuzzy/IMG_0707.png` on the VM (1200x630 PNG)
2. Copy it to the web root:
```bash
sudo cp /home/fuzzy/IMG_0707.png /var/www/html/preview.png
```
3. Bump the cache-bust version in `index.html`:
```bash
sudo sed -i 's|preview.png?v=2|preview.png?v=3|g' /var/www/html/index.html
```
4. Verify the file is live:
```bash
curl -I http://localhost/preview.png | grep Content-Length
```
5. Force-scrape on Facebook debugger to confirm:
   https://developers.facebook.com/tools/debug/?q=https%3A%2F%2Fwww.daizyx402.com

---

### Option B — Rebuild with PIL (text overlay on source image)

The script `rebuild_preview.py` in this repo composites text onto the source image.

1. Pull latest and run:
```bash
cd ~/awesome-x402 && git pull origin claude/fix-link-preview-K21Ao
sudo ~/.local/share/pipx/venvs/playwright/bin/python3 rebuild_preview.py
```
2. Bump the `?v=N` in `index.html` (see step 3 above)
3. Scrape on Facebook debugger

---

### Option C — Enhance brightness/color/contrast only

```bash
sudo ~/.local/share/pipx/venvs/playwright/bin/python3 << 'EOF'
from PIL import Image, ImageEnhance
img = Image.open('/var/www/html/preview.png')
img = ImageEnhance.Brightness(img).enhance(1.5)
img = ImageEnhance.Color(img).enhance(2.0)
img = ImageEnhance.Contrast(img).enhance(1.3)
img.save('/var/www/html/preview.png')
print('Done')
EOF
```

---

## Cache Busting

Facebook, iMessage, and other platforms cache OG images aggressively.
**Always bump the `?v=N` query parameter** in `index.html` after changing `preview.png`, then hit Scrape Again on the Facebook debugger.

Current version: `?v=2`

Next update: change to `?v=3`, then `?v=4`, etc.

---

## Key Files

| File | Location |
|------|----------|
| Preview image | `/var/www/html/preview.png` (VM) |
| Site HTML | `/var/www/html/index.html` (VM) |
| Source image | `/home/fuzzy/IMG_0707.png` (VM) |
| PIL rebuild script | `rebuild_preview.py` (this repo) |
| Deploy script | `~/deploy.sh` (VM) |

## PIL Fonts (on VM)
```
/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf
/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf
/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf
```
