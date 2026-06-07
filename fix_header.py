header_code = """import React, { useState, useEffect } from 'react';
import { useTranslation } from '../I18nContext';

const Header = () => {
  const { lang, setLang, t } = useTranslation();
  const [scrolled, setScrolled] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const handleNavClick = () => setMenuOpen(false);

  return (
    <header className={`header ${scrolled ? 'scrolled' : ''}`} id="header">
      <div className="header-top">
        <div className="container">
          <div className="header-top-inner">
            <div className="ht-contact">
              <a href="https://wa.me/18094654750" target="_blank" rel="noreferrer">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                <span>{t('header.callUs')}</span>: +1 (809) 465-4750
              </a>
              <a href="mailto:bhbtravelandtour@gmail.com">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                bhbtravelandtour@gmail.com
              </a>
            </div>
            
            <div className="lang-switcher" id="langSwitcherDesktop">
              <button className={`lang-btn ${lang === 'es' ? 'active' : ''}`} onClick={() => setLang('es')}><img src="https://flagcdn.com/w40/es.png" className="flag-icon" alt="ES" /></button>
              <button className={`lang-btn ${lang === 'en' ? 'active' : ''}`} onClick={() => setLang('en')}><img src="https://flagcdn.com/w40/gb.png" className="flag-icon" alt="EN" /></button>
              <button className={`lang-btn ${lang === 'pt' ? 'active' : ''}`} onClick={() => setLang('pt')}><img src="https://flagcdn.com/w40/pt.png" className="flag-icon" alt="PT" /></button>
            </div>
          </div>
        </div>
      </div>

      <div className="header-main">
        <div className="container header-inner">
          <a href="#" className="logo logo-header">
            <img src="/img/logo.png" alt="BHB Travel and Tour" className="logo-img" />
          </a>
          <nav className={`nav ${menuOpen ? 'open' : ''}`} id="nav">
            <a href="#tours" onClick={handleNavClick}>{t('nav.tours')}</a>
            <a href="#about" onClick={handleNavClick}>{t('nav.about')}</a>
            <a href="#contact" onClick={handleNavClick}>{t('nav.contact')}</a>
            <a href="#contact" className="btn-nav" onClick={handleNavClick}>{t('nav.reserve')}</a>
            
            <div className="lang-switcher-mobile">
              <button className={`lang-btn ${lang === 'es' ? 'active' : ''}`} onClick={() => {setLang('es'); handleNavClick();}}><img src="https://flagcdn.com/w40/es.png" className="flag-icon" alt="ES" /></button>
              <button className={`lang-btn ${lang === 'en' ? 'active' : ''}`} onClick={() => {setLang('en'); handleNavClick();}}><img src="https://flagcdn.com/w40/gb.png" className="flag-icon" alt="EN" /></button>
              <button className={`lang-btn ${lang === 'pt' ? 'active' : ''}`} onClick={() => {setLang('pt'); handleNavClick();}}><img src="https://flagcdn.com/w40/pt.png" className="flag-icon" alt="PT" /></button>
            </div>
          </nav>

          <button className={`hamburger ${menuOpen ? 'open' : ''}`} onClick={() => setMenuOpen(!menuOpen)}>
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </div>
    </header>
  );
};

export default Header;
"""

with open('src/components/Header.jsx', 'w', encoding='utf-8') as f:
    f.write(header_code)

print("Header logic fixed")
