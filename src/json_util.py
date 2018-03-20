class JsonUtil:
    def __init__(self):
        pass

    @staticmethod
    def get_terminal_kv_pairs(json_text):
        terminal_kv_pairs = {}
        key_prefix = ''
        key_prefix_stack = []
        text_buffer = ''
        paren_counter = 0

        for c in json_text:
            if c == ',':
                if text_buffer != '':
                    key, value = text_buffer.split(':')
                    terminal_kv_pairs[key_prefix + key] = value
                    text_buffer = ''
            elif c == '{':
                if paren_counter > 0:
                    key = text_buffer[:text_buffer.find(':')]
                    key_prefix += key + '.'
                    key_prefix_stack.append(key)
                    text_buffer = ''
                paren_counter += 1
            elif c == '}':
                if text_buffer != '':
                    key, value = text_buffer.split(':')
                    terminal_kv_pairs[key_prefix + key] = value
                if paren_counter > 1:
                    key_prefix_stack.pop()
                key_prefix = '.'.join(key_prefix_stack)
                text_buffer = ''
                paren_counter -= 1
            elif c == ' ' or c == '\n' or c == '\r' or c == '\t' or c == '"' or c == "'":
                pass
            else:
                text_buffer += c
        if paren_counter != 0:
            raise Exception('parenthesis do not match!')
        return terminal_kv_pairs

    @staticmethod
    def print_terminal_kv_pairs(json_dict):
        print("terminal json values:")
        for key in json_dict:
            print('"{0}": {1},'.format(key, json_dict[key]))
