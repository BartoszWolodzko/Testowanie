describe('Dodawanie produktów do koszyka i złożenie zamówienia', () => {
    beforeEach(() => {
      cy.visit('https://www.saucedemo.com')
      cy.intercept('/service-worker.js', { body: undefined })
      cy.login('standard_user', 'secret_sauce')
    })
  
    it('Przeglądanie produktów', () => {
      cy.get('.inventory_list').should('be.visible')
      cy.get('.inventory_item_name').first().should('contain', 'Sauce Labs Backpack')
      cy.get('.inventory_item_price').first().should('contain', '$29.99')
      cy.get('#item_4_img_link').first().click()
      cy.get('.inventory_details_name').should('contain', 'Sauce Labs Backpack')
      cy.get('.inventory_details_price').should('contain', '$29.99')
      cy.go('back')
    })
  
    it('Dodawanie produktów do koszyka', () => {
      cy.get('.inventory_list .inventory_item .btn_primary').each(($el, index) => {
        if (index < 3) {
          cy.wrap($el).click()
        }
      })
      cy.get('.shopping_cart_badge').should('contain', '3')
      cy.get('.shopping_cart_link').click()
      cy.get('.cart_item').should('have.length', 3)
    })
  
    it('Złożenie zamówienia', () => {
      cy.get('.inventory_list .inventory_item .btn_primary').each(($el, index) => {
        if (index < 3) {
          cy.wrap($el).click()
        }
      })
      cy.get('.shopping_cart_link').click()
      cy.get('.cart_item').should('have.length', 3)
      cy.get('.checkout_button').click()
      cy.get('#first-name').type('John')
      cy.get('#last-name').type('Doe')
      cy.get('#postal-code').type('12345')
      cy.get('.cart_button').click()
      cy.get('.summary_info').should('contain', 'SauceCard #31337')
      cy.get('.summary_info').should('contain', 'Free Pony Express Delivery!')
      cy.get('.cart_button').click()
      cy.get('.complete-header').should('contain', 'Thank you for your order!')
    })
  })