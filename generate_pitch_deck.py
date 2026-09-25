import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    # Set 16:9 Widescreen dimensions
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

    def add_header(slide, title_text, category_text="DON'T STOP — PITCH DECK"):
        # Header text container
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        # Category / Eyebrow
        p1 = tf.paragraphs[0]
        p1.text = category_text.upper()
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = ACCENT_MINT
        p1.space_after = Pt(4)
        
        # Title
        p2 = tf.add_paragraph()
        p2.text = title_text
        p2.font.size = Pt(26)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE

    # -------------------------------------------------------------------------
    # SLIDE 1: Cover Slide
    # -------------------------------------------------------------------------
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1)

    # Accent decorative background shape
    card1 = slide1.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(1.0), Inches(1.2), Inches(11.333), Inches(5.1)
    )
    card1.fill.solid()
    card1.fill.fore_color.rgb = CARD_BG
    card1.line.color.rgb = CARD_BORDER
    card1.line.width = Pt(1.5)

    tb = slide1.shapes.add_textbox(Inches(1.6), Inches(1.8), Inches(10.133), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "DON'T STOP"
    p.font.size = Pt(46)
    p.font.bold = True
    p.font.color.rgb = ACCENT_MINT
    p.space_after = Pt(6)

    p = tf.add_paragraph()
    p.text = "REAL-WORLD TERRITORY CAPTURE & GAMIFIED FITNESS PLATFORM"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(20)

    p = tf.add_paragraph()
    p.text = "Turning daily walking and running into competitive guild territory control."
    p.font.size = Pt(15)
    p.font.color.rgb = TEXT_MUTED
    p.space_after = Pt(36)

    # Key highlights pill box
    p = tf.add_paragraph()
    p.text = "🎯 Target Funding Ask: $50,000 USD (Pre-Seed)   |   📍 Stage: Fully Built & Test-Verified Web Engine"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD

    # -------------------------------------------------------------------------
    # SLIDE 2: Problem & Opportunity
    # -------------------------------------------------------------------------
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    add_header(slide2, "The Problem & Market Opportunity")

    # Left Box - Problem
    c_prob = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(5.6), Inches(5.1))
    c_prob.fill.solid()
    c_prob.fill.fore_color.rgb = CARD_BG
    c_prob.line.color.rgb = RGBColor(255, 59, 48)
    c_prob.line.width = Pt(1.5)

    tf_prob = c_prob.text_frame
    tf_prob.word_wrap = True
    tf_prob.margin_left = tf_prob.margin_right = tf_prob.margin_top = Inches(0.3)

    p = tf_prob.paragraphs[0]
    p.text = "⚠️ THE PROBLEM"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 59, 48)
    p.space_after = Pt(14)

    problems = [
        ("Boring Fitness Apps:", "Traditional tracking apps (Strava, Nike Run) feel like work, leading to high 30-day user churn."),
        ("Lack of Social Pride:", "Users run alone without meaningful team goals or local territory control."),
        ("Gamification Gap:", "Mobile gamers want real-world movement mechanics, but existing apps lack deep guild systems.")
    ]
    for title, desc in problems:
        p = tf_prob.add_paragraph()
        p.text = f"• {title} "
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(2)
        
        p_desc = tf_prob.add_paragraph()
        p_desc.text = f"  {desc}"
        p_desc.font.size = Pt(12)
        p_desc.font.color.rgb = TEXT_MUTED
        p_desc.space_after = Pt(12)

    # Right Box - Solution & Opportunity
    c_sol = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.7), Inches(5.6), Inches(5.1))
    c_sol.fill.solid()
    c_sol.fill.fore_color.rgb = CARD_BG
    c_sol.line.color.rgb = ACCENT_MINT
    c_sol.line.width = Pt(1.5)

    tf_sol = c_sol.text_frame
    tf_sol.word_wrap = True
    tf_sol.margin_left = tf_sol.margin_right = tf_sol.margin_top = Inches(0.3)

    p = tf_sol.paragraphs[0]
    p.text = "🚀 THE SOLUTION & MARKET"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_MINT
    p.space_after = Pt(14)

    solutions = [
        ("Gamified Fitness Turf Warfare:", "Walk or run in closed loops to capture city ground on interactive live maps."),
        ("Guild Power & Social Rivalry:", "Form 10-member Guilds with custom Vector Emblems, tags, and team tactics."),
        ("Massive Market Potential:", "Crossing the $14B Move-to-Earn / Gamified Fitness & $180B Mobile Gaming markets.")
    ]
    for title, desc in solutions:
        p = tf_sol.add_paragraph()
        p.text = f"✔ {title} "
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(2)

        p_desc = tf_sol.add_paragraph()
        p_desc.text = f"  {desc}"
        p_desc.font.size = Pt(12)
        p_desc.font.color.rgb = TEXT_MUTED
        p_desc.space_after = Pt(12)

    # -------------------------------------------------------------------------
    # SLIDE 3: Product & Core Technology
    # -------------------------------------------------------------------------
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_header(slide3, "Core Product Architecture & Key Features")

    features = [
        ("📍 Closed-Loop GPS Tracking", "Real-time vector loop preview & connection gap calculation via high-precision Kalman filtering."),
        ("🛡️ 10-Member Guild System", "Custom Vector Emblems (Shield, Swords, Crown, Zap, Flame, Trophy, Gem, Target, Citadel, Skull)."),
        ("🔒 Privacy & Anti-Cheat", "200m Privacy Radius hide-home protection, PostGIS spatial exclusions (schools/buildings), teleport detection."),
        ("🌐 5-Language Engine", "Full localization in Karakalpak (qq), Uzbek (uz), Kazakh (kk), Turkish (tr), and English (en)."),
        ("⚡ High Performance Stack", "FastAPI Python backend + PostGIS spatial DB + Redis + MapLibre GL vector rendering.")
    ]

    for idx, (title, desc) in enumerate(features):
        row = idx // 2
        col = idx % 2
        
        if idx == 4: # Center bottom
            w, h = Inches(11.7), Inches(1.3)
            x, y = Inches(0.8), Inches(5.5)
        else:
            w, h = Inches(5.6), Inches(1.6)
            x = Inches(0.8) if col == 0 else Inches(6.9)
            y = Inches(1.8) + Inches(1.8 * row)

        c = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = ACCENT_MINT if idx % 2 == 0 else ACCENT_CYAN
        c.line.width = Pt(1.2)

        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GOLD if idx == 2 else TEXT_WHITE
        p.space_after = Pt(4)

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(12)
        p2.font.color.rgb = TEXT_MUTED

    # -------------------------------------------------------------------------
    # SLIDE 4: Business Model & Monetization
    # -------------------------------------------------------------------------
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4)
    add_header(slide4, "Monetization Strategy & Revenue Streams")

    models = [
        ("🎟️ Seasonal Battle Pass", "Cosmetic territory trail effects, exclusive Guild Emblems, custom map color themes ($4.99/mo)."),
        ("🏢 B2B Brand Sponsorships", "Local brands sponsor 2x Territory Events, branded capture zones, and sponsored tournaments ($2K–$10K/event)."),
        ("💎 Microtransactions", "Guild creation tokens, premium avatar customization items, nickname change passes ($0.99–$9.99)."),
        ("📊 B2B Fitness Analytics", "Anonymized urban mobility insights for municipal planning & fitness brand partnerships.")
    ]

    for idx, (title, desc) in enumerate(models):
        x = Inches(0.8 + (idx % 2) * 6.1)
        y = Inches(1.8 + (idx // 2) * 2.6)
        
        c = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(5.6), Inches(2.3))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = CARD_BORDER
        c.line.width = Pt(1.5)

        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.25)

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GOLD if idx == 1 else ACCENT_MINT
        p.space_after = Pt(8)

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(13)
        p2.font.color.rgb = TEXT_MUTED

    # -------------------------------------------------------------------------
    # SLIDE 5: 3-Year Growth Roadmap & Forecast (3M, 6M, 1Y, 2Y, 3Y)
    # -------------------------------------------------------------------------
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5)
    add_header(slide5, "Growth Forecast & 3-Year Milestones")

    milestones = [
        ("3 Months", "Pilot Launch", "15K Users", "500 Guilds", "Nukus & Tashkent rollout, APK release."),
        ("6 Months", "Regional Push", "75K Users", "2.5K Guilds", "Samarkand, Almaty, Shymkent ($12K/mo rev)."),
        ("1 Year", "Multi-Country", "300K Users", "10K Guilds", "Istanbul, Astana, Baku ($50K/mo rev)."),
        ("2 Years", "Global Expansion", "1.2M Users", "40K Guilds", "MENA & Eastern Europe ($180K/mo rev)."),
        ("3 Years", "Ecosystem Scale", "4.5M Users", "150K Guilds", "Global B2B Sponsors ($4M+ Annual Rev).")
    ]

    col_width = Inches(2.2)
    col_gap = Inches(0.18)

    for idx, (period, stage, users, guilds, details) in enumerate(milestones):
        x = Inches(0.8 + idx * (col_width + col_gap))
        y = Inches(1.8)

        c = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, col_width, Inches(5.1))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = ACCENT_GOLD if idx == 2 else (ACCENT_MINT if idx < 2 else ACCENT_CYAN)
        c.line.width = Pt(1.5)

        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.15)

        p = tf.paragraphs[0]
        p.text = period
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GOLD if idx == 2 else ACCENT_MINT
        p.space_after = Pt(2)

        p_stage = tf.add_paragraph()
        p_stage.text = stage
        p_stage.font.size = Pt(11)
        p_stage.font.bold = True
        p_stage.font.color.rgb = TEXT_WHITE
        p_stage.space_after = Pt(10)

        # Users pill
        p_u = tf.add_paragraph()
        p_u.text = f"👥 {users}"
        p_u.font.size = Pt(13)
        p_u.font.bold = True
        p_u.font.color.rgb = ACCENT_CYAN
        p_u.space_after = Pt(4)

        # Guilds pill
        p_g = tf.add_paragraph()
        p_g.text = f"🛡️ {guilds}"
        p_g.font.size = Pt(12)
        p_g.font.bold = True
        p_g.font.color.rgb = ACCENT_GOLD
        p_g.space_after = Pt(12)

        p_det = tf.add_paragraph()
        p_det.text = details
        p_det.font.size = Pt(11)
        p_det.font.color.rgb = TEXT_MUTED

    # -------------------------------------------------------------------------
    # SLIDE 6: Investment Ask & Budget Allocation ($50,000 Minimum)
    # -------------------------------------------------------------------------
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6)
    add_header(slide6, "Funding Request: Minimum $50,000 USD (12-Month Runway)")

    # Left Side: High Level Investment Summary
    c_sum = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(4.2), Inches(5.1))
    c_sum.fill.solid()
    c_sum.fill.fore_color.rgb = CARD_BG
    c_sum.line.color.rgb = ACCENT_GOLD
    c_sum.line.width = Pt(2)

    tf_sum = c_sum.text_frame
    tf_sum.word_wrap = True
    tf_sum.margin_left = tf_sum.margin_right = tf_sum.margin_top = Inches(0.3)

    p = tf_sum.paragraphs[0]
    p.text = "💰 INVESTMENT ASK"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(10)

    p_amt = tf_sum.add_paragraph()
    p_amt.text = "$50,000 USD"
    p_amt.font.size = Pt(32)
    p_amt.font.bold = True
    p_amt.font.color.rgb = ACCENT_MINT
    p_amt.space_after = Pt(16)

    summary_bullets = [
        "12-Month Operational Runway",
        "Full Mobile APK Launch & Growth",
        "Team Salary Coverage (5 Key Roles)",
        "Server & Map Infrastructure Scale",
        "Local Influencer & Campus Marketing"
    ]
    for b in summary_bullets:
        p = tf_sum.add_paragraph()
        p.text = f"✔  {b}"
        p.font.size = Pt(12)
        p.font.color.rgb = TEXT_WHITE
        p.space_after = Pt(8)

    # Right Side: Detailed Budget Table / Allocation Cards
    budget_items = [
        ("Backend Developer", "$12,000", "24%", "Spatial PostGIS API, Anti-cheat algorithms, Real-time WebSockets"),
        ("Frontend & UI/UX Developer", "$10,000", "20%", "MapLibre GL Vector UI, Capacitor Mobile App, Responsive Dashboards"),
        ("Game Dev / Spatial Engineer", "$10,000", "20%", "Closed-loop vector math, Territory decay engine, Mobile bridge"),
        ("Graphic & Brand Designer", "$6,000", "12%", "Vector emblem badges, UI assets, Marketing kits & social branding"),
        ("Marketing & Community Mgr", "$7,000", "14%", "Influencer campaigns, TikTok/Instagram viral runs, Campus leagues"),
        ("Server & Infrastructure", "$5,000", "10%", "PostGIS Database, Redis cluster, Map tiles, Legal & Contingency")
    ]

    for idx, (role, cost, pct, desc) in enumerate(budget_items):
        y = Inches(1.8 + idx * 0.83)
        c_item = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(5.3), y, Inches(7.2), Inches(0.75))
        c_item.fill.solid()
        c_item.fill.fore_color.rgb = CARD_BG
        c_item.line.color.rgb = CARD_BORDER
        c_item.line.width = Pt(1)

        tf_item = c_item.text_frame
        tf_item.word_wrap = True
        tf_item.margin_left = Inches(0.2)
        tf_item.margin_top = Inches(0.1)

        p = tf_item.paragraphs[0]
        p.text = f"{role}  —  "
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE

        run_amt = p.add_run()
        run_amt.text = f"{cost} ({pct})"
        run_amt.font.bold = True
        run_amt.font.color.rgb = ACCENT_GOLD

        p_d = tf_item.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(10.5)
        p_d.font.color.rgb = TEXT_MUTED

    # -------------------------------------------------------------------------
    # SLIDE 7: Execution Plan & Handoff Readiness
    # -------------------------------------------------------------------------
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7)
    add_header(slide7, "Technical Execution & Mobile Handoff")

    cards = [
        ("💻 Fully Functional Web Stack", "FastAPI Python backend + PostGIS spatial database + MapLibre GL frontend engine already 100% built and verified with 105 automated unit/integration tests."),
        ("📱 Turnkey Mobile APK Pipeline", "Frontend built with React + Vite + Capacitor wrapper pipeline, allowing instant mobile APK/AAB builds for Android Play Store and Apple App Store."),
        ("🔒 Production Security & Quality", "Strict 8-digit numeric Player ID system, 200m Privacy Radius protection, spatial building exclusions, and multi-language engine (QQ, UZ, KK, TR, EN).")
    ]

    for idx, (title, desc) in enumerate(cards):
        x = Inches(0.8 + idx * 4.0)
        c = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, Inches(1.8), Inches(3.7), Inches(5.1))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = ACCENT_MINT if idx == 0 else (ACCENT_CYAN if idx == 1 else ACCENT_GOLD)
        c.line.width = Pt(1.5)

        tf = c.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.25)

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = ACCENT_MINT if idx == 0 else (ACCENT_CYAN if idx == 1 else ACCENT_GOLD)
        p.space_after = Pt(14)

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(13)
        p2.font.color.rgb = TEXT_WHITE

    # -------------------------------------------------------------------------
    # SLIDE 8: Call to Action / Closing
    # -------------------------------------------------------------------------
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8)

    c_close = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.5), Inches(10.333), Inches(4.5))
    c_close.fill.solid()
    c_close.fill.fore_color.rgb = CARD_BG
    c_close.line.color.rgb = ACCENT_MINT
    c_close.line.width = Pt(2)

    tf_close = c_close.text_frame
    tf_close.word_wrap = True
    tf_close.margin_left = tf_close.margin_right = tf_close.margin_top = Inches(0.5)

    p = tf_close.paragraphs[0]
    p.text = "JOIN THE REAL-WORLD GAMING REVOLUTION"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = ACCENT_MINT
    p.space_after = Pt(12)

    p = tf_close.add_paragraph()
    p.text = "Don't Stop turns cities into live interactive gaming battlegrounds."
    p.font.size = Pt(16)
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(24)

    p = tf_close.add_paragraph()
    p.text = "💼 Minimum Funding Ask: $50,000 USD (Pre-Seed)"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(8)

    p = tf_close.add_paragraph()
    p.text = "🚀 Web Engine Live & Ready for Mobile APK Deployment"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT_CYAN

    # Save Presentation
    output_dir = r"c:\Users\hylgi\OneDrive\Desktop\Новая папка (2)"
    output_path = os.path.join(output_dir, "dont_stop_investor_pitch_deck.pptx")
    prs.save(output_path)
    print(f"Presentation successfully saved to: {output_path}")

if __name__ == "__main__":
    create_presentation()
