import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { useTranslation } from '../I18nContext';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  Star, 
  MapPin, 
  Clock, 
  CheckCircle2, 
  XCircle, 
  ChevronDown, 
  ChevronUp, 
  Play, 
  Image as ImageIcon,
  ShieldCheck,
  CalendarCheck
} from 'lucide-react';
import BavaroActivities from '../components/BavaroActivities';

import heroSaona from '../assets/bhb/Saona Island.jpeg';
import heroCongo from '../assets/bhb/congo.jpeg';
import heroCongoVip from '../assets/bhb/congoVip.jpeg';
import heroSantoDomingo from '../assets/bhb/SantoDomingo.jpeg';
import heroDolphinExplorer from '../assets/bhb/Dolphin Explorer.jpeg';
import heroScapePark from '../assets/bhb/Scape Park.jpeg';
import heroHaciendaPark from '../assets/bhb/Hacienda Park.jpeg';
import heroScubaDoo from '../assets/bhb/Scuba Doo.jpeg';
import heroPescaFishing from '../assets/bhb/Pesca Fishing.jpeg';
import heroFunPark from '../assets/bhb/Fun Park 4x1.jpeg';
import heroSamana from '../assets/bhb/Samaná.jpeg';
import heroCatalinaIsland from '../assets/bhb/Catalina Island.jpeg';
import heroParasailing from '../assets/bhb/Parasailing.jpeg';
import heroElDorado from '../assets/bhb/El Dorado Park.jpeg';
import heroAtv from '../assets/bhb/boguie.png';
import elDorado1 from '../assets/bhb/El Dorado Park/1.jpeg';
import elDorado2 from '../assets/bhb/El Dorado Park/2.jpeg';
import elDorado3 from '../assets/bhb/El Dorado Park/3.jpeg';
import elDorado4 from '../assets/bhb/El Dorado Park/4.jpeg';

import saona1 from '../assets/bhb/Saona Island/1.jpg';
import saona2 from '../assets/bhb/Saona Island/2.jpg';
import saona3 from '../assets/bhb/Saona Island/3.webp';
import saona4 from '../assets/bhb/Saona Island/4.jpg';
import saona5 from '../assets/bhb/Saona Island/5.jpg';

import party1 from '../assets/bhb/Party boat/1.jpg';
import party2 from '../assets/bhb/Party boat/2.jpg';
import party3 from '../assets/bhb/Party boat/3.jpg';
import party4 from '../assets/bhb/Party boat/4.jpg';
import party5 from '../assets/bhb/Party boat/5.jpg';

import congo1 from '../assets/bhb/congo/1.jpg';
import congo2 from '../assets/bhb/congo/2.jpg';
import congo3 from '../assets/bhb/congo/3.jpg';
import congo4 from '../assets/bhb/congo/4.jpg';
import congo5 from '../assets/bhb/congo/5.jpg';

import boguie1 from '../assets/bhb/boguie/1.png';
import boguie2 from '../assets/bhb/boguie/2.png';
import boguie3 from '../assets/bhb/boguie/3.png';
import boguie4 from '../assets/bhb/boguie/4.png';
import boguie5 from '../assets/bhb/boguie/5.png';

import samanaImage1 from '../assets/bhb/Samaná/1.jpg';
import samanaImage2 from '../assets/bhb/Samaná/2.jpg';
import samanaImage3 from '../assets/bhb/Samaná/3.jpg';
import samanaImage4 from '../assets/bhb/Samaná/4.jpg';

import pescaImage1 from '../assets/bhb/Pesca Fishing/1.jpg';
import pescaImage2 from '../assets/bhb/Pesca Fishing/2.jpg';
import pescaImage3 from '../assets/bhb/Pesca Fishing/3.jpg';
import pescaImage4 from '../assets/bhb/Pesca Fishing/4.jpg';

import catalinaImage1 from '../assets/bhb/Catalina Island/1.jpg';
import catalinaImage2 from '../assets/bhb/Catalina Island/2.jpg';
import catalinaImage3 from '../assets/bhb/Catalina Island/3.jpg';
import catalinaImage4 from '../assets/bhb/Catalina Island/4.jpg';
import catalinaImage5 from '../assets/bhb/Catalina Island/5.jpg';

import santodomingoImage1 from '../assets/bhb/City Tour in Santo Domingo/1.jpg';
import santodomingoImage2 from '../assets/bhb/City Tour in Santo Domingo/2.jpg';
import santodomingoImage3 from '../assets/bhb/City Tour in Santo Domingo/3.jpg';
import santodomingoImage4 from '../assets/bhb/City Tour in Santo Domingo/4.jpg';
import santodomingoImage5 from '../assets/bhb/City Tour in Santo Domingo/5.jpg';

import bavaroImage1 from '../assets/bhb/barvaro/1.jpg';
import bavaroImage2 from '../assets/bhb/barvaro/2.jpg';
import bavaroImage3 from '../assets/bhb/barvaro/3.jpg';
import bavaroImage4 from '../assets/bhb/barvaro/4.jpg';
import bavaroImage5 from '../assets/bhb/barvaro/5.jpg';

import parasailingImage1 from '../assets/bhb/Parasailing/1.jpg';
import parasailingImage2 from '../assets/bhb/Parasailing/2.jpg';
import parasailingImage3 from '../assets/bhb/Parasailing/3.jpg';
import parasailingImage4 from '../assets/bhb/Parasailing/4.jpg';
import parasailingImage5 from '../assets/bhb/Parasailing/5.jpg';

import dolphinImage1 from '../assets/bhb/Dolphin Explorer/1.jpg';
import dolphinImage2 from '../assets/bhb/Dolphin Explorer/2.jpg';
import dolphinImage3 from '../assets/bhb/Dolphin Explorer/3.jpg';
import dolphinImage4 from '../assets/bhb/Dolphin Explorer/4.jpg';
import dolphinImage5 from '../assets/bhb/Dolphin Explorer/5.jpg';

import scapeImage1 from '../assets/bhb/Scape Park/1.jpg';
import scapeImage2 from '../assets/bhb/Scape Park/2.jpg';
import scapeImage3 from '../assets/bhb/Scape Park/3.jpg';
import scapeImage4 from '../assets/bhb/Scape Park/4.jpg';
import scapeImage5 from '../assets/bhb/Scape Park/5.jpg';

const defaultGallery = [
  'https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?q=80&w=800&auto=format&fit=crop',
  'https://images.unsplash.com/photo-1510414842594-a61c69b5ae57?q=80&w=600&auto=format&fit=crop',
  'https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?q=80&w=600&auto=format&fit=crop',
  'https://images.unsplash.com/photo-1584346904677-2f3b61073809?q=80&w=600&auto=format&fit=crop',
  'https://images.unsplash.com/photo-1549643276-fdf2fab574f5?q=80&w=600&auto=format&fit=crop'
];

const getGallery = (customGallery) => {
  if (!customGallery) return defaultGallery;
  const fullGallery = [...customGallery];
  while (fullGallery.length < 5) {
    fullGallery.push(defaultGallery[fullGallery.length]);
  }
  return fullGallery;
};

const tourImages = {
  saona: { hero: heroSaona, gallery: getGallery([saona1, saona2, saona3, saona4, saona5]), video: 'https://player.cloudinary.com/embed/?cloud_name=dmtqsct7k&public_id=WhatsApp_Video_2026-06-01_at_3.06.31_PM_bqgkan', videoVertical: true },
  saonavip: { hero: heroSaona, gallery: getGallery([saona1, saona2, saona3, saona4, saona5]), video: 'https://player.cloudinary.com/embed/?cloud_name=dmtqsct7k&public_id=WhatsApp_Video_2026-06-01_at_3.06.31_PM_bqgkan', videoVertical: true },
  santodomingo: { hero: heroSantoDomingo, gallery: getGallery([santodomingoImage1, santodomingoImage2, santodomingoImage3, santodomingoImage4, santodomingoImage5]) },
  party: { hero: heroCongo, gallery: getGallery([party1, party2, party3, party4, party5]) },
  atv: { hero: heroAtv, gallery: getGallery([boguie1, boguie2, boguie3, boguie4, boguie5]), video: 'https://player.cloudinary.com/embed/?cloud_name=dmtqsct7k&public_id=WhatsApp_Video_2026-06-01_at_3.07.29_PM_c1gjp2', videoVertical: true },
  cocobongo: { hero: heroCongo, gallery: getGallery([congo1, congo2, congo3, congo4, congo5]) },
  scubadoo: { hero: heroScubaDoo, gallery: getGallery(['https://images.unsplash.com/photo-1561081533-3d09a067fffc?q=80&w=800&auto=format&fit=crop']), video: 'https://player.cloudinary.com/embed/?cloud_name=dmtqsct7k&public_id=WhatsApp_Video_2026-06-01_at_3.08.59_PM_hhlhh7', videoVertical: true },
  cocobongovip: { hero: heroCongoVip, gallery: getGallery([congo1, congo2, congo3, congo4, congo5]) },
  dolphinexplorer: { hero: heroDolphinExplorer, gallery: getGallery([dolphinImage1, dolphinImage2, dolphinImage3, dolphinImage4, dolphinImage5]) },
  scapepark: { hero: heroScapePark, gallery: getGallery([scapeImage1, scapeImage2, scapeImage3, scapeImage4, scapeImage5]) },
  haciendapark: { hero: heroHaciendaPark, gallery: getGallery(['https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?q=80&w=800&auto=format&fit=crop']), video: 'https://res.cloudinary.com/dmtqsct7k/video/upload/v1780847645/WhatsApp_Video_2026-06-07_at_10.51.14_AM_qihqnp.mp4', videoVertical: true },
  pescafishing: { hero: heroPescaFishing, gallery: getGallery([pescaImage1, pescaImage2, pescaImage3, pescaImage4]) },
  funpark: { hero: heroFunPark, gallery: getGallery(['https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?q=80&w=800&auto=format&fit=crop']) },
  samana: { hero: heroSamana, gallery: getGallery([samanaImage1, samanaImage2, samanaImage3, samanaImage4]) },
  catalinaisland: { hero: heroCatalinaIsland, gallery: getGallery([catalinaImage1, catalinaImage2, catalinaImage3, catalinaImage4, catalinaImage5]) },
  parasailing: { hero: heroParasailing, gallery: getGallery([parasailingImage1, parasailingImage2, parasailingImage3, parasailingImage4, parasailingImage5]) },
  eldorado: { hero: heroElDorado, gallery: getGallery([elDorado1, elDorado2, elDorado3, elDorado4]) },
  bavaropark: { hero: heroAtv, gallery: getGallery([bavaroImage1, bavaroImage2, bavaroImage3, bavaroImage4, bavaroImage5]), video: 'https://res.cloudinary.com/dmtqsct7k/video/upload/v1780848151/WhatsApp_Video_2026-06-07_at_10.55.21_AM_x865ht.mp4', videoVertical: true },
  default: { hero: 'https://images.unsplash.com/photo-1548574505-5e239809ee19?q=80&w=1400&auto=format&fit=crop', gallery: defaultGallery }
};

const WhatsAppIcon = ({ className }) => (
  <svg viewBox="0 0 24 24" fill="currentColor" className={className} width="24" height="24">
    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51a12.8 12.8 0 0 0-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z"/>
  </svg>
);

const FAQItem = ({ question, answer }) => {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <div className="td2-faq-item">
      <button className="td2-faq-question" onClick={() => setIsOpen(!isOpen)}>
        <span>{question}</span>
        {isOpen ? <ChevronUp size={20} className="text-gray-500" /> : <ChevronDown size={20} className="text-gray-500" />}
      </button>
      <AnimatePresence>
        {isOpen && (
          <motion.div 
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: 'auto', opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            className="td2-faq-answer"
          >
            <p>{answer}</p>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

const BookingForm = ({ price, name, id, getLabel, t }) => {
  const [date, setDate] = useState('');
  const [adults, setAdults] = useState(2);
  const [kids, setKids] = useState(0);

  const basePrice = parseInt(price) || 0;
  let adultPrice = basePrice;
  let kidsPrice = basePrice; 

  if (id === 'eldorado' || id === 'scapepark') {
    adultPrice = 129;
    kidsPrice = 69;
  }

  const total = (adults * adultPrice) + (kids * kidsPrice);

  const handleBook = (e) => {
    e.preventDefault();
    if (!date) {
      alert(getLabel('Please select a date', 'Por favor selecciona una fecha', 'Por favor selecione uma data'));
      return;
    }
    const msg = `Hola, me interesa reservar el tour: *${name}*\n\n📅 Fecha: ${date}\n👥 Personas: ${adults} Adultos, ${kids} Niños.\n💰 Total estimado: $${total} USD.`;
    const whatsappUrl = `https://wa.me/18295555555?text=${encodeURIComponent(msg)}`;
    window.open(whatsappUrl, '_blank');
  };

  const getToday = () => new Date().toISOString().split('T')[0];

  return (
    <div className="td2-booking-card" id="booking-form">
      <div className="td2-bc-header">
        <span className="td2-price-label">{getLabel('Price', 'Precio', 'Preço')}</span>
        <div className="td2-price-amount">
          <span>$</span>{adultPrice} <span>USD / {id === 'parasailing' ? getLabel('2 People', '2 Personas', '2 Pessoas') : getLabel('Adult', 'Adulto', 'Adulto')}</span>
        </div>
      </div>

      <div className="td2-bc-body">
        <div className="td2-input-group">
          <label>{getLabel('Date', 'Fecha', 'Data')}</label>
          <input 
            type="date" 
            className="td2-input" 
            value={date} 
            onChange={e => setDate(e.target.value)} 
            min={getToday()} 
          />
        </div>

        <div className="td2-guests-grid">
          <div className="td2-guest-row">
            <div className="td2-guest-info">
              <strong>{id === 'parasailing' ? getLabel('Couples (2 People)', 'Parejas (2 Personas)', 'Casais (2 Pessoas)') : getLabel('Adults', 'Adultos', 'Adultos')}</strong>
              <span>${adultPrice} USD</span>
            </div>
            <div className="td2-counter">
              <button type="button" onClick={() => setAdults(Math.max(1, adults - 1))}>-</button>
              <span>{adults}</span>
              <button type="button" onClick={() => setAdults(adults + 1)}>+</button>
            </div>
          </div>
          
          <div className="td2-guest-row">
            <div className="td2-guest-info">
              <strong>{getLabel('Kids', 'Niños', 'Crianças')}</strong>
              <span>${kidsPrice} USD</span>
            </div>
            <div className="td2-counter">
              <button type="button" onClick={() => setKids(Math.max(0, kids - 1))}>-</button>
              <span>{kids}</span>
              <button type="button" onClick={() => setKids(kids + 1)}>+</button>
            </div>
          </div>
        </div>

        <div className="td2-total-row">
          <span>{getLabel('Total estimated', 'Total estimado', 'Total estimado')}</span>
          <strong>${total} USD</strong>
        </div>

        <button onClick={handleBook} className="td2-btn-whatsapp-large mt-3">
          <WhatsAppIcon className="mr-2" />
          {getLabel('Book via WhatsApp', 'Reservar por WhatsApp', 'Reservar via WhatsApp')}
        </button>

        <div className="td2-safe-badge mt-3">
          <ShieldCheck size={18} />
          <span>{t('tour.safeReserve') || getLabel('Secure Booking', 'Reserva Segura', 'Reserva Segura')}</span>
        </div>
      </div>
    </div>
  );
};

const TourDetail = () => {
  const { id } = useParams();
  const { t, lang } = useTranslation();
  
  useEffect(() => {
    window.scrollTo(0, 0);
  }, [id]);

  const name = t(`tour.${id}.name`);
  const location = t(`tour.${id}.location`);
  const duration = t(`tour.${id}.duration`);
  const price = t(`tour.${id}.price`);
  const shortDesc = t(`tour.${id}.shortDesc`);
  const rating = t(`tour.${id}.rating`) || "4.9";
  const reviewsCount = t(`tour.${id}.reviewsCount`) || "300";
  
  const images = tourImages[id] || tourImages.default;

  // Inclusions
  const inclusions = [];
  for(let i=1; i<=12; i++) {
    const f = t(`tour.${id}.f${i}`);
    if (f && typeof f === 'string' && !f.includes(`tour.${id}.f${i}`)) inclusions.push(f);
  }

  // Not Included
  const notIncluded = [];
  for(let i=1; i<=3; i++) {
    const ni = t(`tour.${id}.notIncluded${i}`);
    if (ni && typeof ni === 'string' && !ni.includes(`tour.${id}.notIncluded${i}`)) notIncluded.push(ni);
  }

  // Reviews
  const reviews = [];
  for(let i=1; i<=2; i++) {
    const rName = t(`tour.${id}.review${i}Name`);
    const rText = t(`tour.${id}.review${i}Text`);
    if (rName && !rName.includes(`review${i}Name`)) {
      reviews.push({ name: rName, text: rText });
    }
  }

  const getLabel = (en, es, pt) => {
    if (lang === 'en') return en;
    if (lang === 'pt') return pt;
    return es;
  };

  const scrollToBooking = (e) => {
    e.preventDefault();
    const el = document.getElementById('booking-form');
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  };

  return (
    <div className="tour-detail-v2">
      
      {/* 1. HERO PREMIUM FULLSCREEN */}
      <section className="td2-hero">
        <div className="td2-hero-bg">
          <img src={images.hero} alt={name} />
          <div className="td2-hero-overlay"></div>
        </div>
        
        <div className="td2-container">
          <motion.div 
            className="td2-hero-content"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
          >
            <div className="td2-breadcrumbs">
              <Link to="/">{getLabel('Home', 'Inicio', 'Início')}</Link> 
              <span>/</span> 
              <span>{name}</span>
            </div>
            
            <h1 className="td2-title">{name}</h1>
            
            <div className="td2-meta">
              <div className="td2-meta-item">
                <Star className="td2-icon-yellow" size={20} fill="currentColor" />
                <span><strong>{rating}</strong> ({reviewsCount} {getLabel('reviews', 'opiniones', 'avaliações')})</span>
              </div>
              <div className="td2-meta-item">
                <MapPin size={20} />
                <span>{location}</span>
              </div>
              <div className="td2-meta-item">
                <Clock size={20} />
                <span>{duration}</span>
              </div>
            </div>

            <div className="td2-hero-actions">
              {id === 'bavaropark' ? (
                <a href="#bavaro-activities" onClick={(e) => { e.preventDefault(); document.getElementById('bavaro-activities').scrollIntoView({behavior: 'smooth', block: 'start'})}} className="td2-btn-primary">
                  {getLabel('View Activities', 'Ver Actividades', 'Ver Atividades')}
                </a>
              ) : (
                <a href="#booking-form" onClick={scrollToBooking} className="td2-btn-primary">
                  <WhatsAppIcon className="mr-2" />
                  {getLabel('Book', 'Reservar', 'Reservar')}
                </a>
              )}
              <button className="td2-btn-secondary" onClick={() => document.getElementById('gallery').scrollIntoView({behavior: 'smooth'})}>
                <ImageIcon size={20} className="mr-2" />
                {t('tour.showAllPhotos') || 'Mostrar fotos'}
              </button>
            </div>
          </motion.div>
        </div>
      </section>

      {/* 2. MASONRY GALLERY */}
      <section id="gallery" className="td2-container td2-gallery-section">
        <div className="td2-gallery-grid desktop-only">
          <div className="td2-gallery-main">
            <img src={images.gallery[0]} alt="Gallery 1" />
          </div>
          <div className="td2-gallery-side">
            <img src={images.gallery[1]} alt="Gallery 2" />
            <img src={images.gallery[2]} alt="Gallery 3" />
            <img src={images.gallery[3]} alt="Gallery 4" />
            <img src={images.gallery[4]} alt="Gallery 5" />
          </div>
        </div>
        
        <div className="td2-gallery-mobile mobile-only">
          {images.gallery.map((img, i) => (
            <img key={i} src={img} alt={`Gallery ${i+1}`} className="td2-mobile-slide" />
          ))}
        </div>
      </section>

      {/* 3. MAIN CONTENT */}
      {id === 'bavaropark' ? (
        <section className="td2-container" id="bavaro-activities">
          <BavaroActivities />
          
          {/* VIDEO PREMIUM */}
          {images.video && (
            <motion.div 
              className="td2-block"
              style={{marginTop: '40px'}}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
            >
              <h2 className="td2-section-title">{getLabel('Video', 'Video', 'Vídeo')}</h2>
              <div className={`td2-video-container ${images.videoVertical ? 'is-vertical' : ''}`}>
                {images.video.includes('embed') ? (
                  <iframe
                    src={images.video}
                    allow="autoplay; fullscreen; encrypted-media; picture-in-picture"
                    allowFullScreen
                    frameBorder="0"
                    title="Video"
                  ></iframe>
                ) : (
                  <video controls preload="metadata">
                    <source src={images.video} type="video/mp4" />
                    {getLabel('Browser not supported.', 'Navegador no soportado.', 'Navegador não suportado.')}
                  </video>
                )}
              </div>
            </motion.div>
          )}

          {/* REVIEWS */}
          {reviews.length > 0 && (
            <motion.div 
              className="td2-block"
              style={{marginTop: '40px'}}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
            >
              <h2 className="td2-section-title">{getLabel('Traveler Reviews', 'Opiniones Reales', 'Avaliações Reais')}</h2>
              <div className="td2-reviews-slider">
                {reviews.map((rev, i) => (
                  <div key={i} className="td2-review-card">
                    <div className="td2-review-header">
                      <div className="td2-avatar">{rev.name.charAt(0)}</div>
                      <div>
                        <h4>{rev.name}</h4>
                        <div className="td2-stars">
                          {[1,2,3,4,5].map(s => <Star key={s} size={14} fill="currentColor" />)}
                        </div>
                      </div>
                    </div>
                    <p>"{rev.text}"</p>
                  </div>
                ))}
              </div>
            </motion.div>
          )}

          {/* FAQ */}
          <motion.div 
            className="td2-block"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="td2-section-title">{t('tour.faqTitle') || getLabel('FAQ', 'Preguntas Frecuentes', 'Perguntas Frequentes')}</h2>
            <div className="td2-faq-list">
              {[1,2,3,4].map(num => (
                <FAQItem 
                  key={num} 
                  question={t(`tour.faq.q${num}`)} 
                  answer={t(`tour.faq.a${num}`)} 
                />
              ))}
            </div>
          </motion.div>
        </section>
      ) : (
        <section className="td2-container td2-layout">
          
          <div className="td2-content-left">
          
          {/* ABOUT THE EXPERIENCE */}
          <motion.div 
            className="td2-block"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="td2-section-title">{t('tour.aboutTitle') || getLabel('The Experience', 'La Experiencia', 'A Experiência')}</h2>
            <p className="td2-desc">{shortDesc}</p>
          </motion.div>

          {/* HIGHLIGHTS CARDS */}
          <motion.div 
            className="td2-block"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="td2-section-title">{getLabel('Highlights', 'Destacados', 'Destaques')}</h2>
            <div className="td2-highlights-grid">
              {inclusions.slice(0, 6).map((inc, i) => (
                <div key={i} className="td2-highlight-card">
                  <CheckCircle2 className="td2-highlight-icon" />
                  <span>{inc}</span>
                </div>
              ))}
            </div>
          </motion.div>

          {/* VIDEO PREMIUM */}
          {images.video && (
            <motion.div 
              className="td2-block"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
            >
              <h2 className="td2-section-title">{getLabel('Video', 'Video', 'Vídeo')}</h2>
              <div className={`td2-video-container ${images.videoVertical ? 'is-vertical' : ''}`}>
                {images.video.includes('embed') ? (
                  <iframe
                    src={images.video}
                    allow="autoplay; fullscreen; encrypted-media; picture-in-picture"
                    allowFullScreen
                    frameBorder="0"
                    title="Video"
                  ></iframe>
                ) : (
                  <video controls preload="metadata">
                    <source src={images.video} type="video/mp4" />
                    {getLabel('Browser not supported.', 'Navegador no soportado.', 'Navegador não suportado.')}
                  </video>
                )}
              </div>
            </motion.div>
          )}

          {/* WHAT'S INCLUDED / NOT INCLUDED */}
          <motion.div 
            className="td2-block td2-inc-exc"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <div className="td2-inc-card">
              <h3>{t('tour.includes') || getLabel('Included', 'Incluye', 'Incluído')}</h3>
              <ul>
                {inclusions.map((inc, i) => (
                  <li key={i}><CheckCircle2 className="td2-icon-green" /> {inc}</li>
                ))}
              </ul>
            </div>
            <div className="td2-exc-card">
              <h3>{t('tour.notIncludes') || getLabel('Not Included', 'No incluye', 'Não incluso')}</h3>
              <ul>
                {notIncluded.map((ni, i) => (
                  <li key={i}><XCircle className="td2-icon-red" /> {ni}</li>
                ))}
              </ul>
            </div>
          </motion.div>

          {/* MOBILE BOOKING FORM (Hidden on desktop, visible on mobile) */}
          <div className="td2-mobile-booking">
             <h2 className="td2-section-title">{getLabel('Reserve your spot', 'Reserva tu lugar', 'Reserve o seu lugar')}</h2>
             <BookingForm price={price} name={name} id={id} getLabel={getLabel} t={t} />
          </div>

          {/* REVIEWS */}
          {reviews.length > 0 && (
            <motion.div 
              className="td2-block"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
            >
              <h2 className="td2-section-title">{getLabel('Traveler Reviews', 'Opiniones Reales', 'Avaliações Reais')}</h2>
              <div className="td2-reviews-slider">
                {reviews.map((rev, i) => (
                  <div key={i} className="td2-review-card">
                    <div className="td2-review-header">
                      <div className="td2-avatar">{rev.name.charAt(0)}</div>
                      <div>
                        <h4>{rev.name}</h4>
                        <div className="td2-stars">
                          {[1,2,3,4,5].map(s => <Star key={s} size={14} fill="currentColor" />)}
                        </div>
                      </div>
                    </div>
                    <p>"{rev.text}"</p>
                  </div>
                ))}
              </div>
            </motion.div>
          )}

          {/* FAQ */}
          <motion.div 
            className="td2-block"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="td2-section-title">{t('tour.faqTitle') || getLabel('FAQ', 'Preguntas Frecuentes', 'Perguntas Frequentes')}</h2>
            <div className="td2-faq-list">
              {[1,2,3,4].map(num => (
                <FAQItem 
                  key={num} 
                  question={t(`tour.faq.q${num}`)} 
                  answer={t(`tour.faq.a${num}`)} 
                />
              ))}
            </div>
          </motion.div>

        </div>

        {/* RIGHT COLUMN: STICKY CARD (Desktop only) */}
        <div className="td2-content-right td2-desktop-booking">
           <div className="td2-sticky-container">
              <BookingForm price={price} name={name} id={id} getLabel={getLabel} t={t} />
              
              <div className="td2-sticky-features mt-4">
                <div className="td2-sf-item">
                  <Clock className="td2-sf-icon" />
                  <div>
                    <strong>{getLabel('Duration', 'Duración', 'Duração')}</strong>
                    <span>{duration}</span>
                  </div>
                </div>
                <div className="td2-sf-item">
                  <CalendarCheck className="td2-sf-icon" />
                  <div>
                    <strong>{getLabel('Availability', 'Disponibilidad', 'Disponibilidade')}</strong>
                    <span>{getLabel('Daily', 'Todos los días', 'Diariamente')}</span>
                  </div>
                </div>
              </div>
           </div>
        </div>
      </section>
      )}

      {/* 4. FINAL CTA BANNER */}
      <section className="td2-final-cta">
        <div className="td2-container">
          <motion.div 
            className="td2-cta-content"
            initial={{ opacity: 0, scale: 0.95 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true }}
          >
            <h2>{t('tour.ctaFinalTitle') || getLabel('Ready?', '¿Listo?', 'Pronto?')}</h2>
            <p>{t('tour.ctaFinalSub')}</p>
            <a href={id === 'bavaropark' ? "#bavaro-activities" : "#booking-form"} onClick={id === 'bavaropark' ? (e) => { e.preventDefault(); document.getElementById('bavaro-activities').scrollIntoView({behavior: 'smooth', block: 'start'})} : scrollToBooking} className="td2-btn-white">
              <WhatsAppIcon className="mr-2" />
              {id === 'bavaropark' ? getLabel('View Activities', 'Ver Actividades', 'Ver Atividades') : getLabel('Book Now', 'Reserva Ahora', 'Reservar Agora')}
            </a>
          </motion.div>
        </div>
      </section>

      {/* MOBILE STICKY BOTTOM BAR */}
      {id !== 'bavaropark' && (
      <div className="td2-mobile-sticky-bar">
        <div className="td2-ms-price">
          <span className="td2-ms-label">{getLabel('Price', 'Precio', 'Preço')}</span>
          <span className="td2-ms-value">${price} USD</span>
        </div>
        <a href="#booking-form" onClick={scrollToBooking} className="td2-btn-whatsapp-mobile">
          <WhatsAppIcon className="mr-1" />
          {getLabel('Book', 'Reservar', 'Reservar')}
        </a>
      </div>
      )}

    </div>
  );
};

export default TourDetail;
