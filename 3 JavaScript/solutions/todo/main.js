let todoList = document.querySelector('#todo-list')
let doneList = document.querySelector('#done-list')
let inputDiv = document.querySelector('#input-div')
let input = inputDiv.querySelector('input')
let submitBtn = inputDiv.querySelector('button')

let emptyBox = '<i class="fa fa-square-o"></i>'
let checkBox = '<i class="fa fa-check-square-o"></i>'
let trash = '<i class="fa fa-trash-o"></i>'


submitBtn.addEventListener('click', todo)
input.addEventListener('keydown', function (event) {
    if (event.key === "Enter") {
        todo()
    }
})

function todo() {
    let text = input.value
    let div = document.createElement('div')
    let p = document.createElement('p')
    let done = document.createElement('button')
    let deleteBtn = document.createElement('button')

    p.innerText = text
    div.append(p)

    done.innerHTML = emptyBox
    done.className = "btn"
    div.append(done)
    done.addEventListener('click', function () {
        if (done.innerHTML === checkBox) {
            doneList.prepend(div)
            done.innerHTML = emptyBox
        } else {
            todoList.prepend(div)
            done.innerHTML = checkBox
        }
    })

    deleteBtn.innerHTML = trash
    deleteBtn.className = "btn"
    div.append(deleteBtn)
    deleteBtn.addEventListener('click', function () {
        let parent = deleteBtn.parentNode
        let grandParent = deleteBtn.parentNode.parentNode
        grandParent.removeChild(div)
        // try {
        //     todoList.removeChild(div)
        //     doneList.removeChild(div)
        // } catch {

        // }
    })

    div.className = "todo-item"
    todoList.prepend(div)

    input.value = ""
}



// document.addEventListener('mousemove', function (event) {
//     if (event.screenX > 800 && event.screenY > 600) {
//         inputDiv.style.background = "blue"
//     } else {
//         inputDiv.style.background = "white"
//     }
// })