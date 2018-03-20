from json_util import JsonUtil

# test covering multi-level json in various orderings
ex_text = '''{
                "a": 1,
                "b": "true",
                "c": {
                    "d": 3,
                    "e": {
                        "f": 4,
                        "g": 5
                    }
                },
                "h": 6,
                "i": {
                    "j": 7
                },
                "k": 8
            }'''
JsonUtil.print_terminal_kv_pairs(JsonUtil.get_terminal_kv_pairs(ex_text))
