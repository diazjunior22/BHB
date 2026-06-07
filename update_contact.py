import os

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
    <section className="section contact-premium" id="contact">
      <div className="container">
        <div className="contact-premium-card fade-up">
          <div className="contact-premium-left">
            <h2 className="contact-premium-title">{lang === 'en' ? "Let's talk about your next trip" : lang === 'pt' ? "Vamos falar sobre a sua próxima viagem" : "Hablemos de tu próximo viaje"}</h2>
            <p className="contact-premium-desc">
              {lang === 'en' ? "We are here to help you plan the perfect experience in Punta Cana. Leave us your message and we will respond quickly." : lang === 'pt' ? "Estamos aqui para ajudar você a planejar a experiência perfeita em Punta Cana. Deixe sua mensagem e responderemos rapidamente." : "Estamos aquí para ayudarte a planear la experiencia perfecta en Punta Cana. Déjanos tu mensaje y responderemos rápidamente."}
            </p>
            
            <div className="contact-premium-methods">
              <div className="contact-premium-method">
                <div className="cp-icon">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                </div>
                <div className="cp-text">+1 (809) 465-4750</div>
              </div>
              <div className="contact-premium-method">
                <div className="cp-icon">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                </div>
                <div className="cp-text">bhbtravelandtour@gmail.com</div>
              </div>
            </div>

            <div className="contact-premium-social">
              <a href="#" aria-label="Instagram">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
              </a>
              <a href="#" aria-label="Facebook">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
              </a>
            </div>
          </div>
          
          <div className="contact-premium-right">
            <h3 className="contact-premium-form-title">{lang === 'en' ? 'Send Message' : lang === 'pt' ? 'Enviar mensagem' : 'Enviar mensaje'}</h3>
            <form id="contactFormPremium" onSubmit={handleSubmit}>
              <div className="cp-form-group">
                <label htmlFor="name">{lang === 'en' ? 'Full name' : lang === 'pt' ? 'Nome completo' : 'Nombre completo'}</label>
                <input type="text" id="name" required value={formData.name} onChange={handleChange} />
              </div>
              
              <div className="cp-form-group">
                <label htmlFor="email">{lang === 'en' ? 'Email address' : lang === 'pt' ? 'Correio eletrônico' : 'Correo electrónico'}</label>
                <input type="email" id="email" required value={formData.email} onChange={handleChange} />
              </div>
              
              <div className="cp-form-row">
                <div className="cp-form-group" style={{ flex: 2 }}>
                  <label htmlFor="tourSelect">{t('form.tour')}</label>
                  <div className="cp-select-wrapper">
                    <select id="tourSelect" value={formData.tourSelect} onChange={handleChange}>
                      <option value="">{t('form.tourPlaceholder')}</option>
                      <option value="saona">{t('tour.saona.name')}</option>
                      <option value="party">{t('tour.party.name')}</option>
                      <option value="atv">{t('tour.atv.name')}</option>
                      <option value="santodomingo">{t('tour.santodomingo.name')}</option>
                    </select>
                    <svg className="cp-select-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                  </div>
                </div>
                
                <div className="cp-form-group" style={{ flex: 1 }}>
                  <label htmlFor="people">{t('form.people')}</label>
                  <input type="number" id="people" min="1" value={formData.people} onChange={handleChange} />
                </div>
              </div>
              
              <div className="cp-form-group">
                <label htmlFor="message">{t('form.message')}</label>
                <textarea id="message" rows="4" required value={formData.message} onChange={handleChange}></textarea>
              </div>
              
              <button type="submit" className="cp-btn-submit">
                {lang === 'en' ? 'Send Message' : lang === 'pt' ? 'Enviar mensagem' : 'Enviar mensaje'}
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
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

with open('src/components/Contact.jsx', 'w', encoding='utf-8') as f:
    f.write(contact_code)

css_append = """
/* --- Premium Contact Section --- */
.contact-premium {
  padding: 100px 0;
  background-color: #F8FAFC; /* Pearl gray / Light blue subtle */
  position: relative;
}

.contact-premium-card {
  background: var(--white);
  border-radius: 24px;
  box-shadow: 0 20px 50px rgba(0, 18, 96, 0.08);
  display: grid;
  grid-template-columns: 1fr 1.3fr;
  overflow: hidden;
  max-width: 1050px;
  margin: 0 auto;
}

/* Left Column */
.contact-premium-left {
  background: linear-gradient(135deg, var(--navy-dark) 0%, var(--navy) 100%);
  color: var(--white);
  padding: 60px 50px;
  display: flex;
  flex-direction: column;
  position: relative;
}

.contact-premium-title {
  font-family: 'Bodoni Moda', serif;
  font-size: 36px;
  font-weight: 700;
  line-height: 1.1;
  margin-bottom: 20px;
  color: var(--white);
}

.contact-premium-desc {
  font-size: 16px;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.85);
  margin-bottom: 50px;
}

.contact-premium-methods {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.contact-premium-method {
  display: flex;
  align-items: center;
  gap: 16px;
}

.cp-icon {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--yellow);
  flex-shrink: 0;
}

.cp-text {
  font-size: 17px;
  font-weight: 500;
  color: var(--white);
}

.contact-premium-social {
  margin-top: auto;
  padding-top: 60px;
  display: flex;
  gap: 16px;
}

.contact-premium-social a {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
  transition: all 0.3s ease;
}

.contact-premium-social a:hover {
  background: var(--yellow);
  color: var(--navy-dark);
  transform: translateY(-3px);
}

/* Right Column */
.contact-premium-right {
  padding: 60px 50px;
  background: var(--white);
}

.contact-premium-form-title {
  font-size: 28px;
  font-weight: 700;
  color: var(--navy-dark);
  margin-bottom: 30px;
}

.cp-form-group {
  margin-bottom: 24px;
}

.cp-form-row {
  display: flex;
  gap: 20px;
}

.cp-form-group label {
  display: block;
  font-size: 14px;
  font-weight: 600;
  color: var(--gray-700);
  margin-bottom: 8px;
}

.cp-form-group input,
.cp-form-group select,
.cp-form-group textarea {
  width: 100%;
  padding: 14px 16px;
  background: var(--gray-50);
  border: 1px solid var(--gray-100);
  border-radius: 12px;
  font-family: inherit;
  font-size: 16px;
  color: var(--gray-900);
  transition: all 0.3s ease;
}

.cp-select-wrapper {
  position: relative;
}
.cp-select-wrapper select {
  appearance: none;
  cursor: pointer;
  padding-right: 40px;
}
.cp-select-icon {
  position: absolute;
  right: 16px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--gray-500);
  pointer-events: none;
}

.cp-form-group input:focus,
.cp-form-group select:focus,
.cp-form-group textarea:focus {
  outline: none;
  border-color: var(--navy);
  background: var(--white);
  box-shadow: 0 0 0 4px rgba(0, 34, 158, 0.08);
}

.cp-form-group textarea {
  resize: vertical;
  min-height: 120px;
}

.cp-btn-submit {
  width: 100%;
  padding: 16px;
  background-color: var(--yellow);
  color: var(--navy-dark);
  font-size: 16px;
  font-weight: 600;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  transition: all 0.3s ease;
  margin-top: 10px;
}

.cp-btn-submit:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(233, 200, 33, 0.3);
}

/* Responsive */
@media (max-width: 991px) {
  .contact-premium-card {
    grid-template-columns: 1fr;
  }
  .contact-premium-left {
    padding: 40px 30px;
  }
  .contact-premium-right {
    padding: 40px 30px;
  }
  .contact-premium-social {
    padding-top: 40px;
  }
}

@media (max-width: 576px) {
  .cp-form-row {
    flex-direction: column;
    gap: 0;
  }
  .contact-premium-left,
  .contact-premium-right {
    padding: 30px 20px;
  }
}
"""

with open('src/index.css', 'a', encoding='utf-8') as f:
    f.write(css_append)

print("Contact updated")
