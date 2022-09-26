a = 10
b = 5
s = 'div'
result = switch (s,
                "add" = a+b,
                "minus" = a-b,
                "prod" = a*b,
                "div" = a/b
)
print(result)