import os

tour_card_code = """import React from 'react';
import { useTranslation } from '../I18nContext';

const TourCard = ({ id, img, badgeKey, nameKey, locationKey, featuresKeys, noteKey, delay }) => {
  const { t } = useTranslation();
  return (
    <div className={`tour-card fade-up ${delay ? 'fade-up-' + delay : ''}`}>
      <div className="tour-card-top">
        <span className="tour-card-badge">
          <span className="star">★</span> <span>{t(badgeKey)}</span>
        </span>
        <img src={img} alt={t(nameKey)} />
      </div>
      <div className="tour-card-body">
        <h3>{t(nameKey)}</h3>
        <div className="tour-location">{t(locationKey)}</div>
        {noteKey && <div style={{fontSize: '12px', color: 'var(--yellow)', marginBottom: '12px'}}>{t(noteKey)}</div>}
        <ul className="tour-features">
          {featuresKeys.map((fKey, index) => (
            <li key={index}>
              {index % 2 === 0 ? (
                <svg className="check" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                  <polyline points="20 6 9 17 4 12" />
                </svg>
              ) : (
                <svg className="star-icon" viewBox="0 0 24 24" fill="currentColor" stroke="none">
                  <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" />
                </svg>
              )}
              <span>{t(fKey)}</span>
            </li>
          ))}
        </ul>
        <a href="#contact" className="btn btn-outline-card">{t('tour.cta')}</a>
      </div>
    </div>
  );
};

export default TourCard;
"""

tours_grid_code = """import React from 'react';
import { useTranslation } from '../I18nContext';
import TourCard from './TourCard';

const ToursGrid = () => {
  const { t } = useTranslation();
  return (
    <section className="section tours" id="tours">
      <div className="container">
        <div className="section-header">
          <h2 className="section-title fade-up">
            {t('tours.title.1')} <span className="hl-yellow">{t('tours.title.2')}</span>
          </h2>
          <p className="body-lg fade-up" style={{ marginTop: '12px' }}>
            {t('tours.desc')}
          </p>
        </div>
        <div className="tours-grid">
          
          <TourCard 
            id="saona"
            img="img/island.jpg"
            badgeKey="tour.saona.badge"
            nameKey="tour.saona.name"
            locationKey="tour.saona.location"
            featuresKeys={['tour.saona.f1', 'tour.saona.f2', 'tour.saona.f3', 'tour.saona.f4']}
          />

          <TourCard 
            id="party"
            img="img/catamaran.png"
            badgeKey="tour.party.badge"
            nameKey="tour.party.name"
            locationKey="tour.party.location"
            featuresKeys={['tour.party.f1', 'tour.party.f2', 'tour.party.f3', 'tour.party.f4']}
            delay="d1"
          />

          <TourCard 
            id="atv"
            img="img/buggy.png"
            badgeKey="tour.atv.badge"
            nameKey="tour.atv.name"
            locationKey="tour.atv.location"
            featuresKeys={['tour.atv.f1', 'tour.atv.f2', 'tour.atv.f3']}
            delay="d2"
          />
          
          <TourCard 
            id="santodomingo"
            img="img/island.jpg"
            badgeKey="tour.santodomingo.badge"
            nameKey="tour.santodomingo.name"
            locationKey="tour.santodomingo.location"
            noteKey="tour.santodomingo.note"
            featuresKeys={[
              'tour.santodomingo.f1', 'tour.santodomingo.f2', 'tour.santodomingo.f3', 
              'tour.santodomingo.f4', 'tour.santodomingo.f5', 'tour.santodomingo.f6',
              'tour.santodomingo.f7', 'tour.santodomingo.f8', 'tour.santodomingo.f9',
              'tour.santodomingo.f10', 'tour.santodomingo.f11', 'tour.santodomingo.f12'
            ]}
            delay="d3"
          />

        </div>
      </div>
    </section>
  );
};

export default ToursGrid;
"""

with open('src/components/TourCard.jsx', 'w', encoding='utf-8') as f:
    f.write(tour_card_code)

with open('src/components/ToursGrid.jsx', 'w', encoding='utf-8') as f:
    f.write(tours_grid_code)

print("Tours components generated")
