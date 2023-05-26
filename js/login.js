document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("form").addEventListener("submit", (e) => {
        e.preventDefault();
    })
    document.querySelector("button").addEventListener("click", () => {
        fetch("/api", {
            method: "POST",
            headers:{'Content-Type': 'application/json'},
            body: JSON.stringify({
                id: 'log',
                mail: document.querySelector("[name='mail']").value,
                password: document.querySelector("[name='password']").value,
            })
        })
            .then(res => res.json())
            .then(json => {
                console.log(json);
                var person = json;
                console.log(person);
                if (person["message"] === "Введите данные")
                    window.alert("Введите данные");
                else if (person["message"] === "Вы вошли"){                    
                    window.alert("Вы вошли");
                    window.location.href = 'index.html';               
                }else if (person["message"] === "Пароль указан не верно")
                    window.alert("Пароль указан не верно");
                else if (person["message"] === "Пользователь не существует")
                    window.alert("Пользователь не существует");
            })
    })
})