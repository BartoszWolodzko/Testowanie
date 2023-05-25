describe('Logowanie i przeglądanie produktów', () => {
    beforeEach(() => {
        cy.visit('https://www.saucedemo.com')
        cy.intercept('/service-worker.js', {
          body: undefined
        })
      })
    it('Poprawne logowanie', () => {
        cy.login('standard_user', 'secret_sauce')
        cy.get('.inventory_list').should('be.visible')
    })

    it('Niepoprawne logowanie', () => {
        cy.login('standard_user', 'secret_sauce1')
        cy.get('#login_button_container').should('be.visible')
    })

    it('Wylogowanie', () => {
        cy.login('standard_user', 'secret_sauce')
        
        cy.get('#react-burger-menu-btn').click()
        cy.get('#logout_sidebar_link').click()
        cy.get('#login-button').should('be.visible')
    })
})
