<template>
  <div>
    <LandingNav /> 
    <div class="relative items-center h-full max-w-7xl mt-20 mx-auto">
      <div class="text-5xl mb-10 flex">
        <p class="text-4xl self-center mx-auto"> API Document </p>
      </div>
      <div class="flex flex-col max-w-4xl mx-auto">
        <div class="overflow-x-auto">
          <div class="py-2 align-middle inline-block min-w-full">
            <div class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg">
              <table class="min-w-full divide-y divide-gray-200">
                <tr class="bg-gray-50">
                  <th scope="col" class="w-1/2 px-6 py-3 text-left text-base font-medium text-gray-500">
                    資料表
                  </th>
                  <th scope="col" class="w-1/2 px-6 py-3 text-left text-base font-medium text-gray-500">
                    API
                  </th>
                </tr>
                <tbody class="bg-white divide-y divide-gray-200">
                  <tr v-for="(api, i) in apis" :key="i">
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="flex items-center">
                        <div class="ml-4">
                          <div class="text-base font-medium text-gray-900">
                            {{ api.title }}
                          </div>
                          <div v-for="(service, j) in api.services" :key=j class="mt-1">
                            <div class="text-sm text-gray-500">
                              - {{ service }}
                            </div>
                          </div>
                        </div>
                      </div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap text-left ">
                      <code>
                        {{ api.request }}
                        <!-- <div class="text-lg text-indigo-700">{{  }}</div> -->
                      </code>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  <LandingFooter />
  </div>
  
</template>

<script>
// import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'
import LandingNav from './LandingNav.vue'
import LandingFooter from './LandingFooter.vue'

export default {
  name: 'APIDocument',
  components: {
    LandingNav,
    LandingFooter
  },
  methods: {
  },
  data() {
    return {
      apis: [{
          title: '公司基本資訊',
          services: ['公司名稱', '英文簡稱', '產業', '細產業別', '內銷比重', '外銷比重', '上市上櫃', '實收資本額	59,414 (佰萬)', '本益比', '股價淨值比', '單月營收', '單月營收年成長率', '...'],
          request: 'get_stock_basic_info(stock_id)',
      }, {
          title: '本益比',
          services: ['收盤價', '法人預估本益比', '本益比(近4季)', '本益比(季高)', '本益比(季低)', 'EPS' ],
          request: 'get_per_and_pbr(stock_id, start_date)',
      }, {
          title: '現金流量表',
          services: ['稅前純益', '營業活動現金流量', '投資活動現金流量', '理財活動現金流量', '淨現金流量', '期末現金及約當現金', '自由現金流量'],
          request: 'get_cash_flow_statement(stock_id, start_date)',
      }, {
          title: '資產負債表',
          services: ['流動資產', '現金及約當現金', '存貨', '長期投資', '固定資產', '土地', '累積折舊', '其他資產', '資產總計', '流動負債', '應付帳款合計', '長期負債', '其他負債', '負債總計', '股本', '股東權益', '公告每股淨值'],
          request: 'get_balance_sheet(stock_id, start_date)',
      }, {
          title: '損益表',
          services: ['年季', '營業收入淨額', '營業成本', '營業毛利', '營業費用', '營業利益', '營業外收入', '營業外支出', '稅前純益', '稅後純益', '每股稅後盈餘(元)'],
          request: 'get_income_statement(stock_id, start_date)',
      }, {
          title: '財務比率',
          services: ['毛利率', '營業利益率', '稅前純益率', '稅後純益率', '稅後股東權益報酬率', '稅後資產報酬率', '每股營業額', '公告每股淨值', '每股稅後盈餘'],
          request: 'get_financial_ratios((stock_id, start_date)',
      }]
    }
  }
}
</script>

<style>
  
</style>