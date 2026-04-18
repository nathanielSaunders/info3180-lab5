<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]); 

const fetchMovies = () => {
    fetch("/api/v1/movies") 
        .then(response => response.json())
        .then(data => {
            movies.value = data.movies; 
        });
};

onMounted(fetchMovies); 
</script>

<template>
  <div class="container">
    <div class="row">
      <div v-for="movie in movies" :key="movie.id" class="col-md-4"> 
        <div class="card">
          <img :src="movie.poster" class="card-img-top" :alt="movie.title"> 
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p class="card-text">{{ movie.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>