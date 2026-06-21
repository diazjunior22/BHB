import React, { useState } from 'react';
import { useTranslation } from '../I18nContext';

const Transport = () => {
  const { lang, t } = useTranslation();
  const [formData, setFormData] = useState({
    origin: '',
    destination: '',
    date: '',
    time: '',
    people: '1',
    note: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.id]: e.target.value });
  };

  const getToday = () => new Date().toISOString().split('T')[0];

  const getLabel = (en, es, pt) => {
    if (lang === 'en') return en;
    if (lang === 'pt') return pt;
    return es;
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    let intro = getLabel(
      'Hello! I would like to book a transfer.',
      '¡Hola! Me gustaría reservar un transporte.',
      'Olá! Gostaria de reservar um transporte.'
    );
    let labelOrigin = getLabel('Pickup / Origin', 'Origen / Pickup', 'Origem / Pickup');
    let labelDestination = getLabel('Destination', 'Destino', 'Destino');
    let labelDate = getLabel('Transfer date', 'Fecha del traslado', 'Data do traslado');
    let labelTime = getLabel('Pickup time', 'Hora de recogida', 'Horário de coleta');
    let labelPeople = getLabel('People', 'Personas', 'Pessoas');
    let labelNote = getLabel('Note', 'Nota', 'Observação');

    const text = `${intro}\n\n` +
      `*${labelOrigin}:* ${formData.origin}\n` +
      `*${labelDestination}:* ${formData.destination}\n` +
      `*${labelDate}:* ${formData.date}\n` +
      `*${labelTime}:* ${formData.time}\n` +
      `*${labelPeople}:* ${formData.people}\n` +
      `*${labelNote}:* ${formData.note || '—'}`;

    const whatsappNumber = '18094654750';
    const url = `https://api.whatsapp.com/send?phone=${whatsappNumber}&text=${encodeURIComponent(text)}`;
    window.open(url, '_blank');
  };

  return (
    <section className="transport-section">
      <div className="transport-hero">
        <div className="transport-hero-bg" />
        <div className="transport-hero-overlay" />
        <div className="container transport-hero-content">
          <span className="label transport-label">
            {getLabel('Transfers', 'Transporte', 'Transporte')}
          </span>
          <h1 className="heading-lg transport-hero-title">
            {getLabel(
              <>Book Your<br/>Private Transfer</>,
              <>Reserva tu<br/>Transporte Privado</>,
              <>Reserve seu<br/>Transporte Privado</>
            )}
          </h1>
          <p className="body-lg transport-hero-desc">
            {getLabel(
              'We pick you up and take you to your destination. Comfortable, safe, and on time.',
              'Te recogemos y llevamos a tu destino. Cómodo, seguro y puntual.',
              'Nós buscamos e levamos ao seu destino. Confortável, seguro e pontual.'
            )}
          </p>
        </div>
      </div>

      <div className="container transport-form-wrap fade-up">
        <div className="transport-card">
          <div className="transport-card-header">
            <h2>{getLabel('Transfer Details', 'Detalles del Traslado', 'Detalhes do Traslado')}</h2>
            <p>{getLabel('Fill in the information and we will confirm your transfer.', 'Completa la información y te confirmaremos el traslado.', 'Preencha as informações e confirmaremos o traslado.')}</p>
          </div>

          <form onSubmit={handleSubmit}>
            <div className="transport-form-row">
              <div className="tp-form-group">
                <label htmlFor="origin">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg>
                  {getLabel('Pickup / Origin', 'Origen / Pickup', 'Origem / Pickup')}
                </label>
                <input
                  type="text"
                  id="origin"
                  required
                  placeholder={getLabel(
                    'Where should we pick you up?',
                    '¿Dónde te recogemos?',
                    'Onde devemos buscá-lo?'
                  )}
                  value={formData.origin}
                  onChange={handleChange}
                />
              </div>

              <div className="tp-form-group">
                <label htmlFor="destination">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                  {getLabel('Destination', 'Destino', 'Destino')}
                </label>
                <input
                  type="text"
                  id="destination"
                  required
                  placeholder={getLabel(
                    'Where are you going?',
                    '¿A dónde vas?',
                    'Para onde você vai?'
                  )}
                  value={formData.destination}
                  onChange={handleChange}
                />
              </div>
            </div>

            <div className="transport-form-row transport-form-row-3">
              <div className="tp-form-group">
                <label htmlFor="date">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                  {getLabel('Transfer date', 'Fecha del traslado', 'Data do traslado')}
                </label>
                <input
                  type="date"
                  id="date"
                  required
                  value={formData.date}
                  onChange={handleChange}
                  min={getToday()}
                />
              </div>

              <div className="tp-form-group">
                <label htmlFor="time">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
                  {getLabel('Pickup time', 'Hora de recogida', 'Horário de coleta')}
                </label>
                <input
                  type="time"
                  id="time"
                  required
                  value={formData.time}
                  onChange={handleChange}
                />
              </div>

              <div className="tp-form-group">
                <label htmlFor="people">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                  {getLabel('People', 'Personas', 'Pessoas')}
                </label>
                <input
                  type="number"
                  id="people"
                  min="1"
                  required
                  value={formData.people}
                  onChange={handleChange}
                />
              </div>
            </div>

            <div className="tp-form-group">
              <label htmlFor="note">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
                {getLabel('Note', 'Nota', 'Observação')}
              </label>
              <textarea
                id="note"
                rows="3"
                placeholder={getLabel(
                  'Any additional details... (optional)',
                  'Detalles adicionales... (opcional)',
                  'Detalhes adicionais... (opcional)'
                )}
                value={formData.note}
                onChange={handleChange}
              />
            </div>

            <button type="submit" className="tp-btn-submit">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
              {getLabel(
                'Book via WhatsApp',
                'Reservar por WhatsApp',
                'Reservar via WhatsApp'
              )}
            </button>
          </form>
        </div>
      </div>
    </section>
  );
};

export default Transport;
