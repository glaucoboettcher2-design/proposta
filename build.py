import re

# Read the HTML template
with open("index.html", "r", encoding="utf-8") as f:
    index = f.read()

head_match = re.search(r'(?s)(<html.*?</head>)', index)
head = head_match.group(1) if head_match else '<html lang="pt-BR"><head></head>'

extra_style = """
<style>
    html { scroll-snap-type: y mandatory; overflow-y: scroll; scroll-behavior: smooth; }
    .slide-wrapper { min-height: 100vh; width: 100%; display: flex; align-items: center; justify-content: center; scroll-snap-align: start; padding: 2rem 0; }
    @media (max-width: 1024px) { .slide-wrapper { padding: 0; } }
    .custom-gradient-text { background: linear-gradient(90deg, #9ca3af, #d1d5db); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    /* Custom Scrollbar for inner scrolling areas */
    .overflow-y-auto::-webkit-scrollbar { width: 6px; }
    .overflow-y-auto::-webkit-scrollbar-track { background: transparent; }
    .overflow-y-auto::-webkit-scrollbar-thumb { background: #d4d4d8; border-radius: 4px; }
    .overflow-y-auto:hover::-webkit-scrollbar-thumb { background: #a1a1aa; }
</style>
"""
head = head.replace('</head>', extra_style + '</head>')

# HTML pieces
html_start = head + '\n<body class="block w-full min-h-screen bg-center selection:bg-slate-900 selection:text-white text-slate-800 bg-zinc-500 bg-cover p-0 m-0 relative">\n'
html_end = '\n</body>\n</html>'

def make_slide(content, bg_class="bg-white/40 border border-zinc-200/50"):
    header = """
            <header class="flex md:mb-12 z-10 mb-6 relative gap-x-6 gap-y-6 items-center justify-between shrink-0">
                <div class="flex items-center gap-2 text-zinc-900">
                    <div class="flex text-white bg-gradient-to-b from-black/60 to-black/20 w-8 h-8 rounded-full items-center justify-center" style="position: relative; --border-gradient: linear-gradient(180deg, rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1)); --border-radius-before: 9999px">
                        <svg aria-hidden="true" class="w-[16px] h-[16px]" fill="none" height="16" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="0.5" style="width: 16px; height: 16px; color: rgb(255, 255, 255)" viewBox="0 0 24 24" width="16" xmlns="http://www.w3.org/2000/svg">
                            <path d="M3.464 20.536C4.93 22 7.286 22 12 22s7.071 0 8.535-1.465C22 19.072 22 16.714 22 12s0-7.071-1.465-8.536C19.072 2 16.714 2 12 2S4.929 2 3.464 3.464C2 4.93 2 7.286 2 12s0 7.071 1.464 8.535" fill="#ffffff" opacity=".5"></path>
                            <path d="M9.5 8.75A3.25 3.25 0 1 0 12.75 12a.75.75 0 0 1 1.5 0A4.75 4.75 0 1 1 9.5 7.25a.75.75 0 0 1 0 1.5" fill="#ffffff"></path>
                            <path d="M17.75 12a3.25 3.25 0 0 1-3.25 3.25a.75.75 0 0 0 0 1.5A4.75 4.75 0 1 0 9.75 12a.75.75 0 0 0 1.5 0a3.25 3.25 0 0 1 6.5 0" fill="#ffffff"></path>
                        </svg>
                    </div>
                    <span class="text-lg font-medium tracking-tight">SEBRAE<span class="text-zinc-400">PROPOSTA</span></span>
                </div>
                <nav class="hidden md:flex uppercase text-xs font-medium text-zinc-500 tracking-widest bg-white/50 border-white/60 border rounded-full pt-2 pr-6 pb-2 pl-6 shadow-[0px_2px_3px_-1px_rgba(0,0,0,0.1),0px_1px_0px_0px_rgba(25,28,33,0.02),0px_0px_0px_1px_rgba(25,28,33,0.08)] backdrop-blur-sm gap-x-8 gap-y-8 items-center">
                    <span class="hover:text-zinc-900 transition-colors duration-300">Confidencial</span>
                </nav>
            </header>
    """
    
    return f"""
    <div class="slide-wrapper">
        <main class="glass-panel overflow-hidden flex flex-col xl:max-w-[1300px] z-10 xl:border-white/50 border-none xl:border xl:rounded-[2.5rem] md:pt-10 md:pr-10 md:pb-10 md:pl-10 xl:pt-12 xl:pr-12 xl:pb-12 xl:pl-12 xl:shadow-2xl min-h-screen xl:min-h-[700px] w-full rounded-none pt-6 pr-6 pb-6 pl-6 relative shadow-none mx-auto snap-center">
            <div class="absolute inset-0 flex justify-between pointer-events-none z-0 px-6 md:px-10 xl:px-12 w-full h-full">
                <div class="h-full w-[1px] bg-zinc-950/5"></div>
                <div class="h-full w-[1px] bg-zinc-950/5 hidden md:block"></div>
                <div class="h-full w-[1px] bg-zinc-950/5 hidden lg:block"></div>
                <div class="h-full w-[1px] bg-zinc-950/5 hidden xl:block"></div>
                <div class="h-full w-[1px] bg-zinc-950/5"></div>
            </div>
            {header}
            <div class="flex-grow flex flex-col relative z-10 w-full overflow-hidden">
                {content}
            </div>
        </main>
    </div>
    """

slides = []

# Slide 1: Capa
slides.append(make_slide("""
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-20 h-full flex-grow relative z-10 items-center overflow-y-auto pr-2 pb-8">
        <div class="lg:col-span-7 flex flex-col relative justify-center">
            <div class="inline-flex bg-white/60 w-max rounded-full mb-8 pt-1.5 pr-5 pb-1.5 pl-1.5 shadow-sm backdrop-blur-sm items-center" style="position: relative; --border-gradient: linear-gradient(180deg, rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0)); --border-radius-before: 9999px">
                <span class="text-xs font-medium text-zinc-600 tracking-wide ml-3">
                    <span class="text-zinc-900 uppercase font-bold">Apresentação Estratégica</span>
                </span>
            </div>
            <h1 class="leading-[0.95] lg:text-[4rem] text-4xl font-medium text-zinc-900 tracking-tighter mb-8">
                Estrutura de aquisição e vendas para o credenciamento Sebrae
            </h1>
            <p class="text-base text-zinc-500 font-medium max-w-xl mb-10 leading-relaxed tracking-wide border-l-2 border-zinc-200 pl-6">
                Proposta de estruturação completa do funil, da atração de interessados à gestão contínua da operação.
            </p>
        </div>
        <div class="lg:col-span-5 relative flex items-center justify-center">
            <img src="assets/30104e3c-5eea-4b93-93e9-531369_da6550c805a8.webp" class="w-full object-cover rounded-[2rem] shadow-[0_20px_50px_rgba(0,0,0,0.1)] rotate-2 hover:rotate-0 transition-transform duration-500" />
        </div>
    </div>
"""))

# Slide 2: Como o sistema funciona
slides.append(make_slide("""
    <div class="flex flex-col justify-center items-center h-full max-w-5xl mx-auto text-center px-4 overflow-y-auto pb-8">
        <h1 class="leading-[0.95] lg:text-[4rem] text-4xl font-medium text-zinc-900 tracking-tighter mb-10">
            Como o sistema funciona
        </h1>
        <p class="text-lg text-zinc-600 font-medium mb-12 leading-relaxed tracking-wide text-center">
            A estrutura acompanha o interessado do primeiro contato com o anúncio até o pós-fechamento. Cada etapa alimenta a seguinte com dados, e a campanha é otimizada continuamente com base em quem avança no processo comercial. O trabalho está organizado em 6 etapas: Atração, Conversão, Inteligência de Dados, Atendimento e Vendas, Pós-venda e Gestão Contínua.
        </p>
    </div>
"""))

# Content mapping for stages
stages = [
    {
        "title": "Atração",
        "subtitle": "Colocar a oferta na frente das pessoas certas.",
        "desc": "Campanhas de tráfego pago estruturadas no Meta Ads, com definição de públicos, otimização contínua e criativos desenvolvidos para o perfil de quem busca atuar como consultor.",
        "deliverables": [
            ("Estratégia de aquisição e gestão de tráfego pago.", "Definição de públicos, estrutura de campanha, objetivo de otimização por evento de conversão e orçamento diário ajustado ao investimento definido."),
            ("Criativos estáticos, com variações para teste.", "Peças gráficas para os anúncios, desenvolvidas em mais de uma versão para permitir comparação de performance."),
            ("Criativos em vídeo, com roteirização e direção criativa.", "Vídeos usados nos anúncios, aproveitando o mesmo dia de captação da mini aula para otimizar custo e tempo de produção."),
            ("Linha editorial com cerca de 10 conteúdos orgânicos.", "Estruturada para sustentar a autoridade do sócio à frente do conteúdo, aquecendo a audiência antes de ela chegar à oferta.")
        ]
    },
    {
        "title": "Conversão",
        "subtitle": "Transformar cliques em conversas qualificadas.",
        "desc": "O interessado chega a uma página com uma mini aula gratuita sobre o credenciamento. Antes de assistir, passa por uma qualificação rápida. Ao final, é direcionado ao WhatsApp já entendendo o que está contratando. Isso eleva a qualidade das conversas e reduz o tempo gasto com contatos sem perfil.",
        "deliverables": [
            ("Landing page principal com VSL.", "Copy, design e construção da página que recebe o tráfego, incluindo a transição direta para o WhatsApp ao final da mini aula."),
            ("Estruturação completa do roteiro da mini aula.", "Desenvolvimento de começo, meio e fim, pensado para gerar consciência sobre o processo de credenciamento antes da conversa comercial começar."),
            ("Mecanismo de qualificação anterior ao acesso à aula.", "Perguntas respondidas antes da mini aula, funcionando como filtro de perfil e como fonte de dado sobre quem está chegando."),
            ("Variações de funil para teste.", "Ao menos uma estrutura alternativa de captação, testada em paralelo à VSL para validar o caminho mais eficiente com dados reais, sem depender de uma única hipótese.")
        ]
    },
    {
        "title": "Inteligência de dados",
        "subtitle": "A campanha aprende com quem compra.",
        "desc": "Toda a estrutura é rastreada com Pixel e API de Conversão server-side, que envia os eventos diretamente do servidor para a plataforma de anúncios. Conforme o lead avança no processo comercial, cada marco (qualificação, reunião, venda) retorna como sinal para a campanha. Com o tempo, o sistema passa a buscar pessoas cada vez mais parecidas com quem fecha contrato.",
        "deliverables": [
            ("Implementação de Pixel e API de Conversão em toda a estrutura do funil.", "Elevando a precisão do rastreamento além do que o pixel de navegador sozinho consegue captar hoje."),
            ("Conexão da API de Conversão às etapas do CRM.", "Cada avanço do lead no processo comercial dispara um sinal de volta para a campanha, ensinando o algoritmo a buscar pessoas parecidas com quem realmente compra."),
            ("Análise de comportamento na página e de retenção da mini aula.", "Leitura de onde o interessado avança ou abandona, tornando os testes de funil e criativo interpretáveis com base em dado real.")
        ]
    },
    {
        "title": "Atendimento e vendas",
        "subtitle": "Organização completa do processo comercial.",
        "desc": "Os leads chegam ao WhatsApp e são organizados em um CRM com pipeline desenhado para o processo da equipe. Cada lead tem responsável definido, etapa clara e cadência de acompanhamento, garantindo que nenhuma oportunidade se perca por falta de follow-up.",
        "deliverables": [
            ("Implementação e estruturação do CRM com pipeline comercial.", "Desenhado especificamente para o processo da equipe, com os leads organizados por responsável e etapa."),
            ("Apoio consultivo na elaboração dos scripts de atendimento.", "Contribuição na abordagem inicial, condução até a reunião e tratamento de objeções, respeitando o domínio que a equipe já tem do próprio serviço."),
            ("Estruturação do processo comercial, com cadências de follow-up e fluxo de acompanhamento.", "Endereçando diretamente o ponto onde historicamente mais se perde venda: a condução, não a geração do lead.")
        ]
    },
    {
        "title": "Pós-venda e recorrência",
        "subtitle": "Cada cliente pode trazer o próximo.",
        "desc": "Quem se credencia conhece outros profissionais no mesmo caminho. Um programa de indicação estruturado transforma clientes atendidos em fonte de novos interessados. Em paralelo, a base de contatos já existente, formada por pessoas que demonstraram interesse e não fecharam, recebe uma estratégia dedicada de reativação.",
        "deliverables": [
            ("Programa de indicação estruturado.", "Mecanismo de incentivo para que clientes já credenciados indiquem outros profissionais interessados no mesmo caminho."),
            ("Estratégia de reativação da base existente.", "Resgate dos contatos que já demonstraram interesse no funil anterior e não fecharam, um dos caminhos de retorno mais rápido da operação, por já serem leads qualificados.")
        ]
    },
    {
        "title": "Gestão contínua",
        "subtitle": "A operação evolui todo mês.",
        "desc": "Depois de estruturado, o sistema entra em regime de otimização permanente: análise de métricas, troca de criativos, testes de funil e leitura estratégica dos resultados, com o objetivo de reduzir o custo por cliente e aumentar a previsibilidade.",
        "deliverables": [
            ("Gestão e otimização das campanhas.", "Acompanhamento de métricas e ajustes de público e orçamento ao longo do tempo."),
            ("Testes estruturados de funil e criativo.", "Validação contínua de novas variações, mantendo a operação em evolução ativa, não em manutenção passiva."),
            ("Acompanhamento do funil comercial e da qualidade dos dados.", "Verificação de que o pipeline está atualizado e que os eventos que alimentam a otimização da campanha continuam confiáveis."),
            ("Leitura estratégica periódica.", "Consolidação do que os dados mostram e definição de rota para os meses seguintes.")
        ]
    }
]

for idx, stage in enumerate(stages):
    items_html = ""
    for bold_part, text_part in stage['deliverables']:
        items_html += f"""
        <div class="bg-white/60 p-6 rounded-2xl border border-zinc-100 shadow-sm flex flex-col gap-2 hover:shadow-md transition-all">
            <strong class="text-zinc-900 text-lg leading-tight">{bold_part}</strong>
            <p class="text-base text-zinc-600 leading-relaxed">{text_part}</p>
        </div>
        """
    
    slides.append(make_slide(f"""
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-16 h-full w-full">
            <div class="lg:col-span-5 flex flex-col justify-center overflow-y-auto pb-8 pr-4">
                <div class="text-6xl font-black text-zinc-200 mb-4">{idx + 1}</div>
                <h2 class="text-4xl font-medium text-zinc-900 mb-6">{stage['title']}</h2>
                <h3 class="text-2xl text-zinc-800 font-medium mb-6 leading-tight">{stage['subtitle']}</h3>
                <p class="text-zinc-600 text-lg leading-relaxed border-l-2 border-zinc-300 pl-4">
                    {stage['desc']}
                </p>
            </div>
            <div class="lg:col-span-7 flex flex-col bg-zinc-50/50 rounded-3xl p-6 lg:p-8 h-full border border-zinc-200/50">
                <h4 class="text-sm font-bold uppercase text-zinc-400 mb-6 tracking-widest shrink-0">Entregáveis</h4>
                <div class="space-y-4 overflow-y-auto pr-4 h-full flex-grow">
                    {items_html}
                </div>
            </div>
        </div>
    """))

# Tudo que será construído
slides.append(make_slide("""
    <div class="flex flex-col justify-center items-center h-full max-w-4xl mx-auto text-center px-4 overflow-y-auto pb-8">
        <h1 class="leading-[0.95] lg:text-[4rem] text-4xl font-medium text-zinc-900 tracking-tighter mb-10">
            Tudo que será construído
        </h1>
        <p class="text-2xl text-zinc-600 font-medium mb-12 leading-relaxed tracking-wide text-center">
            São 20 frentes de trabalho distribuídas em 6 etapas da jornada, cobrindo da primeira impressão no anúncio ao programa de indicação após o fechamento.
        </p>
    </div>
"""))

# Investimento
slides.append(make_slide("""
    <div class="flex flex-col relative justify-center h-full overflow-y-auto pb-8 w-full">
        <h1 class="leading-[0.95] lg:text-[4rem] text-4xl font-medium text-zinc-900 tracking-tighter mb-12 text-center shrink-0">
            Investimento
        </h1>
        
        <p class="text-center text-zinc-600 mb-12 max-w-2xl mx-auto text-lg shrink-0">
            O investimento é dividido em duas fases: a estruturação inicial, onde todo o sistema é construído, e a operação contínua, onde ele é gerido e otimizado.
        </p>
        
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <div class="bg-white/60 border border-zinc-200/50 rounded-3xl p-8 flex flex-col shadow-sm relative overflow-hidden">
                <div class="absolute top-0 left-0 w-full h-1 bg-zinc-200"></div>
                <div class="mb-4 mt-2">
                    <span class="px-3 py-1 bg-zinc-900 text-white text-[10px] font-bold uppercase tracking-widest rounded-full">Fase 1</span>
                </div>
                <h3 class="text-2xl font-bold text-zinc-900 mb-2">Estruturação inicial</h3>
                <p class="text-sm text-zinc-600 mb-6 flex-grow">Pagamento único, referente à construção de toda a estrutura: páginas, VSL, funil, rastreamento, CRM, processo comercial e campanhas.</p>
                <div class="text-4xl font-medium tracking-tighter text-zinc-900 mb-4">R$ 3.000</div>
            </div>

            <div class="bg-zinc-900 border border-zinc-800 rounded-3xl p-8 flex flex-col shadow-2xl relative overflow-hidden lg:-translate-y-4">
                <div class="absolute top-0 left-0 w-full h-1 bg-zinc-500"></div>
                <div class="mb-4 mt-2">
                    <span class="px-3 py-1 bg-zinc-100 text-zinc-900 text-[10px] font-bold uppercase tracking-widest rounded-full">Operação contínua • Formato 1</span>
                </div>
                <h3 class="text-2xl font-bold text-white mb-2">Fixo</h3>
                <p class="text-sm text-zinc-400 mb-6 flex-grow">Gestão completa da operação com valor previsível.</p>
                <div class="text-4xl font-medium tracking-tighter text-white mb-4">R$ 2.000<span class="text-base text-zinc-500 font-normal"> /mês</span></div>
            </div>

            <div class="bg-white/60 border border-zinc-200/50 rounded-3xl p-8 flex flex-col shadow-sm relative overflow-hidden">
                <div class="absolute top-0 left-0 w-full h-1 bg-zinc-200"></div>
                <div class="mb-4 mt-2">
                    <span class="px-3 py-1 bg-zinc-200 text-zinc-700 text-[10px] font-bold uppercase tracking-widest rounded-full">Operação contínua • Formato 2</span>
                </div>
                <h3 class="text-2xl font-bold text-zinc-900 mb-2">Fixo reduzido com participação</h3>
                <p class="text-sm text-zinc-600 mb-6 flex-grow">O valor mensal diminui e parte da remuneração passa a depender diretamente das vendas realizadas.</p>
                <div class="mb-4">
                    <div class="text-4xl font-medium tracking-tighter text-zinc-900 mb-1">R$ 1.000<span class="text-base text-zinc-400 font-normal"> /mês</span></div>
                    <div class="text-base font-bold text-zinc-600 mt-2">+ 8% sobre cada contrato fechado</div>
                </div>
            </div>
        </div>
    </div>
"""))

# Custos operacionais
slides.append(make_slide("""
    <div class="flex flex-col justify-center h-full w-full overflow-y-auto pb-8">
        <h2 class="text-4xl font-medium text-zinc-900 tracking-tighter mb-6 shrink-0">Custos operacionais</h2>
        <p class="text-lg text-zinc-600 mb-10 shrink-0 max-w-4xl">
            Além do serviço, a operação possui custos próprios de ferramentas e mídia, pagos diretamente pela empresa aos fornecedores. Eles estão mapeados desde já para que o investimento total seja transparente.
        </p>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 w-full">
            <div class="bg-white/60 p-6 rounded-2xl border border-zinc-100 shadow-sm flex flex-col gap-2">
                <strong class="text-zinc-900 text-lg">Verba de mídia: R$ 1.000 a R$ 1.500 por mês</strong>
                <p class="text-base text-zinc-600">Investidos diretamente na plataforma de anúncios.</p>
            </div>
            
            <div class="bg-white/60 p-6 rounded-2xl border border-zinc-100 shadow-sm flex flex-col gap-2">
                <strong class="text-zinc-900 text-lg">Plataforma de CRM: estimado em R$ 500 por trimestre</strong>
                <p class="text-base text-zinc-600">Na versão necessária para suportar a API de Conversão.</p>
            </div>
            
            <div class="bg-white/60 p-6 rounded-2xl border border-zinc-100 shadow-sm flex flex-col gap-2">
                <strong class="text-zinc-900 text-lg">Produção audiovisual: estimado entre R$ 800 e R$ 1.000 na produção inicial</strong>
                <p class="text-base text-zinc-600">Referente à captação e edição da mini aula e dos criativos em vídeo.</p>
            </div>
            
            <div class="bg-white/60 p-6 rounded-2xl border border-zinc-100 shadow-sm flex flex-col gap-2">
                <strong class="text-zinc-900 text-lg">Mensageria no WhatsApp</strong>
                <p class="text-base text-zinc-600">Sem custo no atendimento manual. Caso a equipe opte por automações dentro do CRM, como lembretes de reunião e réguas de contato, passa a existir um custo por mensagem enviada, a partir de poucos centavos por mensagem, dimensionado conforme a estratégia adotada.</p>
            </div>
        </div>
    </div>
"""))

# Como começamos & Próximo passo
slides.append(make_slide("""
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-20 h-full w-full overflow-y-auto pb-8">
        
        <div class="bg-white/40 border border-zinc-200/50 rounded-3xl p-10 flex flex-col justify-center shadow-sm">
            <h2 class="text-4xl font-medium text-zinc-900 tracking-tighter mb-6">Como começamos</h2>
            <p class="text-lg text-zinc-700 leading-relaxed">
                Aprovada a proposta, a estruturação inicial segue esta sequência: alinhamento estratégico e coleta de informações, produção da mini aula e dos criativos, construção das páginas e do rastreamento, implementação do CRM e do processo comercial, e lançamento das campanhas. 
                <br/><br/>
                A partir daí, a operação entra em gestão contínua, com um ponto de revisão conjunto entre 60 e 90 dias para ajustar rotas com base nos primeiros dados reais.
            </p>
        </div>

        <div class="bg-gradient-to-b from-zinc-900 to-zinc-800 border border-zinc-700 rounded-3xl p-10 flex flex-col justify-center text-center relative overflow-hidden shadow-2xl">
            <div class="absolute inset-0 bg-[url('assets/a5387a0b-52c6-40c2-b3be-ef8632_5ea829d0de5b.webp')] bg-cover opacity-10"></div>
            <div class="relative z-10">
                <h2 class="text-5xl font-medium text-white tracking-tighter mb-8">Próximo passo</h2>
                <p class="text-zinc-400 mb-12 text-lg max-w-md mx-auto leading-relaxed">
                    Com a aprovação da proposta, agendamos o alinhamento inicial e damos início à estruturação.
                </p>
                <div class="inline-block hover:bg-white/90 transition-all text-base font-medium text-zinc-900 bg-white rounded-full pt-5 pr-10 pb-5 pl-10 shadow-xl cursor-pointer shadow-white/10">
                    Aprovar Proposta
                </div>
            </div>
        </div>
        
    </div>
"""))

with open("proposta-presencial.html", "w", encoding="utf-8") as out_file:
    out_file.write(html_start)
    for slide in slides:
        out_file.write(slide)
    out_file.write(html_end)
