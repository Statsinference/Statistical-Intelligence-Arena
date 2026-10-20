# Leaderboard Demo — real website via GitHub Pages

Our demo requires no Vercel or backend: it is a standalone HTML/CSS/JavaScript page.

**Actual website address (after publishing):** https://statsarena.github.io/

## Publish the demo

1. From the `StatsArena` organization, create a **Public** repository named exactly **`statsarena.github.io`**. This is separate from the **Private** `statistical-inference-arena` benchmark repository.
2. In the **public website repo only**, upload:
   - `index.html` (the supplied leaderboard demo as a webpage)
   - `statsarena-logo.jpg`
   - `.nojekyll` (optional)
   - `README.md` (website repository guidance)
   Put them in the root of the website repo; do **not** upload the ZIP as a single file.
3. In `StatsArena/statsarena.github.io`, go to **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: main → /(root) → Save**.
4. Wait for Pages to deploy and use **Visit site**. Verify that `https://statsarena.github.io/` shows the **rendered interactive page**, not GitHub source.
5. The main benchmark README button is **already linked** to that public URL; it will start working without further README edits after publishing.

**Privacy:** Keep the primary Benchmark repo private. Only the illustrative standalone mock website is public. GitHub Pages makes the demo available to everyone without login. If private access to the *demo itself* is required instead, GitHub Pages on Free does not provide that and you need an authenticated preview host.

**Important:** All leaderboard rankings, costs, coverage values, histories, methods support indications and DGP counts are **simulated demonstration data**, not actual benchmark measurements. The demo tabs are illustrative and do not replace the six official causal-inference categories.

## Local preview

Open `index.html` in a browser, or from the website files directory run `python3 -m http.server 8000` and open `http://127.0.0.1:8000/`. A local preview is not a public link.
