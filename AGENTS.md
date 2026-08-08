# AGENTS.md — BHB Travel & Tour

## What this is

React 19 + Vite 8 SPA for a Punta Cana tour operator. Deployed on Vercel. No TypeScript, no backend, no test suite.

## Commands

- `npm run dev` — local dev server
- `npm run build` — production build to `dist/`
- `npm run lint` — ESLint (only verification step available)
- No typecheck, no test runner

## Architecture

- **Entry**: `src/main.jsx` → `src/App.jsx` (BrowserRouter + Routes)
- **Routes**: `/` (Home), `/tours/:id` (TourDetail), `/transporte` (Transport)
- **Pages**: `src/pages/` — Home, TourDetail, Transport
- **Components**: `src/components/` — Header, Footer, Hero, About, Contact, TourCard, ToursGrid, Testimonials, BavaroActivities
- **CSS**: Separate files per concern (`TourCard.css`, `TourDetail.css`, `Transport.css`, `BavaroActivities.css`) — not CSS modules
- **Deploy**: Vercel SPA rewrite in `vercel.json`

## i18n — READ THIS FIRST

Custom context-based i18n (no library). Three languages: `es` (default), `en`, `pt`.

- Locale files: `src/locales/{es,en,pt}.json`
- Context: `src/I18nContext.jsx` — provides `useTranslation()` hook returning `{ lang, setLang, t }`
- **When adding or changing any user-visible text, you MUST update all three locale JSON files with matching keys.**
- Keys follow dot notation: `tour.saona.name`, `contact.title`, etc.
- Some translation values contain raw HTML (`<br>`, `<strong>`, `<span>`). Render with `dangerouslySetInnerHTML` or equivalent — the `t()` function returns raw strings.
- `src/legacy.js` is dead code from the old vanilla-JS implementation. Ignore it.

## Key libraries

- `react-router-dom` v7 — routing
- `framer-motion` v12 — animations
- `lucide-react` — icons
- No UI framework (raw CSS)

## Conventions

- JavaScript only (`.jsx`, `.js`). No TypeScript.
- Components are function components with hooks.
- Scroll animations use IntersectionObserver adding `.visible` class to `.fade-up` elements.
- Tour data is defined inline in components and locale files — no external API or database.
- Contact form submits via WhatsApp deep link (not a backend).
- Images live in `public/img/`.
