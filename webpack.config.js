const path = require('path');
const webpack = require('webpack');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const ManifestRevisionPlugin = require('manifest-revision-webpack-plugin');

var rootAssetPath = './assets';

module.exports = {
  mode: 'development',
  entry: {
    app_js: './assets/js/main.js',
    home_js: './assets/js/home.js',
    app_css: './assets/css/main.scss',
  },
  output: {
    path: path.resolve(__dirname, 'build/public'),
    publicPath: 'http://localhost:2992/assets/',
    filename: '[name].[chunkhash].js',
    chunkFilename: '[id].[chunkhash].js',
  },
  resolve: {
    extensions: ['.js', '.css']
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      },
      {
        test: /\.scss$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader
          },
          'css-loader',
          'sass-loader'
        ]
      },
      {
        test: /\.(jpe?g|png|gif|svg)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[hash].[ext]'
            }
          }
        ]
      }
    ]
  },
  plugins: [
    new ManifestRevisionPlugin(path.join('build', 'manifest.json'), {
      rootAssetPath: rootAssetPath,
      ignorePaths: ['/js', '/css'],
      extensionsRegex: /\.(jpe?g|png|gif|svg)$/
    }),
    new webpack.ProvidePlugin({
      $: 'jquery',
      moment: 'moment',
    }),
    new CleanWebpackPlugin(),
    new MiniCssExtractPlugin({
      filename: '[name].[chunkhash].css',
      chunkFilename: '[id].[chunkhash].css'
    })
  ]
};
