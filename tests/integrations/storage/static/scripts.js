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
            await fetch('/api/v1/carts', {
                method: 'post',
                body: data
            })
            this.fetchAllCarts();
        },

        async updateCart(cart) {
            let data = new FormData();
            data.append('product_id', cart.product.id);
            data.append('quantity', cart.quantity);
            await fetch(`/api/v1/carts/${cart.id}`, {
                method: 'put',
                body: data
            })
            this.fetchAllCarts();
        },

        async deleteCart(cart) {
            await fetch(`/api/v1/carts/${cart.id}`, {
                method: 'delete'
            })
            this.fetchAllCarts()
        }
    }))
})