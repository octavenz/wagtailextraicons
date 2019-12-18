const fs = require('fs');
const path = require('path');

const IconfontPlugin = require('iconfont-plugin-webpack');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const WebpackOnBuildPlugin = require('on-build-webpack');

const entryPath = path.resolve(__dirname, 'wagtailextraicons/static_src/wagtailextraicons');
const outputPath = path.resolve(__dirname, 'wagtailextraicons/static/wagtailextraicons');

const fontEntryPath = path.join(entryPath, 'extraicons');

module.exports = {
  mode: 'production',
  entry: {
    'main': path.join(entryPath, 'scss/main.scss')
  },
  output: {
    path: outputPath,
    publicPath: '/static/'
  },
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          'sass-loader'
        ]
      },
      {
        test: /\.(svg|eot|ttf|woff|woff2)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              outputPath: 'fonts/',
              name: '[name].[contenthash].[ext]'
            },
          }
        ]
      }
    ]
  },
  plugins: [
    new IconfontPlugin({
      src: fontEntryPath,
      family: 'extraicons',
      dest: {
        font: path.join(entryPath, 'fonts/[family].[type]'),
        css: path.join(entryPath, 'scss/[family].scss')
      },
      watch: {
        pattern: fontEntryPath + '/**/*.svg'
      }
    }),
    new MiniCssExtractPlugin({
      filename: 'css/[name].css'
    }),
    new WebpackOnBuildPlugin(function () {
      const extraJs = path.join(outputPath, 'main.js');
      if(fs.existsSync(extraJs)) {
        fs.unlinkSync(extraJs);
      }
    })
  ]
};
