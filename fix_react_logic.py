import os

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
    <header className={`header ${scrolled ? 'scrolled' : ''}`}>
      <div className="container">
        <div className="header-inner">
          <a href="#" className="logo">
            <img src="img/logo.png" alt="BHB Travel and Tour" />
            <div className="logo-text">
              <span className="logo-title">BHB Travel &amp; Tour</span>
              <span className="logo-sub">{t('header.tag')}</span>
            </div>
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
          <div className="lang-switcher" id="langSwitcherDesktop">
              <button className={`lang-btn ${lang === 'es' ? 'active' : ''}`} onClick={() => setLang('es')}><img src="https://flagcdn.com/w40/es.png" className="flag-icon" alt="ES" /></button>
              <button className={`lang-btn ${lang === 'en' ? 'active' : ''}`} onClick={() => setLang('en')}><img src="https://flagcdn.com/w40/gb.png" className="flag-icon" alt="EN" /></button>
              <button className={`lang-btn ${lang === 'pt' ? 'active' : ''}`} onClick={() => setLang('pt')}><img src="https://flagcdn.com/w40/pt.png" className="flag-icon" alt="PT" /></button>
          </div>
          <button className={`hamburger ${menuOpen ? 'open' : ''}`} onClick={() => setMenuOpen(!menuOpen)}>
            <span></span><span></span><span></span>
          </button>
        </div>
      </div>
    </header>
  );
};
export default Header;
"""

hero_code = """import React, { useEffect, useRef, useState } from 'react';
import { useTranslation } from '../I18nContext';

const Hero = () => {
  const { t } = useTranslation();
  const heroRef = useRef(null);
  const contentRef = useRef(null);
  const bgRef = useRef(null);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 100);
    };
    window.addEventListener('scroll', handleScroll, { passive: true });
    
    const heroSection = heroRef.current;
    const heroContent = contentRef.current;
    const heroBg = bgRef.current;
    
    let isTouch = 'ontouchstart' in window;
    const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    
    const handleMouseMove = (e) => {
      if (isTouch || prefersReduced) return;
      const rect = heroSection.getBoundingClientRect();
      if (e.clientY < rect.top || e.clientY > rect.bottom) return;
      const x = (e.clientX / window.innerWidth - .5) * 2;
      const y = (e.clientY / window.innerHeight - .5) * 2;
      heroContent.style.transform = `rotateX(${y * -2}deg) rotateY(${x * 2}deg) translateZ(0)`;
      heroBg.style.transform = `translateX(${x * -8}px) translateY(${y * -8}px) scale(1.04)`;
    };
    
    const handleMouseLeave = () => {
      if (isTouch || prefersReduced) return;
      heroContent.style.transform = '';
      heroBg.style.transform = '';
    };

    heroSection.addEventListener('mousemove', handleMouseMove);
    heroSection.addEventListener('mouseleave', handleMouseLeave);
    
    return () => {
      window.removeEventListener('scroll', handleScroll);
      heroSection.removeEventListener('mousemove', handleMouseMove);
      heroSection.removeEventListener('mouseleave', handleMouseLeave);
    };
  }, []);

  return (
    <section className="hero" id="hero" ref={heroRef}>
      <div className="hero-bg" id="heroBg" ref={bgRef}></div>
      <div className="hero-noise"></div>
      <div className="hero-overlay"></div>
      <div className="hero-glow"></div>
      <div className="hero-glow-yellow"></div>
      <div className="hero-line hero-line-top"></div>
      <div className="hero-line hero-line-bottom"></div>
      <div className="hero-particles">
        <div className="hero-particle"></div>
        <div className="hero-particle"></div>
        <div className="hero-particle"></div>
        <div className="hero-particle"></div>
        <div className="hero-particle"></div>
      </div>
      
      <div className="container">
        <div className="hero-content" id="heroContent" ref={contentRef}>
          <div className="hero-tag"><span className="dot"></span> <span>{t('hero.tag')}</span></div>
          <h1 className="hero-title" dangerouslySetInnerHTML={{ __html: t('hero.title') }}></h1>
          <div className="hero-sub">{t('hero.sub')}</div>
          <p className="hero-desc">{t('hero.desc')}</p>
          <div className="hero-actions">
            <a href="#tours" className="btn btn-primary">
              {t('hero.btnTours')}
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </a>
            <a href="#contact" className="btn btn-outline">{t('hero.btnContact')}</a>
          </div>
          
          <div className="hero-stats">
            <div className="hero-stat">
              <div className="hero-stat-value">5k+</div>
              <div className="hero-stat-label">{t('stats.travelers')}</div>
            </div>
            <div className="hero-stat">
              <div className="hero-stat-value">12+</div>
              <div className="hero-stat-label">{t('stats.tours')}</div>
            </div>
            <div className="hero-stat">
              <div className="hero-stat-value">8+</div>
              <div className="hero-stat-label">{t('stats.experience')}</div>
            </div>
            <div className="hero-stat">
              <div className="hero-stat-value">4.9</div>
              <div className="hero-stat-label">{t('stats.satisfaction')}</div>
            </div>
          </div>
        </div>
      </div>
      
      <div className="hero-scroll-indicator" style={{ opacity: scrolled ? 0 : 1, pointerEvents: scrolled ? 'none' : 'auto' }}>
        <div className="mouse"></div>
      </div>
    </section>
  );
};
export default Hero;
"""

contact_code = """import React, { useState } from 'react';
import { useTranslation } from '../I18nContext';

const Contact = () => {
  const { lang, t } = useTranslation();
  const [formData, setFormData] = useState({ name: '', email: '', tourSelect: '', people: '1', message: '' });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.id]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    let intro = "¡Hola! Me gustaría consultar sobre una excursión.";
    let labelName = "Nombre";
    let labelEmail = "Email";
    let labelTour = "Tour de interés";
    let labelPeople = "Personas";
    let labelMessage = "Mensaje";

    if (lang === 'en') {
      intro = "Hello! I would like to inquire about an excursion.";
      labelName = "Name";
      labelEmail = "Email";
      labelTour = "Tour of interest";
      labelPeople = "People";
      labelMessage = "Message";
    } else if (lang === 'pt') {
      intro = "Olá! Gostaria de obter informações sobre um passeio.";
      labelName = "Nome";
      labelEmail = "Email";
      labelTour = "Passeio de interesse";
      labelPeople = "Pessoas";
      labelMessage = "Mensagem";
    }

    const tourText = formData.tourSelect || (lang === 'en' ? 'General inquiry' : lang === 'pt' ? 'Consulta geral' : 'Consulta general');
    
    const text = `${intro}\\n\\n` +
      `*${labelName}:* ${formData.name}\\n` +
      `*${labelEmail}:* ${formData.email}\\n` +
      `*${labelTour}:* ${tourText}\\n` +
      `*${labelPeople}:* ${formData.people}\\n` +
      `*${labelMessage}:* ${formData.message}`;

    const whatsappNumber = "18094654750";
    const url = `https://api.whatsapp.com/send?phone=${whatsappNumber}&text=${encodeURIComponent(text)}`;
    window.open(url, '_blank');
  };

  return (
    <section className="section contact" id="contact">
      <div className="container">
        <div className="contact-grid">
          <div className="contact-info fade-up">
            <h2 className="section-title">
              {t('contact.title.1')} <span className="hl-yellow">{t('contact.title.2')}</span>
            </h2>
            <p className="body-lg" style={{ marginTop: '16px' }}>{t('contact.desc')}</p>
            <div className="contact-methods">
              <div className="contact-method">
                <div className="cm-icon">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                </div>
                <div>
                  <strong>{t('contact.whatsapp')}</strong>
                  <div>+1 (809) 465-4750</div>
                </div>
              </div>
              <div className="contact-method">
                <div className="cm-icon">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                </div>
                <div>
                  <strong>{t('contact.email')}</strong>
                  <div>bhbtravelandtour@gmail.com</div>
                </div>
              </div>
            </div>
            <div style={{ marginTop: '40px' }}>
              <div style={{ fontWeight: 600, marginBottom: '16px', color: 'var(--white)' }}>{t('contact.follow')}</div>
              <div className="social-links">
                <a href="#" aria-label="Instagram">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                </a>
                <a href="#" aria-label="Facebook">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
                </a>
                <a href="#" aria-label="TripAdvisor">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg>
                </a>
              </div>
            </div>
          </div>
          <div className="contact-form fade-up fade-up-d1">
            <h3 style={{ fontSize: '24px', fontWeight: 700, marginBottom: '8px' }}>{t('form.title')}</h3>
            <p style={{ color: 'rgba(255,255,255,0.6)', marginBottom: '32px' }}>{t('form.subtitle')}</p>
            <form id="contactForm" onSubmit={handleSubmit}>
              <div className="form-group">
                <label className="form-label" htmlFor="name">{t('form.name')}</label>
                <input type="text" id="name" className="form-control" required value={formData.name} onChange={handleChange} />
              </div>
              <div className="form-group">
                <label className="form-label" htmlFor="email">{t('form.email')}</label>
                <input type="email" id="email" className="form-control" required value={formData.email} onChange={handleChange} />
              </div>
              <div className="form-group">
                <label className="form-label" htmlFor="tourSelect">{t('form.tour')}</label>
                <select id="tourSelect" className="form-control" value={formData.tourSelect} onChange={handleChange}>
                  <option value="">{t('form.tourPlaceholder')}</option>
                  <option value="saona">{t('tour.saona.name')}</option>
                  <option value="party">{t('tour.party.name')}</option>
                  <option value="atv">{t('tour.atv.name')}</option>
                  <option value="santodomingo">{t('tour.santodomingo.name')}</option>
                </select>
              </div>
              <div className="form-group">
                <label className="form-label" htmlFor="people">{t('form.people')}</label>
                <input type="number" id="people" className="form-control" min="1" value={formData.people} onChange={handleChange} />
              </div>
              <div className="form-group">
                <label className="form-label" htmlFor="message">{t('form.message')}</label>
                <textarea id="message" className="form-control" rows="4" required value={formData.message} onChange={handleChange}></textarea>
              </div>
              <button type="submit" className="btn btn-primary" style={{ width: '100%', justifyContent: 'center' }}>
                {t('form.submit')}
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
              </button>
            </form>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Contact;
"""

with open('src/components/Header.jsx', 'w', encoding='utf-8') as f:
    f.write(header_code)

with open('src/components/Hero.jsx', 'w', encoding='utf-8') as f:
    f.write(hero_code)

with open('src/components/Contact.jsx', 'w', encoding='utf-8') as f:
    f.write(contact_code)

print("Logic fixed")
