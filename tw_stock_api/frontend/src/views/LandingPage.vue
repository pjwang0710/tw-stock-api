<template>
  <div>
    <LandingNav /> 
    <section class="relative pt-16 items-center flex h-full max-w-7xl mx-auto">
      <div class="grid grid-cols-2">
        <div class="w-full my-auto mx-20">
          <div class="text-left">
            <h2 class="font-semibold text-4xl text-blueGray-600">
              <span>掌握台股脈動</span>
              <h1 class="font-semibold text-5xl mt-2">
                <span class="text-indigo-600">指引人生方向</span>
              </h1>
            </h2>
            <div class="mt-6 w-2/3">
              <p class="text-base text-gray-500 mt-5">
                我們提供最新台股資訊，不僅讓你第一手獲得最新資料，我們也運用 AI 分析模型，做精準的預測與分析！
              </p>  
            </div>
            <div class="mt-10 rounded-md">
              <a href="/signup" class="px-8 border border-transparent text-base font-medium rounded-md text-indigo-700 bg-indigo-100 hover:bg-indigo-200 py-4">
                註冊帳號
              </a>
            </div>
          </div>
        </div>
        
        <div class="w-full my-auto">
          <img src="../assets/banner.png" class="w-full"/>
        </div>
      </div>
    </section>
    <div class="relative items-center flex h-full max-w-7xl mx-auto overflow-hidden">
      <div class="grid grid-cols-2">
        <div class="w-full my-auto">
          <img src="../assets/landing1.png" class="w-full"/>
        </div>
        <div class="w-full my-auto mx-20">
          <div class="text-left">
            <h2 class="font-semibold text-4xl text-blueGray-600 mb-5">
              <span> 台股資料 API </span>
            </h2>
            <ul class="flex flex-wrap">
              <div v-for="(services, i) in all_services" :key="i" class="flex-none w-2/5 space-y-2">
                <div v-for="(service, j) in services" :key="j">
                  <div v-if="service.isTitle" class="mt-5">
                    <span class="text-lg font-bold text-indigo-700"> {{ service.name }}</span>
                  </div>
                  <div v-else>
                    <li class="flex items-center">
                      <svg class="w-6 h-6 text-indigo-700"
                          aria-hidden="true"
                          xmlns="http://www.w3.org/2000/svg"
                          viewBox="0 0 20 20"
                          fill="currentColor">
                          <path fill-rule="evenodd"
                                d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                                clip-rule="evenodd"/>
                      </svg>
                      <span class="ml-2 text-base"> {{ service.name }}</span>
                    </li>
                  </div>
                </div>
                
              </div>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <!-- 流程 -->
    
    <div class="relative flex h-full max-w-7xl justify-center mx-auto mt-10">
      <div class="flex flex-col">
        <p class="text-4xl self-center -mb-6"> 使用流程 </p>
        <div v-for="(step, i) in steps" :key="i" class="-my-6">
          <div class="flex md:flex-row flex-col bg-teal-200">
              <div>
                <div class="w-56 h-10 md:flex hidden" >
                    <div class="h-full  border-teal-300 border-solid"></div>
                </div>
                <img alt="step1" class="w-56 h-56 rounded-full my-5 object-scale-down" :src="getImgUrl(step.image)"> 
                <div v-if="i != 2">
                  <div class="w-56 h-10 md:flex hidden justify-center">
                    <div class="h-full border-r-4 border-teal-300 border-solid"></div>
                  </div>
                </div>
              </div>
              <div class="ml-5 p-10 flex flex-col justify-center max-w-2xl rounded bg-teal-200">
                <div class="text-sm uppercase font-bold text-gray-400 text-teal-500">步驟 {{ i + 1 }}</div>
                <div class="md:text-3xl text-xl font-bold text-teal-700">{{ step.stepName }}</div>
                <div class="mt-4 text-teal-800 text-lg">
                  <div v-html="step.description"></div>
                </div>
              </div>
          </div>
        </div>
      </div>
    </div>
    <div class="relative items-center h-full max-w-7xl mt-20 mx-auto">
      <div class="text-5xl mb-10 flex">
        <p class="text-4xl self-center mx-auto"> 收費方式 </p>
      </div>
      <div class="flex flex-col">
        <div class="overflow-x-auto">
          <div class="py-2 align-middle inline-block min-w-full">
            <div class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg">
              <table class="min-w-full divide-y divide-gray-200">
                <tr class="bg-gray-50">
                  <th scope="col" class="row-span-2 px-6 py-3 text-left text-base font-medium text-gray-500">
                    功能
                  </th>
                  <th scope="col" class="px-6 py-3 text-center text-base font-medium text-gray-500">
                    每個月前 1000 個
                  </th>
                  <th scope="col" class="px-6 py-3 text-center text-base font-medium text-gray-500">
                    每個月第 1001 個以上
                  </th>
                </tr>
                <tbody class="bg-white divide-y divide-gray-200">
                  <tr v-for="(price, i) in prices" :key="i">
                    <td class="px-6 py-4 whitespace-nowrap">
                      <div class="flex items-center">
                        <div class="ml-4">
                          <div class="text-base font-medium text-gray-900">
                            {{ price.title }}
                          </div>
                          <div v-for="(service, j) in price.services" :key=j class="mt-1">
                            <div class="text-sm text-gray-500">
                              - {{ service }}
                            </div>
                          </div>
                        </div>
                      </div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap text-center ">
                      <div class="text-lg text-indigo-700">{{ price.basic }}</div>
                    </td>
                    <td class="px-6 py-4 whitespace-nowrap text-center">
                      <div class="text-lg text-gray-900">{{ price.advance }}</div>
                      <div class="text-sm text-gray-600">每 100 個為 1 單位</div>
                      <!-- <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-100 text-green-800">
                        Active
                      </span> -->
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- 方案 -->
    <!-- <div class="relative items-center flex h-full max-w-7xl">
      <div class="text-5xl mx-auto my-10">
        <p> 方案 </p>
      </div>
    </div>
    <div class="relative items-center flex h-full max-w-7xl mx-auto">
      <div class="h-full flex flex-row">
        <div v-for="(plan, i) in plans" v-bind:key="i" class="flex-1 mx-2">
          <div class="max-w-sm p-12 rounded-2xl shadow-lg border-2 border-black-600">
            <div>
              <span class="text-4xl font-medium"> NTD {{ plan.price.monthly }}</span>
            </div>
            <div class="pb-6 space-y-2 border-b">
                <h2 class="text-2xl font-normal"> {{ plan.name }}</h2>
                <p class="text-sm text-gray-400"> {{ plan.description }} </p>
            </div>
            <ul class="flex-1 space-y-4 mt-10">
              <div v-for="(feature, i) in plan.features" :key="i">
                <li class="flex items-start">
                  <svg
                      class="w-6 h-6 text-indigo-700"
                      aria-hidden="true"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                      >
                    <path
                          fill-rule="evenodd"
                          d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                          clip-rule="evenodd"
                          />
                  </svg>
                  <span class="ml-3 text-base font-medium"> {{ feature }}</span>
                </li>
              </div>
            </ul>
            <div class="flex-shrink-0 pt-4">
              <button class="inline-flex items-center justify-center w-full max-w-xs px-4 py-2 transition-colors border rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">{{ plan.name }}</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div> -->
  <LandingFooter />
  </div>
  
</template>

<script>
// import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'
import LandingNav from './LandingNav.vue'
import LandingFooter from './LandingFooter.vue'

export default {
  name: 'LandingPage',
  components: {
    LandingNav,
    LandingFooter
  },
  methods: {
    getImgUrl(pic) {
        return require('../assets/'+pic)
    }
  },
  data() {
    return {
      prices: [{
          title: '基本面',
          services: ['基本資料', '本益比', '淨值比'],
          basic: '免費',
          advance: '每單位 10 元台幣',
      }, {
          title: '財務面',
          services: ['資產負債表', '損益表', '現金流量表', '財務比率'],
          basic: '免費',
          advance: '每單位 10 元台幣',
      }, {
          title: '籌碼面',
          services: ['1分K', '日K', '投行分點交易量'],
          basic: '免費',
          advance: '每單位 15 元台幣',
      }],
      steps: [{
        'stepName': '註冊/登錄帳號',
        'description': '請至<a href="/signup" class="text-indigo-700 font-bolder">註冊頁面</a>申請帳號，並且<a href="/login" class="text-indigo-700 font-bolder">登入</a>後拿到 secret key。',
        'url': '',
        'image': 'login.png',
      }, {
        'stepName': '安裝套件',
        'description': '<code>$ pip install tw_stocks </code> ',
        'url': '',
        'image': 'install.png',
      }, {
        'stepName': '開始 Coding',
        'description': '<code> from tw_stocks import TWStocks <br />twstocks = TWStocks("API secret key") <br />twstocks.get_cash_flow_statement("1101", "2021-01-01") </code>',
        'url': '',
        'image': 'coding.png',
      }],
      all_services: [[{
        'isTitle': true,
        'name': '基本面'
      }, {
        'isTitle': false,
        'name': '基本資料'
      }, {
        'isTitle': false,
        'name': '本益比'
      }, {
        'isTitle': false,
        'name': '淨值比'
      }], [{
        'isTitle': true,
        'name': '籌碼面'
      }, {
        'isTitle': false,
        'name': '1分K、日K'
      }, {
        'isTitle': false,
        'name': '投行分點交易量'
      }], [{
        'isTitle': true,
        'name': '財務面'
      }, {
        'isTitle': false,
        'name': '資產負債表'
      }, {
        'isTitle': false,
        'name': '損益表'
      }, {
        'isTitle': false,
        'name': '現金流量表'
      }, {
        'isTitle': false,
        'name': '財務比率'
      }]],
      plans: [
        {
            name: 'Easy',
            description: 'All the basics for businesses that are just getting started.',
            price: {
              monthly: 29,
              annually: 29 * 12 - 199,
            },
            features: ['One project', 'Your dashboard'],
        },
        {
            name: 'Basic',
            description: 'Better for growing businesses that want more customers.',
            price: {
              monthly: 59,
              annually: 59 * 12 - 100,
            },
            features: ['Two projects', 'Your dashboard', 'Components included', 'Advanced charts'],
        },
        {
            name: 'Custom',
            description: 'Advanced features for pros who need more customization.',
            price: {
              monthly: 139,
              annually: 139 * 12 - 100,
            },
            features: ['Unlimited projects', 'Your dashboard', '+300 Components', 'Chat support'],
        },
        ]
    }
  }
}
</script>

<style>
  .gradient {
    background: linear-gradient(90deg, #d53369 0%, #daae51 100%);
  }
</style>