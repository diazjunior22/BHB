import React from 'react';
import { useTranslation } from '../I18nContext';


const Footer = () => {
  const { t } = useTranslation();
  return (
    <>
<footer className="footer">
    <div className="container">
      <div className="footer-grid">
        <div className="footer-brand">
          <a href="#" className="logo">
            <img src="/img/logo.png" alt="BHB Travel and Tour" className="logo-img" />
          </a>
          <p data-i18n="footer.desc">Tu mejor opción en excursiones por República Dominicana. Experiencias auténticas
            con la calidez del Caribe.</p>
        </div>
        <div>
          <h4>{t("footer.toursTitle")}</h4>
          <ul>
            <li><a href="#tours">{t("footer.linkSaona")}</a></li>
            <li><a href="#tours">{t("footer.linkParty")}</a></li>
            <li><a href="#tours">{t("footer.linkAtv")}</a></li>
          </ul>
        </div>
        <div>
          <h4>{t("footer.companyTitle")}</h4>
          <ul>
            <li><a href="#about">{t("footer.linkAbout")}</a></li>
            <li><a href="#contact">{t("footer.linkContact")}</a></li>
          </ul>
        </div>
        <div>
          <h4>{t("footer.followTitle")}</h4>
          <ul>
            <li><a href="https://www.instagram.com/bhbtravelgroup?utm_source=qr&igsh=MWQ3b3Y4cTFrNzQ5eQ==" target="_blank" rel="noopener noreferrer">{t("footer.linkInstagram")}</a></li>
            <li><a href="https://www.facebook.com/share/1777UPK32s/" target="_blank" rel="noopener noreferrer">{t("footer.linkFacebook")}</a></li>
            <li><a href="#">{t("footer.linkTiktok")}</a></li>
            <li><a href="https://www.facebook.com/share/1BS54SLtta/" target="_blank" rel="noopener noreferrer">{t("footer.linkFacebookPersonal")}</a></li>
          </ul>
        </div>
      </div>
      <div className="footer-bottom">
        <span>{t("footer.copyright")}</span>
        <div className="footer-social">
          <a href="https://www.instagram.com/bhbtravelgroup?utm_source=qr&igsh=MWQ3b3Y4cTFrNzQ5eQ==" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"
              strokeLinejoin="round">
              <rect x="2" y="2" width="20" height="20" rx="5" ry="5" />
              <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z" />
              <line x1="17.5" y1="6.5" x2="17.51" y2="6.5" />
            </svg>
          </a>
          <a href="https://www.facebook.com/share/1777UPK32s/" target="_blank" rel="noopener noreferrer" aria-label="Facebook BHB">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"
              strokeLinejoin="round">
              <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z" />
            </svg>
          </a>
          <a href="https://www.facebook.com/share/1BS54SLtta/" target="_blank" rel="noopener noreferrer" aria-label="Facebook Personal">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"
              strokeLinejoin="round">
              <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z" />
            </svg>
          </a>
          <a href="#" aria-label="TikTok">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"
              strokeLinejoin="round">
              <path d="M9 12a4 4 0 1 0 0 8 4 4 0 0 0 0-8z" />
              <path d="M15 8a4 4 0 0 0 4-4" />
              <path d="M15 8v8a4 4 0 0 1-8 0V8z" />
            </svg>
          </a>
        </div>
      </div>
    </div>
  </footer>
    </>
  );
};

export default Footer;
