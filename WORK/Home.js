const navToggle= ()=>{
    
}
const active = ()=>{
    const  link = document.querySelector(".nav-links li") 
    link.addEventListener("click",()=>{
        link.classList.toggle("active")
    })

}
