// webpack.mix.js
const mix = require('laravel-mix')
const path = require('path')
const NodePolyfillPlugin = require("node-polyfill-webpack-plugin");


mix.js('tests/integrations/resources/js/app.js', 'src/masonite_commerce/resources/js')
  .postCss('tests/integrations/resources/css/app.css', 'src/masonite_commerce/resources/css', [
    //
  ])

// ensure root directory of mix is project root
mix.setPublicPath(".")

// add an alias to js code
mix.alias({
    "@": path.resolve("resources/js/"),
}).webpackConfig(webpack => {
    return {
        plugins: [
            new NodePolyfillPlugin(),
        ]
    }
})

// add version hash in production
if (mix.inProduction()) {
mix.version()
}
// Disable compilation success notification
mix.disableSuccessNotifications()