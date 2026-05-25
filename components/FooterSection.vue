<template>
  <footer id="contact" class="bg-pravis-950 text-white py-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid gap-10 lg:grid-cols-[1.2fr_0.8fr_0.9fr_1.1fr] mb-12">
        <div class="space-y-5">
          <div class="flex items-center space-x-3">
            <div class="flex h-11 w-11 items-center justify-center rounded-full border border-pravis-300/40 bg-white/10">
              <span class="font-display text-lg font-bold tracking-wide text-pravis-300">PB</span>
            </div>
            <div>
              <h4 class="font-display font-bold text-lg">Pravis Boutique</h4>
              <p class="text-pravis-300 text-sm">Indian attire catalog</p>
            </div>
          </div>
          <p class="text-sm leading-7 text-gray-300">
            A frontend storefront for browsing Indian attires, checking new drops on Instagram, and starting purchase conversations through WhatsApp.
          </p>
          <div class="flex flex-wrap gap-3">
            <a
              v-for="channel in channelLinks"
              :key="channel.name"
              :href="channel.url"
              target="_blank"
              rel="noopener noreferrer"
              class="rounded-full bg-white/10 px-4 py-2 text-sm font-semibold text-white transition hover:bg-pravis-700"
            >
              {{ channel.name }}
            </a>
          </div>
        </div>

        <div>
          <h5 class="font-semibold mb-6 text-pravis-300">Browse</h5>
          <ul class="space-y-3 text-sm">
            <li v-for="link in quickLinks" :key="link.text">
              <a :href="link.href" class="text-gray-300 hover:text-pravis-300 transition-colors">
                {{ link.text }}
              </a>
            </li>
          </ul>
        </div>

        <div>
          <h5 class="font-semibold mb-6 text-pravis-300">Contact</h5>
          <div class="space-y-4 text-sm text-gray-300">
            <a :href="whatsappUrl" target="_blank" rel="noopener noreferrer" class="flex items-center gap-3 hover:text-pravis-300">
              <span class="flex h-9 w-9 items-center justify-center rounded-full bg-white/10">WA</span>
              <span>+91 6300208234</span>
            </a>
            <a href="https://www.instagram.com/pravis.handlooms/?hl=en" target="_blank" rel="noopener noreferrer" class="flex items-center gap-3 hover:text-pravis-300">
              <span class="flex h-9 w-9 items-center justify-center rounded-full bg-white/10">IG</span>
              <span>@pravis.handlooms</span>
            </a>
            <div class="flex items-start gap-3">
              <span class="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-white/10">IN</span>
              <span>Hyderabad, Telangana<br>India</span>
            </div>
          </div>
        </div>

        <div class="rounded-2xl border border-white/10 bg-white/5 p-5">
          <h5 class="font-semibold text-pravis-300">Shop from your preferred channel</h5>
          <p class="mt-3 text-sm leading-6 text-gray-300">
            Use the website to browse the collection, WhatsApp for availability and ordering, Instagram for latest photos, and Amazon for marketplace browsing.
          </p>
          <div class="mt-5 grid gap-3">
            <a :href="whatsappUrl" target="_blank" rel="noopener noreferrer" class="rounded-xl bg-pravis-700 px-4 py-3 text-center text-sm font-semibold text-white transition hover:bg-pravis-800">Start WhatsApp Inquiry</a>
            <a href="https://www.amazon.in/s?k=Pravis+Boutique+Indian+attire" target="_blank" rel="noopener noreferrer" class="rounded-xl bg-[#232f3e] px-4 py-3 text-center text-sm font-semibold text-white transition hover:bg-[#131921]">Browse on Amazon</a>
          </div>
        </div>
      </div>

      <div class="border-t border-white/10 pt-8 flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <p class="text-sm text-gray-400">
          2026 Pravis Boutique. Indian attire storefront and catalog experience.
        </p>
        <div class="flex flex-wrap gap-5 text-sm text-gray-400">
          <a href="/privacy" class="hover:text-pravis-300 transition-colors">Privacy Policy</a>
          <a href="/terms" class="hover:text-pravis-300 transition-colors">Terms of Service</a>
          <a :href="whatsappUrl" target="_blank" rel="noopener noreferrer" class="hover:text-pravis-300 transition-colors">Order Help</a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
const whatsappUrl = 'https://wa.me/916300208234?text=Hi%20Pravis%20Boutique%2C%20I%20want%20help%20browsing%20Indian%20attires.'

const channelLinks = [
  { name: 'WhatsApp', url: whatsappUrl },
  { name: 'Instagram', url: 'https://www.instagram.com/pravis.handlooms/?hl=en' },
  { name: 'Amazon', url: 'https://www.amazon.in/s?k=Pravis+Boutique+Indian+attire' }
]

const quickLinks = [
  { text: 'Shop Collection', href: '/shop' },
  { text: 'Sarees', href: '/shop' },
  { text: 'Suit Sets', href: '/shop' },
  { text: 'Dupattas', href: '/shop' },
  { text: 'Contact', href: '#contact' }
]
</script>
