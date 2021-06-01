<template>
  <div>
    <LandingNav />
    <div class="mt-10 sm:mt-0">
    <div class="md:grid md:grid-cols-1">
        <div class="mt-5 md:mt-0 md:col-span-2 mx-auto">
        <form action="#" method="POST">
            <div class="shadow overflow-hidden sm:rounded-md">
            <div class="px-4 py-5 bg-white sm:p-6">
                <div class="grid grid-cols-6 gap-6">
                <div class="col-span-6 sm:col-span-3">
                    <label for="first_name" class="block text-sm font-medium text-gray-700">First name</label>
                    <input type="text" placeholder="First name" name="first_name" id="first_name" autocomplete="given-name" class="mt-3 py-2 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-black-300 rounded-md">
                </div>

                <div class="col-span-6 sm:col-span-3">
                    <label for="last_name" class="block text-sm font-medium text-gray-700">Last name</label>
                    <input type="text" placeholder="Last name" name="last_name" id="last_name" autocomplete="family-name" class="mt-3 py-2 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-black-300 rounded-md">
                </div>

                <div class="col-span-6 sm:col-span-4">
                    <label for="email_address" class="block text-sm font-medium text-gray-700">Email address</label>
                    <input type="text" placeholder="email" name="email_address" id="email_address" autocomplete="email" class="mt-3 py-2 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-black-400 rounded-md">
                </div>
                <div class="col-span-6 sm:col-span-3">
                    <label for="password1" class="block text-sm font-medium text-gray-700">Password</label>
                    <input type="password" name="password1" id="password1" autocomplete="password" class="mt-3 py-2 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-black-300 rounded-md">
                </div>

                <div class="col-span-6 sm:col-span-3">
                    <label for="password2" class="block text-sm font-medium text-gray-700">Confirm password</label>
                    <input type="password" name="password2" id="password2" autocomplete="password" class="mt-3 py-2 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-black-300 rounded-md">
                </div>
                </div>
            </div>
            <div class="px-4 py-3 bg-gray-50 text-right sm:px-6">
                <button type="submit" class="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                Submit
                </button>
            </div>
            </div>
        </form>
        </div>
    </div>
    </div>
  </div>
</template>

<script>
// import { Popover, PopoverButton, PopoverPanel } from '@headlessui/vue'
import LandingNav from "./LandingNav.vue";

export default {
  name: "LandingPage",
  components: {
    LandingNav,
  }
};
</script>