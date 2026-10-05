/* Lesson engine — click-to-reveal class pages. Plain JavaScript, no dependencies.
   A class page only writes content; this file adds the top bar, the cover page,
   one-step-at-a-time navigation, one-thing-at-a-time reveal, code highlighting,
   quizzes, votes, traces and timers. */
(function () {
  'use strict';
  const D = document, B = D.body;
  const KEY = (B.dataset.key || 'lesson') + '.';
  const $ = (s, r) => (r || D).querySelector(s);
  const $$ = (s, r) => [...(r || D).querySelectorAll(s)];
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} },
    del(k) { try { localStorage.removeItem(k); } catch (e) {} }
  };
  const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  const el = (tag, cls, html) => { const e = D.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; };
  const fmt = s => Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0');
  const QS = new URLSearchParams(location.search);
  const REVIEW = QS.has('all');            // review view: everything visible, nothing saved
  if (REVIEW) B.classList.add('review');
  if (REVIEW) { const w = $('.wrap'); if (w) w.prepend(el('div', 'review-note', 'All steps are on one page here. <a href="' + location.pathname + '">Open the step-by-step view</a> to see one thing at a time.')); }

  /* ---------- theme ---------- */
  const savedTheme = store.get('lesson.theme');
  if (savedTheme) D.documentElement.dataset.theme = savedTheme;

  /* ---------- page chrome: progress bar, top bar, path ---------- */
  const progress = el('div', 'progress');
  const topbar = el('div', 'topbar',
    '<div class="brand"><span class="logo">' + esc(B.dataset.class || '') + '</span><span class="bt">' + esc(B.dataset.title || '') + '</span>' +
    (B.dataset.course ? '<span class="sub">· ' + esc(B.dataset.course) + '</span>' : '') + '</div>' +
    '<div class="right"><button class="tbtn" data-act="path">☰ Path</button><span class="counter" id="counter"></span>' +
    '<button class="tbtn" data-act="view" title="One step on screen, or all opened steps in a scroll"></button>' +
    '<a class="tbtn" href="https://scaler-pylens.vercel.app/" target="_blank" rel="noopener">PyLens ↗</a>' +
    '<button class="tbtn" data-act="theme">🌙 Theme</button><button class="tbtn" data-act="reset" title="Start from the beginning">↺ Reset</button></div>');
  const nav = el('nav', 'sidenav', '<div class="lbl">Today\'s path</div>');
  B.prepend(nav); B.prepend(topbar); B.prepend(progress);

  /* ---------- Python highlighter ---------- */
  const KW = /^(if|elif|else|match|case|and|or|not|in|is|True|False|None|while|for|def|return|import|from|as|pass|break|continue|class|try|except|finally|raise|with|lambda|global|del|yield|assert)$/;
  const BI = /^(print|input|int|float|str|bool|type|len|range|round|abs|min|max|sum|sorted|list|dict|set|tuple|map|filter|zip|enumerate|open|isinstance)$/;
  function hlLine(s) {
    let out = '', i = 0;
    while (i < s.length) {
      const c = s[i];
      if (c === '#') { out += '<span class="cm">' + esc(s.slice(i)) + '</span>'; break; }
      if (c === '"' || c === "'") { let j = i + 1; while (j < s.length && s[j] !== c) { if (s[j] === '\\') j++; j++; } out += '<span class="st">' + esc(s.slice(i, j + 1)) + '</span>'; i = j + 1; continue; }
      if (s.startsWith('__________', i)) { out += '<span class="blank">__________</span>'; i += 10; continue; }
      if (/[A-Za-z_]/.test(c)) {
        let j = i; while (j < s.length && /\w/.test(s[j])) j++;
        const w = s.slice(i, j), call = /^\s*\(/.test(s.slice(j));
        if (KW.test(w)) out += '<span class="kw">' + w + '</span>';
        else if (call && BI.test(w)) out += '<span class="bi">' + w + '</span>';
        else out += esc(w);
        i = j; continue;
      }
      if (/[0-9]/.test(c)) { let j = i; while (j < s.length && /[0-9._]/.test(s[j])) j++; out += '<span class="nu">' + s.slice(i, j) + '</span>'; i = j; continue; }
      if (/[<>=!+\-*\/%]/.test(c)) { let j = i; while (j < s.length && /[<>=!+\-*\/%]/.test(s[j])) j++; out += '<span class="op">' + esc(s.slice(i, j)) + '</span>'; i = j; continue; }
      out += esc(c); i++;
    }
    return out;
  }
  function ranges(spec) { const set = new Set(); (spec || '').split(',').forEach(p => { p = p.trim(); if (!p) return; const m = p.split('-').map(Number); for (let n = m[0]; n <= (m[1] || m[0]); n++) set.add(n); }); return set; }

  /* <pre class="py" data-file="x.py" data-kind="good|bad" data-hl="3-4" data-plain data-nocopy> */
  $$('pre.py').forEach(pre => {
    const raw = pre.textContent.replace(/^\n/, '').replace(/\s+$/, '');
    const hl = ranges(pre.dataset.hl), plain = pre.hasAttribute('data-plain');
    const box = el('div', 'code' + (pre.dataset.kind ? ' ' + pre.dataset.kind : ''));
    const ch = el('div', 'ch', '<span class="dots"><i></i><i></i><i></i>' + (pre.dataset.file ? '<span class="fn">' + esc(pre.dataset.file) + '</span>' : '') + '</span>' +
      (pre.hasAttribute('data-nocopy') ? '' : '<button class="copy" type="button">copy</button>'));
    pre.parentNode.insertBefore(box, pre); box.appendChild(ch); box.appendChild(pre);
    pre.dataset.raw = raw;
    pre.innerHTML = raw.split('\n').map((l, i) => '<span class="line' + (hl.has(i + 1) ? ' new' : '') + '" data-n="' + (i + 1) + '"><span class="lno">' + (i + 1) + '</span>' + (plain ? esc(l) : hlLine(l)) + '</span>').join('');
  });
  D.addEventListener('click', e => {
    const b = e.target.closest('.code .copy'); if (!b) return;
    const pre = b.closest('.code').querySelector('pre');
    if (navigator.clipboard) navigator.clipboard.writeText(pre.dataset.raw).then(() => { b.textContent = 'copied ✓'; setTimeout(() => b.textContent = 'copy', 1200); });
  });

  /* ---------- steps: heading, footer, path entry ---------- */
  const steps = $$('.step'), TOTAL = steps.length;
  let unlocked = 0, cur = 0;
  steps.forEach((s, i) => {
    if (!s.id) s.id = 's' + (i + 1);
    const h = $('h2', s), head = el('div', 'step-head');
    head.appendChild(el('span', 'step-num', String(i + 1)));
    if (h) head.appendChild(h);
    if (s.dataset.tag) head.appendChild(el('span', 'ver', esc(s.dataset.tag)));
    s.prepend(head);
    s.appendChild(el('div', 'foot', '<button class="back" type="button">◂ Back</button><span class="kbd">press <kbd>→</kbd></span><button class="next" type="button">' + (i < TOTAL - 1 ? 'Next ▸' : 'Next ▸') + '</button>'));
    const a = el('a', 'locked', '<span class="n">' + (i + 1) + '</span><span class="t">' + esc(s.dataset.nav || (h ? h.textContent : '')) + '</span>');
    a.href = '#' + s.id; a.addEventListener('click', e => { e.preventDefault(); jump(i); });
    nav.appendChild(a);
  });

  /* ---------- reveal buttons and their panels ---------- */
  function targetOf(b) {
    if (b._t !== undefined) return b._t;
    let t = null;
    if (b.dataset.reveal === 'next') { t = b.nextElementSibling; while (t && !t.classList.contains('reveal')) t = t.nextElementSibling; }
    else t = D.getElementById(b.dataset.reveal);
    return (b._t = t);
  }
  function voteOf(b) {
    if (b._v !== undefined) return b._v;
    let v = null;
    if (b.dataset.vote === 'prev') { v = b.previousElementSibling; while (v && !v.classList.contains('vote')) v = v.previousElementSibling; }
    else if (b.dataset.vote) v = D.getElementById(b.dataset.vote);
    return (b._v = v);
  }
  const revealBtns = $$('.rv[data-reveal]');
  revealBtns.forEach(b => { targetOf(b); voteOf(b); b.textContent = b.textContent.replace(/^[^A-Za-z0-9"“(]+/u, ''); });      // resolve before the layout below moves things

  /* ---------- wide screens: code on the left, its result on the right ---------- */
  function duoize(box) {
    const kids = [...box.children];
    for (let i = 0; i < kids.length; i++) {
      const k = kids[i]; if (!k.matches('.code')) continue;
      let j = i + 1; const mid = [];
      while (kids[j] && kids[j].matches('.ask, .vote')) mid.push(kids[j++]);
      let right = null, btn = null;
      if (kids[j] && kids[j].matches('.rv[data-reveal]') && kids[j + 1] && kids[j + 1] === targetOf(kids[j])) { btn = kids[j]; right = kids[j + 1]; }
      else if (!mid.length && kids[j] && kids[j].matches('.out')) right = kids[j];
      if (!right) continue;
      const duo = el('div', 'duo'), L = el('div', 'duo-l'), R = el('div', 'duo-r');
      box.insertBefore(duo, k); L.append(k, ...mid); if (btn) L.append(btn); R.append(right); duo.append(L, R);
      i = kids.indexOf(right);
    }
  }
  steps.forEach(duoize); $$('.reveal').forEach(duoize);

  /* ---------- a few presses per step ----------
     A step opens with its heading and its first group (the question). Each further press shows
     one group: an answer panel as a whole, or the next run of blocks. A new group starts at a
     question (.ask), a label (.lab), a quiz, a project build, the result side of a code pair,
     or any block marked data-brk. Table rows, trace steps and type cards keep their own press. */
  const mark = n => { n.classList.add('frag'); return n; };
  function buildItems(step) {
    const list = []; let grp = null, groups = 0;
    const close = () => { grp = null; };
    const tail = n => { const last = list[list.length - 1]; if (last) (last.also || (last.also = [])).push(mark(n)); else add(n); };
    const extras = n => {                 // parts of a block that still take their own press
      $$('table.tbl', n).concat(n.matches('table.tbl') ? [n] : []).forEach(t => $$('tr', t).slice(1).forEach(r => list.push({ el: mark(r), also: [] })));
      $$('.trace', n).concat(n.matches('.trace') ? [n] : []).forEach(t => list.push({ trace: t }));
      $$('.types', n).concat(n.matches('.types') ? [n] : []).forEach(g => [...g.children].forEach(c => { if (!c.classList.contains('on')) list.push({ card: c }); }));
      $$('.chips, .anat', n).concat(n.matches('.chips, .anat') ? [n] : []).forEach(g => { const cs = [...g.children].filter(c => !c.classList.contains('on')); if (cs.length) list.push({ cards: cs }); });
    };
    const add = n => {
      if (!grp) { grp = { el: mark(n), also: [] }; list.push(grp); groups++; } else grp.also.push(mark(n));
      if (n.matches('.types, .chips, .anat, .diag, .tbl, .steps-list')) grp.heavy = true;   // a question after these gets its own press
      extras(n);
    };
    const walk = box => [...box.children].forEach(ch => {
      if (ch.matches('.step-head, .foot, script, style, .tbl-hint')) return;
      if (ch.matches('.duo, .duo-l')) { walk(ch); return; }
      if (ch.matches('.duo-r')) { const f = ch.firstElementChild; if (!(f && f.matches('.reveal'))) close(); walk(ch); return; }
      if (ch.matches('.reveal')) { extras(ch); return; }                  // shown as a whole by its button
      if (ch.matches('.rv[data-reveal]')) {
        if (grp) grp.also.push(mark(ch)); else tail(ch);
        list.push({ btn: ch }); close(); return;
      }
      if (ch.matches('.take, .note')) { if (grp && list[list.length - 1] === grp) grp.also.push(mark(ch)); else tail(ch); return; }
      if (ch.matches('.quiz, .build, .case')) { close(); add(ch); close(); return; }
      if (ch.matches('.lab, [data-brk]')) { close(); add(ch); return; }
      if (ch.matches('.ask')) { if (grp && (groups > 1 || grp.ask || grp.heavy)) close(); add(ch); grp.ask = true; return; }
      add(ch);
    });
    walk(step);
    return list;
  }
  steps.forEach(s => { s._items = buildItems(s); });
  const frags = $$('.frag');
  $$('table.tbl').forEach(t => t.insertAdjacentElement('afterend', el('div', 'tbl-hint', 'click the table for the next row')));
  const isDone = it => it.el ? it.el.classList.contains('frag-on') : it.btn ? targetOf(it.btn).classList.contains('on') : it.trace ? !!it.trace.dataset.done : it.cards ? it.cards.every(c => c.classList.contains('on')) : it.card.classList.contains('on');
  const showAlso = it => (it.also || []).forEach(n => n.classList.add('frag-on'));
  const show = it => { it.el.classList.add('frag-on'); showAlso(it); return it.el; };
  const sweep = step => { if (step && step._items) step._items.forEach(it => { if (isDone(it)) showAlso(it); }); };
  function bring(n) {
    if (!n) return; const r = n.getBoundingClientRect();
    if (r.top < 80 || r.bottom > innerHeight - 24) n.scrollIntoView({ behavior: 'smooth', block: r.height > innerHeight * 0.65 ? 'start' : 'center' });
  }
  let viaKey = false;
  function openStepwise(btn) {       // open an answer panel from code
    btn.click(); const step = btn.closest('.step'); sweep(step);
    const panel = targetOf(btn); saveState(); setTimeout(() => bring(panel), 40); return panel;
  }
  function advance(i) {              // show the next group of step i; false when nothing is left
    const items = steps[i]._items; sweep(steps[i]);
    const it = items.find(x => !isDone(x));
    if (!it) return false;
    let focus;
    if (it.el) focus = show(it);
    else if (it.btn) { it.btn.click(); focus = targetOf(it.btn); }
    else if (it.trace) { $('.rv', it.trace).click(); focus = it.trace; }
    else if (it.cards) { it.cards.forEach(c => c.classList.add('on')); focus = it.cards[0].parentElement; }
    else { it.card.click(); focus = it.card; }
    if (isDone(it)) showAlso(it);
    saveState(); bring(focus); return true;
  }
  D.addEventListener('click', e => { const s = e.target.closest('.step'); if (s) setTimeout(() => { sweep(s); saveState(); }, 0); });

  /* ---------- navigation ---------- */
  let SOLO = store.get('lesson.solo') !== '0';       // one step on screen (default) or a scroll of all opened steps
  function paint() {
    B.classList.toggle('solo', SOLO && !REVIEW);
    progress.style.width = (TOTAL ? unlocked / TOTAL * 100 : 0) + '%';
    $('#counter').textContent = REVIEW ? 'Review view · all open' : 'Step ' + (unlocked ? cur + 1 : 0) + ' / ' + TOTAL;
    $('[data-act=view]', topbar).textContent = SOLO ? '▤ All steps' : '▣ One step';
    $$('a', nav).forEach((a, i) => { a.classList.toggle('locked', i >= unlocked); a.classList.toggle('open', i < unlocked); a.classList.toggle('current', i === cur && unlocked > 0); });
    steps.forEach((s, i) => { s.classList.toggle('cur', i === cur && unlocked > 0); const bk = $('.foot .back', s); if (bk) bk.style.visibility = i === 0 ? 'hidden' : ''; });
    if (!REVIEW) { store.set(KEY + 'unlocked', String(unlocked)); store.set(KEY + 'cur', String(cur)); }
  }
  function scrollToStep(i) { const y = steps[i].getBoundingClientRect().top + window.scrollY - 80; window.scrollTo({ top: y, behavior: 'smooth' }); }
  function openStep(i) { if (i >= TOTAL) return; steps[i].classList.add('open'); unlocked = Math.max(unlocked, i + 1); }
  function setCur(i) {
    cur = Math.max(0, Math.min(i, unlocked - 1)); paint();
    if (B.classList.contains('solo')) window.scrollTo(0, 0); else setTimeout(() => scrollToStep(cur), 30);
  }
  function forward() {
    if (!unlocked) { openStep(0); setCur(0); advance(0); return; }
    if (advance(cur)) return;
    if (cur < unlocked - 1) { setCur(cur + 1); if (!steps[cur]._items.some(isDone)) advance(cur); return; }
    if (unlocked < TOTAL) { openStep(unlocked); setCur(unlocked - 1); advance(cur); }
  }
  function back() { if (cur > 0) setCur(cur - 1); }
  function jump(i) {                 // the path can take you to any step, reached or not
    if (cover) cover.classList.add('off');
    for (let k = unlocked; k <= i; k++) openStep(k);
    setCur(i);
    if (!steps[i]._items.some(isDone)) advance(i);
  }
  function showAll() {               // the whole class as one readable page
    for (let i = 0; i < TOTAL; i++) openStep(i);
    B.classList.add('showall'); if (!REVIEW) store.set(KEY + 'showall', '1'); paint();
  }
  D.addEventListener('click', e => {          // a click on a table shows its next row
    const t = e.target.closest('table.tbl'); if (!t) return;
    const r = $$('tr.frag', t).find(x => !x.classList.contains('frag-on'));
    if (r) { r.classList.add('frag-on'); saveState(); }
  });
  D.addEventListener('click', e => {
    if (e.target.closest('.step .foot .next')) { const s = e.target.closest('.step'); cur = steps.indexOf(s); forward(); }
    else if (e.target.closest('.step .foot .back')) back();
  });
  topbar.addEventListener('click', e => {
    const b = e.target.closest('[data-act]'); if (!b) return;
    if (b.dataset.act === 'path') B.classList.toggle('navon');
    if (b.dataset.act === 'view') { SOLO = !SOLO; store.set('lesson.solo', SOLO ? '1' : '0'); paint(); if (!SOLO && unlocked) setTimeout(() => scrollToStep(cur), 30); else window.scrollTo(0, 0); }
    if (b.dataset.act === 'theme') { const h = D.documentElement; h.dataset.theme = h.dataset.theme === 'dark' ? 'light' : 'dark'; store.set('lesson.theme', h.dataset.theme); }
    if (b.dataset.act === 'reset') { if (!confirm('Start this class from the beginning?')) return; ['unlocked', 'cur', 'state', 'showall'].forEach(k => store.del(KEY + k)); location.href = location.pathname + location.search; }
  });

  /* ---------- cover page ---------- */
  const cover = $('#cover');
  function start(all) { if (cover) cover.classList.add('off'); if (all) showAll(); else if (!unlocked) forward(); window.scrollTo(0, 0); }
  if (cover) {
    const d = new Date();
    const today = d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') + '-' + String(d.getDate()).padStart(2, '0');
    const live = QS.has('live') || (!QS.has('replay') && (!B.dataset.date || today <= B.dataset.date));
    const acts = el('div', 'acts');
    if (live) {
      const wait = el('div', 'wait', '<span class="wt">We start in the next 5 minutes</span><span class="cd" title="click to restart the timer">5:00</span>');
      cover.appendChild(wait);
      const cd = $('.cd', wait), wt = $('.wt', wait); let left = 300;
      const tick = () => { cd.textContent = fmt(Math.max(left, 0)); if (left <= 0) { wt.textContent = 'Starting now'; cd.style.display = 'none'; } };
      setInterval(() => { if (left > 0) { left--; tick(); } }, 1000);
      cd.addEventListener('click', () => { left = 300; wt.textContent = 'We start in the next 5 minutes'; cd.style.display = ''; tick(); });
      const box = el('div', 'shout'); cover.appendChild(box);
      const sc = el('script'); sc.src = 'shoutouts.local.js';
      sc.onload = () => { (window.SHOUTOUTS || []).forEach(g => { if (!g.names || !g.names.length) return; box.appendChild(el('div', 'grp', '<h4>' + esc(g.title || '') + '</h4><div class="names">' + g.names.map(n => '<span>' + esc(n) + '</span>').join('') + '</div>')); }); };
      sc.onerror = () => {};
      D.head.appendChild(sc);
      acts.appendChild(el('button', 'next', 'Start ▸'));
    } else {
      cover.appendChild(el('div', 'wait', '<span class="wt">Class notes · go at your own pace</span>'));
      acts.appendChild(el('button', 'ghost', 'Show everything'));
      acts.appendChild(el('button', 'next', 'Step by step ▸'));
    }
    cover.appendChild(acts);
    acts.addEventListener('click', e => { if (e.target.closest('.next')) start(false); else if (e.target.closest('.ghost')) start(true); });
  }

  /* ---------- reveals, cards, quizzes ---------- */
  function syncReveal(b) {      // make the button and its vote reflect the panel's state
    const t = targetOf(b); if (!t) return;
    const on = t.classList.contains('on'); b.classList.toggle('done', on);
    const v = voteOf(b); if (v) { v.classList.toggle('done', on); $$('.vopt', v).forEach(o => { o.classList.toggle('win', o.hasAttribute('data-win') && on); if (!on) o.classList.remove('wrong'); }); }
  }
  const revs = $$('.reveal'), toggles = $$('.chip, .anat .a, .ty'), quizzes = $$('.quiz');
  let restoring = false;
  const SIG = revs.length + ':' + frags.length + ':' + toggles.length;   // saved state only fits the page it was made on
  function saveState() {       // what is open survives a refresh
    if (REVIEW || restoring) return;
    const idx = (list, cls) => list.map((x, i) => x.classList.contains(cls) ? i : -1).filter(i => i >= 0);
    store.set(KEY + 'state', JSON.stringify({ sig: SIG, r: idx(revs, 'on'), t: idx(toggles, 'on'), f: idx(frags, 'frag-on'), q: quizzes.map(q => q.dataset.pick === undefined ? -1 : +q.dataset.pick) }));
  }
  revealBtns.forEach(b => b.addEventListener('click', () => {
    const t = targetOf(b); if (!t) return;
    const on = t.classList.toggle('on'); syncReveal(b);
    if (on && !viaKey) $$('.frag', t).forEach(n => { if (n.tagName !== 'TR' && !n.closest('.reveal:not(.on)')) n.classList.add('frag-on'); });   // a mouse click opens the whole panel; table rows still wait for their own click
    saveState();
  }));
  toggles.forEach(c => {
    if (!c.classList.contains('on') && !$('.hint', c)) c.appendChild(el('div', 'hint', 'click to reveal'));
    c.addEventListener('click', () => { c.classList.toggle('on'); saveState(); });
  });
  const LV = { s: 'Simple', m: 'Medium', t: 'Tough' };
  quizzes.forEach(q => {
    const lv = q.dataset.level, qt = $('.qt', q);
    if (lv && qt) qt.prepend(el('span', 'lvl ' + lv, LV[lv] || lv));
    $$('.opt', q).forEach((o, oi) => { o.type = 'button'; o.addEventListener('click', () => {
      if (q.classList.contains('done')) return;
      q.classList.add('done'); q.dataset.pick = oi;
      $$('.opt', q).forEach(x => { if (x.hasAttribute('data-ok')) x.classList.add('right'); });
      if (!o.hasAttribute('data-ok')) o.classList.add('wrong');
      saveState(); setTimeout(() => bring($('.expl', q)), 60);
    }); });
  });

  /* ---------- quick questions: click an option, the right one lights up and the result opens ---------- */
  $$('.vote').forEach(v => $$('.vopt', v).forEach(o => {
    o.setAttribute('role', 'button'); o.tabIndex = 0;
    o.addEventListener('click', () => {
      if (v.classList.contains('done')) return;
      v.classList.add('done');
      if (!o.hasAttribute('data-win')) o.classList.add('wrong');
      $$('.vopt', v).forEach(x => x.classList.toggle('win', x.hasAttribute('data-win')));
      const btn = revealBtns.find(b => voteOf(b) === v);
      if (btn && !targetOf(btn).classList.contains('on')) openStepwise(btn);
    });
  }));

  /* ---------- traces: step through code, watch memory and output ---------- */
  $$('.trace').forEach(tr => {
    let st; try { st = JSON.parse(tr.dataset.steps); } catch (e) { console.error('trace JSON', e); return; }
    const pre = D.getElementById(tr.dataset.code); if (!pre) return;
    const mem = st.some(x => x.m) ? el('div', 'mem') : null, log = el('div', 'steps-list');
    const out = st.some(x => x.o !== undefined) ? el('div', 'out') : null, btn = el('button', 'rv small', 'Step ▸');
    btn.type = 'button'; [mem, log, out, btn].forEach(x => x && tr.appendChild(x));
    let k = 0; const vars = {};
    const drawMem = () => { if (!mem) return; const ks = Object.keys(vars); mem.innerHTML = '<span class="ml">memory</span>' + (ks.length ? ks.map(n => '<span class="mv"><b>' + esc(n) + '</b> → ' + esc(vars[n]) + '</span>').join('') : '<em>nothing stored yet</em>'); };
    drawMem();
    btn.addEventListener('click', () => {
      const lines = $$('.line', pre);
      if (k >= st.length) { k = 0; log.innerHTML = ''; if (out) out.textContent = ''; Object.keys(vars).forEach(n => delete vars[n]); drawMem(); lines.forEach(l => l.classList.remove('hi', 'ok', 'skip')); btn.textContent = 'Step ▸'; delete tr.dataset.done; return; }
      const s = st[k]; lines.forEach(l => l.classList.remove('hi', 'ok'));
      const ls = Array.isArray(s.l) ? s.l : [s.l];
      ls.forEach(n => { const L = $('.line[data-n="' + n + '"]', pre); if (!L) return; if (s.r === 's') L.classList.add('skip'); else { L.classList.add('hi'); if (s.r === 't') L.classList.add('ok'); } });
      const markTxt = s.r === 't' ? '✓' : s.r === 's' ? 'skipped' : s.r === 'f' ? '✗' : '';
      log.appendChild(el('div', 'sl on', '<span class="ln">line ' + ls.join(', ') + '</span>' + s.n + (markTxt ? ' <span class="r ' + (s.r === 't' ? 't' : 'f') + '">' + markTxt + '</span>' : '')));
      log.scrollTop = log.scrollHeight;
      if (s.m) { Object.assign(vars, s.m); drawMem(); }
      if (out && s.o !== undefined) { out.textContent += s.o; out.scrollTop = out.scrollHeight; }
      k++; if (k >= st.length) { btn.textContent = '↺ Restart'; tr.dataset.done = '1'; }
    });
  });

  /* ---------- timers: click to start / pause, double-click to reset ---------- */
  $$('.timer').forEach(t => {
    const total = parseInt(t.dataset.sec, 10) || 60; let left = total, h = null;
    const draw = () => { t.textContent = '⏱ ' + (left > 0 ? fmt(left) : 'Time!'); t.classList.toggle('run', !!h); t.classList.toggle('done', left <= 0); };
    t.title = 'click to start or pause · double-click to reset';
    t.addEventListener('click', () => {
      if (left <= 0) { left = total; draw(); return; }
      if (h) { clearInterval(h); h = null; } else h = setInterval(() => { left--; if (left <= 0) { clearInterval(h); h = null; } draw(); }, 1000);
      draw();
    });
    t.addEventListener('dblclick', () => { clearInterval(h); h = null; left = total; draw(); });
    draw();
  });

  /* ---------- restore after a refresh: steps, the step on screen, and what was open ---------- */
  (function restore() {
    if (REVIEW) { if (cover) cover.classList.add('off'); for (let i = 0; i < TOTAL; i++) openStep(i); paint(); return; }
    const n = Math.min(parseInt(store.get(KEY + 'unlocked') || '0', 10), TOTAL);
    for (let i = 0; i < n; i++) openStep(i);
    if (n > 0) { if (cover) cover.classList.add('off'); cur = Math.max(0, Math.min(parseInt(store.get(KEY + 'cur') || String(n - 1), 10), n - 1)); }
    let st; try { st = JSON.parse(store.get(KEY + 'state') || 'null'); } catch (e) { st = null; }
    if (st && st.sig === SIG && n > 0) {
      restoring = true;
      (st.r || []).forEach(i => revs[i] && revs[i].classList.add('on'));
      revealBtns.forEach(syncReveal);
      (st.t || []).forEach(i => toggles[i] && toggles[i].classList.add('on'));
      (st.f || []).forEach(i => frags[i] && frags[i].classList.add('frag-on'));
      (st.q || []).forEach((oi, qi) => { const q = quizzes[qi]; if (q && oi >= 0) { const o = $$('.opt', q)[oi]; if (o) o.click(); } });
      restoring = false;
    }
    if (store.get(KEY + 'showall') === '1') B.classList.add('showall');
    if (!cover && !n) forward();
    paint();
  })();

  /* ---------- keyboard: → the next thing, ← the previous step ---------- */
  D.addEventListener('keydown', e => {
    if (/^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName) || e.target.isContentEditable || e.metaKey || e.ctrlKey || e.altKey) return;
    if ($('#cf-tour-bar.cf-visible, #cf-editor.cf-visible')) return;   // a review tool on the page is using the arrow keys
    if (REVIEW) return;
    if (e.key === 'U' && e.shiftKey) { start(true); return; }
    if (B.classList.contains('showall')) return;
    if (e.key === 'ArrowRight' || e.key === 'PageDown') {
      e.preventDefault();
      if (cover && !cover.classList.contains('off')) { start(false); return; }
      forward();
    }
    if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); back(); }
  });
})();
