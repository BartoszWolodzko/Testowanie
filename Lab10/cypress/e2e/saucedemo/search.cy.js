describe('Sortowanie produktów', () => {
    beforeEach(() => {
        cy.visit('https://www.saucedemo.com')
        cy.intercept('/service-worker.js', {
          body: undefined
        })
        cy.login('standard_user', 'secret_sauce')
        cy.get('.inventory_list').should('be.visible')
    })

    it('Nazwa (A-Z)', () => {
        cy.get('.product_sort_container').select('Name (A to Z)')
        cy.get('.inventory_item_name').first().should('contain', 'Sauce Labs Backpack')
    })

    it('Nazwa (Z-A)', () => {
        cy.get('.product_sort_container').select('Name (Z to A)')
        cy.get('.inventory_item_name').first().should('contain', 'Test.allTheThings() T-Shirt (Red)')
    })

    it('Cena (od najniższej)', () => {
        cy.get('.product_sort_container').select('Price (low to high)')
        cy.get('.inventory_item_price').first().should('contain', '$7.99')
    })

    it('Cena (od najwyższej)', () => {
        cy.get('.product_sort_container').select('Price (high to low)')
        cy.get('.inventory_item_price').first().should('contain', '$49.99')
    })
})
