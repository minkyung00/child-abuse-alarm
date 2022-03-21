const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  devServer: {
    proxy: process.env.VUE_APP_API_URL
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
