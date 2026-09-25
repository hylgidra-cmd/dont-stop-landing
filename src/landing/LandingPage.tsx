import { useState } from 'react';
import {
  Download,
  FileText,
  Globe,
  MapPin,
  Play,
  QrCode,
  Shield,
  ShieldAlert,
  Sparkles,
  Swords,
  Trophy,
  User,
  Zap,
} from 'lucide-react';
import {
  SUPPORTED_LANGUAGES,
  getLanguage,
  setLanguage,
  type LanguageCode,
} from '../i18n';
import { GUILD_EMBLEMS_LIST, GuildEmblem } from '../profile/GuildEmblem';
import { PhoneQr } from '../ui/PhoneQr';

interface LandingPageProps {
  onStartApp: () => void;
  onOpenLeaderboard: () => void;
}

export function LandingPage({ onStartApp, onOpenLeaderboard }: LandingPageProps) {
  const [currentLang, setCurrentLang] = useState<LanguageCode>(getLanguage());
  const [qrOpen, setQrOpen] = useState(false);
  const [activeDeckTab, setActiveDeckTab] = useState<'uz' | 'ru' | 'en'>('uz');

  const handleLangChange = (code: LanguageCode) => {
    setLanguage(code);
    setCurrentLang(code);
    if (code === 'uz' || code === 'ru' || code === 'en') {
      setActiveDeckTab(code);
    }
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
          <div className="landing-brand" onClick={onStartApp} style={{ cursor: 'pointer' }}>
            <span className="brand-mark">DS</span>
            <div className="brand-titles">
              <span className="brand-title">DON'T STOP</span>
              <span className="brand-sub">TERRITORY CAPTURE</span>
            </div>
          </div>

          <nav className="landing-menu">
            <a href="#features">Xususiyatlar</a>
            <a href="#presentation">Prizintatsiya</a>
            <a href="#guilds">Gildiyalar</a>
            <a href="#how-it-works">Qanday ishlaydi</a>
            <a href="#download">APK / App</a>
          </nav>

          <div className="landing-nav-actions">
            {/* Header Language Selector */}
            <div className="lang-switcher landing-lang">
              <Globe size={14} className="lang-icon" style={{ color: '#21D8A0' }} />
              <select
                value={currentLang}
                onChange={(e) => handleLangChange(e.target.value as LanguageCode)}
                className="topbar-lang-select"
              >
                {SUPPORTED_LANGUAGES.map((l) => (
                  <option key={l.code} value={l.code}>
                    {l.flag} {l.name}
                  </option>
                ))}
              </select>
            </div>

            <button type="button" className="landing-btn-secondary" onClick={() => setQrOpen(true)}>
              <QrCode size={15} /> <span>QR Scan</span>
            </button>

            <button type="button" className="landing-btn-primary" onClick={onStartApp}>
              <Play size={15} fill="#10251F" /> <span>Xaritaga O'tish</span>
            </button>
          </div>
        </div>
      </header>

      {/* ── Hero Section ──────────────────────────────────────────── */}
      <section className="landing-hero">
        <div className="hero-content">
          <div className="hero-pill">
            <Sparkles size={14} style={{ color: '#FFB800' }} />
            <span>REAL-WORLD GAMIFIED FITNESS PLATFORM</span>
          </div>

          <h1 className="hero-title">
            Yugur, Shenber Sız hám <span className="highlight-text">Óz Aymaǵıńdı Iyele!</span>
          </h1>

          <p className="hero-subtitle">
            PlayStride va Run an Empire uslubida real hayotdagi ko'chalarda yugurib, o'zingiz va 10 kishilik Gildiyangiz uchun yerlarni bosib oling.
          </p>

          <div className="hero-cta-group">
            <button type="button" className="hero-main-btn" onClick={onStartApp}>
              <Play size={18} fill="#10251F" /> <span>O'yinni Boshlash (Web App)</span>
            </button>

            <a href="#presentation" className="hero-presentation-btn">
              <FileText size={18} /> <span>Investor Taqdimoti (PPTX)</span>
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
              <Globe size={20} className="stat-icon cyan" />
              <div>
                <strong>3 Primary Languages</strong>
                <span>UZB • RUS • ENG</span>
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
          <p className="eyebrow">XUSUSIYATLAR</p>
          <h2>Nega Don't Stop Eng Zo'r Hudud O'yini?</h2>
          <p className="section-lead">Sport va mobil o'yinlarni birlashtirgan innovatsion imkoniyatlar.</p>
        </div>

        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-icon mint">
              <MapPin size={24} />
            </div>
            <h3>1. Real-World Loop Capture</h3>
            <p>
              Ko'chada yuguring yoki yuring. Tizim avtomatik closed-loop (yopiq aylana) konturini chizadi va bosib olingan yerlarni hisoblab beradi.
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-icon gold">
              <Shield size={24} />
            </div>
            <h3>2. 10-Kishilik Gildiyalar & Gerblar</h3>
            <p>
              Do'stlaringiz bilan 10 kishilik Gildiya tuzing. Unique teg (`[TAG]`) va 10 ta eksklyuziv Vektor Gerb bilan shahar yetakchisiga aylaning.
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-icon cyan">
              <ShieldAlert size={24} />
            </div>
            <h3>3. Maxfiylik va Anticheat</h3>
            <p>
              200 metrli Privacy Zone bilan uyingiz joylashuvini yashiring. Bino va harbiy zonalarni chiqarib tashlovchi PostGIS spatial filtri.
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-icon red">
              <Trophy size={24} />
            </div>
            <h3>4. Reyting va Real-Time Xabarlar</h3>
            <p>
              Dunyoviy va shahar reytinglarida #1 o'rinni egallang. Raqiblar hududingizga kirganda real-vaqtda jangovar bildirishnoma oling.
            </p>
          </div>
        </div>
      </section>

      {/* ── INVESTOR PRESENTATION DECK SECTION ─────────────────────── */}
      <section id="presentation" className="landing-section dark-alt">
        <div className="section-head">
          <p className="eyebrow">INVESTOR PITCH DECK</p>
          <h2>Investorlar uchun Taqdimot (PPTX)</h2>
          <p className="section-lead">
            Pre-Seed $50,000 investitsiya rejasi, 3 yillik moliyaviy prognozlar hamda 3 tilda (UZB, RUS, ENG) tayyorlangan slaydlar.
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
                <span>Taqdimotni Yuklab Olish (PPTX)</span>
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
          <p className="eyebrow">GILDIYA GERBLARI</p>
          <h2>Professional Vektor Gerblar To'plami</h2>
          <p className="section-lead">Gildiyangiz shon-sharafini aks ettiruvchi 10 ta eksklyuziv gaming emblemalar.</p>
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
          <p className="eyebrow">QANDAY ISHLAYDI</p>
          <h2>4 Oddiy Qadamda Hudud Egallang</h2>
        </div>

        <div className="steps-grid">
          <div className="step-card">
            <div className="step-num">01</div>
            <h3>Appni Ochg hám GPS Yoqın</h3>
            <p>Telefonda brauzer yoki APK ilovani ochib, xaritada joylashuv tugmasini bosing.</p>
          </div>

          <div className="step-card">
            <div className="step-num">02</div>
            <h3>Yugur hám Shenber Sız</h3>
            <p>Ko'chada yuguring. Tizim yugurgan yo'lingizni real-vaqtda xaritada aks ettiradi.</p>
          </div>

          <div className="step-card">
            <div className="step-num">03</div>
            <h3>Shenberni Yoping</h3>
            <p>Boshlagan nuqtangizga qaytib keling. Tizim yopiq maydonni (`m²`) avtomatik egallaydi.</p>
          </div>

          <div className="step-card">
            <div className="step-num">04</div>
            <h3>Gildiyangizni Yetakchi Qiling</h3>
            <p>Jamoangiz bilan shahar va global reytinglarda g'olib bo'ling!</p>
          </div>
        </div>
      </section>

      {/* ── Download & Testing Section ─────────────────────────────── */}
      <section id="download" className="landing-download-banner">
        <div className="download-content">
          <h2>Hoziroq Don't Stop'ni Sinab Ko'ring!</h2>
          <p>Telefonda skanerlang yoki veb-versiyada yugurishni boshlang.</p>
          <div className="download-cta-row">
            <button type="button" className="hero-main-btn" onClick={onStartApp}>
              <Play size={18} fill="#10251F" /> <span>Xaritaga O'tish</span>
            </button>
            <button type="button" className="landing-btn-secondary" onClick={onOpenLeaderboard}>
              <Trophy size={18} /> <span>Reyting Jadvali</span>
            </button>
          </div>
        </div>
      </section>

      {/* ── Footer ─────────────────────────────────────────────────── */}
      <footer className="landing-footer">
        <div className="footer-container">
          <div className="footer-brand">
            <span className="brand-mark">DS</span>
            <strong>DON'T STOP</strong>
          </div>
          <p>© 2026 Don't Stop Territory Capture. Barcha huquqlar himoyalangan.</p>
        </div>
      </footer>

      {qrOpen && <PhoneQr defaultOpen={true} />}
    </div>
  );
}
