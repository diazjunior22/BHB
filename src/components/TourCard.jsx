import React from 'react';
import { useTranslation } from '../I18nContext';
import { Link } from 'react-router-dom';

const TourCard = ({ id, img, badgeKey, nameKey, locationKey, featuresKeys, noteKey, delay }) => {
  const { t, lang } = useTranslation();
  
  // Max 3 features
  const displayFeatures = featuresKeys.slice(0, 3);
  
  // Price, duration, shortDesc
  const price = t(`tour.${id}.price`);
  const duration = t(`tour.${id}.duration`);
  const shortDesc = t(`tour.${id}.shortDesc`);

  // Translate static labels
  const getLabel = (en, es, pt) => {
    if (lang === 'en') return en;
    if (lang === 'pt') return pt;
    return es;
  };

  return (
    <div className={`tour-card fade-up ${delay ? 'fade-up-' + delay : ''}`}>
      <Link to={`/tours/${id}`} className="tour-card-img-wrapper">
        {badgeKey && t(badgeKey) && (
          <span className="tour-card-badge">
            <span>{t(badgeKey)}</span>
          </span>
        )}
        <img src={img} alt={t(nameKey)} className="tour-card-img" />
        <div className="tour-card-gradient"></div>
      </Link>
      
      <div className="tour-card-content">
        <Link to={`/tours/${id}`} className="tour-card-title-link">
          <h3 className="tour-card-title">{t(nameKey)}</h3>
        </Link>
        <div className="tour-card-location">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
            <circle cx="12" cy="10" r="3"></circle>
          </svg>
          {t(locationKey)}
        </div>
        
        <div className="tour-card-meta">
          <span className="tour-meta-item">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
              <circle cx="12" cy="12" r="10"></circle>
              <polyline points="12 6 12 12 16 14"></polyline>
            </svg>
            {duration}
          </span>
        </div>

        <p className="tour-card-desc">{shortDesc}</p>
        
        <div className="tour-card-features">
          {displayFeatures.map((fKey, index) => (
            <div key={index} className="tour-feature">
              <svg viewBox="0 0 24 24" fill="none" stroke="#00BCD4" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                <polyline points="20 6 9 17 4 12" />
              </svg>
              <span>{t(fKey)}</span>
            </div>
          ))}
        </div>
        
        <div className="tour-card-footer">
          <div className="tour-card-price">
            <span className="price-label">{getLabel('From', 'Desde', 'A partir de')}</span>
            <span className="price-value">${price} USD</span>
          </div>
          <div className="tour-card-actions">
            <Link to={`/tours/${id}`} className="btn-tour-primary">{getLabel('View Tour', 'Ver Tour', 'Ver Tour')}</Link>
            <a href="https://wa.me/18295555555" target="_blank" rel="noreferrer" className="btn-tour-secondary">
              {getLabel('Book Now', 'Reservar Ahora', 'Reservar Agora')}
            </a>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TourCard;
