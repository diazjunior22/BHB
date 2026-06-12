import React from 'react';
import './BavaroActivities.css';
import { Clock, CheckCircle2, AlertTriangle, Moon, Anchor, ShieldCheck } from 'lucide-react';

const activities = [
  {
    title: 'Polaris VIP',
    price: 149,
    duration: '4.5 horas',
    details: [
      'Vehículos de hasta 4 personas',
      'Recorrido off-road en mina abandonada y selva'
    ]
  },
  {
    title: 'Buggy VIP',
    price: 99,
    duration: '4.5 horas',
    details: [
      'Vehículos de hasta 4 personas',
      'Ruta privada entre bosque y pista en mina abandonada'
    ]
  },
  {
    title: 'Zipline Mega Splash',
    price: 99,
    duration: '4.5 horas',
    details: [
      'Circuito de 6 líneas de tirolesa',
      'Puente colgante del Himalaya',
      'Acuatizaje (landing en el agua)'
    ]
  },
  {
    title: 'Splash of Emotions',
    subtitle: '(Sacred River & Jungle River)',
    price: 99,
    duration: '4.5 horas',
    details: [
      'Navegación en balsas por río sagrado',
      'Cascadas ocultas',
      'Cavernas y selva tropical'
    ]
  },
  {
    title: 'Horseback Riding VIP',
    price: 99,
    duration: '4.5 horas',
    details: [
      'Recorrido por senderos rodeados de naturaleza',
      'Diseñado para toda la familia'
    ]
  },
  {
    title: 'Magic Mystic Memories',
    subtitle: '(Polaris de Noche)',
    price: 149,
    duration: '3.5 horas',
    badge: 'Nocturno',
    badgeIcon: <Moon size={14} />,
    details: [
      'Martes, Jueves y Sábados (6:30 PM a 10:00 PM)',
      'Incluye cena Surf & Turf',
      'Barra libre y selección de vinos',
      'Experiencia sensorial nocturna',
      'No incluye almuerzo típico'
    ]
  },
  {
    title: 'Private Catamaran',
    price: 89,
    duration: '3 horas',
    badge: 'Mar',
    badgeIcon: <Anchor size={14} />,
    details: [
      'Mínimo 15, máximo 70 personas',
      'Incluye barra libre nacional',
      'Nachos con dips y snorkeling',
      'Visita a playa semi-virgen',
      'No incluye almuerzo ni atracciones en tierra'
    ]
  },
  {
    title: 'Explorer VIP',
    subtitle: 'Premium Private Catamaran',
    price: 129,
    duration: '4 horas',
    badge: 'Premium',
    badgeIcon: <Anchor size={14} />,
    details: [
      'Mínimo 15, máximo 70 personas',
      'Foto de bienvenida y vino espumoso',
      'Barra libre premium y aperitivos premium',
      'Snorkeling incluido'
    ]
  }
];

const standardIncludes = [
  'Transporte de ida y vuelta al hotel',
  'Charla de seguridad y equipo',
  'Cenote Blue Lagoon',
  'Piscina con cascada (Waterfall Pool)',
  'Jardín Laberinto (Maze Garden)',
  'Pueblo Dominicano (Dominican Village)',
  'Almuerzo típico dominicano (Bebidas no incluidas)'
];

const standardExcludes = [
  'Fotos',
  'Propinas',
  'Souvenirs',
  'Casilleros (lockers)',
  'Consumos adicionales'
];

const restrictions = [
  'Conductores (Polaris/Buggy): Mayores de 18 años con licencia válida.',
  'Altura mínima: 1.30m (4.26ft) para las actividades.',
  'Peso máximo: 130kg (285lb) para Zipline y Paseo a Caballo.',
  'Seguridad: Prohibido celulares/cámaras, sombreros, chanclas o bolsos durante las actividades.'
];

const BavaroActivities = () => {
  const handleBook = (title) => {
    const msg = `Hola, me interesa reservar la actividad: *${title}* en Bávaro Adventure Park.`;
    window.open(`https://wa.me/18094654750?text=${encodeURIComponent(msg)}`, '_blank');
  };

  return (
    <div className="bavaro-section">
      <div className="bavaro-header-info">
        <h2>Paquetes y Actividades</h2>
        <p>Elige tu aventura en Bávaro Adventure Park. Conoce nuestras opciones llenas de adrenalina y diversión.</p>
      </div>

      <div className="bavaro-grid">
        {activities.map((act, i) => (
          <div key={i} className={`bavaro-card ${act.badge ? 'bavaro-card-featured' : ''}`}>
            {act.badge && (
              <div className={`bavaro-badge ${act.badge === 'Nocturno' ? 'badge-night' : 'badge-sea'}`}>
                {act.badgeIcon} {act.badge}
              </div>
            )}
            <div className="bavaro-card-header">
              <h3 className="bavaro-card-title">{act.title}</h3>
              {act.subtitle && <span className="bavaro-card-subtitle">{act.subtitle}</span>}
            </div>
            
            <div className="bavaro-card-price-row">
              <div className="bavaro-price">
                <span className="bavaro-price-label">Desde</span>
                <span className="bavaro-price-value">US${act.price}</span>
              </div>
              <div className="bavaro-duration">
                <Clock size={16} />
                <span>{act.duration}</span>
              </div>
            </div>

            <ul className="bavaro-card-details">
              {act.details.map((det, j) => (
                <li key={j}>
                  <CheckCircle2 size={16} className="text-green-500" />
                  <span>{det}</span>
                </li>
              ))}
            </ul>

            <button onClick={() => handleBook(act.title)} className="bavaro-btn-book">
              Reservar Paquete
            </button>
          </div>
        ))}
      </div>

      <div className="bavaro-info-grid">
        <div className="bavaro-info-card">
          <div className="bavaro-info-header">
            <CheckCircle2 className="icon-green" size={24} />
            <h3>Todos los paquetes estándar incluyen:</h3>
          </div>
          <ul className="bavaro-list-check">
            {standardIncludes.map((inc, i) => <li key={i}>{inc}</li>)}
          </ul>
        </div>

        <div className="bavaro-info-card">
          <div className="bavaro-info-header">
            <AlertTriangle className="icon-red" size={24} />
            <h3>Lo que NO incluyen:</h3>
          </div>
          <ul className="bavaro-list-cross">
            {standardExcludes.map((exc, i) => <li key={i}>{exc}</li>)}
          </ul>
        </div>
      </div>

      <div className="bavaro-restrictions">
        <div className="bavaro-info-header">
          <ShieldCheck className="icon-yellow" size={24} />
          <h3>Restricciones Importantes</h3>
        </div>
        <ul>
          {restrictions.map((rest, i) => <li key={i}>{rest}</li>)}
        </ul>
      </div>
    </div>
  );
};

export default BavaroActivities;
