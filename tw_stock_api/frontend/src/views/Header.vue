<template>
    <header class="header bg-white shadow py-4 px-4">
    <div class="header-content flex items-center flex-row">
        <div class="flex ml-auto">
            <Menu as="div" class="ml-3 relative">
            <div>
              <MenuButton class="bg-gray-800 flex text-sm rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white">
                <span class="sr-only">Open user menu</span>
                <img class="h-8 w-8 rounded-full" src="../assets/user.png" alt="" />
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