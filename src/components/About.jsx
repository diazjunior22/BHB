import React from 'react';
import { useTranslation } from '../I18nContext';


const About = () => {
  const { t } = useTranslation();
  return (
    <>
<section className="section about" id="about">
    <div className="container">
      <div className="about-grid">
        <div className="about-visual fade-up">
          <div className="about-frame">
            <svg viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M100 15L185 72V128L100 185L15 128V72L100 15Z" stroke="white" strokeWidth="1.5" opacity=".3" />
              <path d="M60 100L80 118L120 82" stroke="white" strokeWidth="3" strokeLinecap="round"
                strokeLinejoin="round" opacity=".6" />
              <circle cx="50" cy="50" r="6" fill="white" opacity=".15" />
              <circle cx="150" cy="45" r="4" fill="white" opacity=".1" />
              <circle cx="155" cy="130" r="5" fill="white" opacity=".12" />
            </svg>
            <img src="img/logo.png" alt="BHB Travel and Tour" className="about-logo" />
          </div>
          <div className="about-card">
            <div className="about-card-num">10+</div>
            <div className="about-card-text">
              <strong>{t("about.card.title")}</strong>
              <span>{t("about.card.desc")}</span>
            </div>
          </div>
        </div>
        <div className="about-content">
          <div className="fade-up">
            <span className="label">{t("about.label")}</span>
            <h2 className="heading-lg" style={{ /* margin-top:12px; */ }} data-i18n-html="about.title">Tu puerta al<br />Caribe
              auténtico</h2>
          </div>
          <p className="body-sm fade-up fade-up-d1" style={{ /* margin-top:20px; */ }} data-i18n="about.p1">
            En BHB Travel and Tour somos apasionados por mostrar lo mejor de la República Dominicana. Cada excursión
            está diseñada para que vivas momentos inolvidables, con total seguridad y comodidad.
          </p>
          <p className="body-sm fade-up fade-up-d2" data-i18n="about.p2">
            Desde Isla Saona hasta aventuras en ATV, nos encargamos de todo: transporte, comida, bebidas y la mejor
            animación.
          </p>
          <ul className="about-grid-list fade-up fade-up-d3">
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round"
                strokeLinejoin="round">
                <polyline points="20 6 9 17 4 12" />
              </svg>
              <span>{t("about.f1")}</span>
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round"
                strokeLinejoin="round">
                <polyline points="20 6 9 17 4 12" />
              </svg>
              <span>{t("about.f2")}</span>
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round"
                strokeLinejoin="round">
                <polyline points="20 6 9 17 4 12" />
              </svg>
              <span>{t("about.f3")}</span>
            </li>
            <li>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round"
                strokeLinejoin="round">
                <polyline points="20 6 9 17 4 12" />
              </svg>
              <span>{t("about.f4")}</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>
    </>
  );
};

export default About;
