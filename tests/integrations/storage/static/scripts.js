document.addEventListener('alpine:init', () => {
    Alpine.data('mcommerce', () => ({
        products: [],
        carts: [],

        init() {
            this.fetchAllProducts();
            this.fetchAllCarts();
        },

        async fetchAllProducts() {
            const response = await fetch('/api/v1/products?per-page=8')
            const { data } = await response.json()
            this.products = data;
        },

        async fetchAllCarts() {
            const response = await fetch('/api/v1/carts')
            const { data } = await response.json()
            this.carts = data;
        },

        async addToCart(product) {
            let data = new FormData();
            data.append('product_id', product.id);
            data.append('quantity', 1);
            const response = await fetch('/api/v1/carts', {
                method: 'post',
                body: data
            })
            await response.json()
            this.fetchAllCarts();
        },
    }))
})