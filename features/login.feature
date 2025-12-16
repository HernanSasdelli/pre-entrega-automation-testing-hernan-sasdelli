@smoke
Feature: Login SauceDemo
  Scenario: Login exitoso
    Given estoy en la pagina de login
    When ingreso usuario "standard_user" y password "secret_sauce"
    Then debo ver la pagina de productos
