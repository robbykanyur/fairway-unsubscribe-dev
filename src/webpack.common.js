const path = require('path');
const webpack = require('webpack');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const ManifestRevisionPlugin = require('manifest-revision-webpack-plugin');

var rootAssetPath = './src/assets';

module.exports = {
  resolve: {
    alias: {
      'jquery': path.resolve(__dirname, '../node_modules/jquery/dist/jquery'),
      'jquery-validation': path.resolve(__dirname, '../node_modules/jquery-validation/dist/jquery.validate'),
      'moment': path.resolve(__dirname, '../node_modules/moment/moment')
    },
    extensions: ['.js', '.css'],
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: [
          {
            loader: 'babel-loader'
          }
        ]
      },
      {
        test: /\.scss$/,
        use: [
          {
            loader: MiniCssExtractPlugin.loader,
            options: {
              hmr: process.env.NODE_ENV === 'development'
            }
          },
          'css-loader',
          'sass-loader',
          'postcss-loader',
        ]
      },
      {
        test: /\.(jpe?g|png|gif|svg)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[contenthash].[ext]',
            }
          }
        ]
      }
    ]
  },
  plugins: [
    new CleanWebpackPlugin(),
    new ManifestRevisionPlugin(path.join('src/build', 'manifest.json'), {
      rootAssetPath: rootAssetPath,
      ignorePaths: ['/js', '/css'],
      extensionsRegex: /\.(jpe?g|png|gif|svg)$/
    }),
    new MiniCssExtractPlugin({
      filename: '[name].[contenthash].css',
      chunkFilename: '[id].[contenthash].css'
    })
  ]
};
