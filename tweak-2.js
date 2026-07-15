const fs = require('fs');
let html = fs.readFileSync('proposta-presencial.html', 'utf8');

// 1. Substituir os gradientes brancos por gradiente zinco (cinza claro Apple)
html = html.replace(/bg-gradient-to-b from-white to-white\/60/g, 'bg-gradient-to-r from-zinc-400 to-zinc-200');
html = html.replace(/bg-gradient-to-b from-white to-white\/70/g, 'bg-gradient-to-r from-zinc-400 to-zinc-200');

// 2. Ajustar a grade geométrica (linhas finas claras)
const oldGrid = `<svg class="apple-grid" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <pattern height="64" id="grid" patternUnits="userSpaceOnUse" width="64">
                <path d="M64 0H0v64" fill="none" stroke="white" stroke-width="0.5"></path>
            </pattern>
        </defs>
        <rect fill="url(#grid)" height="100%" width="100%"></rect>
    </svg>`;

const newGrid = `<div class="fixed inset-0 z-[-15] pointer-events-none opacity-[0.25]" style="background-image: linear-gradient(rgba(255,255,255,0.12) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,0.12) 1px, transparent 1px); background-size: 40px 40px;"></div>`;

if (html.includes('<svg class="apple-grid"')) {
    html = html.replace(oldGrid, newGrid);
} else if (!html.includes('background-image: linear-gradient(rgba(255,255,255,0.12) 1px')) {
    html = html.replace('<div class="sebrae-bg"></div>', '<div class="sebrae-bg"></div>\n    ' + newGrid);
}

fs.writeFileSync('proposta-presencial.html', html);
console.log('Tweak 2 done');
