require("./bootstrap.js")

Alpine.data('main', () => ({
    open: false,

    toggle() {
        this.open = ! this.open
    }
}))

Alpine.data('navbar', () => ({}))

Alpine.start()