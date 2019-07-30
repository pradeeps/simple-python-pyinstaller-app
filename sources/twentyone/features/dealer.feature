# Created by P_Susarla at 18/01/2019
Feature: The dealer for the game of 21
  Scenario: Deal initial set of cards
    Given a dealer
    When the round starts
    Then the dealer gives itself two cards

  Scenario Outline: Deal dealers ego and kick him out
    Given a dealer has huge <emotion>
    When he cheats
    Then the dealer is kicked out and looses cards
    Examples:
    | emotion |
    | ego     |
    | temper  |
