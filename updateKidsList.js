/*
fetch("players_sorted.json")
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
*/

fetch("players_sorted.json")
.then(function(response) {
    return response.json();
})
.then(function(players) {
    for (let player in players) {
        const row = document.createElement("tr");
        const cell1 = document.createElement("td");
        const cell2 = document.createElement("td");
        const playerName = document.createTextNode(players[player]["name"]);
        const playerRating = document.createTextNode(players[player]["rating"]);
        const testVar = document.createTextNode(player);
        console.log(players[player]);

        cell1.appendChild(playerName);
        row.appendChild(cell1);
        cell2.appendChild(playerRating);
        row.appendChild(cell2);
        document.getElementById("data-output").appendChild(row);
    }
});