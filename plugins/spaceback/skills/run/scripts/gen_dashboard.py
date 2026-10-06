#!/usr/bin/env python3
# SpaceBack — a JDAC product. Copyright (c) 2026 JDAC, LLC. All rights reserved.
# Personal use only, on the recipient's own folders/projects — not on others' projects
# or for service delivery without written authorization from JDAC, LLC. Do not alter,
# resell, sublicense, redistribute, or present as your own work.
# Jonathan Schafer / JDAC Consulting / JDAC.ai
"""
SpaceBack dashboard generator.

Produces the "Storage Cleanup Tracker" HTML for a cleanup run, computes the
current category breakdown by scanning the target folder, and appends the run
to a history file so the dashboard shows progress over time.

Usage:
  python3 gen_dashboard.py --root ~/Downloads \
      --before-gb 35 --after-gb 12 --dupes 79 --folders 6 \
      --label Downloads --out tracker.html --history spaceback-history.json

--reclaimed-gb is optional (defaults to before - after).
Compatible with Python 3.9+.
"""
import os, sys, json, argparse, html, datetime


def dir_size(path):
    total = 0
    for dp, dirs, files in os.walk(path):
        for f in files:
            if f == ".DS_Store":
                continue
            fp = os.path.join(dp, f)
            try:
                if not os.path.islink(fp):
                    total += os.path.getsize(fp)
            except OSError:
                pass
    return total


def human(nbytes):
    n = float(nbytes)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024 or unit == "TB":
            return ("%.0f %s" % (n, unit)) if unit in ("B", "KB") else ("%.1f %s" % (n, unit))
        n /= 1024


def categories(root):
    """Top-level folders of root with sizes, largest first (+ loose files)."""
    cats = []
    loose = 0
    try:
        entries = sorted(os.listdir(root))
    except OSError:
        return cats
    for name in entries:
        if name.startswith("."):
            continue
        p = os.path.join(root, name)
        if os.path.isdir(p) and not os.path.islink(p):
            cats.append((name, dir_size(p)))
        elif os.path.isfile(p):
            try:
                loose += os.path.getsize(p)
            except OSError:
                pass
    cats.sort(key=lambda c: c[1], reverse=True)
    if loose:
        cats.append(("(loose files)", loose))
    return cats


CSS = """
:root{--bg:#eef1f4;--surface:#fff;--surface-2:#f6f8fa;--ink:#1b2430;--muted:#5a6675;
--line:#dce2e9;--accent:#0e8f9e;--good:#2f9e63;
--sans:-apple-system,BlinkMacSystemFont,'Segoe UI',system-ui,Roboto,sans-serif;--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace;}
@media(prefers-color-scheme:dark){:root{--bg:#0e141b;--surface:#161f29;--surface-2:#1c2731;
--ink:#e7ecf1;--muted:#9aa7b4;--line:#2a3744;--accent:#3fc3d2;color-scheme:dark;}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);line-height:1.5}
.wrap{max-width:860px;margin:0 auto;padding:32px 16px}
.mono{font-family:var(--mono);font-variant-numeric:tabular-nums}
header.head{display:flex;flex-wrap:wrap;align-items:baseline;gap:8px 14px;border-bottom:2px solid var(--ink);padding-bottom:14px}
.brand{font-weight:700;font-size:1.45rem;letter-spacing:-.01em}.brand .tick{color:var(--accent)}
.head .sub{color:var(--muted);font-size:.9rem}.stamp{margin-left:auto;font-family:var(--mono);font-size:.72rem;color:var(--muted);text-align:right}
h2{font-size:.78rem;font-weight:600;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);margin:34px 0 14px}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}@media(max-width:620px){.kpis{grid-template-columns:repeat(2,1fr)}}
.kpi{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:16px}
.kpi .v{font-family:var(--mono);font-weight:600;font-size:1.7rem;letter-spacing:-.02em;line-height:1.1}
.kpi .v small{font-size:.9rem;color:var(--muted);font-weight:500}.kpi .l{font-size:.8rem;color:var(--muted);margin-top:6px}
.kpi.hero{background:var(--accent);border-color:var(--accent);color:#fff}.kpi.hero .v,.kpi.hero .l{color:#fff}
.panel{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:18px}
.ba{display:flex;align-items:center;gap:12px;margin:10px 0}.ba .tag{width:62px;flex:none;font-size:.82rem;color:var(--muted)}
.ba .track{flex:1;background:var(--surface-2);border-radius:6px;height:30px;overflow:hidden}
.ba .fill{height:100%;border-radius:6px;display:flex;align-items:center;justify-content:flex-end;padding-right:9px;color:#fff;font-family:var(--mono);font-size:.82rem;font-weight:600}
.ba.before .fill{background:linear-gradient(90deg,#8a97a6,#6d7a8a)}.ba.after .fill{background:linear-gradient(90deg,var(--accent),#0b6f7b)}
.cat{display:grid;grid-template-columns:150px 1fr 72px;align-items:center;gap:12px;padding:7px 0}
@media(max-width:520px){.cat{grid-template-columns:110px 1fr 64px}}
.cat .name{font-size:.88rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.cat .bt{background:var(--surface-2);border-radius:5px;height:14px}.cat .bf{height:100%;border-radius:5px;background:var(--accent)}
.cat .sz{font-family:var(--mono);font-size:.82rem;text-align:right;color:var(--muted)}
table{width:100%;border-collapse:collapse;font-size:.9rem}th,td{text-align:left;padding:10px 12px;border-bottom:1px solid var(--line)}
th{font-size:.72rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
td.r,th.r{text-align:right;font-family:var(--mono)}tbody tr:last-child td{border-bottom:none}
footer{margin-top:34px;border-top:1px solid var(--line);padding-top:14px;color:var(--muted);font-size:.78rem;display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap}
footer a{color:inherit;text-decoration:underline;text-decoration-color:var(--line);text-underline-offset:2px}
footer a:hover{text-decoration-color:var(--muted)}
"""


def render(label, root, before, after, reclaimed, dupes, folders, cats, history, today):
    def esc(s):
        return html.escape(str(s))

    pct_after = (after / before * 100) if before else 0
    maxcat = max([c[1] for c in cats], default=1) or 1
    cat_rows = "\n".join(
        '<div class="cat"><span class="name">%s</span><div class="bt"><div class="bf" style="width:%.1f%%"></div></div><span class="sz">%s</span></div>'
        % (esc(name), (size / maxcat * 100), human(size))
        for name, size in cats
    )
    hist_rows = "\n".join(
        "<tr><td>%s</td><td>%s</td><td class='r'>%s &rarr; %s</td><td class='r'>%s</td><td class='r'>%s</td></tr>"
        % (esc(h.get("date", "")), esc(h.get("label", "")),
           esc(h.get("before_gb", "")) + " GB", esc(h.get("after_gb", "")) + " GB",
           esc(h.get("reclaimed_gb", "")) + " GB", esc(h.get("dupes", "")))
        for h in reversed(history)
    )
    return """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SpaceBack Reclaim Report</title>
<style>%s</style></head><body><div class="wrap">
<header class="head"><span class="brand">SpaceBack · The Reclaim Report</span>
<span class="sub">%s</span><span class="stamp">LAST RUN %s<br>re-run monthly</span></header>

<h2>Most recent cleanup</h2>
<div class="kpis">
  <div class="kpi hero"><div class="v">%s<small> GB</small></div><div class="l">reclaimed (%s)</div></div>
  <div class="kpi"><div class="v">%s<small>&rarr;%s GB</small></div><div class="l">before &rarr; after</div></div>
  <div class="kpi"><div class="v">%s</div><div class="l">duplicates removed</div></div>
  <div class="kpi"><div class="v">%s</div><div class="l">folders organized</div></div>
</div>

<h2>Folder size</h2>
<div class="panel">
  <div class="ba before"><span class="tag">Before</span><div class="track"><div class="fill" style="width:100%%">%s GB</div></div></div>
  <div class="ba after"><span class="tag">After</span><div class="track"><div class="fill" style="width:%.1f%%">%s GB</div></div></div>
</div>

<h2>What's there now, by category</h2>
<div class="panel">%s</div>

<h2>Cleanup history</h2>
<div class="panel" style="overflow-x:auto"><table>
<thead><tr><th>Date</th><th>Target</th><th class="r">Before &rarr; After</th><th class="r">Reclaimed</th><th class="r">Dupes</th></tr></thead>
<tbody>%s</tbody></table></div>

<footer><a href="mailto:jonathan@jdacllc.org">Jonathan Schafer</a><span>Generated by SpaceBack, powered by <a href="https://jdac.ai">JDAC.ai</a></span></footer>
</div></body></html>""" % (
        CSS, esc(os.path.basename(root.rstrip("/")) or root), esc(today),
        esc(reclaimed), ("-%d%%" % round((reclaimed / before * 100)) if before else "0%"),
        esc(before), esc(after), esc(dupes), esc(folders),
        esc(before), pct_after, esc(after),
        cat_rows or "<div class='cat'><span class='name'>(empty)</span></div>",
        hist_rows,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--before-gb", type=float, required=True)
    ap.add_argument("--after-gb", type=float, required=True)
    ap.add_argument("--reclaimed-gb", type=float, default=None)
    ap.add_argument("--dupes", type=int, default=0)
    ap.add_argument("--folders", type=int, default=0)
    ap.add_argument("--label", default="")
    ap.add_argument("--out", required=True)
    ap.add_argument("--history", default=None)
    a = ap.parse_args()

    root = os.path.expanduser(a.root)
    reclaimed = a.reclaimed_gb if a.reclaimed_gb is not None else round(a.before_gb - a.after_gb, 1)
    today = datetime.date.today().isoformat()

    hist = []
    if a.history and os.path.exists(a.history):
        try:
            hist = json.load(open(a.history))
        except (OSError, ValueError):
            hist = []
    run = {"date": today, "label": a.label or os.path.basename(root.rstrip("/")),
           "root": root, "before_gb": a.before_gb, "after_gb": a.after_gb,
           "reclaimed_gb": reclaimed, "dupes": a.dupes, "folders": a.folders}
    hist.append(run)
    if a.history:
        try:
            json.dump(hist, open(a.history, "w"), indent=2)
        except OSError:
            pass

    cats = categories(root)
    out_html = render(a.label, root, a.before_gb, a.after_gb, reclaimed,
                      a.dupes, a.folders, cats, hist, today)
    with open(a.out, "w") as f:
        f.write(out_html)
    print("Wrote %s (%d category rows, %d runs in history)" % (a.out, len(cats), len(hist)))


if __name__ == "__main__":
    main()
