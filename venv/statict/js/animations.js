const btn = document.querySelector(".btnMobile")

btn.addEventListener('click', () => {
    const box = document.querySelector("ul")
    box.classList.toggle('show')
})