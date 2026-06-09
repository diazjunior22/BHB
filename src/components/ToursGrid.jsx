import React from 'react';
import { useTranslation } from '../I18nContext';
import TourCard from './TourCard';

import imgSaona from '../assets/bhb/Saona Island.jpeg';
import imgCongo from '../assets/bhb/congo.jpeg';
import imgCongoVip from '../assets/bhb/congoVip.jpeg';
import imgSantoDomingo from '../assets/bhb/SantoDomingo.jpeg';
import imgDolphinExplorer from '../assets/bhb/Dolphin Explorer.jpeg';
import imgScapePark from '../assets/bhb/Scape Park.jpeg';
import imgHaciendaPark from '../assets/bhb/Hacienda Park.jpeg';
import imgScubaDoo from '../assets/bhb/Scuba Doo.jpeg';
import imgPescaFishing from '../assets/bhb/Pesca Fishing.jpeg';
import imgFunPark from '../assets/bhb/Fun Park 4x1.jpeg';
import imgSamana from '../assets/bhb/Samaná.jpeg';
import imgCatalinaIsland from '../assets/bhb/Catalina Island.jpeg';
import imgParasailing from '../assets/bhb/Parasailing.jpeg';
import imgElDorado from '../assets/bhb/El Dorado Park.jpeg';
import imgAtv from '../assets/bhb/boguie.png';
import imgBavaro from '../assets/bhb/bavaro.png';
import imgPartyBoat from '../assets/bhb/partyboat.jpeg';

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
            img={imgSaona}
            badgeKey="tour.saona.badge"
            nameKey="tour.saona.name"
            locationKey="tour.saona.location"
            featuresKeys={['tour.saona.f1', 'tour.saona.f2', 'tour.saona.f3', 'tour.saona.f4']}
          />

          <TourCard 
            id="saonavip"
            img={imgSaona}
            badgeKey="tour.saonavip.badge"
            nameKey="tour.saonavip.name"
            locationKey="tour.saonavip.location"
            featuresKeys={['tour.saonavip.f1', 'tour.saonavip.f2', 'tour.saonavip.f3', 'tour.saonavip.f4']}
            delay="d1"
          />

          <TourCard 
            id="party"
            img={imgPartyBoat}
            badgeKey="tour.party.badge"
            nameKey="tour.party.name"
            locationKey="tour.party.location"
            featuresKeys={['tour.party.f1', 'tour.party.f2', 'tour.party.f3', 'tour.party.f4']}
            delay="d1"
          />

          <TourCard 
            id="atv"
            img={imgAtv}
            badgeKey="tour.atv.badge"
            nameKey="tour.atv.name"
            locationKey="tour.atv.location"
            featuresKeys={['tour.atv.f1', 'tour.atv.f2', 'tour.atv.f3']}
            delay="d2"
          />
          
          <TourCard 
            id="santodomingo"
            img={imgSantoDomingo}
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

          <TourCard 
            id="cocobongo"
            img={imgCongo} 
            badgeKey="tour.cocobongo.badge"
            nameKey="tour.cocobongo.name"
            locationKey="tour.cocobongo.location"
            noteKey="tour.cocobongo.note"
            featuresKeys={[
              'tour.cocobongo.f1', 
              'tour.cocobongo.f2', 
              'tour.cocobongo.f3', 
              'tour.cocobongo.f4'
            ]}
            delay="d1"
          />

          <TourCard 
            id="cocobongovip"
            img={imgCongoVip} 
            badgeKey="tour.cocobongovip.badge"
            nameKey="tour.cocobongovip.name"
            locationKey="tour.cocobongovip.location"
            noteKey="tour.cocobongovip.note"
            featuresKeys={[
              'tour.cocobongovip.f1', 
              'tour.cocobongovip.f2', 
              'tour.cocobongovip.f3', 
              'tour.cocobongovip.f4',
              'tour.cocobongovip.f5'
            ]}
            delay="d2"
          />

          <TourCard 
            id="dolphinexplorer"
            img={imgDolphinExplorer} 
            badgeKey="tour.dolphinexplorer.badge"
            nameKey="tour.dolphinexplorer.name"
            locationKey="tour.dolphinexplorer.location"
            noteKey="tour.dolphinexplorer.note"
            featuresKeys={[
              'tour.dolphinexplorer.f1', 
              'tour.dolphinexplorer.f2', 
              'tour.dolphinexplorer.f3', 
              'tour.dolphinexplorer.f4',
              'tour.dolphinexplorer.f5',
              'tour.dolphinexplorer.f6'
            ]}
            delay="d3"
          />

          <TourCard 
            id="scapepark"
            img={imgScapePark} 
            badgeKey="tour.scapepark.badge"
            nameKey="tour.scapepark.name"
            locationKey="tour.scapepark.location"
            noteKey="tour.scapepark.note"
            featuresKeys={[
              'tour.scapepark.f1', 
              'tour.scapepark.f2', 
              'tour.scapepark.f3', 
              'tour.scapepark.f4',
              'tour.scapepark.f5',
              'tour.scapepark.f6',
              'tour.scapepark.f7'
            ]}
            delay="d1"
          />

          <TourCard 
            id="haciendapark"
            img={imgHaciendaPark} 
            badgeKey="tour.haciendapark.badge"
            nameKey="tour.haciendapark.name"
            locationKey="tour.haciendapark.location"
            noteKey="tour.haciendapark.note"
            featuresKeys={[
              'tour.haciendapark.f1', 
              'tour.haciendapark.f2', 
              'tour.haciendapark.f3', 
              'tour.haciendapark.f4',
              'tour.haciendapark.f5',
              'tour.haciendapark.f6',
              'tour.haciendapark.f7',
              'tour.haciendapark.f8',
              'tour.haciendapark.f9',
              'tour.haciendapark.f10'
            ]}
            delay="d2"
          />

          <TourCard 
            id="scubadoo"
            img={imgScubaDoo} 
            badgeKey="tour.scubadoo.badge"
            nameKey="tour.scubadoo.name"
            locationKey="tour.scubadoo.location"
            noteKey="tour.scubadoo.note"
            featuresKeys={[
              'tour.scubadoo.f1', 
              'tour.scubadoo.f2', 
              'tour.scubadoo.f3', 
              'tour.scubadoo.f4',
              'tour.scubadoo.f5',
              'tour.scubadoo.f6',
              'tour.scubadoo.f7'
            ]}
            delay="d3"
          />

          <TourCard 
            id="pescafishing"
            img={imgPescaFishing} 
            badgeKey="tour.pescafishing.badge"
            nameKey="tour.pescafishing.name"
            locationKey="tour.pescafishing.location"
            noteKey="tour.pescafishing.note"
            featuresKeys={[
              'tour.pescafishing.f1', 
              'tour.pescafishing.f2', 
              'tour.pescafishing.f3', 
              'tour.pescafishing.f4',
              'tour.pescafishing.f5',
              'tour.pescafishing.f6',
              'tour.pescafishing.f7'
            ]}
            delay="d1"
          />

          <TourCard 
            id="funpark"
            img={imgFunPark} 
            badgeKey="tour.funpark.badge"
            nameKey="tour.funpark.name"
            locationKey="tour.funpark.location"
            noteKey="tour.funpark.note"
            featuresKeys={[
              'tour.funpark.f1', 
              'tour.funpark.f2', 
              'tour.funpark.f3', 
              'tour.funpark.f4',
              'tour.funpark.f5',
              'tour.funpark.f6',
              'tour.funpark.f7',
              'tour.funpark.f8',
              'tour.funpark.f9'
            ]}
            delay="d2"
          />

          <TourCard 
            id="samana"
            img={imgSamana} 
            badgeKey="tour.samana.badge"
            nameKey="tour.samana.name"
            locationKey="tour.samana.location"
            noteKey="tour.samana.note"
            featuresKeys={[
              'tour.samana.f1', 
              'tour.samana.f2', 
              'tour.samana.f3', 
              'tour.samana.f4',
              'tour.samana.f5',
              'tour.samana.f6',
              'tour.samana.f7',
              'tour.samana.f8',
              'tour.samana.f9',
              'tour.samana.f10',
              'tour.samana.f11'
            ]}
            delay="d3"
          />

          <TourCard 
            id="catalinaisland"
            img={imgCatalinaIsland} 
            badgeKey="tour.catalinaisland.badge"
            nameKey="tour.catalinaisland.name"
            locationKey="tour.catalinaisland.location"
            noteKey="tour.catalinaisland.note"
            featuresKeys={[
              'tour.catalinaisland.f1', 
              'tour.catalinaisland.f2', 
              'tour.catalinaisland.f3', 
              'tour.catalinaisland.f4',
              'tour.catalinaisland.f5',
              'tour.catalinaisland.f6',
              'tour.catalinaisland.f7'
            ]}
            delay="d1"
          />

          <TourCard 
            id="parasailing"
            img={imgParasailing} 
            badgeKey="tour.parasailing.badge"
            nameKey="tour.parasailing.name"
            locationKey="tour.parasailing.location"
            noteKey="tour.parasailing.note"
            featuresKeys={[
              'tour.parasailing.f1', 
              'tour.parasailing.f2', 
              'tour.parasailing.f3', 
              'tour.parasailing.f4',
              'tour.parasailing.f5'
            ]}
            delay="d2"
          />

          <TourCard 
            id="eldorado"
            img={imgElDorado} 
            badgeKey="tour.eldorado.badge"
            nameKey="tour.eldorado.name"
            locationKey="tour.eldorado.location"
            noteKey="tour.eldorado.note"
            featuresKeys={[
              'tour.eldorado.f1', 
              'tour.eldorado.f2', 
              'tour.eldorado.f3', 
              'tour.eldorado.f4',
              'tour.eldorado.f5',
              'tour.eldorado.f6',
              'tour.eldorado.f7',
              'tour.eldorado.f8'
            ]}
            delay="d3"
          />

          <TourCard 
            id="bavaropark"
            img={imgBavaro} 
            badgeKey="tour.bavaropark.badge"
            nameKey="tour.bavaropark.name"
            locationKey="tour.bavaropark.location"
            noteKey="tour.bavaropark.note"
            featuresKeys={[
              'tour.bavaropark.f1', 
              'tour.bavaropark.f2', 
              'tour.bavaropark.f3', 
              'tour.bavaropark.f4',
              'tour.bavaropark.f5'
            ]}
            delay="d1"
          />
        </div>
      </div>
    </section>
  );
};

export default ToursGrid;
