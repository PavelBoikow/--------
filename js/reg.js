document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("form").addEventListener("submit", (e) => {
        e.preventDefault();
    })
    document.querySelector("button").addEventListener("click", () => {
        fetch("/api", {
            method: "POST",
            headers:{'Content-Type': 'application/json'},
            body: JSON.stringify({
                id: 'reg',
                mail: document.querySelector("[name='mail']").value,
                password: document.querySelector("[name='password']").value,
            })
        })
            .then(res => res.json())
            .then(json => {
                console.log(json);
                var person = json;
                console.log(person);
                if (person["message"] === "Пользователь сущестует"){
                    window.alert("Пользователь сущестует");
                    setTimeout(function(){
                        window.location.href = 'login.html';
                    }, 5 * 10);
                }else if (person["message"] === "Пользователь добавлен"){
                    window.alert("Пользователь добавлен");
                    setTimeout(function(){
                        window.location.href = 'login.html';
                    }, 5 * 10);
                }
            })
    })
})