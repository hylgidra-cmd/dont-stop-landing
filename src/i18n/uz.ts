import type { TranslationDictionary } from './qq';

export const uz: TranslationDictionary = {
  brand: {
    name: "Don't Stop",
    home: "Bosh sahifa",
  },

  mode: {
    label: "Hudud rejimi",
    solo: "Yakka",
    clan: "Gildiya",
    clanNeeded: "Gildiya rejimi uchun avval gildiyaga kirish kerak.",
  },

  map: {
    label: "Nukus hudud xaritasi",
    eyebrow: "NUKUS PILOTI",
    headline: "Yo'lingni egalla.",
    lead: "Hududni egallash uchun yopiq aylana chizib yuguring yoki yuring.",
    ready: "Yugurish tayyor",
    offline: "Faqat xarita — bu yerda API yo'q",
    dismiss: "Yopish",
  },

  geo: {
    outOfBounds: "Siz tanlagan shahar hududidan tashqaridasiz, xarita sizni kuzata olmaydi.",
    outsideCity: (city: string) => `Siz tanlagan shaharda (${city}) emassiz! Xarita sizni kuzata olmaydi.`,
    denied: "Ushbu sayt uchun joylashuv bloklangan. Brauzer sozlamalarida ruxsat bering va joylashuv tugmasini qayta bosing.",
    unavailable: "Joylashuv aniqlanmadi. GPS'i yo'q noutbuk Wi-Fi orqali aniqlaydi, u bino ichida ishlamasligi mumkin.",
    timeout: "Joylashuv so'rovining vaqti tugadi. Tugmani qayta bosing.",
    unknown: "Joylashuv hozircha mavjud emas.",
  },

  cities: {
    label: "Shahar",
    select: "Shaharni tanlang",
    change: "Shaharni o'zgartirish",
  },

  run: {
    start: "Yugurishni boshlash",
    finish: "Yakunlash",
    checking: "Tekshirilmoqda…",
    close: "Yopish",
    release: "Bo'shatish",
    captured: "HUDUD EGALLANDI",
    rejected: "YUGURISH BEKOR QILINDI",
    excluded: (area: string) => `${area} bino va yopiq hududlar uchun olib tashlandi`,
    closedGap: (distance: string) => `Boshlashga qadar ${distance} masofa server tomonidan yopildi`,
    takenFrom: (owners: string) => `${owners} dan olindi`,
    tracking: (count: number) => `${count} nuqta yozildi. Boshlagan joyingizga qaytib boring, so'ng yakunlang.`,
    noApi: "Bu manzilda API yo'q, shuning uchun yugurishni yozib bo'lmaydi.",
    couldNotStart: "Yugurishni boshlab bo'lmadi.",
    couldNotFinish: "Yugurishni yakunlab bo'lmadi.",
    couldNotUpload: "Nuqtalarni yuborib bo'lmadi.",
    couldNotRelease: "Yugurishni bo'shatib bo'lmadi.",
    noGeolocation: "Bu brauzerde Geolocation API yo'q.",
  },

  activity: {
    walk: "yurish",
    run: "yugurish",
    bike: "velosiped",
    vehicle: "transport",
  },

  reasons: {
    LOOP_NOT_CLOSED: "Aylana boshlangan joyga qaytmadi. Boshlagan joyingizda yakunlang.",
    TOO_SHORT: "Aylana bu server ruxsat etgan eng kichik uzunlikdan qisqa.",
    AREA_TOO_SMALL: "O'ralgan maydon ruxsat etilgan eng kichik miqdordan kichik.",
    BAD_SHAPE: "Trek hech qanday maydonni o'ramaydi.",
    ACTIVITY_NOT_ALLOWED: "Faqat yurish va yugurish hisoblanadi.",
    TELEPORT_DETECTED: "Trekda sakrash aniqlandi.",
    LOW_GPS_QUALITY: "GPS signali ishonchsiz edi.",
    OUTSIDE_REGION: "Aylana pilot hududidan tashqarida.",
    NO_AWARDABLE_AREA: "Taqiqlar olib tashlangach hech narsa qolmadi.",
    DUPLICATE_RUN: "Bu yugurish oldin yuborilgan.",
    NOT_IN_CLAN: "Gildiya uchun yugurish uchun avval gildiyaga kiring.",
  },

  legend: {
    title: "Hisoblanmaydigan joy",
    hide: "Yashirish",
    show: "Ko'rsatish",
    kinds: {
      building: "Binolar",
      private: "Xususiy mulk",
      school: "Maktablar",
      hospital: "Kasalxonalar",
      military: "Harbiy hudud",
      water: "Suv",
      industrial: "Sanoat hududi",
      other: "Boshqa",
    },
    count: (count: number) => `${count} ta hudud chiqarib tashlanadi.`,
    truncated: "Joylar ko'p — yaqinlashtiring.",
  },

  qr: {
    title: "TELEFONDA OCHISH",
    label: "Ushbu demoni telefonda ochish",
    hide: "Telefon havolasini yashirish",
    reopen: "Telefon havolasi",
    preparing: "Kod tayyorlanmoqda…",
    hint: "Skanerlang va kartadagi joylashuv tugmasini bosing.",
    localhost: "Localhost telefonda ochilmaydi.",
  },

  profile: {
    open: "Profilni ochish",
    title: "Profil",
    close: "Yopish",
    playerId: "O'yinchi ID",
    copy: "Nusxalash",
    copied: "Nusxalandi",
    name: "Ism",
    save: "Saqlash",
    saving: "Saqlanmoqda…",
    nameTooShort: "Ism kamida 2 belgidan iborat bo'lishi kerak.",
    nameTooLong: "Ism eng ko'pi 24 belgi.",
    runs: "Yugurishlar",
    soloArea: "Yakka maydon",
    clanArea: "Gildiya maydoni",
    joined: "Qo'shilgan",
    loading: "Yuklanmoqda…",
    unavailable: "Profil mavjud emas.",
    logout: "Chiqish",
    privacyZone: "Maxfiylik zonasi (200m radius)",
    privacyActive: "Maxfiylik zonasi faol",
  },

  events: {
    banner: "🔥 Event: 2x Maydon bonus!",
    daysLeft: (days: number) => `Muddat: ${days} kun qoldi`,
  },

  friends: {
    add: "Do'stlikka qo'shish",
    sent: "Do'stlik taklifi yuborildi!",
    received: (name: string) => `${name} do'stlik taklif qilmoqda`,
    alreadySent: "Taklif yuborilgan",
  },

  clan: {
    title: "Gildiya",
    none: "Gildiyaga qo'shilmagansiz",
    create: "Gildiya tuzish",
    creating: "Tuzilmoqda…",
    join: "Gildiyaga qo'shilish",
    joining: "Qo'shilinmoqda…",
    nameField: "Gildiya nomi",
    tagField: "Teg",
    tagHint: "2–5 belgi: A–Z, 0–9",
    colorField: "Rang",
    emblemField: "Gildiya gerbi",
    codeField: "Chaqiruv kodi",
    codeHint: "6 belgili kod",
    inviteCode: "Chaqiruv kodi",
    members: (count: number) => `A'zolar ${count}/10`,
    area: "Gildiya maydoni",
    leave: "Gildiyadan chiqish",
    leaving: "Chiqilmoqda…",
    remove: "Chiqarish",
    roles: {
      owner: "Boshliq",
      officer: "Yordamchi",
      member: "A'zo",
    },
    errors: {
      alreadyInClan: "Siz allaqachon gildiyadasiz.",
      tagTaken: "Bul teg band.",
      full: "Gildiya to'la — 10 a'zo.",
      codeNotFound: "Gildiya topilmadi.",
      invalid: "Ma'lumotlar noto'g'ri.",
      generic: "Bajarib bo'lmadi.",
    },
  },

  notifications: {
    territoryInvaded: (invader: string, area: number) =>
      `⚔️ ${invader} sening ${area} m² maydoningga kirdi!`,
    dismiss: "Yopish",
  },
};
