describe('Home Page', () => {
  beforeEach(() => {
    cy.visit('/')
  })

  it('should load the home page', () => {
    cy.get('body').should('be.visible')
    cy.title().should('include', 'Pravis Boutique')
  })

  it('should navigate to voice assistant', () => {
    // Find and click the voice assistant button
    cy.get('[data-cy="voice-assistant-button"]').should('exist')
    cy.get('[data-cy="voice-assistant-button"]').click()
    
    // Verify voice assistant modal is visible
    cy.get('[data-cy="voice-assistant-modal"]').should('be.visible')
  })
  
  it('should display navigation menu', () => {
    // Check for main navigation
    cy.get('nav').should('be.visible')
    
    // Check for menu items
    cy.get('nav').find('a').should('have.length.at.least', 3)
  })
})
