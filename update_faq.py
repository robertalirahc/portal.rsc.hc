from bs4 import BeautifulSoup
from pathlib import Path
import shutil, re, zipfile
root=Path('/mnt/data/faq_work')

FAQ_URL='https://drive.google.com/file/d/1VhdOGoJmjpVEaIsg-2QTxiIRKxzlasTm/view?usp=sharing'
MANUAL_URL='https://drive.google.com/file/d/1psn-NYYbdoyS_3LPmlGGJ00HbqApXJS_/view?usp=sharing'
DEC_URL='https://robertalirahc.github.io/portal.rsc.hc/assets/decreto-13048-2026.pdf'
PORT_URL='https://www.ufpe.br/documents/38962/7361421/PORTARIA+NORMATIVA+N%C2%BA+24%2C+DE+20+DE+JULHO+DE+2026+-+RSC+NA+UFPE.pdf/ecd74214-c5be-46f5-be5f-151c6a9ea8fe'
LOC_URL='https://robertalirahc.github.io/portal.rsc.hc/documentos/manual-localizacao-documentos.pdf'
SOUGOV_URL='https://robertalirahc.github.io/portal.rsc.hc/documentos/oficio-progepe-30-2026.pdf'
PROAD_URL='https://robertalirahc.github.io/portal.rsc.hc/documentos/oficio-proad-2-2026.pdf'
GED_URL='https://robertalirahc.github.io/portal.rsc.hc/documentos/oficio-hc-documentos-institucionais-44-2026.pdf'

cats=[
('elegibilidade','👤','Antes de começar: posso solicitar o RSC?',[
('O que é o RSC-PCCTAE?','O Reconhecimento de Saberes e Competências — RSC é um mecanismo de reconhecimento dos conhecimentos e habilidades desenvolvidos pelo servidor ao longo de sua trajetória profissional, observados os requisitos e critérios estabelecidos na legislação.',[(FAQ_URL,'FAQ oficial da UFPE'),(DEC_URL,'Decreto nº 13.048/2026')]),
('Quem pode solicitar o RSC?','Servidores ativos e efetivos do Plano de Carreira dos Cargos Técnico-Administrativos em Educação — PCCTAE.',[(FAQ_URL,'FAQ oficial da UFPE'),(MANUAL_URL,'Manual do RSC-PCCTAE — PROGEPE')]),
('Servidor em estágio probatório pode solicitar o RSC?','Não. O RSC-PCCTAE não se aplica ao servidor em estágio probatório. Entretanto, atividades realizadas durante esse período poderão ser consideradas futuramente, desde que tenham ocorrido no exercício de cargo integrante do PCCTAE e atendam aos requisitos do RSC.',[(FAQ_URL,'FAQ oficial da UFPE'),(MANUAL_URL,'Manual do RSC-PCCTAE — PROGEPE')]),
('Posso utilizar atividades realizadas antes de ingressar na UFPE?','Sim, desde que tenham sido desenvolvidas no exercício de cargos integrantes da carreira do PCCTAE e atendam aos demais requisitos da regulamentação.',[(FAQ_URL,'FAQ oficial da UFPE')]),
('Posso utilizar atividades realizadas em outra instituição?','Sim. A atividade não precisa ter sido realizada na UFPE, mas deve ter ocorrido no exercício de cargo integrante do PCCTAE, estar enquadrada nos critérios e ser devidamente comprovada.',[(FAQ_URL,'FAQ oficial da UFPE')]),
('Mudei de cargo dentro do PCCTAE. Posso utilizar atividades realizadas no cargo anterior?','Sim, porque foram atividades realizadas no exercício de cargos integrantes da carreira do PCCTAE.',[(FAQ_URL,'FAQ oficial da UFPE')]),
]),
('aposentadoria','🕒','Aposentadoria e situações funcionais',[
('Servidor aposentado pode solicitar o RSC?','Não pela via administrativa atualmente prevista. O RSC-PCCTAE é destinado a servidores ativos. Em situações específicas, confirme a orientação com a PROGEPE.',[]),
('O RSC será incorporado automaticamente à aposentadoria?','Não há uma resposta única. A repercussão do Incentivo à Qualificação decorrente do RSC depende da regra previdenciária aplicável ao servidor e deve ser analisada pelos setores competentes.',[]),
('Servidor cedido, requisitado ou movimentado pode solicitar?','Sim, desde que seja servidor ativo, permanente, em efetivo exercício e integrante do PCCTAE. O Manual inclui servidores requisitados, movimentados para composição da força de trabalho e cedidos.',[(MANUAL_URL,'Manual do RSC-PCCTAE — PROGEPE')]),
]),
('atividades','🧭','O que posso utilizar?',[
('Que tipos de atividades podem ser apresentadas para fins de RSC?','Devem ser observadas as atividades, experiências e requisitos previstos nos Anexos do Decreto nº 13.048/2026. O servidor deverá verificar em qual critério suas experiências podem ser enquadradas.',[(FAQ_URL,'FAQ oficial da UFPE'),(DEC_URL,'Decreto nº 13.048/2026')]),
('Atividades desenvolvidas fora da UFPE podem pontuar?','Sim, desde que atendam aos requisitos do RSC, tenham sido realizadas no exercício de cargo integrante da carreira do PCCTAE e sejam devidamente comprovadas.',[(FAQ_URL,'FAQ oficial da UFPE')]),
('Cursos realizados antes do ingresso na UFPE podem ser utilizados?','Sim, desde que tenham sido realizados no exercício de cargo integrante da carreira do PCCTAE e atendam aos demais requisitos previstos para o RSC.',[(FAQ_URL,'FAQ oficial da UFPE')]),
('Cursos realizados fora da UFPE podem ser utilizados?','Sim. Poderão ser considerados cursos de interesse institucional realizados no exercício do PCCTAE, desde que sejam devidamente comprovados, atendam à regulamentação, não tenham sido utilizados para outra concessão e sejam apresentados e fundamentados no Memorial.',[(FAQ_URL,'FAQ oficial da UFPE')]),
('Cursos EAD são aceitos?','Sim, desde que atendam aos requisitos estabelecidos na regulamentação e sejam devidamente comprovados.',[(FAQ_URL,'FAQ oficial da UFPE')]),
('Congressos, eventos, palestras e treinamentos internos podem ser considerados?','Sim, desde que a atividade esteja contemplada nos critérios dos Anexos e seja comprovada mediante documentação admitida pelo art. 4º do Decreto nº 13.048/2026.',[(FAQ_URL,'FAQ oficial da UFPE'),(DEC_URL,'Decreto nº 13.048/2026')]),
('Qual é a carga horária mínima para cursos?','A carga horária mínima indicada é de 10 horas, observados os critérios específicos previstos nos Anexos.',[(FAQ_URL,'FAQ oficial da UFPE'),(DEC_URL,'Decreto nº 13.048/2026')]),
('O que é considerado curso de interesse institucional?','É o curso ou ação de capacitação que contribui para o desenvolvimento de competências relacionadas à atuação profissional do servidor, às atividades desenvolvidas no âmbito do PCCTAE, às necessidades da unidade de exercício ou aos objetivos e finalidades institucionais da UFPE. O interesse institucional não se limita às atribuições específicas do cargo.',[(FAQ_URL,'FAQ oficial da UFPE')]),
('Posso utilizar curso ou atividade que já foi utilizado para outra concessão funcional?','Deve ser observada a vedação quanto à utilização de título, certificado ou atividade já empregado para outra concessão. Antes de incluir o documento no Memorial, verifique se existe impedimento para sua reutilização.',[(FAQ_URL,'FAQ oficial da UFPE'),(DEC_URL,'Decreto nº 13.048/2026')]),
]),
('pontuacao','⭐','Como funciona a pontuação?',[
('Como é calculada a pontuação do RSC?','A pontuação é atribuída conforme os critérios, valores e condições estabelecidos nos Anexos do Decreto nº 13.048/2026. Antes de elaborar o Memorial, identifique a relação: atividade → critério → pontuação → condição aplicável.',[(FAQ_URL,'FAQ oficial da UFPE'),(DEC_URL,'Decreto nº 13.048/2026')]),
('Existe limite de pontuação por critério?','O FAQ oficial informa que não há limite geral por critério. Entretanto, é necessário observar a pontuação e a quantidade mínima de critérios específicos exigidos para cada nível, além das condições próprias dos níveis IV, V e VI.',[(FAQ_URL,'FAQ oficial da UFPE'),(DEC_URL,'Decreto nº 13.048/2026')]),
('O mesmo documento pode gerar pontuação em mais de um critério?','Não. Cada documento comprobatório deverá ser utilizado em apenas um critério, não podendo gerar pontuação simultaneamente em dois ou mais critérios.',[(FAQ_URL,'FAQ oficial da UFPE'),(DEC_URL,'Decreto nº 13.048/2026')]),
('Minha atividade pode ser enquadrada em mais de um critério. O que devo fazer?','Consulte os Anexos e identifique o critério que melhor corresponda à atividade. Quando houver mais de uma possibilidade, considere a pontuação correspondente e, respeitadas as regras aplicáveis, indique o enquadramento mais favorável.',[(FAQ_URL,'FAQ oficial da UFPE'),(DEC_URL,'Decreto nº 13.048/2026')]),
('Quem define o enquadramento da atividade?','O servidor indica e fundamenta no Memorial o enquadramento pretendido. A análise e a atribuição da pontuação competem à Comissão de Avaliação do RSC, conforme a documentação e os critérios da regulamentação.',[(FAQ_URL,'FAQ oficial da UFPE'),(PORT_URL,'Portaria Normativa UFPE nº 24/2026')]),
('Qual é a pontuação mínima para cada nível?','RSC I: 10 pontos; RSC II: 15 pontos e 2 critérios; RSC III: 25 pontos e 2 critérios; RSC IV: 30 pontos e 3 critérios; RSC V: 52 pontos e 5 critérios; RSC VI: 75 pontos e 7 critérios. Os níveis IV, V e VI também exigem critérios vinculados a requisitos específicos.',[(MANUAL_URL,'Manual do RSC-PCCTAE — PROGEPE'),(DEC_URL,'Decreto nº 13.048/2026')]),
('Os pontos não utilizados são perdidos?','Não. A pontuação reconhecida tem caráter cumulativo, e o saldo não aproveitado poderá ser utilizado em concessões futuras, observadas as regras aplicáveis.',[(MANUAL_URL,'Manual do RSC-PCCTAE — PROGEPE'),(DEC_URL,'Decreto nº 13.048/2026')]),
]),
('documentacao','📄','Como comprovar minhas atividades?',[
('Quais documentos podem ser utilizados?','Podem ser utilizados os documentos previstos no art. 4º do Decreto nº 13.048/2026, desde que exista correspondência entre o documento e a atividade declarada: portarias, atos de designação, diplomas, certificados, declarações, atas, relatórios, produções técnicas, manuais, projetos, termos de referência e outros documentos institucionais admitidos.',[(FAQ_URL,'FAQ oficial da UFPE'),(DEC_URL,'Decreto nº 13.048/2026'),(LOC_URL,'Manual de localização de documentos')]),
('Cursos e capacitações precisam ser comprovados?','Sim. A realização deverá ser demonstrada por certificado, declaração ou documento equivalente admitido pela regulamentação.',[(FAQ_URL,'FAQ oficial da UFPE'),(DEC_URL,'Decreto nº 13.048/2026')]),
('Portarias, atas, declarações e publicações podem servir como comprovação?','Sim, desde que permitam identificar adequadamente a atividade, o servidor e, quando necessário, o período de realização.',[(FAQ_URL,'FAQ oficial da UFPE'),(DEC_URL,'Decreto nº 13.048/2026'),(LOC_URL,'Manual de localização de documentos')]),
('Como comprovar a autoria de manual, protocolo, parecer, cartilha ou produto técnico?','A autoria poderá ser demonstrada pela própria publicação ou por documentação que identifique de forma inequívoca a participação do servidor na elaboração do produto.',[(FAQ_URL,'FAQ oficial da UFPE'),(DEC_URL,'Decreto nº 13.048/2026')]),
('Como comprovar participação em POPs, manuais, planos, protocolos e outros documentos institucionais do HC-UFPE?','Apresente preferencialmente a versão oficial e não editável publicada no GED, contendo a identificação da sua participação e a assinatura eletrônica de validação do Setor da Qualidade.',[(GED_URL,'Ofício-Circular SEI nº 44/2026 — HC-UFPE'),('documentos/tutorial-ged.jpeg','Tutorial de pesquisa no GED')]),
('Documentos emitidos por outras instituições são aceitos?','Sim, desde que correspondam a atividades ou experiências passíveis de aproveitamento para o RSC e atendam aos requisitos de comprovação previstos na regulamentação.',[(FAQ_URL,'FAQ oficial da UFPE')]),
('Preciso apresentar todos os documentos da minha carreira no PCCTAE?','Não. Apresente os documentos necessários para comprovar as atividades que efetivamente indicar no Memorial para fins de pontuação.',[(FAQ_URL,'FAQ oficial da UFPE')]),
('Como obter declarações funcionais?','O SOUGOV.BR permite emitir automaticamente declarações de dados funcionais, tempo de serviço, jornada, lotação, tempo averbado e cargos e funções, entre outras.',[(SOUGOV_URL,'Ofício-Circular PROGEPE nº 30/2026')]),
('Como obter declaração de atuação como gestor ou fiscal de contrato?','Solicite a declaração ao Ordenador de Despesas do respectivo contrato. Apresente as portarias de designação e informe o período de atuação. A declaração somente poderá abranger o período formalmente respaldado pelas portarias.',[(PROAD_URL,'Ofício-Circular PROAD nº 2/2026')]),
]),
('memorial','✍️','Como elaborar o Memorial?',[
('O que é o Memorial?','É o documento no qual o servidor apresenta as atividades e experiências que pretende utilizar para o RSC, indicando seu enquadramento nos critérios e a respectiva documentação comprobatória.',[(FAQ_URL,'FAQ oficial da UFPE'),(MANUAL_URL,'Manual do RSC-PCCTAE — PROGEPE')]),
('Como elaborar o Memorial?','A UFPE disponibiliza o Assistente RSC-PCCTAE para auxiliar na elaboração e organização das informações que integrarão o Memorial.',[(FAQ_URL,'FAQ oficial da UFPE'),('https://rsc.ufpe.br','Assistente RSC-PCCTAE')]),
('Basta relacionar meus documentos no Memorial?','Não. O Memorial deve apresentar e fundamentar sua trajetória, demonstrando a relação entre a atividade desenvolvida, o critério escolhido e o documento que a comprova.',[(FAQ_URL,'FAQ oficial da UFPE'),(MANUAL_URL,'Manual do RSC-PCCTAE — PROGEPE')]),
('Preciso indicar o critério correspondente a cada atividade?','Sim. Recomenda-se estabelecer uma relação clara entre atividade realizada, critério escolhido e documento comprobatório.',[(FAQ_URL,'FAQ oficial da UFPE')]),
('Como justificar uma atividade no Memorial?','A justificativa deve ser objetiva e demonstrar a correspondência entre a experiência apresentada e o critério escolhido, identificando atividade, período, critério e documento comprobatório.',[(FAQ_URL,'FAQ oficial da UFPE')]),
('Existe modelo de Memorial?','O Assistente RSC-PCCTAE possui espaço destinado à produção do Memorial e organiza as informações inseridas pelo servidor.',[(FAQ_URL,'FAQ oficial da UFPE'),('https://rsc.ufpe.br','Assistente RSC-PCCTAE')]),
]),
('processo','📁','Como protocolar o pedido?',[
('Quando posso solicitar o RSC na UFPE?','A abertura dos processos na UFPE começou em 3 de agosto de 2026.',[(FAQ_URL,'FAQ oficial da UFPE'),(MANUAL_URL,'Manual do RSC-PCCTAE — PROGEPE')]),
('Onde devo abrir o processo?','O processo deverá ser aberto no SIPAC, conforme o passo a passo estabelecido no Manual do RSC-PCCTAE e nas orientações institucionais.',[(FAQ_URL,'FAQ oficial da UFPE'),(MANUAL_URL,'Manual do RSC-PCCTAE — PROGEPE')]),
('Quais documentos devem integrar o processo?','O processo deve conter o Requerimento gerado pelo Assistente, o Memorial, o PDF único com os anexos comprobatórios e o comprovante da última titulação, além de outros documentos eventualmente exigidos.',[(MANUAL_URL,'Manual do RSC-PCCTAE — PROGEPE')]),
('Em que ordem devo reunir os anexos comprobatórios?','Os documentos devem ser reunidos em um único arquivo PDF, rigorosamente na ordem dos requisitos e critérios. No portal, siga exatamente a ordem disponibilizada pelo Assistente.',[(MANUAL_URL,'Manual do RSC-PCCTAE — PROGEPE')]),
]),
('avaliacao','✅','Como será feita a avaliação?',[
('Quem avaliará meu processo?','O processo será analisado pela Comissão de Reconhecimento de Saberes e Competências — CRSC-PCCTAE, constituída e organizada conforme a regulamentação da UFPE.',[(FAQ_URL,'FAQ oficial da UFPE'),(PORT_URL,'Portaria Normativa UFPE nº 24/2026')]),
('Qual é o prazo para análise?','A Comissão deverá realizar a análise no prazo máximo de até 120 dias, contados do protocolo do requerimento ou da data de complementação da documentação solicitada.',[(FAQ_URL,'FAQ oficial da UFPE'),(DEC_URL,'Decreto nº 13.048/2026')]),
('Se faltar algum documento, meu pedido será automaticamente indeferido?','O pedido será analisado com base na documentação apresentada. Se ela for insuficiente e o servidor não alcançar a pontuação mínima necessária, o pedido poderá ser indeferido. A Comissão também poderá solicitar documentação complementar.',[(FAQ_URL,'FAQ oficial da UFPE'),(MANUAL_URL,'Manual do RSC-PCCTAE — PROGEPE')]),
('Posso apresentar reconsideração contra o resultado?','Sim. O FAQ oficial informa prazo de 10 dias para solicitar reconsideração à Comissão.',[(FAQ_URL,'FAQ oficial da UFPE'),(PORT_URL,'Portaria Normativa UFPE nº 24/2026')]),
('Quando começam os efeitos financeiros?','Os efeitos financeiros incidem a partir da data do deferimento. Se a análise ultrapassar o prazo legal, aplicam-se as regras de retroação previstas no Decreto nº 13.048/2026.',[(MANUAL_URL,'Manual do RSC-PCCTAE — PROGEPE'),(DEC_URL,'Decreto nº 13.048/2026')]),
]),
]

def source_html(srcs):
    if not srcs: return '<p class="faq-source faq-source-note"><strong>Observação:</strong> orientação mantida a pedido da unidade; confirme a situação individual com a PROGEPE.</p>'
    links=' · '.join(f'<a href="{u}" target="_blank" rel="noopener noreferrer">{t} ↗</a>' for u,t in srcs)
    return f'<p class="faq-source"><strong>Referência:</strong> {links}</p>'

def build_inner(home=False):
    nav=''.join(f'<a href="#{id}"><span aria-hidden="true" class="faq-category-card-icon">{icon}</span><span class="faq-category-card-label">{title}</span></a>' for id,icon,title,_ in cats)
    out=f'<input aria-label="Pesquisar no FAQ" class="search" id="faq-search" placeholder="Pesquisar uma dúvida" type="search"/><div class="faq-revisao-banner" role="note"><div class="faq-nav-heading">Encontre sua dúvida por assunto</div><p>As respostas abaixo foram mantidas somente quando havia correspondência em documentos disponíveis na Biblioteca. Cada resposta apresenta sua referência.</p></div><nav aria-label="Categorias do FAQ" class="faq-categorias-grid">{nav}</nav>'
    for id,icon,title,items in cats:
        out += f'<h2 class="faq-category-title faq-anchor-target" id="{id}"><span aria-hidden="true" class="faq-category-icon">{icon}</span><span>{title}</span></h2><div class="faq">'
        for q,a,s in items:
            out += f'<details><summary>{q}</summary><div class="faq-answer"><p>{a}</p>{source_html(s)}</div></details>'
        out += '</div>'
    out += '<p hidden id="no-faq">Nenhuma pergunta encontrada.</p>'
    return out

# FAQ page
p=root/'faq.html'; soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
container=soup.select_one('main .section .container')
container.clear(); container.append(BeautifulSoup(build_inner(), 'html.parser'))
hero_p=soup.select_one('.page-hero p'); hero_p.string='Respostas verificadas nos documentos oficiais reunidos na Biblioteca do portal.'
# menu label
for a in soup.select('nav.nav a[href="faq.html"]'): a.string='Perguntas Frequentes'
# style source
style=soup.new_tag('style'); style.string='''.faq-source{margin-top:.8rem;padding-top:.65rem;border-top:1px solid rgba(0,0,0,.12);font-size:.9rem}.faq-source a{font-weight:700}.faq-source-note{background:#fff8e6;padding:.75rem;border-left:4px solid #d79b00}.faq-answer p:first-child{margin-top:0}'''
soup.head.append(style)
p.write_text(str(soup),encoding='utf-8')

# Homepage replace section content after section-head
p=root/'index.html'; soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
sec=soup.select_one('#faq-completo .container')
head=sec.select_one('.section-head')
sec.clear(); sec.append(head); sec.append(BeautifulSoup(build_inner(home=True),'html.parser'))
for a in soup.select('nav.nav a[href="faq.html"]'): a.string='Perguntas Frequentes'
style=soup.new_tag('style'); style.string='''.faq-source{margin-top:.8rem;padding-top:.65rem;border-top:1px solid rgba(0,0,0,.12);font-size:.9rem}.faq-source a{font-weight:700}.faq-source-note{background:#fff8e6;padding:.75rem;border-left:4px solid #d79b00}'''; soup.head.append(style)
p.write_text(str(soup),encoding='utf-8')

# Update menu labels all pages
for p in root.glob('*.html'):
    soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
    changed=False
    for a in soup.select('nav.nav a[href="faq.html"]'):
        if a.get_text(strip=True)!='Perguntas Frequentes': a.string='Perguntas Frequentes'; changed=True
    if changed: p.write_text(str(soup),encoding='utf-8')

# Add HC document to library and card
shutil.copy2('/mnt/data/SEI_SEDE - 63537638 - Ofício-Circular - SEI (1).pdf', root/'documentos/oficio-hc-documentos-institucionais-44-2026.pdf')
p=root/'biblioteca.html'; soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
# add card if missing
if not soup.find('a',href='documentos/oficio-hc-documentos-institucionais-44-2026.pdf'):
    sec=next((d for d in soup.select('.library-section') if 'Reúna seus documentos' in d.get_text()),None)
    grid=sec.select_one('.grid')
    card=BeautifulSoup('<a class="card" href="documentos/oficio-hc-documentos-institucionais-44-2026.pdf" rel="noopener noreferrer" target="_blank"><span class="tag">Ofício</span><h3>Documentos institucionais do HC-UFPE no GED</h3><p>Orientação para comprovar participação em POPs, manuais, planos, protocolos e outros documentos validados pelo Setor da Qualidade.</p></a>','html.parser')
    grid.append(card)
for a in soup.select('nav.nav a[href="faq.html"]'): a.string='Perguntas Frequentes'
p.write_text(str(soup),encoding='utf-8')

# Validate links/FAQ count
faq=BeautifulSoup((root/'faq.html').read_text(encoding='utf-8'),'html.parser')
print('FAQ questions',len(faq.select('details')),'sources',len(faq.select('.faq-source')))
# zip
out=Path('/mnt/data/portal-rsc-v12-faq-referenciado.zip')
if out.exists(): out.unlink()
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
    for f in root.rglob('*'):
        if f.is_file(): z.write(f,f.relative_to(root))
print(out, out.stat().st_size)
