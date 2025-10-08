ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list[-1] = "World"

y = list(ft_tuple)
y[-1] = "Morocco"
ft_tuple = tuple(y)

ft_set.add("Benguerir")
ft_set.pop()


ft_dict["Hello"] = "1337Bg"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)