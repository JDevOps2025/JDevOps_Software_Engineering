/* Cypress Configuration File
   Description: This file contains end-to-end tests for the homepage of the web application.
   It uses Cypress to automate browser interactions and verify that the homepage loads correctly and displays the expected content.
   Functional test to verify homepage renders the headline
*/

describe("Homepage", () => {
  it("loads and shows the expected text", () => {
    cy.visit("http://localhost:5000/");
    cy.contains("AI & MACHINE LEARNING PLATFORM NEW DEVELOPMENT"); // header text
    /* cy.get("h2").should(
      "contain.text",
      "Best platform for AI technology products"
    ); // main message */
  });
});
