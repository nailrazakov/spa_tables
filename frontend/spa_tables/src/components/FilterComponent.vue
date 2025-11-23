<template>
    <div class="filter-container">
      <div class="row mb-3">
        <div class="col-md-3">
          <select v-model="column" class="form-select" @change="onFilterChange">
            <option value="">Выберите колонку</option>
            <option value="name">Название</option>
            <option value="quantity">Количество</option>
            <option value="distance">Расстояние</option>
          </select>
        </div>
        
        <div class="col-md-3">
          <select v-model="condition" class="form-select" @change="onFilterChange" :disabled="!column">
            <option value="">Выберите условие</option>
            <option v-if="column === 'name'" value="equals">Равно</option>
            <option v-if="column === 'name'" value="contains">Содержит</option>
            <option v-if="column !== 'name'" value="equals">Равно</option>
            <option v-if="column !== 'name'" value="greater">Больше</option>
            <option v-if="column !== 'name'" value="less">Меньше</option>
          </select>
        </div>
        
        <div class="col-md-4">
          <input 
            v-model="filterValue" 
            type="text" 
            class="form-control" 
            placeholder="Введите значение"
            @input="onFilterChange"
            :disabled="!condition"
          >
        </div>
        
        <div class="col-md-2">
          <button @click="clearFilters" class="btn btn-secondary w-100">
            Сбросить
          </button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'FilterComponent',
    data() {
      return {
        column: '',
        condition: '',
        filterValue: ''
      }
    },
    methods: {
      onFilterChange() {
        this.$emit('filter-changed', {
          column: this.column,
          condition: this.condition,
          value: this.filterValue
        })
      },
      
      clearFilters() {
        this.column = ''
        this.condition = ''
        this.filterValue = ''
        this.onFilterChange()
      }
    }
  }
  </script>