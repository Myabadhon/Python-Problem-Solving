def string_validator(g_str):
    print(any(s.isalnum() for s in g_str))
    print(any(s.isalpha() for s in g_str))
    print(any(s.isdigit() for s in g_str))
    print(any(s.islower() for s in g_str))
    print(any(s.isupper() for s in g_str))

g_str = input()
string_validator(g_str)