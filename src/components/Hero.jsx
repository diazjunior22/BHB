import React, { useRef } from 'react';
import { motion, useScroll, useTransform, useSpring, useMotionValue, useInView, useReducedMotion } from 'framer-motion';
import { useTranslation } from '../I18nContext';

const AnimatedCounter = ({ target, suffix = '' }) => {
  const ref = useRef(null);
  const isInView = useInView(ref, { once: true, margin: '-50px' });
  const [displayValue, setDisplayValue] = React.useState(0);

  React.useEffect(() => {
    if (!isInView) return;
    const num = parseFloat(target);
    if (isNaN(num)) return;

    const duration = 1800;
    const startTime = performance.now();
    const animate = (currentTime) => {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = Math.round(eased * num * 10) / 10;
      setDisplayValue(Number.isInteger(num) ? Math.round(eased * num) : current);
      if (progress < 1) requestAnimationFrame(animate);
    };
    requestAnimationFrame(animate);
  }, [isInView, target]);

  return <span ref={ref}>{displayValue}{suffix}</span>;
};

const Hero = () => {
  const { t } = useTranslation();
  const heroRef = useRef(null);
  const prefersReduced = useReducedMotion();

  const mouseX = useMotionValue(0);
  const mouseY = useMotionValue(0);

  const springConfig = { damping: 25, stiffness: 120, mass: 0.8 };
  const bgX = useSpring(mouseX, springConfig);
  const bgY = useSpring(mouseY, springConfig);
  const contentRotateX = useSpring(mouseY, { damping: 30, stiffness: 80 });
  const contentRotateY = useSpring(mouseX, { damping: 30, stiffness: 80 });

  const { scrollY } = useScroll();
  const bgScale = useTransform(scrollY, [0, 600], [1.08, 1.0]);
  const bgOpacity = useTransform(scrollY, [0, 500], [1, 0.6]);
  const contentY = useTransform(scrollY, [0, 400], [0, -60]);

  const handleMouseMove = (e) => {
    if (prefersReduced) return;
    const rect = heroRef.current?.getBoundingClientRect();
    if (!rect) return;
    const x = ((e.clientX - rect.left) / rect.width - 0.5) * 2;
    const y = ((e.clientY - rect.top) / rect.height - 0.5) * 2;
    mouseX.set(x * 12);
    mouseY.set(y * 8);
  };

  const handleMouseLeave = () => {
    mouseX.set(0);
    mouseY.set(0);
  };

  const containerVariants = {
    hidden: {},
    visible: {
      transition: { staggerChildren: 0.12, delayChildren: 0.3 }
    }
  };

  const itemVariants = {
    hidden: { opacity: 0, y: 30 },
    visible: {
      opacity: 1, y: 0,
      transition: { type: 'spring', damping: 20, stiffness: 100 }
    }
  };

  const tagVariants = {
    hidden: { opacity: 0, y: 16, scale: 0.95 },
    visible: {
      opacity: 1, y: 0, scale: 1,
      transition: { type: 'spring', damping: 22, stiffness: 120 }
    }
  };

  const stats = [
    { value: '5', suffix: 'k+', label: t('stats.travelers') },
    { value: '12', suffix: '+', label: t('stats.tours') },
    { value: '8', suffix: '+', label: t('stats.experience') },
    { value: '4.9', suffix: '', label: t('stats.satisfaction') },
  ];

  return (
    <motion.section
      className="hero"
      id="hero"
      ref={heroRef}
      onMouseMove={handleMouseMove}
      onMouseLeave={handleMouseLeave}
    >
      <motion.div
        className="hero-bg"
        style={{
          x: prefersReduced ? 0 : bgX,
          y: prefersReduced ? 0 : bgY,
          scale: prefersReduced ? 1 : bgScale,
          opacity: prefersReduced ? 1 : bgOpacity,
        }}
      />
      <div className="hero-noise" />
      <div className="hero-overlay" />
      <div className="hero-glow" />
      <div className="hero-glow-yellow" />
      <div className="hero-line hero-line-top" />
      <div className="hero-line hero-line-bottom" />

      <div className="hero-particles">
        {[...Array(6)].map((_, i) => (
          <div key={i} className={`hero-particle hero-particle-${i + 1}`} />
        ))}
      </div>

      <div className="container">
        <motion.div
          className="hero-content"
          style={{
            rotateX: prefersReduced ? 0 : contentRotateX,
            rotateY: prefersReduced ? 0 : contentRotateY,
            y: prefersReduced ? 0 : contentY,
          }}
          variants={containerVariants}
          initial="hidden"
          animate="visible"
        >
          <motion.div className="hero-tag" variants={tagVariants}>
            <span className="dot" />
            <span>{t('hero.tag')}</span>
          </motion.div>

          <motion.h1
            className="hero-title"
            variants={itemVariants}
            dangerouslySetInnerHTML={{ __html: t('hero.title') }}
          />

          <motion.div className="hero-sub" variants={itemVariants}>
            {t('hero.sub')}
          </motion.div>

          <motion.p className="hero-desc" variants={itemVariants}>
            {t('hero.desc')}
          </motion.p>

          <motion.div className="hero-actions" variants={itemVariants}>
            <a href="#tours" className="btn btn-primary">
              {t('hero.btnTours')}
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                <line x1="5" y1="12" x2="19" y2="12" />
                <polyline points="12 5 19 12 12 19" />
              </svg>
            </a>
            <a href="#contact" className="btn btn-outline">
              {t('hero.btnContact')}
            </a>
          </motion.div>

          <motion.div className="hero-stats" variants={itemVariants}>
            {stats.map((stat, i) => (
              <div className="hero-stat" key={i}>
                <div className="hero-stat-value">
                  <AnimatedCounter target={stat.value} suffix={stat.suffix} />
                </div>
                <div className="hero-stat-label">{stat.label}</div>
              </div>
            ))}
          </motion.div>
        </motion.div>
      </div>

      <motion.div
        className="hero-scroll-indicator"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1.4, duration: 0.8 }}
      >
        <div className="mouse" />
      </motion.div>
    </motion.section>
  );
};

export default Hero;
