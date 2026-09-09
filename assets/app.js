(function () {
  // Mobile nav
  var t = document.getElementById('navToggle'), n = document.getElementById('nav');
  if (t && n) t.addEventListener('click', function () {
    var open = n.classList.toggle('open');
    t.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  // Perforation finder (table filter + sort)
  var table = document.getElementById('finderTable');
  if (table) {
    var rows = Array.prototype.slice.call(table.tBodies[0].rows);
    var f = {
      material: document.getElementById('fMaterial'),
      hole: document.getElementById('fHole'),
      size: document.getElementById('fSize'),
      oa: document.getElementById('fOpen'),
      thick: document.getElementById('fThick'),
      q: document.getElementById('fSearch')
    };
    var count = document.getElementById('finderCount');
    function apply() {
      var shown = 0, q = (f.q.value || '').toLowerCase().trim();
      rows.forEach(function (r) {
        var d = r.dataset, ok = true;
        if (f.material.value && d.material !== f.material.value) ok = false;
        if (ok && f.hole.value && d.hole !== f.hole.value) ok = false;
        if (ok && f.size.value) {
          var s = parseFloat(d.size), b = f.size.value.split('-');
          if (s < parseFloat(b[0]) || s > parseFloat(b[1])) ok = false;
        }
        if (ok && f.oa.value) {
          var o = parseFloat(d.open), ob = f.oa.value.split('-');
          if (o < parseFloat(ob[0]) || o > parseFloat(ob[1])) ok = false;
        }
        if (ok && f.thick.value && (' ' + d.thick + ' ').indexOf(' ' + f.thick.value + ' ') < 0) ok = false;
        if (ok && q && r.textContent.toLowerCase().indexOf(q) < 0) ok = false;
        r.classList.toggle('hidden', !ok);
        if (ok) shown++;
      });
      count.textContent = shown + ' of ' + rows.length + ' perforations shown';
      try { history.replaceState(null, '', shown === rows.length ? location.pathname : location.pathname + '?m=' + encodeURIComponent(f.material.value) + '&h=' + encodeURIComponent(f.hole.value)); } catch (e) {}
    }
    Object.keys(f).forEach(function (k) { f[k].addEventListener('input', apply); });
    // preselect from query string
    try {
      var p = new URLSearchParams(location.search);
      if (p.get('m')) f.material.value = p.get('m');
      if (p.get('h')) f.hole.value = p.get('h');
    } catch (e) {}
    apply();
    // sorting
    Array.prototype.forEach.call(table.tHead.rows[0].cells, function (th, i) {
      var b = th.querySelector('button'); if (!b) return;
      var asc = true;
      b.addEventListener('click', function () {
        var key = th.dataset.key;
        rows.sort(function (a, c) {
          var x = a.dataset[key], y = c.dataset[key];
          var nx = parseFloat(x), ny = parseFloat(y);
          if (!isNaN(nx) && !isNaN(ny)) return asc ? nx - ny : ny - nx;
          return asc ? String(x).localeCompare(String(y)) : String(y).localeCompare(String(x));
        });
        asc = !asc;
        rows.forEach(function (r) { table.tBodies[0].appendChild(r); });
      });
    });
  }

  // Open area calculator
  var calc = document.getElementById('oaCalc');
  if (calc) {
    var g = function (id) { return document.getElementById(id); };
    function run() {
      var shape = g('cShape').value, d = parseFloat(g('cHole').value), p = parseFloat(g('cPitch').value), w = parseFloat(g('cSlot').value || 0);
      var oa = 0;
      if (!(d > 0 && p > 0)) { g('cOut').value = '–'; return; }
      if (shape === 'round-staggered') oa = 90.69 * (d * d) / (p * p);
      else if (shape === 'round-square') oa = 78.54 * (d * d) / (p * p);
      else if (shape === 'square') oa = 100 * (d * d) / (p * p);
      else if (shape === 'slot') { var p2 = parseFloat(g('cPitch2').value); if (!(p2 > 0 && w > 0)) { g('cOut').value = '–'; return; } oa = 100 * (w * d - (1 - Math.PI / 4) * w * w) / (p * p2); }
      if (oa > 100) oa = 100;
      g('cOut').value = oa.toFixed(1) + '%';
      var t = parseFloat(g('cThick').value), dens = parseFloat(g('cMat').value), L = parseFloat(g('cLen').value), W = parseFloat(g('cWid').value);
      if (t > 0 && L > 0 && W > 0) {
        var kg = (L / 1000) * (W / 1000) * t * dens * (1 - oa / 100);
        g('cWeight').value = kg.toFixed(2) + ' kg';
        g('cWeightM2').value = (t * dens * (1 - oa / 100)).toFixed(2) + ' kg/m²';
      }
    }
    ['cShape', 'cHole', 'cPitch', 'cPitch2', 'cSlot', 'cThick', 'cMat', 'cLen', 'cWid'].forEach(function (id) { var el = g(id); if (el) el.addEventListener('input', run); });
    g('cShape').addEventListener('change', function () { g('slotRow').classList.toggle('hidden', g('cShape').value !== 'slot'); });
    run();
  }
})();
