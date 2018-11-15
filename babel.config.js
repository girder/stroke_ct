module.exports = {
  presets: [
    ['@babel/env', {
      modules: false,
      targets: {
        browsers: ['> 1%', 'last 2 versions', 'not ie <= 8']
      },
    }],
  ],
  plugins: [
    '@babel/plugin-syntax-dynamic-import',
  ],
  env: {
    test: {
      presets: ['@babel/env'],
      plugins: [
        'istanbul',
      ],
    },
  },
};
