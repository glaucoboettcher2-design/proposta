const fs = require('fs');
let html = fs.readFileSync('proposta-presencial.html', 'utf8');

// 1. Make the apple-panel (main card) background slightly lighter
html = html.replace(/linear-gradient\(rgba\(15, 15, 15, 0\.7\), rgba\(15, 15, 15, 0\.7\)\)/g, 'linear-gradient(rgba(35, 35, 35, 0.6), rgba(35, 35, 35, 0.6))');

// 2. Add depth to main headings (h1, h2, h3) using background clip text
// h1 in slide 2
html = html.replace('class="text-5xl md:text-7xl lg:text-[5.5rem] mb-6 font-semibold text-white"', 'class="text-5xl md:text-7xl lg:text-[5.5rem] mb-6 font-semibold bg-gradient-to-b from-white to-white/60 bg-clip-text text-transparent"');

// h3 in the cards
html = html.replace(/class="text-xl mb-3 font-medium text-white pr-10"/g, 'class="text-xl mb-3 font-medium bg-gradient-to-b from-white to-white/70 bg-clip-text text-transparent pr-10"');

// text-3xl inside templates
html = html.replace(/class="text-3xl font-semibold text-white mb-6"/g, 'class="text-3xl font-semibold bg-gradient-to-b from-white to-white/60 bg-clip-text text-transparent mb-6"');

// big text R$ 3.000
html = html.replace(/class="text-3xl font-semibold text-white tracking-tighter"/g, 'class="text-3xl font-semibold bg-gradient-to-b from-white to-white/60 bg-clip-text text-transparent tracking-tighter"');

fs.writeFileSync('proposta-presencial.html', html);
console.log('Tweak done');
