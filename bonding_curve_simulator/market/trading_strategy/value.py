# https://github.com/abides-sim/abides/blob/master/agent/ValueAgent.py

from bonding_curve_simulator.mesa.agent.trader import TraderAgent
from bonding_curve_simulator.market.trading_strategy import (
    TradingStrategy,
    TradingStrategyConfig,
)


class ValueStrategy(TradingStrategy):
    def __init__(self, config: TradingStrategyConfig):
        self.config = config

    def execute(self, agent: TraderAgent):
        return super().execute(agent)