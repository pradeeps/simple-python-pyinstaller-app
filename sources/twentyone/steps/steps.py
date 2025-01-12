from behave import *
from twentyone import *
import time


@given("a dealer")
def step_impl(context):
    context.dealer = Dealer()


@when("the round starts")
def step_impl(context):
    context.dealer.new_round()


@then("the dealer gives itself two cards")
def step_impl(context):
    assert len(context.dealer.hand) == 2


@given("a dealer has huge {emotion}")
def step_impl(context, emotion):
    context.dealer = DealerWithEmotion(emotion)


@when("he cheats")
def step_impl(context):
    context.dealer.cheats()


@then("the dealer is kicked out and looses cards")
def step_impl(context):
    assert len(context.dealer.hand) == 0
