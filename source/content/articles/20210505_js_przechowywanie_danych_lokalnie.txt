Title: JavaScript - przechowywanie danych lokalnie i w sesji
Author: mkostyrko
Date: 2020-05-05 10:00
Updated:
Category: javascript
Tags: 
Slug: js-przechowywanie-danych-lokalnie
related_posts: 

    document.querySelector('form').addEventListener('submit', function(e){
      const task = document.getElementById('task').value;

      let tasks;

      if(localStorage.getItem('tasks') === null) {
        tasks = [];
      } else {
        tasks = JSON.parse(localStorage.getItem('tasks'));
      }

      tasks.push(task);

      localStorage.setItem('tasks', JSON.stringify(tasks));

      alert('Task saved');

      e.preventDefault();
    });

    const tasks = JSON.parse(localStorage.getItem('tasks'));

    tasks.forEach(function(taks){
      console.log(task);
    });

---

Źródła:

