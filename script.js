fetch("./kids rating list/players_sorted.json")
.then(function(response){
    return response.json();
})
.then(function(players){
    let placeholder = document.querySelector("#data-output");
    let out = "";
    for(let player of players){
        out += `
            <tr>
                <td>${player.name}</td>
                <td>${player.rating}</td>
            </tr>
        `;
    }
 
    placeholder.innerHTML = out;
});