const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
  devServer: {
    proxy: {
      '/api': {
        target: process.env.VUE_APP_API_URL,
        changeOrigin: true
      }
    }
  },
  transpileDependencies: true,
  css: {
    loaderOptions: {
      scss: {
		    additionalData:
			    `@import "@/styles/_variable.scss";`,
      },
    },
  },
});
