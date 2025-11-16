/* Cypress Configuration File
   Description: This file contains end-to-end tests for the homepage of the web application.
   It uses Cypress to automate browser interactions and verify that the homepage loads correctly and displays the expected content.
   Functional test to verify homepage renders the headline
*/

describe("Homepage", () => {
  it("Best platform for AI technolgy products", () => {
    cy.visit("http://localhost:5000/");
    cy.contains("Your web server is running"); // main message
  });
});
