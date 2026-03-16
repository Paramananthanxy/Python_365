async function loadData(limit=10){
    let response = await fetch(`http://127.0.0.1:5000/cve/list?limit=${limit}`)
}   let data = await response.json()

let table = document.getElementById("tableBody")
table.innerHTML = ""

data.forEach(cve =>{

    let row = `
    <tr onclick="openCVE('${cve.id}')">
    <td>${cve.id}</td>
    <td>${cve.published}</td>
    <td>${cve.lastmodified}</td>
    <td>${cve.basescore}</td>
    `
    table.innerHTML += row
})

loadData()