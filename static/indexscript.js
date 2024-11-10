const input = document.querySelector(".todo-input");
const addButton = document.querySelector(".add-button");
const todosHtml = document.querySelector(".todos");
const emptyImage = document.querySelector(".empty-image");
let todosJson = JSON.parse(localStorage.getItem("todos")) || [];
const deleteAllButton = document.querySelector(".delete-all");
const filters = document.querySelectorAll(".filter");
let filter = '';

showTodos();

function getTodoHtml(todo, index) {
  if (filter && filter != todo.status) return '';
  let checked = todo.status == "completed" ? "checked" : "";
  return `
    <li class="todo">
      <label>
        <input type="checkbox" onclick="updateStatus(this)" ${checked} id="${index}">
        <span>${todo.name}</span>
      </label>
      <button class="delete-btn" onclick="remove(${index})"><i class="fa fa-times"></i></button>
    </li>
  `;
}

function showTodos() {
  todosHtml.innerHTML = todosJson.map(getTodoHtml).join('');
  emptyImage.style.display = todosJson.length ? 'none' : 'block';
}

function addTodo() {
  const todo = input.value.trim();
  if (!todo) return;
  todosJson.push({ name: todo, status: "pending" });
  input.value = '';
  saveAndRender();
}

function updateStatus(checkbox) {
  const id = checkbox.id;
  todosJson[id].status = checkbox.checked ? "completed" : "pending";
  saveAndRender();
}

function remove(index) {
  todosJson.splice(index, 1);
  saveAndRender();
}

function saveAndRender() {
  localStorage.setItem("todos", JSON.stringify(todosJson));
  showTodos();
}

addButton.addEventListener("click", addTodo);
input.addEventListener("keyup", (e) => e.key === "Enter" && addTodo());

filters.forEach(filterBtn => {
  filterBtn.addEventListener("click", () => {
    filters.forEach(btn => btn.classList.remove("active"));
    filterBtn.classList.add("active");
    filter = filterBtn.dataset.filter;
    showTodos();
  });
});

deleteAllButton.addEventListener("click", () => {
  todosJson = [];
  saveAndRender();
});
