html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Control Emisora</title>
    <style>
        :root {
            --bg-dark: #0f172a;
            --card-bg: #1e293b;
            --accent-blue: #38bdf8;
            --accent-green: #22c55e;
            --accent-red: #ef4444;
            --text-main: #f8fafc;
            --text-sub: #94a3b8;
            --border: #334155;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: system-ui, -apple-system, sans-serif;
        }

        body {
            background-color: var(--bg-dark);
            color: var(--text-main);
            padding: 12px;
            max-width: 480px;
            margin: 0 auto;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }

        /* HEADER */
        header {
            background: #090d16;
            padding: 10px 14px;
            border-radius: 10px;
            border: 1px solid var(--border);
            margin-bottom: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.1rem;
            font-weight: bold;
            color: var(--accent-blue);
        }

        .stats {
            display: flex;
            gap: 12px;
            font-size: 0.9rem;
            font-weight: bold;
        }

        .stat-green { color: var(--accent-green); }

        /* PESTAÑAS AMPLIAS Y CÓMODAS */
        .tabs {
            display: flex;
            gap: 8px;
            margin-bottom: 12px;
        }

        .tab-btn {
            flex: 1;
            padding: 12px;
            background: var(--card-bg);
            border: 1px solid var(--border);
            color: var(--text-sub);
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.95rem;
            text-align: center;
        }

        .tab-btn.active {
            background: var(--accent-blue);
            color: #000;
            border-color: var(--accent-blue);
        }

        .panel {
            display: none;
            flex: 1;
        }

        .panel.active {
            display: flex;
            flex-direction: column;
        }

        /* FORMULARIO CÓMODO */
        .form-card {
            background: var(--card-bg);
            padding: 16px;
            border-radius: 10px;
            border: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        label {
            display: block;
            font-size: 0.8rem;
            color: var(--text-sub);
            text-transform: uppercase;
            margin-bottom: 4px;
            font-weight: bold;
        }

        input, select, textarea {
            width: 100%;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid var(--border);
            background: #090d16;
            color: var(--text-main);
            font-size: 0.95rem;
        }

        textarea {
            resize: none;
            height: 60px;
        }

        .btn-add {
            background: var(--accent-green);
            color: #000;
            font-weight: bold;
            padding: 14px;
            border: none;
            border-radius: 8px;
            font-size: 1.05rem;
            cursor: pointer;
            width: 100%;
            margin-top: 6px;
        }

        /* VISTA DJ AMPLIA */
        .dj-container {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 12px;
        }

        .card.done {
            opacity: 0.45;
            text-decoration: line-through;
            border-color: transparent;
            background: #090d16;
        }

        .card-head {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.85rem;
            color: var(--text-sub);
            margin-bottom: 6px;
        }

        .card-head strong {
            color: var(--text-main);
            font-size: 0.95rem;
        }

        .badge {
            background: var(--accent-blue);
            color: #000;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: bold;
        }

        .song {
            font-size: 1.05rem;
            font-weight: bold;
            color: var(--accent-blue);
            margin: 4px 0;
        }

        .msg {
            font-size: 0.9rem;
            font-style: italic;
            color: #f1f5f9;
            background: #090d16;
            padding: 8px;
            border-radius: 6px;
            border-left: 3px solid var(--accent-blue);
            margin: 6px 0;
        }

        .btn-check {
            width: 100%;
            background: #334155;
            color: var(--text-main);
            border: none;
            padding: 10px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: bold;
            cursor: pointer;
            margin-top: 6px;
        }

        .card.done .btn-check {
            background: var(--accent-green);
            color: #000;
        }

        .btn-clean {
            background: var(--accent-red);
            color: #fff;
            border: none;
            padding: 12px;
            border-radius: 8px;
            font-size: 0.9rem;
            font-weight: bold;
            cursor: pointer;
            width: 100%;
            margin-top: 15px;
        }

        #toast {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: var(--accent-green);
            color: #000;
            padding: 8px 20px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.9rem;
            display: none;
            box-shadow: 0 4px 12px rgba(0,0,0,0.5);
        }
    </style>
</head>
<body>

    <header>
        <div class="logo">📻 Emisora Escolar</div>
        <div class="stats">
            <span>Caja: <span id="caja" class="stat-green">$0</span></span>
            <span>Total: <span id="cant" class="stat-green">0</span></span>
        </div>
    </header>

    <div class="tabs">
        <button class="tab-btn active" id="btnTabReg" onclick="switchTab('registro')">+ Nuevo Pedido</button>
        <button class="tab-btn" id="btnTabDJ" onclick="switchTab('dj')">🎧 Vista DJ</button>
    </div>

    <!-- PESTAÑA 1: REGISTRO -->
    <div id="panelRegistro" class="panel active">
        <form id="pForm" class="form-card">
            <div>
                <label>De (Remitente):</label>
                <input type="text" id="de" placeholder="Anónimo">
            </div>
            <div>
                <label>Para (Destinatario):</label>
                <input type="text" id="para" required placeholder="Nombre del compañero/a">
            </div>
            <div>
                <label>Grado:</label>
                <select id="grado" required>
                    <option value="9°">9°</option>
                    <option value="10°">10°</option>
                    <option value="11°">11°</option>
                    <option value="Profe/Otro">Profe / Otro</option>
                </select>
            </div>
            <div>
                <label>Canción y Artista:</label>
                <input type="text" id="cancion" required placeholder="Ej: La Bachata - Manuel Turizo">
            </div>
            <div>
                <label>Mensaje / Saludo:</label>
                <textarea id="mensaje" placeholder="Escribe el mensaje para leer al aire..."></textarea>
            </div>
            <button type="submit" class="btn-add">Guardar y Cobrar $500</button>
        </form>
    </div>

    <!-- PESTAÑA 2: VISTA DJ -->
    <div id="panelDJ" class="panel">
        <div class="dj-container" id="lista"></div>
        <button class="btn-clean" onclick="limpiar()">🧹 Borrar canciones que YA sonaron</button>
    </div>

    <div id="toast">¡Guardado +$500!</div>

    <script>
        let db = JSON.parse(localStorage.getItem('emisora_db')) || [];

        function switchTab(tab) {
            document.getElementById('panelRegistro').classList.remove('active');
            document.getElementById('panelDJ').classList.remove('active');
            document.getElementById('btnTabReg').classList.remove('active');
            document.getElementById('btnTabDJ').classList.remove('active');

            if(tab === 'registro') {
                document.getElementById('panelRegistro').classList.add('active');
                document.getElementById('btnTabReg').classList.add('active');
            } else {
                document.getElementById('panelDJ').classList.add('active');
                document.getElementById('btnTabDJ').classList.add('active');
            }
        }

        function render() {
            const container = document.getElementById('lista');
            container.innerHTML = '';
            
            document.getElementById('caja').innerText = `$${(db.length * 500).toLocaleString()}`;
            document.getElementById('cant').innerText = db.length;

            if(db.length === 0) {
                container.innerHTML = '<p style="text-align:center; color:var(--text-sub); font-size:0.9rem; padding:30px;">No hay pedidos en cola.</p>';
                return;
            }

            db.forEach((item, i) => {
                const card = document.createElement('div');
                card.className = `card ${item.ok ? 'done' : ''}`;
                card.innerHTML = `
                    <div class="card-head">
                        <span>#${i+1} De: <strong>${item.de}</strong> ➔ Para: <strong>${item.para}</strong></span>
                        <span class="badge">${item.grado}</span>
                    </div>
                    <div class="song">🎵 ${item.cancion}</div>
                    ${item.msg ? `<div class="msg">"${item.msg}"</div>` : ''}
                    <button class="btn-check" onclick="toggle(${item.id})">
                        ${item.ok ? '✓ YA SONÓ' : 'MARCAR COMO SONADA'}
                    </button>
                `;
                container.appendChild(card);
            });
        }

        document.getElementById('pForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const nuevo = {
                id: Date.now(),
                de: document.getElementById('de').value.trim() || 'Anónimo',
                para: document.getElementById('para').value.trim(),
                grado: document.getElementById('grado').value,
                cancion: document.getElementById('cancion').value.trim(),
                msg: document.getElementById('mensaje').value.trim(),
                ok: false
            };
            db.push(nuevo);
            localStorage.setItem('emisora_db', JSON.stringify(db));
            this.reset();
            render();

            // Notificación flotante suave
            const t = document.getElementById('toast');
            t.style.display = 'block';
            setTimeout(() => t.style.display = 'none', 1500);
        });

        function toggle(id) {
            db = db.map(x => x.id === id ? {...x, ok: !x.ok} : x);
            localStorage.setItem('emisora_db', JSON.stringify(db));
            render();
        }

        function limpiar() {
            if(confirm('¿Borrar solo las canciones que YA sonaron?')) {
                db = db.filter(x => !x.ok);
                localStorage.setItem('emisora_db', JSON.stringify(db));
                render();
            }
        }

        render();
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:")
    f.write(html_content)

print("Index corregido con pestañas amplias.
