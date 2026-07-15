const fs = require('fs');
let html = fs.readFileSync('proposta-presencial.html', 'utf8');

// 1. Substituir destaques dos títulos (que estão em zinco) para azul (from-blue-400 to-blue-200)
html = html.replace(/from-zinc-400 to-zinc-200/g, 'from-blue-400 to-blue-200');

// 2. Substituir textos cinza escuro/médio para branco (aumentar contraste)
html = html.replace(/text-neutral-400/g, 'text-white/80');
html = html.replace(/text-zinc-400/g, 'text-white/80');
html = html.replace(/text-neutral-500/g, 'text-white/60');
html = html.replace(/text-zinc-500/g, 'text-white/60');

// 3. Substituir a imagem de fundo para "Sebrae Ok.jpg"
html = html.replace(/url\("\.\/sebrae\.jpg"\)/g, 'url("./Sebrae Ok.jpg")');
html = html.replace(/url\('\.\/sebrae\.jpg'\)/g, "url('./Sebrae Ok.jpg')");
// Caso esteja sem aspas
html = html.replace(/url\(\.\/sebrae\.jpg\)/g, "url('./Sebrae Ok.jpg')");

fs.writeFileSync('proposta-presencial.html', html);
console.log('Colors and Background Image tweaked');
