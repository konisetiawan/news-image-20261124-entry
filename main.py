from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1600, 2200
PAPER = '#f7f2e7'
INK = '#1a1a1a'
RED = '#c0392b'
BLUE = '#1f3a5f'
MUTED = '#5e625f'
PALE_BLUE = '#d8e2ea'
GOLD = '#f2b544'
GREEN = '#5c8b68'


def load_font(size, bold=False, italic=False):
    candidates = []
    if bold and italic:
        candidates += ['/usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf']
    elif bold:
        candidates += ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf']
    elif italic:
        candidates += ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf']
    candidates += ['/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            pass
    return ImageFont.load_default()


FONT_16 = load_font(16)
FONT_17 = load_font(17)
FONT_18 = load_font(18)
FONT_20 = load_font(20)
FONT_22B = load_font(22, bold=True)
FONT_24B = load_font(24, bold=True)
FONT_28B = load_font(28, bold=True)
FONT_34B = load_font(34, bold=True)
FONT_76B = load_font(76, bold=True)
FONT_ITALIC = load_font(18, italic=True)

REGIONS = [
    ('EUROPE', [
        ('NATO JETS OVER POLAND', 'Advanced detection aircraft deployed after a missile falls.', 'plane'),
        ('ZAPORIZHZHIA HIT AGAIN', 'Night strike kills 2 and wounds 48 in Ukraine.', 'burst'),
        ('KYIV EXPLAINS LIBYA STRIKE', 'Libya demands answers after drones hit Russian ships.', 'drone'),
        ('TRUMP: IPCC BACKTRACKS', 'Trump says the UN climate body withdrew extreme projections.', 'gavel'),
        ('MACRON EYES SPENDING CAPS', 'French president weighs constitutional limits on spending.', 'chart'),
        ('SANDRINGHAM BREAK-IN', 'Two men detained after break-in at Anmer Hall estate.', 'house'),
    ]),
    ('ASIA-PACIFIC', [
        ('SHENZHOU-24 LIFTS OFF', 'First foreign astronaut joins the Tiangong crew.', 'rocket'),
        ('14 NATIONS BACK ICJ', 'UK, Spain, Canada, Australia and 10 affirm Rohingya ruling.', 'scales'),
        ('NEPAL QUAKE 5.6', 'Quake strikes Koshi province near the China border.', 'quake'),
        ('PYONGYANG EXPELS SWISS', 'North Korea demands closure of a new Swiss office.', 'door'),
        ('SOLOMONS PICK AUSTRALIA', 'Security pact names Australia top partner, excludes China.', 'handshake'),
        ('HANOI BLAST KILLS 6', 'Eatery explosion kills six; more than a dozen are hurt.', 'burst'),
        ('HASINA TO RETURN', 'Ousted Bangladesh leader plans a December 16 return.', 'arrow'),
    ]),
    ('MIDDLE EAST', [
        ('GAZA: “TOXIC LAND”', 'Oxfam warns of toxic ground; strikes kill 3, including UN worker.', 'leaf'),
        ('SAUDI STRIKES KILL DOZENS', 'Houthis report dozens dead in Saudi airstrikes on Yemen.', 'burst'),
        ('DRONE HITS RIYADH TOWER', 'Houthi drone attack injures 11 in the Saudi capital.', 'drone'),
        ('IRAN LASHES SINGER', 'Parastoo Ahmadi gets 74 lashes; Tehran rules out talks.', 'music'),
        ('HOUTHI SIEGE ON ADEN', 'Rebels close in as Yemeni forces dig in around Aden.', 'shield'),
    ]),
    ('AFRICA', [
        ('EBOLA TEAMS TRAPPED', 'Ituri fighting traps DRC responders; cases top 11,000, deaths 5,358.', 'cross'),
        ('SUDAN DOWNS DRONES', 'Army says it shot down drones from Ethiopia in Blue Nile.', 'drone'),
        ('ETHIOPIA HOSTS SUDAN TALKS', 'Addis offers to host inter-Sudanese dialogue.', 'handshake'),
        ('MSF HALTS SOUTH SUDAN WORK', 'Abduction prompts a three-month suspension in Yei.', 'cross'),
    ]),
    ('AMERICAS', [
        ('MEASLES: 9TH DEATH', 'Pennsylvania outbreak spreads across 46 counties.', 'cross'),
        ('CARTAGENA HOSTAGES', 'Gunmen take 25 people hostage in a supermarket.', 'house'),
        ('COLOMBIA CAR BOMB', 'Blast destroys buildings in Villavicencio.', 'burst'),
        ('TRUMP HONOURS GIULIANI', 'Presidential Medal of Freedom awarded to former mayor.', 'medal'),
        ('CIA, ODNI BREACHED', 'Cyber breach hits US intelligence agencies.', 'lock'),
        ('PENTAGON SCOLDS CANADA', 'Defence spending rebuke; F-35 review follows.', 'plane'),
    ]),
    ('MARKETS & TECH', [
        ('WALL ST SOARS', 'S&P +4.7%, Nasdaq +6.5%; Nikkei +3.9%.', 'chart'),
        ('NVIDIA SLIDES 7%', 'Lawmakers seek answers; Dell AI quarter lifts forecasts.', 'chip'),
        ('US TARIFFS LOOM', 'Washington ready to hit China and EU over subsidised output.', 'chart'),
        ('HUAWEI GUILTY', 'US jury finds trade-secret theft, clears racketeering charge.', 'gavel'),
    ]),
    ('SCIENCE & CLIMATE', [
        ('COP31 COLLAPSES', 'No deal: 40 nations object; EU calls text “unconscionable”.', 'leaf'),
        ('GUTERRES: AI RULES IN A YEAR', 'UN chief seeks a multilateral framework for AI risks.', 'chip'),
        ('OLDEST QUASAR FOUND', 'Record quasar formed 630 million years after the Big Bang.', 'star'),
    ]),
]

ROW_H = 55
SECTION_HEAD_H = 40


def draw_icon(draw, kind, x, y, size=34):
    cx, cy = x + size // 2, y + size // 2
    r = size // 2
    draw.ellipse((x, y, x + size, y + size), fill=PALE_BLUE)
    dark = BLUE
    if kind in ('burst', 'quake'):
        points = [(cx, y + 4), (cx + 4, cy - 3), (x + size - 5, cy),
                  (cx + 4, cy + 4), (cx + 1, y + size - 4), (cx - 3, cy + 4),
                  (x + 5, cy + 1), (cx - 2, cy - 3)]
        draw.polygon(points, fill=RED if kind == 'burst' else GOLD)
        if kind == 'quake':
            draw.line((cx - 1, y + 9, cx + 3, cy - 1, cx - 1, cy + 3, cx + 3, y + size - 8), fill=dark, width=2)
    elif kind == 'rocket':
        draw.polygon([(cx, y + 4), (cx + 7, cy + 4), (cx + 5, cy - 5), (cx, y + 2), (cx - 5, cy - 5), (cx - 7, cy + 4)], fill=RED)
        draw.ellipse((cx - 2, cy - 4, cx + 2, cy), fill=PALE_BLUE)
        draw.polygon([(cx - 5, cy + 4), (cx - 10, cy + 11), (cx - 4, cy + 8), (cx, cy + 10), (cx + 4, cy + 8), (cx + 10, cy + 11), (cx + 5, cy + 4)], fill=GOLD)
        draw.line((cx, cy + 10, cx, y + size - 3), fill=RED, width=2)
    elif kind in ('plane', 'drone'):
        draw.polygon([(x + 4, cy), (cx - 2, cy - 2), (cx + 2, y + 6), (cx + 5, y + 6), (cx + 5, cy - 2), (x + size - 4, cy), (cx + 5, cy + 2), (cx + 5, y + size - 7), (cx + 2, y + size - 7), (cx - 2, cy + 2)], fill=dark)
        if kind == 'drone':
            draw.line((x + 6, cy - 6, x + size - 6, cy - 6), fill=RED, width=2)
            draw.ellipse((x + 5, cy - 9, x + 9, cy - 5), fill=RED)
            draw.ellipse((x + size - 9, cy - 9, x + size - 5, cy - 5), fill=RED)
    elif kind in ('chart', 'arrow'):
        draw.line((x + 8, y + size - 8, x + 8, y + 8, x + size - 6, y + 8), fill=dark, width=2)
        draw.line((x + 10, cy + 6, cx - 2, cy + 1, cx + 3, cy + 3, x + size - 7, y + 9), fill=GREEN, width=4)
        draw.polygon([(x + size - 7, y + 5), (x + size - 5, y + 12), (x + size - 12, y + 10)], fill=GREEN)
    elif kind in ('gavel', 'scales'):
        draw.line((cx - 7, y + 9, cx + 7, cy + 5), fill=dark, width=4)
        draw.line((cx + 2, cy + 1, cx - 3, cy + 7), fill=dark, width=3)
        draw.line((x + 8, y + size - 8, x + size - 8, y + size - 8), fill=dark, width=2)
    elif kind in ('house', 'door'):
        draw.polygon([(x + 6, cy - 1), (cx, y + 7), (x + size - 6, cy - 1), (x + size - 8, cy + 1), (x + size - 8, y + size - 7), (x + 8, y + size - 7), (x + 8, cy + 1)], fill=GREEN)
        draw.rectangle((cx - 3, cy + 3, cx + 3, y + size - 7), fill=PAPER if kind == 'door' else GOLD)
    elif kind in ('handshake', 'shield'):
        if kind == 'shield':
            draw.polygon([(cx, y + 6), (x + size - 7, y + 10), (x + size - 9, cy + 7), (cx, y + size - 6), (x + 9, cy + 7), (x + 7, y + 10)], fill=GREEN)
        else:
            draw.line((x + 7, cy - 2, cx - 2, cy + 4, cx + 2, cy + 1, x + size - 7, cy + 6), fill=GREEN, width=5)
            draw.line((cx - 1, cy + 3, cx + 5, cy + 8), fill=GOLD, width=3)
    elif kind in ('leaf', 'cross'):
        if kind == 'leaf':
            draw.ellipse((x + 7, y + 7, x + size - 6, y + size - 7), fill=GREEN)
            draw.line((x + 10, y + size - 8, x + size - 8, y + 9), fill=PAPER, width=2)
        else:
            draw.rounded_rectangle((cx - 4, y + 7, cx + 4, y + size - 7), radius=2, fill=RED)
            draw.rounded_rectangle((x + 7, cy - 4, x + size - 7, cy + 4), radius=2, fill=RED)
    elif kind in ('chip', 'lock'):
        draw.rounded_rectangle((x + 8, y + 8, x + size - 8, y + size - 8), radius=3, fill=dark)
        for offset in (11, 17, 23):
            draw.line((x + offset, y + 5, x + offset, y + 9), fill=dark, width=2)
            draw.line((x + offset, y + size - 9, x + offset, y + size - 5), fill=dark, width=2)
        if kind == 'lock':
            draw.arc((cx - 4, cy - 9, cx + 4, cy + 1), 180, 360, fill=GOLD, width=2)
    elif kind == 'music':
        draw.ellipse((x + 8, y + 21, x + 16, y + 29), fill=RED)
        draw.ellipse((x + 21, y + 17, x + 29, y + 25), fill=RED)
        draw.line((x + 15, y + 22, x + 15, y + 8, x + 28, y + 5, x + 28, y + 19), fill=dark, width=2)
    elif kind == 'medal':
        draw.polygon([(cx - 7, y + 5), (cx - 1, y + 5), (cx - 3, cy), (cx - 8, cy - 1)], fill=RED)
        draw.polygon([(cx + 1, y + 5), (cx + 7, y + 5), (cx + 8, cy - 1), (cx + 3, cy)], fill=BLUE)
        draw.ellipse((cx - 8, cy - 3, cx + 8, cy + 13), fill=GOLD, outline=dark, width=1)
        draw.ellipse((cx - 3, cy + 2, cx + 3, cy + 8), fill=PAPER)
    elif kind == 'star':
        pts = []
        for i in range(10):
            import math
            angle = -math.pi / 2 + i * math.pi / 5
            radius = 12 if i % 2 == 0 else 5
            pts.append((cx + int(math.cos(angle) * radius), cy + int(math.sin(angle) * radius)))
        draw.polygon(pts, fill=GOLD, outline=dark)
    else:
        draw.ellipse((cx - 7, cy - 7, cx + 7, cy + 7), fill=RED)


def draw_story(draw, x, y, width, headline, detail, icon_kind):
    draw_icon(draw, icon_kind, x, y + 10, 34)
    tx = x + 48
    draw.text((tx, y + 1), headline, font=FONT_20, fill=INK, stroke_width=0)
    draw.text((tx, y + 27), detail, font=FONT_16, fill=MUTED)
    draw.line((tx, y + ROW_H - 1, x + width, y + ROW_H - 1), fill='#d8d0c2', width=1)


def draw_region(draw, x, y, width, name, stories):
    draw.rounded_rectangle((x, y, x + width, y + SECTION_HEAD_H), radius=5, fill=BLUE)
    draw.text((x + 14, y + 7), name, font=FONT_22B, fill='#ffffff')
    count = f'{len(stories)} STORIES'
    box = draw.textbbox((0, 0), count, font=FONT_16)
    draw.text((x + width - (box[2] - box[0]) - 14, y + 12), count, font=FONT_16, fill='#ffffff')
    story_y = y + SECTION_HEAD_H
    for headline, detail, icon_kind in stories:
        draw_story(draw, x + 5, story_y, width - 10, headline, detail, icon_kind)
        story_y += ROW_H
    return story_y


def draw_masthead(draw):
    draw.text((58, 30), 'THE WORLD IN ONE DAY', font=FONT_76B, fill=INK)
    draw.text((62, 116), 'Tuesday, 24 November 2026', font=FONT_28B, fill=BLUE)
    draw.text((1230, 58), '35 stories', font=FONT_28B, fill=INK)
    draw.text((1232, 96), '·  7 regions', font=FONT_22B, fill=RED)
    draw.line((58, 170, 1542, 170), fill=RED, width=5)
    draw.line((58, 178, 1542, 178), fill=INK, width=1)


def draw_hero(image, draw):
    top, bottom = 190, 590
    draw.rounded_rectangle((54, top, 1546, bottom), radius=12, fill='#142d4b', outline=RED, width=4)
    # Night sky: restrained stars and a clear Tiangong silhouette.
    stars = [(105, 236), (196, 294), (268, 220), (161, 412), (578, 234), (532, 303), (114, 518), (295, 527)]
    for sx, sy in stars:
        draw.ellipse((sx, sy, sx + 5, sy + 5), fill='#fff4c7')
        draw.line((sx - 4, sy + 2, sx + 9, sy + 2), fill='#fff4c7', width=1)
    # Tiangong and its two solar arrays.
    draw.rectangle((344, 229, 495, 239), fill='#d7e4ef')
    draw.rectangle((397, 215, 443, 253), fill='#e9f0f4', outline=GOLD, width=2)
    draw.rectangle((359, 222, 383, 246), fill='#7698b6', outline='#d7e4ef', width=2)
    draw.rectangle((457, 222, 481, 246), fill='#7698b6', outline='#d7e4ef', width=2)
    for px in (364, 370, 376, 462, 468, 474):
        draw.line((px, 223, px, 245), fill='#b6cce0', width=1)
    draw.line((420, 215, 420, 205), fill='#e9f0f4', width=3)
    draw.ellipse((417, 200, 423, 206), fill=GOLD)
    # Smoke plume behind the ascending launcher.
    for bx, by, br in [(319, 469, 37), (363, 486, 43), (437, 475, 50), (500, 488, 42), (548, 466, 36)]:
        draw.ellipse((bx - br, by - br, bx + br, by + br), fill='#d4d9da')
    draw.ellipse((300, 479, 563, 548), fill='#e4e4dc')
    # Rocket body, nose, porthole and fins.
    draw.polygon([(425, 300), (455, 343), (455, 464), (425, 481), (395, 464), (395, 343)], fill='#f4f1e7', outline=INK)
    draw.polygon([(395, 348), (425, 297), (455, 348)], fill=RED, outline='#f4f1e7')
    draw.rectangle((402, 361, 448, 375), fill=RED)
    draw.ellipse((413, 385, 437, 409), fill='#8db5d1', outline=BLUE, width=3)
    draw.polygon([(395, 433), (373, 470), (404, 459)], fill=RED)
    draw.polygon([(455, 433), (477, 470), (446, 459)], fill=RED)
    draw.rectangle((408, 464, 442, 476), fill='#c8d1d3')
    # Bright exhaust and separated flame tongues.
    draw.polygon([(407, 471), (443, 471), (456, 525), (425, 565), (394, 525)], fill=GOLD)
    draw.polygon([(416, 474), (434, 474), (444, 520), (425, 548), (406, 520)], fill='#f07832')
    draw.polygon([(421, 478), (429, 478), (435, 515), (425, 532), (415, 515)], fill='#fff0a1')
    # Left-side scene label.
    draw.rounded_rectangle((81, 210, 250, 243), radius=7, fill=RED)
    draw.text((95, 216), 'BREAKING • SPACE', font=FONT_16, fill='#ffffff')
    # Story copy at right.
    copy_x = 625
    draw.text((copy_x, 235), 'SHENZHOU-24', font=FONT_34B, fill='#f2b544')
    draw.text((copy_x, 278), 'LIFTS OFF —', font=FONT_34B, fill='#ffffff')
    draw.text((copy_x, 321), "CHINA'S SPACE LEAP", font=FONT_34B, fill='#ffffff')
    draw.line((copy_x, 369, 1492, 369), fill='#7890a8', width=2)
    draw.text((copy_x, 391), 'Two Chinese astronauts and Pakistan’s Zeeshan Ali', font=FONT_20, fill='#ffffff')
    draw.text((copy_x, 420), 'ride to Tiangong — the first foreign astronaut aboard', font=FONT_20, fill='#ffffff')
    draw.text((copy_x, 449), 'China’s outpost.', font=FONT_20, fill='#ffffff')
    draw.text((copy_x, 523), 'TIANGONG  •  3 CREW  •  ORBITAL OUTPOST', font=FONT_16, fill='#c9d7e3')


def draw_footer(draw):
    y = 2090
    draw.line((54, y, 1546, y), fill=RED, width=4)
    draw.rectangle((54, y + 5, 1546, 2191), fill='#eee6d7')
    draw.text((75, y + 17), 'POPE’S DIARY — Francis describes a spiritual crisis and a vision of “the gates of hell.”',
              font=FONT_ITALIC, fill=INK)
    draw.text((75, y + 53), 'Sources: wire reports and official statements, 24 November 2026.',
              font=FONT_16, fill=MUTED)
    draw.text((1441, y + 50), 'WORLD / 01', font=FONT_16, fill=BLUE)


def main():
    image = Image.new('RGB', (W, H), PAPER)
    draw = ImageDraw.Draw(image)
    draw_masthead(draw)
    draw_hero(image, draw)

    left, right, col_w = 54, 816, 730
    y1 = 615
    europe = REGIONS[0][1]
    asia = REGIONS[1][1]
    row1_end = max(draw_region(draw, left, y1, col_w, REGIONS[0][0], europe),
                   draw_region(draw, right, y1, col_w, REGIONS[1][0], asia))

    y2 = row1_end + 17
    middle = draw_region(draw, left, y2, col_w, REGIONS[2][0], REGIONS[2][1])
    africa = draw_region(draw, right, y2, col_w, REGIONS[3][0], REGIONS[3][1])

    y3 = max(middle, africa) + 17
    americas = draw_region(draw, left, y3, col_w, REGIONS[4][0], REGIONS[4][1])
    markets = draw_region(draw, right, y3, col_w, REGIONS[5][0], REGIONS[5][1])

    y4 = max(americas, markets) + 17
    draw_region(draw, 54, y4, 1492, REGIONS[6][0], REGIONS[6][1])
    draw_footer(draw)

    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'entry.png')
    image.save(output_path, format='PNG', optimize=True)
    print(f'Image size: {image.size[0]}x{image.size[1]} px; file size: {os.path.getsize(output_path)} bytes')


if __name__ == '__main__':
    main()
