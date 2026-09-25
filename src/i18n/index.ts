import { uz } from './uz';
import { ru } from './ru';
import { en } from './en';
import { setActiveDict } from './state';
import type { TranslationDictionary } from './qq';

export type LanguageCode = 'uz' | 'ru' | 'en';

export interface LanguageOption {
  code: LanguageCode;
  name: string;
  flag: string;
}

export const SUPPORTED_LANGUAGES: LanguageOption[] = [
  { code: 'uz', name: "O'zbekcha", flag: '🇺🇿' },
  { code: 'ru', name: 'Русский', flag: '🇷🇺' },
  { code: 'en', name: 'English', flag: '🇬🇧' },
];

const DICTIONARIES: Record<LanguageCode, TranslationDictionary> = {
  uz,
  ru,
  en,
};

let currentLang: LanguageCode = (() => {
  const saved = localStorage.getItem('dontstop.lang') as LanguageCode | null;
  if (saved && saved in DICTIONARIES) {
    return saved;
  }
  return 'uz';
})();

setActiveDict(DICTIONARIES[currentLang]);

export function getLanguage(): LanguageCode {
  return currentLang;
}

export function setLanguage(lang: LanguageCode) {
  if (lang in DICTIONARIES) {
    currentLang = lang;
    localStorage.setItem('dontstop.lang', lang);
    setActiveDict(DICTIONARIES[lang]);
  }
}
