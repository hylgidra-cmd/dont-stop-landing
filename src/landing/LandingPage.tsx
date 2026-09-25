import { useState } from 'react';
import {
  Download,
  FileText,
  MapPin,
  Play,
  Shield,
  ShieldAlert,
  Sparkles,
  Swords,
  Trophy,
  User,
  Zap,
} from 'lucide-react';
import {
  getLanguage,
  setLanguage,
  type LanguageCode,
} from '../i18n';
import { getActiveDict } from '../i18n/state';
import { GUILD_EMBLEMS_LIST, GuildEmblem } from '../profile/GuildEmblem';

const REDIRECT_MAP_URL = 'https://qalarun-web.onrender.com';

export function LandingPage() {
  const [currentLang, setCurrentLang] = useState<LanguageCode>(getLanguage());
  const [activeDeckTab, setActiveDeckTab] = useState<'uz' | 'ru' | 'en'>(getLanguage());

  const dict: Record<string, any> = (getActiveDict() as any) || {};

  const handleLangChange = (code: LanguageCode) => {
    setLanguage(code);
    setCurrentLang(code);
    setActiveDeckTab(code);
  };

  const handleGoToMap = () => {
    window.open(REDIRECT_MAP_URL, '_blank');
  };

  const deckFiles = {
    uz: {
      title: "O'zbekcha Taqdimot (UZB Deck)",
      langName: "O'zbekcha",
      flag: '🇺🇿',
      pptxUrl: './presentations/dont_stop_pitch_deck_uz.pptx',
      imgUrl: './presentations/pitch_deck_uz.png',
      slidesCount: 8,
      size: '5.9 MB',
      description: "Pre-Seed $50,000 investitsiya rejasi, 3 yillik moliyaviy prognoz va texnik infratuzilma haqida to'liq ma'lumotlar.",
    },
    ru: {
      title: 'Презентация на русском (RUS Deck)',
      langName: 'Русский',
      flag: '🇷🇺',
      pptxUrl: './presentations/dont_stop_pitch_deck_ru.pptx',
      imgUrl: './presentations/pitch_deck_ru.png',
      slidesCount: 8,
      size: '5.9 MB',
      description: 'Полная информация об инвестиционном плане Pre-Seed $50 000, 3-летнем финансовом прогнозе и стеке технологий.',
    },
    en: {
      title: 'English Pitch Deck (ENG Deck)',
      langName: 'English',
      flag: '🇬🇧',
      pptxUrl: './presentations/dont_stop_pitch_deck_en.pptx',
      imgUrl: './presentations/pitch_deck_en.png',
      slidesCount: 8,
      size: '5.9 MB',
      description: 'Comprehensive investor overview covering the $50,000 Pre-Seed plan, 3-year growth forecast, and tech roadmap.',
    },
  };

  return (
    <div className="landing-shell">
      {/* ── Landing Header ────────────────────────────────────────── */}
      <header className="landing-nav">
        <div className="landing-nav-container">
          <div className="landing-brand" onClick={handleGoToMap} style={{ cursor: 'pointer' }}>
            <span className="brand-mark">DS</span>
            <div className="brand-titles">
              <span className="brand-title">DON'T STOP</span>
              <span className="brand-sub">TERRITORY CAPTURE</span>
            </div>
          </div>

          <nav className="landing-menu">
            <a href="#features">{dict.nav?.features || "Imkoniyatlar"}</a>
            <a href="#presentation">{dict.nav?.presentation || "Taqdimot"}</a>
            <a href="#guilds">{dict.nav?.guilds || "Gildiyalar"}</a>
            <a href="#how-it-works">{dict.nav?.howItWorks || "Qanday ishlaydi"}</a>
          </nav>

          <div className="landing-nav-actions">
            {/* Sleek 3-Pill Language Selector */}
            <div className="header-lang-pills">
              <button
                type="button"
                className={`lang-pill-btn ${currentLang === 'uz' ? 'active' : ''}`}
                onClick={() => handleLangChange('uz')}
              >
                🇺🇿 UZB
              </button>
              <button
                type="button"
                className={`lang-pill-btn ${currentLang === 'ru' ? 'active' : ''}`}
                onClick={() => handleLangChange('ru')}
              >
                🇷🇺 RUS
              </button>
              <button
                type="button"
                className={`lang-pill-btn ${currentLang === 'en' ? 'active' : ''}`}
                onClick={() => handleLangChange('en')}
              >
                🇬🇧 ENG
              </button>
            </div>

            <button type="button" className="landing-btn-primary" onClick={handleGoToMap}>
              <Play size={15} fill="#10251F" /> <span>{dict.hero?.ctaStart || "Xaritaga O'tish"}</span>
            </button>
          </div>
        </div>
      </header>

      {/* ── Hero Section ──────────────────────────────────────────── */}
      <section className="landing-hero">
        <div className="hero-content">
          <div className="hero-pill">
            <Sparkles size={14} style={{ color: '#FFB800' }} />
            <span>{dict.hero?.tag || "GPS HUDUDLAR • GILDIYA TURNIRLARI"}</span>
          </div>

          <h1 className="hero-title">
            {dict.hero?.title || "SHAHAR SEN BILAN O'YNAYDI"}
          </h1>

          <p className="hero-subtitle">
            {dict.hero?.subtitle || "Real hayotdagi ko'chalarda yuguring, yuring va 10 kishilik Gildiyangiz bilan shahar kvartallarini bosib oling."}
          </p>

          <div className="hero-cta-group">
            <button type="button" className="hero-main-btn" onClick={handleGoToMap}>
              <Play size={18} fill="#10251F" /> <span>{dict.hero?.ctaStart || "Xaritaga O'tish"}</span>
            </button>

            <a href="#presentation" className="hero-presentation-btn">
              <FileText size={18} /> <span>{dict.hero?.investorDeck || "Investor Taqdimoti (PPTX)"}</span>
            </a>
          </div>

          <div className="hero-stats-row">
            <div className="hero-stat-card">
              <Zap size={20} className="stat-icon yellow" />
              <div>
                <strong>100% Real-Time</strong>
                <span>Closed-Loop GPS Math</span>
              </div>
            </div>

            <div className="hero-stat-card">
              <Shield size={20} className="stat-icon mint" />
              <div>
                <strong>10 Member</strong>
                <span>Guild Limit & Vector Emblems</span>
              </div>
            </div>

            <div className="hero-stat-card">
              <Trophy size={20} className="stat-icon cyan" />
              <div>
                <strong>$50,000 Pre-Seed</strong>
                <span>3-Year Growth Roadmap</span>
              </div>
            </div>
          </div>
        </div>

        {/* Hero Interactive Showcase Card */}
        <div className="hero-preview-frame">
          <div className="preview-glow" />
          <div className="preview-card">
            <div className="preview-header">
              <div className="preview-user">
                <div className="preview-avatar">🎮</div>
                <div>
                  <strong>Nukus Runners [NKS]</strong>
                  <span>Gildiya Aymaǵı • 12,450 m²</span>
                </div>
              </div>
              <span className="live-status-badge">🟢 ONLAYN</span>
            </div>

            <div className="preview-map-sim">
              <div className="sim-grid" />
              <div className="sim-polygon" />
              <div className="sim-runner-pin">
                <User size={14} color="#10251F" />
              </div>
              <div className="sim-overlay-badge">
                <Swords size={14} style={{ color: '#FF3B30' }} />
                <span>2x Maydon Bonusi Belsendi!</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ── Key Features Grid Section ──────────────────────────────── */}
      <section id="features" className="landing-section">
        <div className="section-head">
          <p className="eyebrow">{dict.nav?.features || "IMKONIYATLAR"}</p>
          <h2>{dict.features?.title || "Nega Don't Stop Eng Zo'r Hudud O'yini?"}</h2>
          <p className="section-lead">{dict.features?.subtitle || "Sport va mobil o'yinlarni birlashtirgan innovatsion imkoniyatlar."}</p>
        </div>

        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-icon mint">
              <MapPin size={24} />
            </div>
            <h3>1. {dict.features?.f1Title || "Real-World Loop Capture"}</h3>
            <p>
              {dict.features?.f1Desc || "Ko'chada yuguring yoki yuring. Tizim avtomatik closed-loop konturini chizadi va bosib olingan yerlarni m² da hisoblaydi."}
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-icon gold">
              <Shield size={24} />
            </div>
            <h3>2. {dict.features?.f2Title || "10-Kishilik Gildiyalar & Vektor Gerblar"}</h3>
            <p>
              {dict.features?.f2Desc || "Do'stlaringiz bilan 10 kishilik Gildiya tuzing. Unique teg ([TAG]) va 10 ta eksklyuziv Vektor Gerb bilan shahar yetakchisiga aylaning."}
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-icon cyan">
              <ShieldAlert size={24} />
            </div>
            <h3>3. {dict.features?.f3Title || "Maxfiylik va Anticheat Himoyasi"}</h3>
            <p>
              {dict.features?.f3Desc || "200 metrli Privacy Zone bilan uyingiz joylashuvini yashiring. Bino va harbiy zonalarni chiqarib tashlovchi PostGIS spatial filtri."}
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-icon red">
              <Trophy size={24} />
            </div>
            <h3>4. {dict.features?.f4Title || "Monetizatsiya va Battle Pass"}</h3>
            <p>
              {dict.features?.f4Desc || "Battle Pass, avatar кастомизация, lokal brend hamkorliklari va homiylik hududiy eventlari."}
            </p>
          </div>
        </div>
      </section>

      {/* ── INVESTOR PRESENTATION DECK SECTION ─────────────────────── */}
      <section id="presentation" className="landing-section dark-alt">
        <div className="section-head">
          <p className="eyebrow">INVESTOR PITCH DECK</p>
          <h2>{dict.presentation?.title || "Investorlar uchun Taqdimot (PPTX)"}</h2>
          <p className="section-lead">
            {dict.presentation?.subtitle || "Pre-Seed $50,000 investitsiya rejasi, 3 yillik moliyaviy prognozlar hamda 3 tilda (UZB, RUS, ENG) tayyorlangan slaydlar."}
          </p>
        </div>

        {/* Presentation Language Switcher Tabs */}
        <div className="deck-lang-tabs">
          <button
            type="button"
            className={`deck-tab-btn ${activeDeckTab === 'uz' ? 'active' : ''}`}
            onClick={() => setActiveDeckTab('uz')}
          >
            🇺🇿 O'zbekcha (UZB)
          </button>
          <button
            type="button"
            className={`deck-tab-btn ${activeDeckTab === 'ru' ? 'active' : ''}`}
            onClick={() => setActiveDeckTab('ru')}
          >
            🇷🇺 Русский (RUS)
          </button>
          <button
            type="button"
            className={`deck-tab-btn ${activeDeckTab === 'en' ? 'active' : ''}`}
            onClick={() => setActiveDeckTab('en')}
          >
            🇬🇧 English (ENG)
          </button>
        </div>

        {/* Selected Deck Showcase Card */}
        <div className="deck-showcase-container">
          <div className="deck-preview-box">
            <img
              src={deckFiles[activeDeckTab].imgUrl}
              alt={deckFiles[activeDeckTab].title}
              className="deck-slide-image"
            />
            <div className="deck-image-overlay">
              <span>8 Slidely Presentation Deck</span>
            </div>
          </div>

          <div className="deck-info-box">
            <div className="deck-badge-row">
              <span className="deck-lang-badge">
                {deckFiles[activeDeckTab].flag} {deckFiles[activeDeckTab].langName}
              </span>
              <span className="deck-format-badge">PPTX • 8 Slayd</span>
            </div>

            <h3 className="deck-title">{deckFiles[activeDeckTab].title}</h3>
            <p className="deck-desc">{deckFiles[activeDeckTab].description}</p>

            <div className="deck-highlights">
              <div className="highlight-item">
                <strong style={{ color: '#21D8A0' }}>$50,000</strong>
                <span>Pre-Seed Byudjet Taqsimoti</span>
              </div>
              <div className="highlight-item">
                <strong style={{ color: '#FFB800' }}>3 Yil</strong>
                <span>$4M+ O'sish Bashorati</span>
              </div>
              <div className="highlight-item">
                <strong style={{ color: '#00E5FF' }}>5 Rol</strong>
                <span>Backend, Mobile, Game Dev, Design, Marketing</span>
              </div>
            </div>

            <div className="deck-download-actions">
              <a
                href={deckFiles[activeDeckTab].pptxUrl}
                download
                className="deck-download-btn-primary"
              >
                <Download size={18} />
                <span>{dict.presentation?.downloadBtn || "Taqdimotni Yuklab Olish (PPTX)"}</span>
              </a>

              <div className="deck-all-downloads">
                <span className="download-label">Barcha tillarda yuklab olish:</span>
                <div className="download-chips">
                  <a href="./presentations/dont_stop_pitch_deck_uz.pptx" download className="download-chip">
                    🇺🇿 UZB
                  </a>
                  <a href="./presentations/dont_stop_pitch_deck_ru.pptx" download className="download-chip">
                    🇷🇺 RUS
                  </a>
                  <a href="./presentations/dont_stop_pitch_deck_en.pptx" download className="download-chip">
                    🇬🇧 ENG
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ── Guild Emblems Showcase Section ──────────────────────────── */}
      <section id="guilds" className="landing-section">
        <div className="section-head">
          <p className="eyebrow">{dict.nav?.guilds || "GILDIYA GERBLARI"}</p>
          <h2>{dict.emblems?.title || "Professional Vektor Gerblar To'plami"}</h2>
          <p className="section-lead">{dict.emblems?.subtitle || "Gildiyangiz shon-sharafini aks ettiruvchi 10 ta eksklyuziv gaming emblemalar."}</p>
        </div>

        <div className="emblems-showcase-grid">
          {GUILD_EMBLEMS_LIST.map((emb) => (
            <div key={emb.id} className="emblem-showcase-card" style={{ borderColor: `${emb.color}44` }}>
              <GuildEmblem emblemId={emb.id} size={28} />
              <strong style={{ color: emb.color }}>{emb.name}</strong>
              <span>{emb.shortName}</span>
            </div>
          ))}
        </div>
      </section>

      {/* ── How It Works (4 Steps) ─────────────────────────────────── */}
      <section id="how-it-works" className="landing-section dark-alt">
        <div className="section-head">
          <p className="eyebrow">{dict.nav?.howItWorks || "QANDAY ISHLAYDI"}</p>
          <h2>{dict.steps?.title || "4 Oddiy Qadamda Hudud Egallang"}</h2>
        </div>

        <div className="steps-grid">
          <div className="step-card">
            <div className="step-num">01</div>
            <h3>{dict.steps?.s1Title || "1. Marshrutni Tanlang"}</h3>
            <p>{dict.steps?.s1Desc || "Xaritani oching va o'zingiz xohlagan zona atrofida yopiq kontur belgilang."}</p>
          </div>

          <div className="step-card">
            <div className="step-num">02</div>
            <h3>{dict.steps?.s2Title || "2. Harakatni Boshlang"}</h3>
            <p>{dict.steps?.s2Desc || "Yuring yoki yuguring. GPS real-vaqtda yo'lingizni xaritada yozib boradi."}</p>
          </div>

          <div className="step-card">
            <div className="step-num">03</div>
            <h3>{dict.steps?.s3Title || "3. Halqani Yoping"}</h3>
            <p>{dict.steps?.s3Desc || "Boshlagan nuqtangizga qayting. Hudud bir zumda Gildiyangiz rangiga bo'yaladi."}</p>
          </div>

          <div className="step-card">
            <div className="step-num">04</div>
            <h3>{dict.steps?.s4Title || "4. Himoya Qiling & G'olib Bo'ling"}</h3>
            <p>{dict.steps?.s4Desc || "Jamoangiz faolligini oshiring va hududlarni raqiblarga berib qo'ymang!"}</p>
          </div>
        </div>
      </section>

      {/* ── Download Banner Section ─────────────────────────────── */}
      <section id="download" className="landing-download-banner">
        <div className="download-content">
          <h2>{dict.downloadBanner?.title || "Hoziroq Don't Stop'ni Sinab Ko'ring!"}</h2>
          <p>{dict.downloadBanner?.subtitle || "Dunyoviy xaritaga o'tib yugurishni va shahar kvartallarini bosib olishni boshlang."}</p>
          <div className="download-cta-row">
            <button type="button" className="hero-main-btn" onClick={handleGoToMap}>
              <Play size={18} fill="#10251F" /> <span>{dict.downloadBanner?.cta || "Xaritaga O'tish"}</span>
            </button>
          </div>
        </div>
      </section>

      {/* ── Footer ─────────────────────────────────────────────────── */}
      <footer className="landing-footer">
        <div className="footer-container">
          <div className="footer-brand" onClick={handleGoToMap} style={{ cursor: 'pointer' }}>
            <span className="brand-mark">DS</span>
            <strong>DON'T STOP</strong>
          </div>
          <p>{dict.footer?.rights || "© 2026 Don't Stop Territory Capture. Barcha huquqlar himoyalangan."}</p>
        </div>
      </footer>
    </div>
  );
}
