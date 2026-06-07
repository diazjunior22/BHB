import React, { createContext, useState, useEffect, useContext } from 'react';
import es from './locales/es.json';
import en from './locales/en.json';
import pt from './locales/pt.json';

const dictionaries = { es, en, pt };

export const I18nContext = createContext();

export const I18nProvider = ({ children }) => {
  const [lang, setLang] = useState('es');

  const t = (key) => {
    return dictionaries[lang]?.[key] || key;
  };

  useEffect(() => {
    document.documentElement.lang = lang;
  }, [lang]);

  return (
    <I18nContext.Provider value={{ lang, setLang, t }}>
      {children}
    </I18nContext.Provider>
  );
};

export const useTranslation = () => useContext(I18nContext);
