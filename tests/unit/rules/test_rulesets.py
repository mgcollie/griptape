from griptape.rules import Rule
from griptape.rules.ruleset import Ruleset


class TestRulesets:
    def test_init(self):
        ruleset = Ruleset("foobar", rules=[Rule("rule1"), Rule("rule2")])

        assert ruleset.name == "foobar"
        assert len(ruleset.rules) == 2