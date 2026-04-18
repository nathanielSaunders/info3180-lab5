<script setup>
import { ref, onMounted } from "vue";

let csrf_token = ref("");

function getCsrfToken() {
    fetch('/api/v1/csrf-token') 
        .then((response) => response.json())
        .then((data) => {
            csrf_token.value = data.csrf_token; 
        });
}

onMounted(() => {
    getCsrfToken(); 
});

function saveMovie() {
    let movieForm = document.getElementById('movieForm'); 
    let form_data = new FormData(movieForm); 

    fetch("/api/v1/movies", {
        method: 'POST', 
        body: form_data, 
        headers: {
            'X-CSRFToken': csrf_token.value 
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); 
    })
    .catch(error => console.log(error)); 
}
</script>

<template>
  <form id="movieForm" @submit.prevent="saveMovie"> 
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input type="text" name="title" class="form-control" /> 
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</template>
