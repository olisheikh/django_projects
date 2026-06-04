const product_div = document.querySelectorAll('.product-div');

product_div.forEach((product) => {
    product.addEventListener('click', () => {
        const product_id = product.dataset.id;
        window.location.href = `/viewsapp/products/${product_id}/`;
    })
})