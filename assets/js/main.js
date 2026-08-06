
const b=document.querySelector('.menu-btn'),n=document.querySelector('.nav');b?.addEventListener('click',()=>{n.classList.toggle('open');b.setAttribute('aria-expanded',n.classList.contains('open'))});
function setupSearch(inputSel,itemSel,emptySel){const i=document.querySelector(inputSel),items=[...document.querySelectorAll(itemSel)],e=document.querySelector(emptySel);if(!i)return;i.addEventListener('input',()=>{const q=i.value.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();let c=0;items.forEach(x=>{const t=(x.textContent+' '+(x.dataset.tags||'')).normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();const ok=!q||t.includes(q);x.classList.toggle('hidden',!ok);if(ok)c++});if(e)e.hidden=c>0})}
setupSearch('#doc-search','.search-item','#no-docs');setupSearch('#faq-search','.faq details','#no-faq');


// Controles dos carrosséis de etapas
 document.querySelectorAll('[data-carousel]').forEach(function(carousel){
   var track=carousel.querySelector('.process-carousel-track');
   var prev=carousel.querySelector('[data-carousel-prev]');
   var next=carousel.querySelector('[data-carousel-next]');
   if(!track) return;
   function step(){ var card=track.querySelector('.process-admin-card'); return card ? card.getBoundingClientRect().width + 16 : 280; }
   if(prev) prev.addEventListener('click',function(){ track.scrollBy({left:-step(),behavior:'smooth'}); });
   if(next) next.addEventListener('click',function(){ track.scrollBy({left:step(),behavior:'smooth'}); });
 });

// Entenda o RSC: abre e destaca o requisito selecionado no índice
(function(){
  const links=[...document.querySelectorAll('.requirement-index a[href^="#requisito-"]')];
  const requirements=[...document.querySelectorAll('.requirement-accordion[id^="requisito-"]')];
  if(!links.length || !requirements.length) return;

  function activate(hash, shouldScroll){
    const id=(hash||'').replace('#','');
    const target=document.getElementById(id);
    if(!target || !target.classList.contains('requirement-accordion')) return;

    requirements.forEach(item=>item.classList.toggle('is-target-highlight',item===target));
    links.forEach(link=>link.classList.toggle('is-active',link.getAttribute('href')==='#'+id));
    target.open=true;

    if(shouldScroll){
      requestAnimationFrame(()=>target.scrollIntoView({behavior:'smooth',block:'start'}));
    }
  }

  links.forEach(link=>link.addEventListener('click',function(event){
    event.preventDefault();
    const hash=this.getAttribute('href');
    history.pushState(null,'',hash);
    activate(hash,true);
  }));

  window.addEventListener('hashchange',()=>activate(location.hash,true));
  if(location.hash) activate(location.hash,false);
})();
