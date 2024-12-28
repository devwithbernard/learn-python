// Select elements
const inputField = document.getElementById('todo-input');
const addButton = document.getElementById('add-btn');
const todoList = document.getElementById('todo-list');

// Add Task
addButton.addEventListener('click', () => {
    const taskText = inputField.value.trim();
    if (taskText) {
        addTask(taskText);
        inputField.value = '';
    }
});

// Add Task to List
function addTask(text) {
    const li = document.createElement('li');

    // Task text
    const taskSpan = document.createElement('span');
    taskSpan.textContent = text;

    // Action buttons
    const actionsDiv = document.createElement('div');
    actionsDiv.className = 'todo-actions';

    // Complete button
    const completeBtn = document.createElement('button');
    completeBtn.innerHTML = '✔️';
    completeBtn.addEventListener('click', () => {
        li.classList.toggle('completed');
    });

    // Delete button
    const deleteBtn = document.createElement('button');
    deleteBtn.innerHTML = '❌';
    deleteBtn.addEventListener('click', () => {
        li.remove();
    });

    actionsDiv.appendChild(completeBtn);
    actionsDiv.appendChild(deleteBtn);

    li.appendChild(taskSpan);
    li.appendChild(actionsDiv);

    todoList.appendChild(li);
}

// Add Task with Enter Key
inputField.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        addButton.click();
    }
});
