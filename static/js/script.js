// Смена класса для ссылки на которую кликнули
function changeClass(event) {
    // Обнуляем классы
    let elemsMenu = document.querySelectorAll('ul.left_list li');
    for (let item of elemsMenu) {
        item.removeAttribute('class');
    }

    // Только для левого меню изменяем класс у ссылки по которой кликнули
    let clik_link = event.target;
    if (clik_link.parentNode.parentNode.className === 'left_list') {
        clik_link.parentNode.className = "active";
        let nameNewH1 = clik_link.innerHTML;

        // Изменяем заголовок текущей страницы
        let elemsH1 = document.querySelector('div.article h1');
        elemsH1.innerHTML = nameNewH1;
    }
}

// Обработчик кликов на странице
document.addEventListener("click", changeClass);