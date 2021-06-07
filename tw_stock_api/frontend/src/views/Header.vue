<template>
    <header class="header bg-white shadow py-4 px-4">
    <div class="header-content flex items-center flex-row">
        <form action="#">
        <div class="hidden md:flex relative">
            <div
            class="inline-flex items-center justify-center absolute left-0 top-0 h-full w-10 text-gray-400"
            >
            <svg
                class="h-6 w-6"
                fill="none"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                viewBox="0 0 24 24"
                stroke="currentColor"
            >
                <path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
            </div>

            <input
            id="search"
            type="text"
            name="search"
            class="text-sm sm:text-base placeholder-gray-500 pl-10 pr-4 rounded-lg border border-gray-300 w-full h-10 focus:outline-none focus:border-indigo-400"
            placeholder="Search..."
            />
        </div>
        <div class="flex md:hidden">
            <a href="#" class="flex items-center justify-center h-10 w-10 border-transparent">
            <svg
                class="h-6 w-6 text-gray-500"
                fill="none"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                viewBox="0 0 24 24"
                stroke="currentColor"
            >
                <path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
            </svg>
            </a>
        </div>
        </form>
        <div class="flex ml-auto">
            <Menu as="div" class="ml-3 relative">
            <div>
              <MenuButton class="bg-gray-800 flex text-sm rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white">
                <span class="sr-only">Open user menu</span>
                <img class="h-8 w-8 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" />
              </MenuButton>
            </div>
            <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
              <MenuItems class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg py-1 bg-white ring-1 ring-black ring-opacity-5 focus:outline-none">
                <MenuItem v-slot="{ active }">
                  <a href="/profile" :class="[active ? 'bg-gray-100' : '', 'block px-4 py-2 text-sm text-gray-700']">Your Profile</a>
                </MenuItem>
                <MenuItem v-slot="{ active }">
                  <a :class="[active ? 'bg-gray-100' : '', 'block px-4 py-2 text-sm text-gray-700 cursor-pointer']" @click="logout()">Sign out</a>
                </MenuItem>
              </MenuItems>
            </transition>
          </Menu>
        </div>
    </div>
    </header>
</template>
<script>
import { Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import { mapMutations } from 'vuex';

export default {
    name: "Header",
    components: {
        Menu,
        MenuButton,
        MenuItem,
        MenuItems,
    },
    data() {
        return {
        };
    },
    methods: {
        ...mapMutations('auth', [
            'REMOVE_AUTH_TOKEN',
        ]),
        logout() {
            this.REMOVE_AUTH_TOKEN();
            console.log(this.token)
            this.$router.replace({ name: 'Login' });
        },
    }
};
</script>