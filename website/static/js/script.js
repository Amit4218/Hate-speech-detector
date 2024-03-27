function loco(){
  gsap.registerPlugin(ScrollTrigger);

// Using Locomotive Scroll from Locomotive https://github.com/locomotivemtl/locomotive-scroll

const locoScroll = new LocomotiveScroll({
el: document.querySelector("#main"),
smooth: true
});
}
loco()

function page1aAni(){
  var tl = gsap.timeline();

 
    tl.from(".barmenu",{
        y: '-10%',
        opacity: 0,
        duration: .5,
        ease: Expo.easeInOut
    })
    tl.from("form",{
        y: '-10%',
        opacity: 0,
        duration: 1,
        ease: Expo.easeInOut
    })

    .to(".aniElem",{
      y: 0,
      duration: 2,
      delay:-1,
      ease: Expo.easeInOut,
      stagger:.2
  })
}

page1aAni();





