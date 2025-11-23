<template>
    <div class="data-table-container">
      <FilterComponent 
        @filter-changed="handleFilterChange"
      />
      
      <div class="table-responsive">
        <table class="table table-striped table-bordered">
          <thead>
            <tr>
              <th>ID</th>
              <th>Дата</th>
              <th @click="sortBy('name')" class="sortable">
                Название 
                <span v-if="sortField === 'name'">
                  {{ sortDirection === 'asc' ? '↑' : '↓' }}
                </span>
              </th>
              <th @click="sortBy('quantity')" class="sortable">
                Количество
                <span v-if="sortField === 'quantity'">
                  {{ sortDirection === 'asc' ? '↑' : '↓' }}
                </span>
              </th>
              <th @click="sortBy('distance')" class="sortable">
                Расстояние
                <span v-if="sortField === 'distance'">
                  {{ sortDirection === 'asc' ? '↑' : '↓' }}
                </span>
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in tableData" :key="item.id">
              <td>{{ item.id }}</td>
              <td>{{ formatDate(item.date) }}</td>
              <td>{{ item.name }}</td>
              <td>{{ item.quantity }}</td>
              <td>{{ item.distance }}</td>
            </tr>
          </tbody>
        </table>
      </div>
  
      <PaginationComponent
        :current-page="currentPage"
        :total-pages="totalPages"
        @page-changed="handlePageChange"
      />
    </div>
  </template>
  
  <script>
  import FilterComponent from './FilterComponent.vue'
  import PaginationComponent from './PaginationComponent.vue'
  import { fetchTableData } from '../services/api'
  
  export default {
    name: 'DataTable',
    components: {
      FilterComponent,
      PaginationComponent
    },
    data() {
      return {
        tableData: [],
        currentPage: 1,
        totalPages: 1,
        sortField: 'name',
        sortDirection: 'asc',
        filters: {
          column: '',
          condition: '',
          value: ''
        }
      }
    },
    mounted() {
      this.loadData()
    },
    methods: {
      async loadData() {
        try {
          const params = {
            page: this.currentPage,
            ordering: this.sortDirection === 'desc' ? `-${this.sortField}` : this.sortField,
            ...this.filters
          }
          
          const response = await fetchTableData(params)
          this.tableData = response.data.results
          this.totalPages = Math.ceil(response.data.count / 10)
        } catch (error) {
          console.error('Error loading data:', error)
        }
      },
      
      sortBy(field) {
        if (this.sortField === field) {
          this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc'
        } else {
          this.sortField = field
          this.sortDirection = 'asc'
        }
        this.currentPage = 1
        this.loadData()
      },
      
      handleFilterChange(filters) {
        this.filters = filters
        this.currentPage = 1
        this.loadData()
      },
      
      handlePageChange(page) {
        this.currentPage = page
        this.loadData()
      },
      
      formatDate(dateString) {
        return new Date(dateString).toLocaleDateString('ru-RU')
      }
    }
  }
  </script>
  
  <style scoped>
  .sortable {
    cursor: pointer;
    user-select: none;
  }
  
  .sortable:hover {
    background-color: #f8f9fa;
  }
  
  .data-table-container {
    padding: 20px;
  }
  </style>