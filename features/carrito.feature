@regression
Feature: Carrito SauceDemo
  Scenario: Agregar producto al carrito
    Given estoy logueado como "standard_user" con password "secret_sauce"
    When agrego el producto "Sauce Labs Backpack" al carrito
    And abro el carrito
    Then debo ver el producto "Sauce Labs Backpack" en el carrito
