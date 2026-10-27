# breasthealth.co.in — test site (final website, Phase 4)

A static build of every page: the 39 Draft 1 pages plus the new Breast Cancer page (`/breast-cancer.php`), 40 in all, each one responsive (phone, tablet and desktop from the same file).

Phase 1 applies Dr. Kirti's feedback: the Breast Cancer page and menu item, IASO and FEBS on the About and Home pages, the new homepage photo, the five consulting hospitals with their new days and phone numbers, and "needle" in place of "fine needle" everywhere.

Phase 4 adds the SEO layer: a unique title and meta description on every page, canonical links on the www address, Open Graph and Twitter share tags (with a 1200 × 630 photo), the Google Search Console verification tag on the home page, schema (doctor, hospitals, medical pages, articles, FAQs, breadcrumbs) and `sitemap.xml`. FAQ answers are now in the page for search engines, while still opening and closing as before.

## Deploy on Vercel

1. Push this folder to a new Git repository (this folder is the repository root).
2. In Vercel: **Add New → Project → Import** the repository.
3. Framework Preset: **Other**. Leave Build Command and Output Directory empty. Deploy.

That's it. There is nothing to install or build.

## How the URLs work

Every link uses the live site's real addresses (`/about.php`, `/mammogram.php`, `/blog/…php`), so SEO-carrying URLs stay exactly as they are today.
The files are saved as `.html`, and `vercel.json` serves each `.php` address from its `.html` file.

## Preview locally

Open a terminal in this folder, run `python3 serve.py`, then open http://localhost:8000 in your browser (Ctrl+C stops it). Or use `npx vercel dev`.
(Opening the files by double-clicking will not work, because links start with `/`.)

## Test-site safeguards

- Every page has `<meta name="robots" content="noindex, nofollow">` (the launch build, made with `LIVE=1`, switches this to index), `vercel.json` sends `X-Robots-Tag: noindex`, and `robots.txt` blocks all crawlers. Remove these three only on the final live site.
- Booking forms do not send anywhere yet (email is connected after review). Submitting shows a confirmation on the page.

## Folder layout

- `index.html` — home (`/`)
- `*.html` — one file per page, named after its live `.php` address
- `blog/` — Breast Health Library (`/blog/`) and the 4 articles
- `assets/img/` — logos and Dr. Kirti's photos
- `assets/js/dc-site.js` — shared script that runs menus, accordions, the video carousel and player, forms and scroll effects

## Moving to cPanel later

Rename each `.html` file to `.php` (same name), drop `vercel.json`, and remove the three noindex safeguards above.
