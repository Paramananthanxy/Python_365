console.log("js is running ")
fetch('http://127.0.0.1:5000/cve/list')
.then(response=>response.json())
.then(data =>{
    let table = document.getElementById("tablebody")

    data.forEach(cve=>{
        let row = `
        <tr>
        <td>${cve.id}</td>
         <td>${cve.published}</td>
          <td>${cve.lastmodified}</td>
        </tr>
        `
        table.innerHTML +=row
    })
})
