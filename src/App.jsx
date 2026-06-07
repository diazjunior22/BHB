import React, { useEffect } from 'react';
import './TourCard.css';
import './TourDetail.css';
import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom';
import { I18nProvider } from './I18nContext';
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './pages/Home';
import TourDetail from './pages/TourDetail';

// ScrollToTop on route change
const ScrollToTop = () => {
  const { pathname, hash } = useLocation();
  useEffect(() => {
    if (!hash) {
      window.scrollTo(0, 0);
    }
  }, [pathname, hash]);
  return null;
};

// Intersection Observer for scroll animations
const ScrollObserver = () => {
  const { pathname } = useLocation();
  
  useEffect(() => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
    
    setTimeout(() => {
      document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));
    }, 100);
    
    return () => observer.disconnect();
  }, [pathname]);

  return null;
};

function App() {
  return (
    <BrowserRouter>
      <I18nProvider>
        <ScrollToTop />
        <ScrollObserver />
        <Header />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/tours/:id" element={<TourDetail />} />
          </Routes>
        </main>
        <Footer />
      </I18nProvider>
    </BrowserRouter>
  );
}

export default App;
