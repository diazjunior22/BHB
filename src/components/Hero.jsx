import React, { useEffect, useRef, useState } from 'react';
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
          <h1 className="hero-title" dangerouslySetInnerHTML={{ __html: t('hero.title') }}></h1>
          <div className="hero-sub">{t('hero.sub')}</div>
          <p className="hero-desc">{t('hero.desc')}</p>
          <div className="hero-tag" style={{marginBottom: "24px"}}><span className="dot"></span> <span>{t('hero.tag')}</span></div>
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
