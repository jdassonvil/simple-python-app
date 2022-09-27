from app import format_messages_list


def test_format_message():
    messages = [{"text": "hello world"}]
    result = format_messages_list(messages)
    assert result == "<ul><li>hello world</li></ul>"
