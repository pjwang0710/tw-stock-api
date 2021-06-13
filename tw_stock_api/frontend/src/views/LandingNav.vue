<template>
  <nav class="top-0 absolute z-50 w-full flex flex-wrap items-center justify-between px-2 py-3">
    <div class="container px-10 mx-auto flex flex-wrap items-center justify-between">
      <div class="w-full relative flex justify-between lg:w-auto lg:static lg:block lg:justify-start">
        <a class="text-base font-bold leading-relaxed inline-block mr-4 py-2 whitespace-nowrap uppercase text-text" href="/">
           <img src="../assets/logo_transparent.png" class="h-12 self-center my-auto" />
        </a>
        <button class="cursor-pointer text-xl leading-none px-3 py-1 border border-solid border-transparent rounded bg-transparent block lg:hidden outline-none focus:outline-none"
                type="button">
          <i class="text-black fas fa-bars"></i>
        </button>
      </div>
      <div class="lg:flex flex-grow items-center bg-white bg-transparent">
        <ul class="flex flex-col lg:flex-row list-none mr-auto">
          <li class="flex items-center" v-for="item in navigation" :key="item.name">
            <a class="hover:text-gray-300 text-gray-800 px-3 py-4 lg:py-2 flex items-center text-base uppercase"
               :href="item.href">
              {{ item.name }}
            </a>
          </li>
          <li class="flex items-center">
            <a href="/signup" class="hover:text-gray-300 text-gray-800 px-3 py-4 lg:py-2 flex items-center text-base uppercase">註冊</a>
          </li>
          <li class="flex items-center">
            <a href="/login" class="hover:text-gray-300 text-gray-800 px-3 py-4 flex items-center text-base uppercase">登入</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>

const navigation = [{ name: "API 文件", href: "/api" }];

export default {
  name: "LandingNav",
  setup() {
    return {
      navigation,
    };
  },
};
</script>