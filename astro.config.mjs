import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://fde.tkxel.com',
  trailingSlash: 'always',
  integrations: [sitemap()],
});
