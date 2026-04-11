from PIL import Image, ImageDraw, ImageFont
import math, os

def make_icon(size):
    # Background
    img = Image.new('RGB', (size, size), (17, 16, 9))  # #111009

    # Sun glow as RGBA layer composited on top
    glow = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    pixels = glow.load()

    cx = size / 2
    cy = size * 0.46  # slightly above center
    max_r = size * 0.40

    for y in range(size):
        for x in range(size):
            dx, dy = x - cx, y - cy
            r = math.sqrt(dx*dx + dy*dy)
            if r >= max_r:
                continue
            t = r / max_r  # 0=center, 1=edge

            # Color stops: white-yellow core → orange mid → rust edge
            if t < 0.25:
                s = t / 0.25
                cr = int(255 * (1 - s) + 255 * s)
                cg = int(245 * (1 - s) + 185 * s)
                cb = int(200 * (1 - s) + 80  * s)
            elif t < 0.55:
                s = (t - 0.25) / 0.30
                cr = int(255 * (1 - s) + 220 * s)
                cg = int(185 * (1 - s) + 90  * s)
                cb = int(80  * (1 - s) + 30  * s)
            else:
                s = (t - 0.55) / 0.45
                cr = int(220 * (1 - s) + 180 * s)
                cg = int(90  * (1 - s) + 55  * s)
                cb = int(30  * (1 - s) + 20  * s)

            # Opacity: bright at core, smooth fade to transparent
            alpha = int(220 * (1 - t**1.4))
            pixels[x, y] = (cr, cg, cb, alpha)

    img.paste(glow, (0, 0), glow)

    draw = ImageDraw.Draw(img)

    # Try to find a bold system font
    font_paths = [
        '/System/Library/Fonts/Supplemental/Impact.ttf',
        '/System/Library/Fonts/Helvetica.ttc',
        '/System/Library/Fonts/Arial Bold.ttf',
        '/Library/Fonts/Arial Bold.ttf',
        '/System/Library/Fonts/SFNSDisplay-Bold.otf',
    ]
    def load_font(sz):
        for fp in font_paths:
            if os.path.exists(fp):
                try:
                    return ImageFont.truetype(fp, sz)
                except Exception:
                    continue
        return ImageFont.load_default()

    padding = size * 0.08

    # Auto-fit "C" to ~60% of icon width
    fs = int(size * 0.60)
    while fs > 8:
        f = load_font(fs)
        bb = draw.textbbox((0, 0), 'C', font=f)
        if (bb[2] - bb[0]) <= size - padding * 2:
            break
        fs -= 1
    font_top = load_font(fs)

    # "26" at similar size to "C"
    font_bot = load_font(int(fs * 0.65))

    # Measure both lines
    bb_top = draw.textbbox((0, 0), 'C',  font=font_top)
    bb_bot = draw.textbbox((0, 0), '26', font=font_bot)
    top_w, top_h = bb_top[2] - bb_top[0], bb_top[3] - bb_top[1]
    bot_w, bot_h = bb_bot[2] - bb_bot[0], bb_bot[3] - bb_bot[1]

    gap = int(size * 0.02)
    total_h = top_h + gap + bot_h

    # Center the block vertically with a slight downward nudge
    block_top = (size - total_h) / 2 + size * 0.03

    top_x = (size - top_w) / 2 - bb_top[0]
    top_y = block_top - bb_top[1]

    bot_x = (size - bot_w) / 2 - bb_bot[0]
    bot_y = block_top + top_h + gap - bb_bot[1]

    # "C" in sand
    draw.text((top_x, top_y), 'C', font=font_top, fill=(245, 237, 224))  # sand

    # "26" in burnt orange
    draw.text((bot_x, bot_y), '26', font=font_bot, fill=(232, 105, 42))  # #e8692a burnt

    return img

os.makedirs('icons', exist_ok=True)
for size, name in [(192, 'icons/icon-192.png'), (512, 'icons/icon-512.png')]:
    img = make_icon(size)
    img.save(name)
    print(f'Saved {name}')
