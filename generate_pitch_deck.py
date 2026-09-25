import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck(lang="uz", output_filename="dont_stop_pitch_deck_uz.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Theme Colors
    BG_DARK = RGBColor(11, 21, 18)       # #0B1512
    CARD_BG = RGBColor(18, 36, 30)       # #12241E
    CARD_BORDER = RGBColor(33, 216, 160) # #21D8A0
    ACCENT_MINT = RGBColor(33, 216, 160) # #21D8A0
    ACCENT_GOLD = RGBColor(255, 184, 0)  # #FFB800
    ACCENT_CYAN = RGBColor(0, 229, 255)  # #00E5FF
    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_MUTED = RGBColor(163, 184, 176)
    TEXT_DARK = RGBColor(11, 21, 18)

    def set_slide_background(slide):
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = BG_DARK

    def add_header(slide, title_text, category_text="DON'T STOP — INVESTOR PITCH DECK"):
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p1 = tf.paragraphs[0]
        p1.text = category_text.upper()
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = ACCENT_MINT
        p1.space_after = Pt(4)
        
        p2 = tf.add_paragraph()
        p2.text = title_text
        p2.font.size = Pt(26)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE

    # Translations for Deck
    content = {
        "uz": {
            "s1_tag": "PRE-SEED • $50 000 • ISHLAYDIGAN WEB ENGINE",
            "s1_title": "Shaharni o'yin maydoniga aylantiradigan hudud egallash va fitness platformasi",
            "s1_subtitle": "Yurish va yugurishni shahar miqyosidagi jamoaviy va taktikal o'yinga aylantiramiz.",
            
            "s2_title": "Muammo va Bozor Imkoniyati",
            "s2_p1_title": "01. Fitness Trekerlar Cheklovi",
            "s2_p1_desc": "Strava va Nike faqat statistikani o'lchaydi, lekin kundalik harakatni jamoaviy o'yinga aylantirmaydi.",
            "s2_p2_title": "02. Yolg'izlik va Motivatsiya Yo'qligi",
            "s2_p2_desc": "Ko'pchilik yuguruvchilar yolg'iz shug'ullanadi. Mahalliy raqobat va jamoaviy maqsad yetishmaydi.",
            "s2_p3_title": "03. Chuqur Guild Mexanikasi Yo'qligi",
            "s2_p3_desc": "Mobil o'yinchilar real dunyoda progressni xohlaydi, mavjud o'yinlarda esa real GPS hudud warfare yo'q.",

            "s3_title": "Mahsulot Qanday Ishlaydi?",
            "s3_step1_title": "1. MARSHRUT",
            "s3_step1_desc": "GPS yopiq kontur va ulanish masofasini real-vaqtda tekshiradi.",
            "s3_step2_title": "2. HUDUD",
            "s3_step2_desc": "Tasdiqlangan kontur ichidagi maydon PostGIS yordamida egallanadi.",
            "s3_step3_title": "3. GILDIYA",
            "s3_step3_desc": "Jamoa hududni himoya qiladi va haftalik reytingda ochko to'playdi.",

            "s4_title": "Gildiya Janglari va Vektor Gerblar",
            "s4_g1_title": "10 Kishilik Gildiyalar",
            "s4_g1_desc": "Do'stlar bilan jamoa tuzing va unique teg ([TAG]) bilan shahar yetakchisiga aylaning.",
            "s4_g2_title": "10 Eksklyuziv Gerb",
            "s4_g2_desc": "Qalqon, Qilichlar, Toj, Yashin, Olov kabi eksklyuziv gerblar bilan jamoa statusini ko'rsating.",

            "s5_title": "Foydalanuvchini Ushlab Qolish va Maxfiylik",
            "s5_r1_title": "HAFTALIK SIKL",
            "s5_r1_desc": "Hudud uchun haftalik bellashuv va sovrinlar yangi maqsad yaratadi.",
            "s5_r2_title": "MAXFIYLIK ZONASI",
            "s5_r2_desc": "200 metrli Privacy Radius uyingiz va shaxsiy manzillaringizni yashiradi.",
            "s5_r3_title": "ANTI-CHEAT",
            "s5_r3_desc": "Teleportatsiyani aniqlash va GPS sifat filtri soxta treklarni bloklaydi.",

            "s6_title": "Raqobatchilar va Don't Stop Ustunligi",
            "s6_c1_title": "Don't Stop",
            "s6_c1_desc": "Real-time Closed-loop GPS + 10-player Guild Warfare + 200m Privacy Radius + Multi-language.",
            "s6_c2_title": "Strava / Nike Run",
            "s6_c2_desc": "Faqat statistikani kuzatish. Jamoaviy hudud egallash va o'yin mexanikasi 0%.",
            "s6_c3_title": "Pokémon GO / Ingress",
            "s6_c3_desc": "Virtual obyektlar. Real yugurish va yopiq kontur maydon hisobi yo'q.",

            "s7_title": "Monetizatsiya va Daromad Modeli",
            "s7_m1_title": "01. BATTLE PASS",
            "s7_m1_desc": "Kosmetik izlar, gerb ramkalari va xarita mavzulari ($4.99 / oy).",
            "s7_m2_title": "02. MIKROTRANSAKSIYA",
            "s7_m2_desc": "Avatar, gildiya tokenlari va nickname pass ($0.99 – $9.99).",
            "s7_m3_title": "03. BREND HAMKORLIGI",
            "s7_m3_desc": "Homiy hududlar va sport kafolari turnirlari ($2K – $10K / event).",
            "s7_m4_title": "04. B2B ANALITIKA",
            "s7_m4_desc": "Anonimlashtirilgan shahar harakati insightlari (Pilotdan keyin).",

            "s8_title": "3 Yillik O'sish Rejasi (Growth Roadmap)",
            "s8_p1_title": "3 OY (Pilot)",
            "s8_p1_desc": "Nukus va Toshkent (15K foydalanuvchi)",
            "s8_p2_title": "6 OY (Regional)",
            "s8_p2_desc": "Samarqand, Olmaota, Chimkent (75K foydalanuvchi)",
            "s8_p3_title": "1 YIL (Xalqaro)",
            "s8_p3_desc": "Istanbul, Astana, Boku (300K foydalanuvchi)",
            "s8_p4_title": "3 YIL (Ekotizim)",
            "s8_p4_desc": "Global B2B homiylar ($4M+ yillik daromad)",

            "s9_title": "$50 000 Pre-Seed Byudjet Taqsimoti",
            "s9_b1_title": "Backend & Spatial API",
            "s9_b1_val": "$12,000 (24%)",
            "s9_b2_title": "Frontend & Mobile",
            "s9_b2_val": "$10,000 (20%)",
            "s9_b3_title": "Game & Spatial Eng.",
            "s9_b3_val": "$10,000 (20%)",
            "s9_b4_title": "Brand & Design",
            "s9_b4_val": "$6,000 (12%)",
            "s9_b5_title": "Marketing & Community",
            "s9_b5_val": "$7,000 (14%)",
            "s9_b6_title": "Server, Legal, Zaxira",
            "s9_b6_val": "$5,000 (10%)",

            "s10_title": "Tayyor Texnologik Asos (Web Engine Ready)",
            "s10_t1_title": "ISHLAYDIGAN WEB ENGINE",
            "s10_t1_desc": "FastAPI + PostGIS + MapLibre GL real-vaqtda GPS konturini hisoblaydi.",
            "s10_t2_title": "105 AVTOMATIK TEST",
            "s10_t2_desc": "100% test qamrovi va toza production build.",
            "s10_t3_title": "MOBILE PIPELINE",
            "s10_t3_desc": "React + Vite + Capacitor orqali Android APK tayyor holatda.",
        },
        "ru": {
            "s1_tag": "PRE-SEED • $50 000 • РАБОЧИЙ WEB ENGINE",
            "s1_title": "Платформа фитнеса и захвата территорий, превращающая город в игровое поле",
            "s1_subtitle": "Превращаем ходьбу и бег в командную и тактическую игру городского масштаба.",
            
            "s2_title": "Проблема и Рыночные Возможности",
            "s2_p1_title": "01. Ограничение Фитнес-Трекеров",
            "s2_p1_desc": "Strava и Nike измеряют показатели, но не превращают ежедневную активность в командную игру.",
            "s2_p2_title": "02. Одиночество и Потеря Мотивации",
            "s2_p2_desc": "Большинство бегунов тренируются поодиночке. Им не хватает локального соперничества.",
            "s2_p3_title": "03. Отсутствие Глубоких Guild-Механик",
            "s2_p3_desc": "Мобильным игрокам нужен прогресс в реальном мире, но на рынке нет реальных GPS guild битв.",

            "s3_title": "Как Работает Продукт?",
            "s3_step1_title": "1. МАРШРУТ",
            "s3_step1_desc": "GPS проверяет замкнутый контур и расстояние до точки соединения в реальном времени.",
            "s3_step2_title": "2. ТЕРРИТОРИЯ",
            "s3_step2_desc": "Площадь внутри замкнутого контура закрепляется с помощью PostGIS.",
            "s3_step3_title": "3. GUILD",
            "s3_step3_desc": "Команда защищает территорию и набирает очки в еженедельном рейтинге.",

            "s4_title": "Guild-Битвы и Векторные Эмблемы",
            "s4_g1_title": "Guild-Команды до 10 человек",
            "s4_g1_desc": "Объединяйтесь с друзьями и используйте уникальный тег ([TAG]) для лидерства в городе.",
            "s4_g2_title": "10 Эксклюзивных Эмблем",
            "s4_g2_desc": "Подчеркните статус команды с помощью гербов Щит, Мечи, Корона, Молния и Огонь.",

            "s5_title": "Удержание Пользователей и Безопасность",
            "s5_r1_title": "НЕДЕЛЬНЫЙ ЦИКЛ",
            "s5_r1_desc": "Еженедельная борьба за территории и турниры создают новую цель.",
            "s5_r2_title": "РАДИУС ПРИВАТНОСТИ",
            "s5_r2_desc": "Приватный радиус 200 метров скрывает домашний адрес игрока.",
            "s5_r3_title": "АНТИЧИТ",
            "s5_r3_desc": "Детекция телепортации и фильтр качества GPS блокируют фейковые треки.",

            "s6_title": "Конкуренты и Преимущество Don't Stop",
            "s6_c1_title": "Don't Stop",
            "s6_c1_desc": "Real-time Closed-loop GPS + 10-player Guild Warfare + 200m Privacy Radius + Multi-language.",
            "s6_c2_title": "Strava / Nike Run",
            "s6_c2_desc": "Только отслеживание статистики. Захват территорий и командные механики 0%.",
            "s6_c3_title": "Pokémon GO / Ingress",
            "s6_c3_desc": "Виртуальные объекты. Нет учета реального бега и замкнутых контуров.",

            "s7_title": "Монетизация и Модель Доходов",
            "s7_m1_title": "01. BATTLE PASS",
            "s7_m1_desc": "Следы, рамки эмблем и темы карты ($4.99 / месяц).",
            "s7_m2_title": "02. МИКРОТРАНЗАКЦИИ",
            "s7_m2_desc": "Аватары, guild-токены и смена имени ($0.99 – $9.99).",
            "s7_m3_title": "03. БРЕНД-ПАРТНЁРСТВА",
            "s7_m3_desc": "Спонсорские зоны и турниры брендов ($2K – $10K / событие).",
            "s7_m4_title": "04. B2B-АНАЛИТИКА",
            "s7_m4_desc": "Анонимизированные данные о городской активности (После пилота).",

            "s8_title": "План Роста на 3 Года (Growth Roadmap)",
            "s8_p1_title": "3 МЕС (Пилот)",
            "s8_p1_desc": "Нукус и Ташкент (15K пользователей)",
            "s8_p2_title": "6 МЕС (Региональный)",
            "s8_p2_desc": "Самарканд, Алматы, Шымкент (75K пользователей)",
            "s8_p3_title": "1 ГОД (Международный)",
            "s8_p3_desc": "Стамбул, Астана, Баку (300K пользователей)",
            "s8_p4_title": "3 ГОДА (Экосистема)",
            "s8_p4_desc": "Глобальные B2B спонсоры ($4M+ выручки в год)",

            "s9_title": "Распределение Инвестиций $50 000",
            "s9_b1_title": "Backend & Spatial API",
            "s9_b1_val": "$12,000 (24%)",
            "s9_b2_title": "Frontend & Mobile",
            "s9_b2_val": "$10,000 (20%)",
            "s9_b3_title": "Game & Spatial Eng.",
            "s9_b3_val": "$10,000 (20%)",
            "s9_b4_title": "Brand & Design",
            "s9_b4_val": "$6,000 (12%)",
            "s9_b5_title": "Marketing & Community",
            "s9_b5_val": "$7,000 (14%)",
            "s9_b6_title": "Server, Legal, Резерв",
            "s9_b6_val": "$5,000 (10%)",

            "s10_title": "Технологическая База (Web Engine Ready)",
            "s10_t1_title": "РАБОЧИЙ WEB ENGINE",
            "s10_t1_desc": "FastAPI + PostGIS + MapLibre GL рассчитывают GPS-контур в реальном времени.",
            "s10_t2_title": "105 АВТОТЕСТОВ",
            "s10_t2_desc": "100% покрытие тестами и чистый production сборка.",
            "s10_t3_title": "MOBILE PIPELINE",
            "s10_t3_desc": "React + Vite + Capacitor готовы для генерации Android APK.",
        },
        "en": {
            "s1_tag": "PRE-SEED • $50,000 • WORKING WEB ENGINE",
            "s1_title": "A territory capture fitness platform turning the city into a live game board",
            "s1_subtitle": "Turning daily walking and running into a city-scale team game.",
            
            "s2_title": "Problem & Market Opportunity",
            "s2_p1_title": "01. Fitness Trackers Limit",
            "s2_p1_desc": "Strava and Nike track metrics, but miss turning daily movement into a team sport.",
            "s2_p2_title": "02. Solo Workout Burnout",
            "s2_p2_desc": "Most runners train alone. Local rivalry and shared team objectives are missing.",
            "s2_p3_title": "03. Missing Guild Warfare",
            "s2_p3_desc": "Mobile gamers want real-world progress, but deep real-world GPS guild mechanics are rare.",

            "s3_title": "How Does The Product Work?",
            "s3_step1_title": "1. ROUTE",
            "s3_step1_desc": "GPS validates closed loop and calculates connection gap in real time.",
            "s3_step2_title": "2. TERRITORY",
            "s3_step2_desc": "Verified loop area becomes captured ground using PostGIS geometry.",
            "s3_step3_title": "3. GUILD",
            "s3_step3_desc": "Teams defend territory and earn points in weekly leaderboards.",

            "s4_title": "Guild Warfare & Vector Emblems",
            "s4_g1_title": "10-Player Guilds",
            "s4_g1_desc": "Form a 10-member squad with a unique tag ([TAG]) to dominate city rankings.",
            "s4_g2_title": "10 Exclusive Badges",
            "s4_g2_desc": "Signal your team status with vector emblems like Shield, Swords, Crown, Zap, and Flame.",

            "s5_title": "User Retention & Safety",
            "s5_r1_title": "WEEKLY LOOP",
            "s5_r1_desc": "Weekly territory reset and tournament leaderboards drive recurring engagement.",
            "s5_r2_title": "PRIVACY RADIUS",
            "s5_r2_desc": "200-meter Privacy Radius obfuscates home address locations.",
            "s5_r3_title": "ANTI-CHEAT",
            "s5_r3_desc": "Teleport detection and GPS quality filter block spoofed routes.",

            "s6_title": "Competitive Matrix & Don't Stop Advantage",
            "s6_c1_title": "Don't Stop",
            "s6_c1_desc": "Real-time Closed-loop GPS + 10-player Guild Warfare + 200m Privacy Radius + Multi-language.",
            "s6_c2_title": "Strava / Nike Run",
            "s6_c2_desc": "Pure stats tracking. 0% team territory capture or gaming mechanics.",
            "s6_c3_title": "Pokémon GO / Ingress",
            "s6_c3_desc": "Virtual POIs. Lacks real running closed-loop area calculations.",

            "s7_title": "Monetization & Business Model",
            "s7_m1_title": "01. BATTLE PASS",
            "s7_m1_desc": "Cosmetic trails, emblem borders and map themes ($4.99 / month).",
            "s7_m2_title": "02. MICROTRANSACTIONS",
            "s7_m2_desc": "Avatars, guild tokens and name change passes ($0.99 – $9.99).",
            "s7_m3_title": "03. BRAND PARTNERSHIPS",
            "s7_m3_desc": "Sponsored zones and branded tournaments ($2K – $10K / event).",
            "s7_m4_title": "04. B2B ANALYTICS",
            "s7_m4_desc": "Anonymized urban activity foot-traffic insights (Post-pilot).",

            "s8_title": "3-Year Growth Roadmap",
            "s8_p1_title": "3 MONTHS (Pilot)",
            "s8_p1_desc": "Nukus and Tashkent (15K users)",
            "s8_p2_title": "6 MONTHS (Regional)",
            "s8_p2_desc": "Samarkand, Almaty, Shymkent (75K users)",
            "s8_p3_title": "1 YEAR (International)",
            "s8_p3_desc": "Istanbul, Astana, Baku (300K users)",
            "s8_p4_title": "3 YEARS (Ecosystem)",
            "s8_p4_desc": "Global B2B sponsors ($4M+ annual revenue)",

            "s9_title": "Use of $50,000 Investment",
            "s9_b1_title": "Backend & Spatial API",
            "s9_b1_val": "$12,000 (24%)",
            "s9_b2_title": "Frontend & Mobile",
            "s9_b2_val": "$10,000 (20%)",
            "s9_b3_title": "Game & Spatial Eng.",
            "s9_b3_val": "$10,000 (20%)",
            "s9_b4_title": "Brand & Design",
            "s9_b4_val": "$6,000 (12%)",
            "s9_b5_title": "Marketing & Community",
            "s9_b5_val": "$7,000 (14%)",
            "s9_b6_title": "Server, Legal, Reserve",
            "s9_b6_val": "$5,000 (10%)",

            "s10_title": "Working Tech Foundation (Engine Ready)",
            "s10_t1_title": "WORKING WEB ENGINE",
            "s10_t1_desc": "FastAPI + PostGIS + MapLibre GL calculate real-time GPS loops.",
            "s10_t2_title": "105 AUTOMATED TESTS",
            "s10_t2_desc": "100% test pass rate and clean production build.",
            "s10_t3_title": "MOBILE PIPELINE",
            "s10_t3_desc": "React + Vite + Capacitor ready for instant Android APK generation.",
        }
    }

    t = content[lang]

    # SLIDE 1: Cover Slide
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1)
    
    tb1 = slide1.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.7), Inches(4.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p1 = tf1.paragraphs[0]
    p1.text = t["s1_tag"]
    p1.font.size = Pt(13)
    p1.font.bold = True
    p1.font.color.rgb = ACCENT_GOLD
    p1.space_after = Pt(14)

    p2 = tf1.add_paragraph()
    p2.text = "DON'T STOP"
    p2.font.size = Pt(54)
    p2.font.bold = True
    p2.font.color.rgb = ACCENT_MINT
    p2.space_after = Pt(10)

    p3 = tf1.add_paragraph()
    p3.text = t["s1_title"]
    p3.font.size = Pt(24)
    p3.font.bold = True
    p3.font.color.rgb = TEXT_WHITE
    p3.space_after = Pt(10)

    p4 = tf1.add_paragraph()
    p4.text = t["s1_subtitle"]
    p4.font.size = Pt(16)
    p4.font.color.rgb = TEXT_MUTED

    # Helper function for card addition
    def add_card(slide, left, top, width, height, title, desc, border_color=CARD_BORDER, title_color=ACCENT_MINT):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = CARD_BG
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.5)
        
        tb = slide.shapes.add_textbox(left + Inches(0.15), top + Inches(0.15), width - Inches(0.3), height - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.size = Pt(16)
        p1.font.bold = True
        p1.font.color.rgb = title_color
        p1.space_after = Pt(6)
        
        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(13)
        p2.font.color.rgb = TEXT_MUTED

    # SLIDE 2: Problem & Opportunity
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    add_header(slide2, t["s2_title"])
    add_card(slide2, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), t["s2_p1_title"], t["s2_p1_desc"])
    add_card(slide2, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), t["s2_p2_title"], t["s2_p2_desc"])
    add_card(slide2, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.8), t["s2_p3_title"], t["s2_p3_desc"])

    # SLIDE 3: How Product Works
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_header(slide3, t["s3_title"])
    add_card(slide3, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), t["s3_step1_title"], t["s3_step1_desc"], border_color=ACCENT_CYAN, title_color=ACCENT_CYAN)
    add_card(slide3, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), t["s3_step2_title"], t["s3_step2_desc"], border_color=ACCENT_GOLD, title_color=ACCENT_GOLD)
    add_card(slide3, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.8), t["s3_step3_title"], t["s3_step3_desc"], border_color=ACCENT_MINT, title_color=ACCENT_MINT)

    # SLIDE 4: Guild Warfare
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4)
    add_header(slide4, t["s4_title"])
    add_card(slide4, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), t["s4_g1_title"], t["s4_g1_desc"], title_color=ACCENT_GOLD)
    add_card(slide4, Inches(6.8), Inches(1.8), Inches(5.6), Inches(4.8), t["s4_g2_title"], t["s4_g2_desc"], title_color=ACCENT_MINT)

    # SLIDE 5: Retention & Privacy
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5)
    add_header(slide5, t["s5_title"])
    add_card(slide5, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), t["s5_r1_title"], t["s5_r1_desc"])
    add_card(slide5, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), t["s5_r2_title"], t["s5_r2_desc"], border_color=ACCENT_CYAN, title_color=ACCENT_CYAN)
    add_card(slide5, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.8), t["s5_r3_title"], t["s5_r3_desc"], border_color=ACCENT_GOLD, title_color=ACCENT_GOLD)

    # SLIDE 6: Competitive Matrix
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6)
    add_header(slide6, t["s6_title"])
    add_card(slide6, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), t["s6_c1_title"], t["s6_c1_desc"], border_color=ACCENT_MINT, title_color=ACCENT_MINT)
    add_card(slide6, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), t["s6_c2_title"], t["s6_c2_desc"], border_color=CARD_BORDER, title_color=TEXT_MUTED)
    add_card(slide6, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.8), t["s6_c3_title"], t["s6_c3_desc"], border_color=CARD_BORDER, title_color=TEXT_MUTED)

    # SLIDE 7: Monetization
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7)
    add_header(slide7, t["s7_title"])
    add_card(slide7, Inches(0.8), Inches(1.8), Inches(2.7), Inches(4.8), t["s7_m1_title"], t["s7_m1_desc"])
    add_card(slide7, Inches(3.8), Inches(1.8), Inches(2.7), Inches(4.8), t["s7_m2_title"], t["s7_m2_desc"])
    add_card(slide7, Inches(6.8), Inches(1.8), Inches(2.7), Inches(4.8), t["s7_m3_title"], t["s7_m3_desc"], border_color=ACCENT_GOLD, title_color=ACCENT_GOLD)
    add_card(slide7, Inches(9.8), Inches(1.8), Inches(2.7), Inches(4.8), t["s7_m4_title"], t["s7_m4_desc"], border_color=ACCENT_CYAN, title_color=ACCENT_CYAN)

    # SLIDE 8: Growth Roadmap
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8)
    add_header(slide8, t["s8_title"])
    add_card(slide8, Inches(0.8), Inches(1.8), Inches(2.7), Inches(4.8), t["s8_p1_title"], t["s8_p1_desc"])
    add_card(slide8, Inches(3.8), Inches(1.8), Inches(2.7), Inches(4.8), t["s8_p2_title"], t["s8_p2_desc"])
    add_card(slide8, Inches(6.8), Inches(1.8), Inches(2.7), Inches(4.8), t["s8_p3_title"], t["s8_p3_desc"])
    add_card(slide8, Inches(9.8), Inches(1.8), Inches(2.7), Inches(4.8), t["s8_p4_title"], t["s8_p4_desc"], border_color=ACCENT_GOLD, title_color=ACCENT_GOLD)

    # SLIDE 9: Budget Allocation
    slide9 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide9)
    add_header(slide9, t["s9_title"])
    add_card(slide9, Inches(0.8), Inches(1.8), Inches(3.6), Inches(2.2), t["s9_b1_title"], t["s9_b1_val"])
    add_card(slide9, Inches(4.8), Inches(1.8), Inches(3.6), Inches(2.2), t["s9_b2_title"], t["s9_b2_val"])
    add_card(slide9, Inches(8.8), Inches(1.8), Inches(3.6), Inches(2.2), t["s9_b3_title"], t["s9_b3_val"])
    add_card(slide9, Inches(0.8), Inches(4.4), Inches(3.6), Inches(2.2), t["s9_b4_title"], t["s9_b4_val"])
    add_card(slide9, Inches(4.8), Inches(4.4), Inches(3.6), Inches(2.2), t["s9_b5_title"], t["s9_b5_val"])
    add_card(slide9, Inches(8.8), Inches(4.4), Inches(3.6), Inches(2.2), t["s9_b6_title"], t["s9_b6_val"], border_color=ACCENT_GOLD, title_color=ACCENT_GOLD)

    # SLIDE 10: Tech Foundation
    slide10 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide10)
    add_header(slide10, t["s10_title"])
    add_card(slide10, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), t["s10_t1_title"], t["s10_t1_desc"])
    add_card(slide10, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), t["s10_t2_title"], t["s10_t2_desc"], border_color=ACCENT_CYAN, title_color=ACCENT_CYAN)
    add_card(slide10, Inches(8.8), Inches(1.8), Inches(3.6), Inches(4.8), t["s10_t3_title"], t["s10_t3_desc"], border_color=ACCENT_GOLD, title_color=ACCENT_GOLD)

    prs.save(output_filename)
    print(f"Successfully generated {output_filename}")

if __name__ == "__main__":
    os.makedirs("public/presentations", exist_ok=True)
    create_deck("uz", "public/presentations/dont_stop_pitch_deck_uz.pptx")
    create_deck("ru", "public/presentations/dont_stop_pitch_deck_ru.pptx")
    create_deck("en", "public/presentations/dont_stop_pitch_deck_en.pptx")
    create_deck("uz", "dont_stop_investor_pitch_deck.pptx")
