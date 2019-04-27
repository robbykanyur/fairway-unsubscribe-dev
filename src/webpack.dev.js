const merge = require('webpack-merge');
const common = require('./webpack.common.js');
const path = require('path');

module.exports = merge(common, {
  mode: 'development',
  entry: {
    app_js: './src/assets/js/main.js',
    home_js: './src/assets/js/home.js',
    admin_js: './src/assets/js/admin.js',
    app_css: './src/assets/css/main.scss',
  },
  output: {
    path: path.resolve(__dirname, 'build/public'),
    publicPath: 'http://localhost:2992/public/',
    filename: '[name].[contenthash].js',
    chunkFilename: '[name].[contenthash].js',
  },
  devtool: 'inline-source-map',
  devServer: {
    host: '0.0.0.0',
    port: 2992,
    publicPath: 'http://localhost:2992/public',
    public: 'http://localhost:2992'
  }
});
