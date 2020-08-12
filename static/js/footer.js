let mapFrame = document.getElementById('yandexMapFrame');
let mapDiv = document.getElementById('yandexMap');

mapFrame.addEventListener('load', e => {
    mapDiv.style.visibility = 'visible'
}, {passive: true})