const merge = require('webpack-merge');
const common = require('./webpack.common.js');
const TerserJSPlugin = require('terser-webpack-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const ImageminPlugin = require('imagemin-webpack-plugin').default
const path = require('path');

module.exports = merge(common, {
  mode: 'production',
  entry: {
    app_js: './src/assets/js/main.js',
    home_js: './src/assets/js/home.js',
    admin_js: './src/assets/js/admin.js',
    app_css: './src/assets/css/main.scss',
  },
  output: {
    path: path.resolve(__dirname, 'build/public'),
    publicPath: '/public/',
    filename: '[name].[contenthash].js',
    chunkFilename: '[name].[contenthash].js',
  },
  optimization: {
    minimizer: [new TerserJSPlugin({sourceMap: true}), new OptimizeCSSAssetsPlugin({})],
  },
  devtool: 'source-map',
  performance: {
    hints: false
  },
  plugins: [
    new ImageminPlugin({
      pngquant: {
        quality: '95-100'
      }
    })
  ]
});
