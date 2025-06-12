module.exports = {
  chainWebpack: config => {
    config.module
      .rule('css')
      .test(/\.css$/)
      .use('style-loader')
      .loader('style-loader')
      .end();
  },
};
