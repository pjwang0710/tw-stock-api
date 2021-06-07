<template>
  <div class="flex flex-row min-h-screen bg-gray-100 text-gray-800">
    <Sidebar />
    <main class="main flex flex-col flex-grow -ml-64 md:ml-0 transition-all duration-150 ease-in">
        <Header />
        <div class="flex flex-wrap">
            <div class="w-1/3 p-3">
                <div class="bg-white border rounded shadow p-2">
                    <div class="flex flex-row items-center">
                        <div class="flex-shrink pr-4">
                            <div class="rounded p-3 bg-green-600"><i class="fa fa-wallet fa-2x fa-fw fa-inverse"></i></div>
                        </div>
                        <div class="flex-1 text-right md:text-center">
                            <h5 class="font-bold uppercase text-gray-500">Total Revenue</h5>
                            <h3 class="font-bold text-3xl">$3249 <span class="text-green-500"><i class="fas fa-caret-up"></i></span></h3>
                        </div>
                    </div>
                </div>
            </div>
            <div class="w-1/3 p-3">
                <!--Metric Card-->
                <div class="bg-white border rounded shadow p-2">
                    <div class="flex flex-row items-center">
                        <div class="flex-shrink pr-4">
                            <div class="rounded p-3 bg-pink-600"><i class="fas fa-users fa-2x fa-fw fa-inverse"></i></div>
                        </div>
                        <div class="flex-1 text-right md:text-center">
                            <h5 class="font-bold uppercase text-gray-500">Total Users</h5>
                            <h3 class="font-bold text-3xl">249 <span class="text-pink-500"><i class="fas fa-exchange-alt"></i></span></h3>
                        </div>
                    </div>
                </div>
                <!--/Metric Card-->
            </div>
            <div class="w-1/3 p-3">
                <!--Metric Card-->
                <div class="bg-white border rounded shadow p-2">
                    <div class="flex flex-row items-center">
                        <div class="flex-shrink pr-4">
                            <div class="rounded p-3 bg-yellow-600"><i class="fas fa-user-plus fa-2x fa-fw fa-inverse"></i></div>
                        </div>
                        <div class="flex-1 text-right md:text-center">
                            <h5 class="font-bold uppercase text-gray-500">New Users</h5>
                            <h3 class="font-bold text-3xl">2 <span class="text-yellow-600"><i class="fas fa-caret-up"></i></span></h3>
                        </div>
                    </div>
                </div>
                <!--/Metric Card-->
            </div>
        </div>
        <div class="flex flex-wrap">
            <div class="w-1/2 p-3">
                <!--Graph Card-->
                <div class="bg-white border rounded shadow">
                    <div class="border-b p-3">
                        <h5 class="font-bold uppercase text-gray-600">Graph</h5>
                    </div>
                    <div class="p-5 w-full">
                        <AreaChart />
                    </div>
                </div>
            </div>
            <div class="w-1/2 p-3">
                <!--Graph Card-->
                <div class="bg-white border rounded shadow">
                    <div class="border-b p-3">
                        <h5 class="font-bold uppercase text-gray-600">Graph</h5>
                    </div>
                    <div class="p-5 w-full">
                        <BarChart />
                    </div>
                </div>
            </div>
        </div>
    </main>
  </div>
</template>

<script>
// import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'
import Sidebar from './Sidebar.vue'
import Header from './Header.vue'
import AreaChart from "../components/AreaChart.vue";
import BarChart from "../components/BarChart.vue";
// import { useToast } from 'vue-toastification'

// const toast = useToast()

export default {
  name: 'Dashboard',
  components: {
    Sidebar,
    Header,
    AreaChart,
    BarChart
  },
  data() {
    return {
      
    }
  }
}
</script>