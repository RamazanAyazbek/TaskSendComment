// Add star rating
const rating = document.querySelector('form[name=rating]');
console.log("Working")
// alert("ramazan")
rating.addEventListener("change", function (e) {
    // Получаем данные из формы
    let data = new FormData(this);
    fetch(`${this.action}`, {
        method: 'POST',
        body: data
    })
        .then(response => alert("Рейтинг установлен"))
        .catch(error => alert("Ошибка"))
        console.log("Working")
});









