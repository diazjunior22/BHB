import React from 'react';
import Hero from '../components/Hero';
import ToursGrid from '../components/ToursGrid';
import About from '../components/About';
import Testimonials from '../components/Testimonials';
import Contact from '../components/Contact';

const Home = () => {
  return (
    <>
      <Hero />
      <ToursGrid />
      <About />
      <Testimonials />
      <Contact />
    </>
  );
};

export default Home;
