import React from 'react';
import { useTranslation } from '../I18nContext';


const Testimonials = () => {
  const { t } = useTranslation();
  return (
    <>
<section className="section testimonials" id="testimonials">
    <div className="testimonials-decor testimonials-decor--car">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1" strokeLinecap="round"
        strokeLinejoin="round">
        <path d="M5 17a2 2 0 0 1-2-2V9l3-5h12l3 5v6a2 2 0 0 1-2 2" />
        <circle cx="7" cy="17" r="2" />
        <circle cx="17" cy="17" r="2" />
        <path d="M5 9h14" />
      </svg>
    </div>
    <div className="testimonials-decor testimonials-decor--map">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1" strokeLinecap="round"
        strokeLinejoin="round">
        <path d="M9 20 3 17V5l6 3Z" />
        <path d="M15 20 9 17V5l6 3Z" />
        <path d="M21 20 15 17V5l6 3Z" />
        <path d="M9 17V5" />
        <path d="M15 17V5" />
      </svg>
    </div>
    <div className="container">
      <div className="testimonials-header fade-up">
        <span className="section-label">{t("testimonials.label")}</span>
        <h2 className="heading-lg" dangerouslySetInnerHTML={{ __html: t("testimonials.title") }}></h2>
      </div>
      <div className="testimonials-grid">

        {/*  1 ─ Sarah  */}
        <div className="testimonial-card fade-up">
          <div className="testimonial-card-header">
            <div className="testimonial-avatar testimonial-avatar--cyan">SM</div>
            <div className="testimonial-meta">
              <h4>{t("testimonial.s1.name")}</h4>
              <div className="loc">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"
                  strokeLinejoin="round">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" />
                  <circle cx="12" cy="10" r="3" />
                </svg>
                <span>{t("testimonial.s1.loc")}</span>
              </div>
            </div>
            <div className="testimonial-date">{t("testimonial.s1.date")}</div>
          </div>
          <div className="testimonial-stars">
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
          </div>
          <p className="testimonial-text" data-i18n="testimonial.s1.text">The Saona Island tour was absolutely breathtaking!
            Crystal clear waters, amazing crew, and the buffet lunch was delicious. Highly recommend!</p>
          <div className="testimonial-image">
            <svg viewBox="0 0 320 180" preserveAspectRatio="xMidYMid meet">
              <img src="img/2.jpg" alt="" />
            </svg>
          </div>
        </div>

        {/*  2 ─ Manoj (with poster)  */}
        <div className="testimonial-card fade-up fade-up-d1">
          <div className="testimonial-card-header">
            <div className="testimonial-avatar testimonial-avatar--yellow">MT</div>
            <div className="testimonial-meta">
              <h4>{t("testimonial.s2.name")}</h4>
              <div className="loc">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"
                  strokeLinejoin="round">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" />
                  <circle cx="12" cy="10" r="3" />
                </svg>
                <span>{t("testimonial.s2.loc")}</span>
              </div>
            </div>
            <div className="testimonial-date">{t("testimonial.s2.date")}</div>
          </div>
          <div className="testimonial-stars">
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
          </div>
          <p className="testimonial-text" data-i18n="testimonial.s2.text">Unforgettable ATV adventure! The cenote was
            stunning and the cultural stop with mamajuana tasting made it truly unique. A must-do!</p>
          <div className="testimonial-image testimonial-image--tight">
            <svg viewBox="0 0 320 180" preserveAspectRatio="xMidYMid meet">
              <img src="img/1.jpg" alt="" />
            </svg>
          </div>
        </div>

        {/*  3 ─ Carolina  */}
        <div className="testimonial-card fade-up fade-up-d2">
          <div className="testimonial-card-header">
            <div className="testimonial-avatar testimonial-avatar--coral">CR</div>
            <div className="testimonial-meta">
              <h4>{t("testimonial.s3.name")}</h4>
              <div className="loc">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"
                  strokeLinejoin="round">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" />
                  <circle cx="12" cy="10" r="3" />
                </svg>
                <span>{t("testimonial.s3.loc")}</span>
              </div>
            </div>
            <div className="testimonial-date">{t("testimonial.s3.date")}</div>
          </div>
          <div className="testimonial-stars">
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
          </div>
          <p className="testimonial-text" data-i18n="testimonial.s3.text">El Party Boat superó todas mis expectativas. El
            DJ, la barra libre y el snorkel hicieron de este día algo mágico. ¡Volveré sin dudas!</p>
        </div>

        {/*  4 ─ James  */}
        <div className="testimonial-card fade-up fade-up-d1">
          <div className="testimonial-card-header">
            <div className="testimonial-avatar testimonial-avatar--navy">JW</div>
            <div className="testimonial-meta">
              <h4>{t("testimonial.s4.name")}</h4>
              <div className="loc">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"
                  strokeLinejoin="round">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" />
                  <circle cx="12" cy="10" r="3" />
                </svg>
                <span>{t("testimonial.s4.loc")}</span>
              </div>
            </div>
            <div className="testimonial-date">{t("testimonial.s4.date")}</div>
          </div>
          <div className="testimonial-stars">
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
          </div>
          <p className="testimonial-text" data-i18n="testimonial.s4.text">Professional from start to finish. They picked us
            up right on time, the guides were knowledgeable, and Saona Island is paradise on earth.</p>
        </div>

        {/*  5 ─ Léa  */}
        <div className="testimonial-card fade-up fade-up-d2">
          <div className="testimonial-card-header">
            <div className="testimonial-avatar testimonial-avatar--green">LD</div>
            <div className="testimonial-meta">
              <h4>{t("testimonial.s5.name")}</h4>
              <div className="loc">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"
                  strokeLinejoin="round">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" />
                  <circle cx="12" cy="10" r="3" />
                </svg>
                <span>{t("testimonial.s5.loc")}</span>
              </div>
            </div>
            <div className="testimonial-date">{t("testimonial.s5.date")}</div>
          </div>
          <div className="testimonial-stars">
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
          </div>
          <p className="testimonial-text" data-i18n="testimonial.s5.text">The ATV tour was the highlight of our trip!
            Driving through the Dominican countryside and ending at Macao Beach was absolutely perfect.</p>
        </div>

        {/*  6 ─ Michael & Priya  */}
        <div className="testimonial-card fade-up fade-up-d3">
          <div className="testimonial-card-header">
            <div className="testimonial-avatar testimonial-avatar--purple">M+P</div>
            <div className="testimonial-meta">
              <h4>{t("testimonial.s6.name")}</h4>
              <div className="loc">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"
                  strokeLinejoin="round">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" />
                  <circle cx="12" cy="10" r="3" />
                </svg>
                <span>{t("testimonial.s6.loc")}</span>
              </div>
            </div>
            <div className="testimonial-date">{t("testimonial.s6.date")}</div>
          </div>
          <div className="testimonial-stars">
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
            <svg viewBox="0 0 20 20">
              <path d="M10 1l2.39 4.84L17.8 6.5l-3.9 3.8.92 5.36L10 13.1l-4.82 2.56.92-5.36L2.2 6.5l5.41-.66Z" />
            </svg>
          </div>
          <p className="testimonial-text" data-i18n="testimonial.s6.text">Booked three tours with BHB and each one was
            better than the last. Exceptional service, great food, and memories we will cherish forever.</p>
        </div>

      </div>
    </div>
  </section>
    </>
  );
};

export default Testimonials;
