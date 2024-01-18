let tasksEl = document.getElementById('tasks')

fetch('/api/task/')
.then(res => res.json())
.then(data => {
    data.forEach(task => {

        let taskEl = document.createElement('div')
        taskEl.innerText = task.text
        
        if(task.is_done){
            taskEl.style.color = "red"
        }

        taskEl.addEventListener('click', ()=>{
            fetch("/api/task/" + task.id, {
                method:"PUT",
                headers: {
                    'Content-Type':'application/json'
                },
                body: JSON.stringify(
                    {
                        "text":task.text,
                        "is_visible":true,
                        "is_done": !task.is_done
                    }
                )
            }).then(res => res.json())
            .then(data => console.log(data))
        })

        tasksEl.appendChild(taskEl)
    });
})